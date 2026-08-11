# Portfolio de QA manual — Módulo PIM de OrangeHRM

**Ciclo de pruebas funcionales completo sobre el módulo de gestión de empleados de un ERP de RRHH:
del plan de pruebas a la recomendación de release.**

38 casos diseñados con técnicas formales · 6 defectos confirmados y 6 hipótesis descartadas ·
trazabilidad requisito → caso → defecto · análisis de causa raíz sobre las peticiones de la API.

[![Verificar documentación](https://github.com/Blistahub/qa-portfolio-orangehrm/actions/workflows/verificar.yml/badge.svg)](https://github.com/Blistahub/qa-portfolio-orangehrm/actions/workflows/verificar.yml)
![Casos de prueba](https://img.shields.io/badge/casos-38-1F3A5F)
![Defectos confirmados](https://img.shields.io/badge/defectos_confirmados-6-c0392b)
![Cobertura de requisitos](https://img.shields.io/badge/cobertura_requisitos-85%25-2d6a4f)
![Veredicto](https://img.shields.io/badge/veredicto-apto_con_reservas-e08b00)

<sub>David Coya Moreno — QA Tester · [LinkedIn](https://linkedin.com/in/david-coya-moreno) ·
davidcoyamoreno@gmail.com</sub>

---

## El resultado en una tabla

| | |
| --- | --- |
| **Aplicación** | OrangeHRM OS 5.9 — instancia pública de demostración |
| **Módulo** | PIM (*Personal Information Management*) |
| **Casos ejecutados** | 36 de 38 — **94,7 %** |
| **Tasa de éxito** | **83,3 %** (30 superados · 6 fallados · 2 bloqueados) |
| **Defectos confirmados** | **6**, todos de severidad Media. Ninguno Crítico ni Alto |
| **Hipótesis descartadas** | **6** — 5 resultaron ser comportamiento correcto, 1 no verificable |
| **Cobertura de requisitos** | **85 %** (34 de 40), con los 6 huecos declarados y justificados |
| **Veredicto** | ⚠️ **APTO CON RESERVAS** — sin defectos Altos, pero la cobertura de ejecución queda por debajo del criterio de salida |

---

## Entregables

| # | Documento | Qué contiene |
| :---: | --- | --- |
| 00 | [Catálogo de requisitos](00-requisitos.md) | 40 requisitos derivados por ingeniería inversa, base de la trazabilidad |
| 01 | [Plan de pruebas](01-plan-de-pruebas.md) | Alcance, **fuera de alcance justificado**, estrategia, criterios de entrada y salida, 7 riesgos con mitigación |
| 02 | [Matriz de casos de prueba](02-casos-de-prueba.md) | 38 casos con requisito, técnica de diseño, prioridad y estado · también en [`.xlsx`](02-casos-de-prueba.xlsx) y [`.csv`](02-casos-de-prueba.csv) |
| 03 | [Reportes de defecto](03-bug-reports/) | 6 defectos confirmados, uno por fichero, con la petición de API observada |
| 03b | [Hipótesis descartadas](03-bug-reports/DESCARTADOS.md) | Las 6 sospechas que **no** llegaron a reportarse, y la comprobación que las descartó |
| 04 | [Informe de ejecución](04-informe-ejecucion.md) | Métricas, evaluación frente a los criterios de salida y recomendación técnica |
| 05 | [Matriz de trazabilidad](05-matriz-trazabilidad.md) | Cruce requisito → casos → defectos, con los huecos de cobertura declarados |
| — | [Guía de ejecución](CHECKLIST-EJECUCION.md) | Runbook para que un tercero reproduzca el ciclo y llegue al mismo resultado |

---

## Qué demuestra este repositorio

### 1. Se comprueba antes de reportar

De 12 hipótesis de defecto formuladas durante el diseño de los casos, **6 se confirmaron y 6 no**.
Las descartadas están documentadas con su comprobación en
[`DESCARTADOS.md`](03-bug-reports/DESCARTADOS.md), en lugar de desaparecer sin dejar rastro.

La más instructiva: se sospechaba que el campo de importe salarial aceptaba valores negativos, lo
que habría sido el defecto más grave del ciclo y sostenía por sí solo una recomendación de *no
apto*. Al comprobarlo, **el campo lo rechaza**:

```
Amount  →  Should be a number
```

Publicar ese reporte sin verificarlo habría producido dos daños: una recomendación de release
equivocada, y un defecto que el equipo de desarrollo habría cerrado como no reproducible. **Un
reporte inválido cuesta tiempo a todo el equipo y desgasta la credibilidad de los siguientes.**

### 2. Los casos se derivan, no se improvisan

Cada uno de los 38 casos declara la **técnica de diseño** de la que sale:

| Técnica | Casos | Ejemplo |
| --- | :---: | --- |
| Particiones de equivalencia | 12 | Una clase válida y las inválidas relevantes por campo, en vez de multiplicar entradas equivalentes |
| Valores límite | 8 | Longitud de nombre: 30 (límite) y 31 (límite + 1) |
| Tabla de decisión | 7 | El alta de empleado con y sin credenciales, modelada en [5 reglas](01-plan-de-pruebas.md#34-tabla-de-decisión--alta-de-empleado) |
| Conjetura de errores | 6 | Fechas futuras, importes negativos, campos con solo espacios |
| Transición de estados | 5 | Ciclo de vida del registro, incluidas las transiciones inválidas |

La [tabla de decisión del alta](01-plan-de-pruebas.md#34-tabla-de-decisión--alta-de-empleado)
ilustra el método: modelar las cinco reglas hizo aparecer un caso que la intuición no genera —qué
ocurre si falla el segundo bloque del formulario, la regla **R5**— y ese caso resultó ser uno de los
puntos donde la aplicación se comporta **mejor** de lo esperado. Una técnica de diseño sirve tanto
para encontrar fallos como para confirmar aciertos.

### 3. Los defectos apuntan al origen, no al síntoma

Cada reporte incluye la petición inspeccionada en las DevTools. Es lo que convierte una observación
de interfaz en un diagnóstico accionable.

> **Extracto de [BUG-011](03-bug-reports/BUG-011.md)** — *un empleado puede ser su propio supervisor*
>
> ```jsonc
> // POST /web/index.php/api/v2/pim/employees/{empNumber}/supervisors
> { "empNumber": 371, "reportingMethodId": 1 }   // el mismo empNumber de la ruta
> // → 200
> ```
>
> El servidor devuelve el propio empleado como su supervisor. La comprobación de que el `empNumber`
> del cuerpo difiere del de la ruta —la validación más simple posible de este problema— no existe.

El hallazgo transversal del ciclo salió de ahí: en **5 de los 6 defectos confirmados la API responde
200 ante datos que la lógica de negocio debería rechazar**. La consecuencia práctica es que corregir
solo el cliente no cierra ninguno de ellos, y eso cambia tanto la estimación como el diseño de la
regresión.

### 4. El criterio se ve en lo que se deja fuera

- **[Fuera de alcance explícito y justificado](01-plan-de-pruebas.md#22-qué-no-entra-en-el-alcance--y-por-qué):**
  cada exclusión lleva su motivo. Nada de pruebas de carga ni de seguridad ofensiva contra un
  servicio ajeno sin autorización — y dicho en el documento, no omitido.
- **Los casos bloqueados se cuentan como bloqueados**, no como superados ni fallados. Y se
  descartó borrar 37 empleados de una demo pública compartida para desbloquear uno de ellos: habría
  contaminado el entorno de los demás usuarios por una comprobación de severidad Media.
- **Severidad y prioridad se clasifican por separado**, y en
  [2 de los 6 defectos divergen](03-bug-reports/README.md#criterios-de-clasificación-aplicados).
- **Tres defectos se marcan «requiere confirmación de negocio»** porque dependen de reglas que el
  fabricante no documenta. Se reportan igual, pero marcados: un tester señala el riesgo, no decide
  el producto.
- **Los identificadores de los defectos descartados no se reutilizan.** Faltan BUG-002, 003, 004,
  005, 007 y 010, y eso es correcto: reasignar el identificador de un defecto retirado rompe la
  trazabilidad de cualquier conversación que lo mencionara.
- **El informe recoge también dónde la aplicación acierta.** Un informe que solo enumere fallos
  describe mal el producto.

### 5. La documentación se verifica sola

Los entregables no se mantienen a mano: se generan desde una única fuente y se comprueban.

```bash
python tools/generar-matriz.py        # → 02-casos-de-prueba.md · .csv · .xlsx
python tools/generar-trazabilidad.py  # → 05-matriz-trazabilidad.md
python tools/verificar.py             # comprueba que nada se contradiga
```

`verificar.py` comprueba que todo caso fallado tenga defecto, que todo defecto referencie un caso
existente, que los reportes tengan las secciones obligatorias y que las capturas enlazadas existan.
Devuelve código de salida 1 si algo no cuadra, así que puede encadenarse en CI.

Una matriz de 38 casos con referencias cruzadas se desincroniza sola a la tercera modificación. Que
esto sea comprobable es parte del entregable.

---

## Los 6 defectos confirmados

| Defecto | Módulo | Severidad | Prioridad |
| --- | --- | :---: | :---: |
| [BUG-001](03-bug-reports/BUG-001.md) — los campos de nombre aceptan dígitos y símbolos | Add Employee | Media | Media |
| [BUG-006](03-bug-reports/BUG-006.md) — «Date of Birth» acepta fechas futuras | Personal Details | Media | Media |
| [BUG-008](03-bug-reports/BUG-008.md) — «Dependents» acepta fecha de nacimiento futura | Dependents | Media | Baja |
| [BUG-009](03-bug-reports/BUG-009.md) — incorporación anterior a la fecha de nacimiento | Job | Media | Media |
| [BUG-011](03-bug-reports/BUG-011.md) — un empleado puede ser su propio supervisor | Report-to | Media | Media |
| [BUG-012](03-bug-reports/BUG-012.md) — los campos no exponen nombre accesible | Add Employee | Media | Baja |

La [recomendación](04-informe-ejecucion.md#7-conclusión-y-recomendación) no es «hay 6 defectos»,
sino un plan de acción ordenado: **6 defectos se resuelven con 3 líneas de trabajo**, porque cinco
de ellos comparten causa raíz.

---

## Entorno

| | |
| --- | --- |
| **URL** | `https://opensource-demo.orangehrmlive.com` |
| **Credenciales** | `Admin` / `admin123` — publicadas por el fabricante en su pantalla de acceso |
| **Sistema** | Windows 11 Pro 24H2 |
| **Navegadores** | Chrome (estable). La ejecución cruzada en Firefox y Edge está planificada para el ciclo 2 |
| **Herramientas** | DevTools (pestaña *Network* y panel *Accessibility*) · Markdown · Excel · Python para la generación de entregables |

### Nota sobre el entorno de pruebas

Las pruebas se ejecutan contra la instancia que **OrangeHRM publica expresamente para demostración y
aprendizaje**, a un ritmo equivalente al de un usuario real. No se ejecutan pruebas de carga,
escáneres ni pruebas de seguridad ofensiva contra ella, y los registros creados se eliminan al
terminar.

Probar sobre sistemas de terceros sin permiso no es una cuestión de estilo, sino de criterio
profesional: es la primera línea del
[plan de pruebas](01-plan-de-pruebas.md#22-qué-no-entra-en-el-alcance--y-por-qué) por ese motivo.

---

## Estructura

```
qa-portfolio-orangehrm/
├── 00-requisitos.md              Catálogo de requisitos (base de la trazabilidad)
├── 01-plan-de-pruebas.md         Alcance, estrategia, criterios y riesgos
├── 02-casos-de-prueba.md         Matriz de 38 casos  (+ .xlsx y .csv)
├── 03-bug-reports/               6 defectos confirmados + hipótesis descartadas
├── 04-informe-ejecucion.md       Métricas y recomendación de release
├── 05-matriz-trazabilidad.md     Requisito → casos → defectos
├── CHECKLIST-EJECUCION.md        Runbook para reproducir el ciclo
├── evidencias/                   Capturas de pantalla de los defectos
└── tools/                        Generación y verificación de los entregables
```

---

## Sobre el autor

**David Coya Moreno** — QA Tester. Testing manual funcional, de regresión, smoke y cross-browser;
automatización E2E con Selenium y Playwright; verificación de API REST con Postman; gestión del
defecto en Jira. Técnico Superior en Desarrollo de Aplicaciones Web, lo que explica que cada reporte
incluya la petición de API observada: leer el código y el tráfico de lo que se prueba acorta el ciclo
entre reportar y corregir.

Madrid · [LinkedIn](https://linkedin.com/in/david-coya-moreno) ·
[GitHub](https://github.com/Blistahub) · davidcoyamoreno@gmail.com

<sub>Documentación bajo [licencia MIT](LICENSE). OrangeHRM es marca de OrangeHRM Inc.; este
repositorio no está afiliado al fabricante y su único fin es formativo y de portfolio.</sub>
