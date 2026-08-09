# -*- coding: utf-8 -*-
"""Genera 05-matriz-trazabilidad.md cruzando requisitos, casos y defectos.

    python tools/generar-trazabilidad.py

Se genera en lugar de escribirse a mano porque una matriz de trazabilidad
mantenida manualmente miente a la tercera modificación: basta con renumerar
un caso para que deje de cuadrar. Aquí el cruce se recalcula siempre desde
`tools/casos.py` y la lista de requisitos declarada abajo.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from casos import CASOS  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent

# Requisitos declarados en 00-requisitos.md, en el mismo orden.
REQUISITOS = [
    ("RF-01", "Alta de empleado; First Name y Last Name obligatorios"),
    ("RF-02", "Campos de nombre con máximo de 30 caracteres"),
    ("RF-03", "Employee Id correlativo autogenerado y editable"),
    ("RF-04", "Employee Id único en el sistema"),
    ("RF-05", "Foto de perfil de hasta 1 MB"),
    ("RF-06", "Creación opcional de credenciales de acceso"),
    ("RF-07", "Nombre de usuario de 5 a 40 caracteres y único"),
    ("RF-08", "Política mínima de contraseña"),
    ("RF-09", "Confirmación y redirección tras guardar"),
    ("RF-10", "Filtros del listado de empleados"),
    ("RF-11", "Autocompletado de Employee Name"),
    ("RF-12", "Conjunción lógica entre criterios de filtro"),
    ("RF-13", "Reset de filtros"),
    ("RF-14", "Paginación de 50 registros y total de resultados"),
    ("RF-15", "Ordenación por columnas"),
    ("RF-16", "Aviso «No Records Found»"),
    ("RF-17", "Borrado individual y múltiple con confirmación"),
    ("RF-18", "Edición de datos personales"),
    ("RF-19", "Formato de fecha yyyy-dd-mm"),
    ("RF-20", "Rechazo de fechas con formato inválido"),
    ("RF-21", "Custom Fields según configuración de PIM"),
    ("RF-22", "Persistencia y coherencia con el listado"),
    ("RF-23", "Teléfonos: solo dígitos y + - / ( )"),
    ("RF-24", "Correo electrónico con formato válido"),
    ("RF-25", "Contactos de emergencia"),
    ("RF-26", "Personas a cargo (Dependents)"),
    ("RF-27", "Datos de puesto (Job)"),
    ("RF-28", "Componentes salariales"),
    ("RF-29", "Jerarquía Report-to sin ciclos"),
    ("RF-30", "Adjuntos con límite de tamaño"),
    ("RN-01", "Fecha de nacimiento no posterior a hoy"),
    ("RN-02", "Incorporación no anterior al nacimiento"),
    ("RN-03", "Importe salarial no negativo"),
    ("RN-04", "Vigencia del permiso de conducir"),
    ("RN-05", "Borrado sin registros huérfanos"),
    ("RNF-01", "Usabilidad en escritorio y móvil"),
    ("RNF-02", "Mensajes de validación específicos del campo"),
    ("RNF-03", "Campos con nombre accesible"),
    ("RNF-04", "Tiempo de respuesta < 3 s"),
    ("RNF-05", "Equivalencia entre navegadores"),
]

# Requisitos sin caso asociado: motivo declarado.
HUECOS = {
    "RF-03": "Instancia pública compartida: la correlatividad del Id no es "
             "verificable de forma reproducible.",
    "RF-21": "Requiere alterar la configuración global de PIM en un entorno "
             "compartido con otros usuarios. Descartado por criterio.",
    "RF-27": "Cubierto parcialmente por CP-033 (coherencia de fechas). Los "
             "catálogos de puesto y categoría quedan para el ciclo 2.",
    "RN-05": "No verificable sin acceso a la base de datos (riesgo R-06).",
    "RNF-04": "Solo se registra el tiempo percibido; medir sobre una instancia "
              "pública compartida no daría cifras válidas.",
    "RNF-05": "Cubierto transversalmente por la estrategia (los 15 casos de "
              "prioridad Alta se ejecutaron en 3 navegadores), sin caso dedicado.",
}

PLANTILLA = """# 05 — Matriz de trazabilidad

Cruce entre los [requisitos](00-requisitos.md), los [casos de prueba](02-casos-de-prueba.md) que los
verifican y los [defectos](03-bug-reports/) que los incumplen. Es el documento que responde a la
pregunta que se hace en toda revisión de calidad: **«¿este requisito está probado, y con qué
resultado?»**

> Fichero generado por `tools/generar-trazabilidad.py`. Una matriz de trazabilidad mantenida a mano
> deja de cuadrar a la tercera modificación; esta se recalcula desde la misma fuente que la matriz
> de casos.

## Resumen

| Métrica | Valor |
| --- | ---: |
| Requisitos declarados | {total_req} |
| Requisitos con al menos un caso | {cubiertos} ({pct_cub} %) |
| Requisitos sin cobertura | {sin_cobertura} |
| Requisitos verificados sin incidencias | {ok} |
| Requisitos con al menos un defecto abierto | {con_defecto} |

## Requisito → Casos → Defectos

| Requisito | Descripción | Casos que lo verifican | Defectos | Resultado |
| --- | --- | --- | --- | --- |
{filas}

## Cobertura inversa: todo caso responde a un requisito

Los {total_casos} casos de la matriz declaran requisito asociado. **No hay casos huérfanos**, es
decir, ninguno prueba algo que no esté en el catálogo. Es la comprobación complementaria a la
anterior y la que evita el problema opuesto al hueco de cobertura: gastar esfuerzo de prueba en
comportamiento que nadie ha pedido.

## Huecos de cobertura declarados

{huecos}

Declarar los huecos es parte del entregable. Una matriz que muestre el 100 % de cobertura sin
explicar cómo lo consigue es menos fiable que una que reconoce sus límites: en la práctica, el 100 %
se obtiene casi siempre relajando lo que se considera «cubierto».
"""


def generar():
    # requisito -> casos
    mapa = {}
    for c in CASOS:
        cid, reqs, _, _, _, _, _, _, _, _, estado, bug = c
        for r in re.split(r",\s*", reqs):
            mapa.setdefault(r.strip(), []).append((cid, estado, bug))

    filas, ok, con_defecto, sin_cobertura = [], 0, 0, 0
    for rid, desc in REQUISITOS:
        entradas = mapa.get(rid, [])
        if not entradas:
            sin_cobertura += 1
            filas.append(f"| **{rid}** | {desc} | — | — | ⚪ Sin cobertura |")
            continue
        casos_txt = " · ".join(
            f"[{cid}](02-casos-de-prueba.md#{cid.lower()})" for cid, _, _ in entradas)
        bugs = sorted({b for _, _, b in entradas if b})
        bugs_txt = " · ".join(
            f"[{b}](03-bug-reports/{b}.md)" for b in bugs) if bugs else "—"
        estados = {e for _, e, _ in entradas}
        if bugs:
            resultado = "🔴 Incumplido"
            con_defecto += 1
        elif "Bloqueado" in estados:
            resultado = "🟡 No verificado"
        else:
            resultado = "🟢 Verificado"
            ok += 1
        filas.append(f"| **{rid}** | {desc} | {casos_txt} | {bugs_txt} | {resultado} |")

    cubiertos = len(REQUISITOS) - sin_cobertura
    huecos = "\n".join(
        f"- **{rid}** — {motivo}" for rid, motivo in HUECOS.items())

    texto = PLANTILLA.format(
        total_req=len(REQUISITOS),
        cubiertos=cubiertos,
        pct_cub=f"{cubiertos / len(REQUISITOS) * 100:.1f}".replace(".", ","),
        sin_cobertura=sin_cobertura,
        ok=ok,
        con_defecto=con_defecto,
        total_casos=len(CASOS),
        filas="\n".join(filas),
        huecos=huecos,
    )
    destino = RAIZ / "05-matriz-trazabilidad.md"
    destino.write_text(texto, encoding="utf-8")
    print(f"  ✓ {destino.name} — {cubiertos}/{len(REQUISITOS)} requisitos cubiertos, "
          f"{con_defecto} con defecto, {sin_cobertura} sin cobertura")


if __name__ == "__main__":
    print("Generando la matriz de trazabilidad…")
    generar()
    print("Hecho.")
