# -*- coding: utf-8 -*-
"""Comprueba que la documentación del repositorio no se contradiga a sí misma.

    python tools/verificar.py

Una matriz de 38 casos y 12 defectos con referencias cruzadas se desincroniza
sola: se renumera un caso, se retira un defecto que no se reprodujo, se cambia
una severidad y media docena de enlaces dejan de cuadrar. Estas comprobaciones
son el equivalente documental de un test de humo.

Devuelve código de salida 1 si encuentra alguna inconsistencia, para poder
encadenarlo en un hook de pre-commit o en CI.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from casos import CASOS  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
BUGS = RAIZ / "03-bug-reports"

errores = []
avisos = []


def comprobar(condicion, mensaje, lista=None):
    if not condicion:
        (lista if lista is not None else errores).append(mensaje)


ids_caso = {c[0] for c in CASOS}
ficheros_bug = sorted(p for p in BUGS.glob("BUG-*.md"))
ids_bug = {p.stem for p in ficheros_bug}

# 1 ── Todo caso fallado declara un defecto, y ese defecto existe -------------
for c in CASOS:
    cid, estado, bug = c[0], c[10], c[11]
    if estado == "Falla":
        comprobar(bool(bug), f"{cid} está en estado «Falla» pero no declara defecto.")
        if bug:
            comprobar(bug in ids_bug,
                      f"{cid} referencia {bug}, que no existe en 03-bug-reports/.")
    elif bug:
        comprobar(False, f"{cid} declara el defecto {bug} pero su estado es «{estado}».")

# 2 ── Todo defecto se corresponde con un caso fallado ------------------------
bugs_declarados = {c[11] for c in CASOS if c[11]}
for bid in sorted(ids_bug):
    comprobar(bid in bugs_declarados,
              f"{bid} existe como fichero pero ningún caso de la matriz lo referencia.")

# 3 ── Cada defecto enlaza a un caso que existe -------------------------------
for p in ficheros_bug:
    texto = p.read_text(encoding="utf-8")
    referenciados = set(re.findall(r"\bCP-\d{3}\b", texto))
    comprobar(bool(referenciados), f"{p.stem} no referencia ningún caso de prueba.")
    for cid in sorted(referenciados - ids_caso):
        comprobar(False, f"{p.stem} referencia {cid}, que no existe en la matriz.")

    # 4 ── Estructura mínima del reporte --------------------------------------
    for seccion in ("## Precondiciones", "## Pasos para reproducir",
                    "## Resultado esperado", "## Resultado obtenido",
                    "## Evidencia", "## Notas técnicas"):
        comprobar(seccion in texto, f"{p.stem} no tiene la sección «{seccion}».")
    for campo in ("**Severidad**", "**Prioridad**", "**Estado**", "**Entorno**"):
        comprobar(campo in texto, f"{p.stem} no declara el campo {campo}.")

# 5 ── Las capturas referenciadas existen -------------------------------------
for p in ficheros_bug:
    texto = p.read_text(encoding="utf-8")
    for img in re.findall(r"!\[[^\]]*\]\(\.\./evidencias/([^)]+)\)", texto):
        comprobar((RAIZ / "evidencias" / img).exists(),
                  f"{p.stem} embebe la captura «{img}», que no existe en evidencias/.")
    # Las tablas de capturas pendientes son un aviso, no un error.
    for nombre in re.findall(r"`(BUG-\d{3}-\d{2}-[a-z0-9\-]+\.png)`", texto):
        comprobar((RAIZ / "evidencias" / nombre).exists(),
                  f"{p.stem}: captura pendiente «{nombre}».", avisos)

# 6 ── Los entregables generados están al día ---------------------------------
for generado, fuente in (("02-casos-de-prueba.md", "tools/casos.py"),
                         ("05-matriz-trazabilidad.md", "tools/casos.py")):
    g, f = RAIZ / generado, RAIZ / fuente
    if g.exists() and f.exists():
        comprobar(g.stat().st_mtime >= f.stat().st_mtime,
                  f"{generado} es anterior a {fuente}: regenerar.", avisos)

# 7 ── Resumen ----------------------------------------------------------------
estados = {}
for c in CASOS:
    estados[c[10]] = estados.get(c[10], 0) + 1

print(f"Casos: {len(CASOS)}  |  " +
      "  ".join(f"{k}: {v}" for k, v in estados.items()) +
      f"  |  Defectos: {len(ids_bug)}")

if avisos:
    print(f"\n{len(avisos)} aviso(s):")
    for a in avisos:
        print(f"  ! {a}")

if errores:
    print(f"\n{len(errores)} inconsistencia(s):")
    for e in errores:
        print(f"  ✗ {e}")
    sys.exit(1)

print("\n✓ Documentación consistente.")
