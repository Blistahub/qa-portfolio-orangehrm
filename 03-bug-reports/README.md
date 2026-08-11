# 03 — Reportes de defecto

**6 defectos confirmados** durante el ciclo de pruebas del módulo PIM. Uno por fichero, con
estructura fija: cabecera de clasificación, precondiciones, pasos, resultado esperado, resultado
obtenido, evidencia, **notas técnicas**, análisis de impacto, recomendación y **verificación**.

Otras 6 hipótesis de defecto se comprobaron y **no llegaron a reportarse**: 5 resultaron ser
comportamiento correcto y 1 no es verificable en este entorno. Están documentadas en
[`DESCARTADOS.md`](DESCARTADOS.md), con la comprobación que las descartó.

## Índice

| ID | Título | Severidad | Prioridad | Módulo | Caso |
| -- | ------ | --------- | --------- | ------ | ---- |
| [BUG-001](BUG-001.md) | Los campos de nombre aceptan cadenas numéricas y símbolos sin validación de formato | Media | Media | Add Employee | [CP-008](../02-casos-de-prueba.md#cp-008) |
| [BUG-006](BUG-006.md) | El campo «Date of Birth» acepta fechas futuras | Media | Media | Personal Details | [CP-024](../02-casos-de-prueba.md#cp-024) |
| [BUG-008](BUG-008.md) | «Dependents» acepta fecha de nacimiento futura en una persona a cargo | Media | Baja | Dependents | [CP-032](../02-casos-de-prueba.md#cp-032) |
| [BUG-009](BUG-009.md) | «Job» admite una fecha de incorporación anterior a la fecha de nacimiento | Media | Media | Job | [CP-033](../02-casos-de-prueba.md#cp-033) |
| [BUG-011](BUG-011.md) | «Report-to» permite asignar a un empleado como supervisor de sí mismo | Media | Media | Report-to | [CP-035](../02-casos-de-prueba.md#cp-035) |
| [BUG-012](BUG-012.md) | Los campos del formulario de alta no exponen nombre accesible | Media | Baja | Add Employee | [CP-038](../02-casos-de-prueba.md#cp-038) |

### Sobre los identificadores no correlativos

Faltan BUG-002, 003, 004, 005, 007 y 010. **No es un error de numeración.** Corresponden a
hipótesis que se descartaron al comprobarlas, y sus identificadores no se reasignan: reutilizar el
identificador de un defecto retirado rompe la trazabilidad de cualquier conversación, correo o
ticket que lo mencionara. Su destino está documentado en [`DESCARTADOS.md`](DESCARTADOS.md).

## Criterios de clasificación aplicados

**Severidad** es una propiedad del defecto: cuánto daño hace si se manifiesta. **Prioridad** es una
decisión de gestión: con qué urgencia conviene corregirlo. Se clasifican por separado de forma
deliberada, y en este ciclo divergen en dos defectos:

| Defecto | Severidad | Prioridad | Por qué divergen |
| --- | --- | --- | --- |
| [BUG-008](BUG-008.md) | Media | Baja | Afecta a datos con efectos fiscales, pero se rellena en raras ocasiones y siempre bajo supervisión. |
| [BUG-012](BUG-012.md) | Media | Baja | Inutiliza el formulario para lectores de pantalla, pero conviene corregirlo en el componente compartido dentro de una revisión más amplia. |

### Escala de severidad

| Nivel | Definición aplicada en este proyecto |
| --- | --- |
| **Crítica** | Impide el uso del módulo o provoca pérdida irreversible de datos, sin camino alternativo. *Ninguno detectado.* |
| **Alta** | Corrompe el dato maestro o produce un resultado económicamente incorrecto. Requiere intervención manual para reparar. *Ninguno detectado: la única sospecha de este nivel, el importe salarial negativo, quedó [descartada](DESCARTADOS.md#4-el-importe-salarial-rechaza-los-valores-negativos).* |
| **Media** | Funcionalidad incorrecta con camino alternativo disponible, o dato inconsistente sin efecto inmediato. |
| **Baja** | Molestia de usabilidad o presentación, sin impacto sobre los datos. |

## Defectos con causa raíz compartida

Tres defectos —[BUG-006](BUG-006.md), [BUG-008](BUG-008.md) y [BUG-009](BUG-009.md)— comparten una
misma causa: **el módulo carece de una validación de fechas transversal** y cada endpoint la resuelve
por separado, o no la resuelve. Se reportan de forma independiente porque son reproducibles y
corregibles por separado, pero se agrupan aquí para que no se aborden como tres parches aislados.

Detectar estas agrupaciones es parte del trabajo de reporte: cambia la estimación de la corrección y
evita que se cierre el síntoma dejando la causa abierta.

## El patrón que comparten cinco de los seis

En [BUG-001](BUG-001.md), [BUG-006](BUG-006.md), [BUG-008](BUG-008.md), [BUG-009](BUG-009.md) y
[BUG-011](BUG-011.md), la comprobación confirmó lo mismo: **la API responde 200 ante datos que la
lógica de negocio debería rechazar**. La sección *Verificación* de cada reporte recoge la petición
y la respuesta observadas.

La consecuencia práctica está desarrollada en el
[informe de ejecución](../04-informe-ejecucion.md#4-hallazgo-transversal-la-validación-de-dominio-falta-en-el-servidor):
corregir solo el cliente no cierra ninguno de los cinco.

## Nota sobre los defectos marcados «requiere confirmación de negocio»

Tres defectos ([BUG-006](BUG-006.md), [BUG-008](BUG-008.md) y [BUG-009](BUG-009.md)) llevan esa
marca. Dependen de reglas de negocio **derivadas por el tester, no documentadas por el fabricante**
(ver la nota metodológica de [`00-requisitos.md`](../00-requisitos.md)).

Se reportan igualmente, porque el riesgo existe y hay que ponerlo sobre la mesa, pero se marcan para
que quien lea el informe sepa distinguir entre *«esto incumple un requisito acordado»* y *«esto
contradice lo que cabe esperar y conviene que alguien lo confirme»*. Un tester señala el riesgo; la
decisión de producto no le corresponde.
