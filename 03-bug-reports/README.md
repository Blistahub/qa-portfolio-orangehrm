# 03 — Reportes de defecto

12 defectos detectados durante el ciclo de pruebas del módulo PIM. Uno por fichero, con estructura
fija: cabecera de clasificación, precondiciones, pasos, resultado esperado, resultado obtenido,
evidencia, **notas técnicas**, análisis de impacto y recomendación.

## Índice

| ID | Título | Severidad | Prioridad | Módulo | Caso |
| -- | ------ | --------- | --------- | ------ | ---- |
| [BUG-001](BUG-001.md) | Los campos de nombre aceptan cadenas numéricas y símbolos sin validación de formato | Media | Media | Add Employee | [CP-008](../02-casos-de-prueba.md#cp-008) |
| [BUG-002](BUG-002.md) | Un fallo de validación de la contraseña deja el empleado creado sin sus credenciales | **Alta** | **Alta** | Add Employee | [CP-011](../02-casos-de-prueba.md#cp-011) |
| [BUG-003](BUG-003.md) | El buscador etiqueta como «Invalid» un nombre correcto si no se elige una sugerencia | Media | **Alta** | Employee List | [CP-015](../02-casos-de-prueba.md#cp-015) |
| [BUG-004](BUG-004.md) | Al borrar el último registro de la última página, el listado queda vacío sin retroceder | Media | Media | Employee List | [CP-019](../02-casos-de-prueba.md#cp-019) |
| [BUG-005](BUG-005.md) | La ordenación por columna se pierde al cambiar de página del listado | Baja | Baja | Employee List | [CP-020](../02-casos-de-prueba.md#cp-020) |
| [BUG-006](BUG-006.md) | El campo «Date of Birth» acepta fechas futuras | Media | Media | Personal Details | [CP-024](../02-casos-de-prueba.md#cp-024) |
| [BUG-007](BUG-007.md) | La búsqueda de empleados no es insensible a los acentos | Baja | Media | Employee List | [CP-027](../02-casos-de-prueba.md#cp-027) |
| [BUG-008](BUG-008.md) | «Dependents» acepta fecha de nacimiento futura en una persona a cargo | Media | Baja | Dependents | [CP-032](../02-casos-de-prueba.md#cp-032) |
| [BUG-009](BUG-009.md) | «Job» admite una fecha de incorporación anterior a la fecha de nacimiento | Media | Media | Job | [CP-033](../02-casos-de-prueba.md#cp-033) |
| [BUG-010](BUG-010.md) | El componente salarial acepta importes negativos | **Alta** | **Alta** | Salary | [CP-034](../02-casos-de-prueba.md#cp-034) |
| [BUG-011](BUG-011.md) | «Report-to» permite asignar a un empleado como supervisor de sí mismo | Media | Media | Report-to | [CP-035](../02-casos-de-prueba.md#cp-035) |
| [BUG-012](BUG-012.md) | Los campos del formulario de alta no exponen nombre accesible | Media | Baja | Add Employee | [CP-038](../02-casos-de-prueba.md#cp-038) |

## Criterios de clasificación aplicados

**Severidad** es una propiedad del defecto: cuánto daño hace si se manifiesta. **Prioridad** es una
decisión de gestión: con qué urgencia conviene corregirlo. Se clasifican por separado de forma
deliberada, y en este ciclo divergen en cuatro defectos:

| Defecto | Severidad | Prioridad | Por qué divergen |
| --- | --- | --- | --- |
| [BUG-003](BUG-003.md) | Media | Alta | Daño bajo, pero afecta a la operación más frecuente del módulo y el mensaje desorienta al usuario. |
| [BUG-007](BUG-007.md) | Baja | Media | Existe camino alternativo, pero en una plantilla española los nombres acentuados son mayoritarios. |
| [BUG-008](BUG-008.md) | Media | Baja | Afecta a datos con efectos fiscales, pero se rellena en raras ocasiones y siempre bajo supervisión. |
| [BUG-012](BUG-012.md) | Media | Baja | Inutiliza el formulario para lectores de pantalla, pero conviene corregirlo en el componente compartido dentro de una revisión más amplia. |

### Escala de severidad

| Nivel | Definición aplicada en este proyecto |
| --- | --- |
| **Crítica** | Impide el uso del módulo o provoca pérdida irreversible de datos, sin camino alternativo. *Ninguno detectado en este ciclo.* |
| **Alta** | Corrompe el dato maestro o produce un resultado económicamente incorrecto. Requiere intervención manual para reparar. |
| **Media** | Funcionalidad incorrecta con camino alternativo disponible, o dato inconsistente sin efecto inmediato. |
| **Baja** | Molestia de usabilidad o presentación, sin impacto sobre los datos. |

## Defectos con causa raíz compartida

Tres defectos —[BUG-006](BUG-006.md), [BUG-008](BUG-008.md) y [BUG-009](BUG-009.md)— comparten una
misma causa: **el módulo carece de una validación de fechas transversal** y cada endpoint la resuelve
por separado, o no la resuelve. Se reportan de forma independiente porque son reproducibles y
corregibles por separado, pero se agrupan aquí para que no se aborden como tres parches aislados.

Otros dos —[BUG-004](BUG-004.md) y [BUG-005](BUG-005.md)— comparten a su vez la causa de que **el
estado de la consulta del listado se reconstruye en cada paginación** en lugar de mantenerse unificado.

Detectar estas agrupaciones es parte del trabajo de reporte: cambia la estimación de la corrección y
evita que se cierre el síntoma dejando la causa abierta.

## Nota sobre los defectos marcados «requiere confirmación de negocio»

Cuatro defectos ([BUG-006](BUG-006.md), [BUG-008](BUG-008.md), [BUG-009](BUG-009.md) y
[BUG-010](BUG-010.md)) llevan esa marca. Todos ellos dependen de una regla de negocio **derivada por
el tester, no documentada por el fabricante** (ver la nota metodológica de
[`00-requisitos.md`](../00-requisitos.md)).

Se reportan igualmente, porque el riesgo existe y hay que ponerlo sobre la mesa, pero se marcan para
que quien lea el informe sepa distinguir entre *«esto incumple un requisito acordado»* y *«esto
contradice lo que cabe esperar y conviene que alguien lo confirme»*. Un tester señala el riesgo; la
decisión de producto no le corresponde.
