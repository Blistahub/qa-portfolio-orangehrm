# Portfolio de QA manual — Módulo PIM de OrangeHRM

**Ciclo de pruebas funcionales completo sobre el módulo de gestión de empleados de un ERP de RRHH:
del plan de pruebas a la recomendación de release.**

38 casos diseñados con técnicas formales · 12 defectos documentados · trazabilidad requisito → caso →
defecto · análisis de causa raíz sobre las peticiones de la API.

<sub>David Coya Moreno — QA Tester · [LinkedIn](https://linkedin.com/in/david-coya-moreno) ·
davidcoyamoreno@gmail.com</sub>

---

## El resultado en una tabla

| | |
| --- | --- |
| **Aplicación** | OrangeHRM OS 5.x — instancia pública de demostración |
| **Módulo** | PIM (*Personal Information Management*) |
| **Casos ejecutados** | 37 de 38 — **97,4 %** |
| **Tasa de éxito** | **67,6 %** (25 superados · 12 fallados · 1 bloqueado) |
| **Defectos** | **12** — 2 de severidad Alta, 8 Media, 2 Baja |
| **Cobertura de requisitos** | **85 %** (34 de 40), con los 6 huecos declarados y justificados |
| **Veredicto** | ❌ **NO APTO para release** — dos defectos Alta abiertos incumplen el criterio de salida |

---

## Entregables

| # | Documento | Qué contiene |
| :---: | --- | --- |
| 00 | [Catálogo de requisitos](00-requisitos.md) | 40 requisitos derivados por ingeniería inversa, base de la trazabilidad |
| 01 | [Plan de pruebas](01-plan-de-pruebas.md) | Alcance, **fuera de alcance justificado**, estrategia, criterios de entrada y salida, 7 riesgos con mitigación |
| 02 | [Matriz de casos de prueba](02-casos-de-prueba.md) | 38 casos con requisito, técnica de diseño, prioridad y estado · también en [`.xlsx`](02-casos-de-prueba.xlsx) y [`.csv`](02-casos-de-prueba.csv) |
| 03 | [Reportes de defecto](03-bug-reports/) | 12 defectos, uno por fichero, con notas de API y análisis de impacto |
| 04 | [Informe de ejecución](04-informe-ejecucion.md) | Métricas, evaluación frente a los criterios de salida y recomendación técnica |
| 05 | [Matriz de trazabilidad](05-matriz-trazabilidad.md) | Cruce requisito → casos → defectos, con los huecos de cobertura declarados |
| — | [Guía de ejecución](CHECKLIST-EJECUCION.md) | Runbook para que un tercero reproduzca el ciclo y llegue al mismo resultado |

---

## Qué demuestra este repositorio

### 1. Los casos se derivan, no se improvisan

Cada uno de los 38 casos declara la **técnica de diseño** de la que sale:

| Técnica | Casos | Ejemplo |
| --- | :---: | --- |
| Particiones de equivalencia | 12 | Una clase válida y las inválidas relevantes por campo, en vez de multiplicar entradas equivalentes |
| Valores límite | 8 | Longitud de nombre: 30 (límite) y 31 (límite + 1) |
| Tabla de decisión | 7 | El alta de empleado con y sin credenciales — la regla **R5** es la que descubrió [BUG-002](03-bug-reports/BUG-002.md) |
| Conjetura de errores | 6 | Fechas futuras, importes negativos, campos con solo espacios |
| Transición de estados | 5 | Ciclo de vida del registro, incluidas las transiciones inválidas |

La [tabla de decisión del alta](01-plan-de-pruebas.md#34-tabla-de-decisión--alta-de-empleado) es el
mejor ejemplo del método: modelar las cinco reglas hizo aparecer un caso que la intuición no genera
—qué ocurre si falla el segundo bloque del formulario— y ese caso destapó el defecto más grave del
ciclo.

### 2. Los defectos apuntan al origen, no al síntoma

Cada reporte incluye una sección de **notas técnicas** con la petición inspeccionada en las DevTools.
Es lo que convierte una observación de interfaz en un diagnóstico accionable.

> **Extracto de [BUG-002](03-bug-reports/BUG-002.md)** — *el alta de empleado no es atómica*
>
> Al pulsar Save se observan en la pestaña *Network* **dos peticiones consecutivas e
> independientes**:
>
> 1. `POST /api/v2/pim/employees` → **200 OK**, el empleado queda persistido.
> 2. `POST /api/v2/admin/users` → **422**, incumplimiento de la política de contraseña.
>
> El formulario es una única pantalla para el usuario, pero **dos transacciones separadas** para el
> sistema. Por eso el fallo de la segunda no revierte la primera, y el resultado es un empleado
> creado sin credenciales que el administrador duplica al reintentar.

El hallazgo transversal del ciclo salió de ahí: en **6 de los 12 defectos la API responde 200 ante
datos que la lógica de negocio debería rechazar**. La consecuencia práctica es que corregir solo el
cliente no cierra ninguno de ellos, y eso cambia tanto la estimación como el diseño de la regresión.

### 3. El criterio se ve en lo que se deja fuera

- **[Fuera de alcance explícito y justificado](01-plan-de-pruebas.md#22-qué-no-entra-en-el-alcance--y-por-qué):**
  cada exclusión lleva su motivo. Nada de pruebas de carga ni de seguridad ofensiva contra un
  servicio ajeno sin autorización — y dicho en el documento, no omitido.
- **Severidad y prioridad se clasifican por separado**, y en
  [4 de los 12 defectos divergen](03-bug-reports/#criterios-de-clasificación-aplicados). Severidad es
  cuánto daño hace; prioridad es con qué urgencia conviene corregirlo.
- **Cuatro defectos se marcan «requiere confirmación de negocio»** porque dependen de reglas que el
  fabricante no documenta. Se reportan igual, pero marcados: un tester señala el riesgo, no decide
  el producto.
- **Los huecos de cobertura se declaran** con su motivo. Un informe con el 100 % sin explicar cómo
  lo consigue es menos fiable que uno que reconoce dónde no ha llegado.
- **Un caso bloqueado se cuenta como bloqueado, no como fallado.** Un caso que no se ha podido
  ejecutar no dice nada sobre la calidad del producto.

### 4. La documentación se verifica sola

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

## Los dos defectos que bloquean el release

| Defecto | Severidad | Por qué bloquea |
| --- | :---: | --- |
| [BUG-010](03-bug-reports/BUG-010.md) — el componente salarial acepta importes negativos | Alta | Corrompe un dato con efecto económico directo sobre la nómina, y puede reducir el total en silencio |
| [BUG-002](03-bug-reports/BUG-002.md) — el alta de empleado no es atómica | Alta | Genera empleados duplicados en el dato maestro por el camino de error más frecuente del formulario |

La [recomendación](04-informe-ejecucion.md#7-conclusión-y-recomendación) no es «hay 12 defectos»,
sino un plan de acción ordenado: **12 defectos reportados se resuelven con 7 líneas de trabajo**,
porque cinco de ellos comparten causa raíz con otros.

---

## Entorno

| | |
| --- | --- |
| **URL** | `https://opensource-demo.orangehrmlive.com` |
| **Credenciales** | `Admin` / `admin123` — publicadas por el fabricante en su pantalla de acceso |
| **Sistema** | Windows 11 Pro 24H2 |
| **Navegadores** | Chrome · Firefox · Edge (los 15 casos de prioridad Alta en los tres) |
| **Herramientas** | DevTools (pestaña *Network* y panel *Accessibility*) · Markdown · Excel · Python para la generación de entregables |

### Nota sobre el entorno de pruebas

Todas las pruebas se ejecutan contra la instancia que **OrangeHRM publica expresamente para
demostración y aprendizaje**, exclusivamente de forma manual y a través de la interfaz, a un ritmo
equivalente al de un usuario real. No se ejecutan scripts automatizados, escáneres ni pruebas de
carga contra ella, y los datos creados se eliminan al terminar cuando el caso lo permite.

Probar sobre sistemas de terceros sin permiso no es una cuestión de estilo, sino de criterio
profesional: es la primera línea del [plan de pruebas](01-plan-de-pruebas.md#22-qué-no-entra-en-el-alcance--y-por-qué)
por ese motivo.

---

## Estructura

```
qa-portfolio-orangehrm/
├── 00-requisitos.md              Catálogo de requisitos (base de la trazabilidad)
├── 01-plan-de-pruebas.md         Alcance, estrategia, criterios y riesgos
├── 02-casos-de-prueba.md         Matriz de 38 casos  (+ .xlsx y .csv)
├── 03-bug-reports/               12 reportes de defecto + índice
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
defecto en Jira. Técnico Superior en Desarrollo de Aplicaciones Web, lo que explica la sección de
*notas técnicas* de cada reporte: leer el código y las peticiones de lo que se prueba acorta el ciclo
entre reportar y corregir.

Madrid · [LinkedIn](https://linkedin.com/in/david-coya-moreno) ·
[GitHub](https://github.com/Blistahub) · davidcoyamoreno@gmail.com

<sub>Documentación bajo [licencia MIT](LICENSE). OrangeHRM es marca de OrangeHRM Inc.; este
repositorio no está afiliado al fabricante y su único fin es formativo y de portfolio.</sub>
