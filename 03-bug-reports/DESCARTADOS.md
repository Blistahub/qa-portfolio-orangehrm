# Hipótesis de defecto descartadas

Seis comportamientos que durante el diseño de los casos se consideraron sospechosos y que, al
comprobarlos contra la aplicación, **resultaron ser correctos o no verificables en este entorno**.
No se han reportado como defectos.

Este documento existe porque el trabajo que lleva detrás es exactamente igual de real que el de los
defectos confirmados, y porque un defecto mal reportado cuesta tiempo a todo el equipo: el
desarrollador lo investiga, no lo reproduce, lo devuelve, y la confianza en los siguientes reportes
del mismo tester baja. **Comprobar antes de reportar es parte del trabajo, no un paso opcional.**

---

## Resumen

| Hipótesis | Caso | Veredicto | Qué ocurre en realidad |
| --- | --- | --- | --- |
| El alta con contraseña inválida deja el empleado creado | [CP-011](../02-casos-de-prueba.md#cp-011) | ❌ Descartada | La aplicación valida la contraseña **antes** de crear nada |
| La búsqueda por texto parcial devuelve «Invalid» | [CP-015](../02-casos-de-prueba.md#cp-015) | ❌ Descartada | La búsqueda parcial funciona con normalidad |
| La búsqueda no encuentra nombres con tilde | [CP-027](../02-casos-de-prueba.md#cp-027) | ❌ Descartada | La búsqueda es insensible a diacríticos |
| El campo de importe salarial acepta negativos | [CP-034](../02-casos-de-prueba.md#cp-034) | ❌ Descartada | El campo rechaza el importe negativo |
| La paginación no retrocede tras borrar el último registro | [CP-019](../02-casos-de-prueba.md#cp-019) | ⚠️ No verificable | El entorno no tiene registros suficientes para paginar |
| La ordenación se pierde al cambiar de página | [CP-020](../02-casos-de-prueba.md#cp-020) | ⚠️ No verificable | Mismo motivo |

---

## 1. El alta con contraseña inválida NO deja el empleado creado

**Hipótesis.** El formulario de alta guarda el empleado y sus credenciales en dos peticiones
separadas. Si la segunda falla por incumplir la política de contraseña, el empleado quedaría creado
sin acceso, y el administrador generaría un duplicado al reintentar.

**Comprobación.** Alta de `QaAtomic Prueba002` con *Create Login Details* activado y la contraseña
`test`, que incumple la política. Después, búsqueda del empleado en el listado.

**Resultado.** El empleado **no se crea**. En la pestaña *Network* se observa una única petición
antes del error:

```
POST /web/index.php/auth/public/validation/password    →  200
     { "password": "test" }
```

La aplicación consulta un **endpoint de validación de contraseña dedicado** y no continúa si la
política no se cumple. `POST /api/v2/pim/employees` no llega a emitirse. La operación es correcta
por diseño: el orden es validar primero, crear después.

**Por qué la hipótesis parecía razonable.** El formulario reúne dos entidades distintas —empleado y
usuario— en una sola pantalla, y ese patrón es una fuente habitual de escrituras parciales. La
sospecha estaba bien fundada; el diseño de la aplicación simplemente la resuelve mejor de lo
previsto.

---

## 2. La búsqueda por texto parcial funciona

**Hipótesis.** El campo *Employee Name* es un selector de entidad disfrazado de campo de texto, de
modo que escribir texto parcial sin elegir una sugerencia produciría el mensaje «Invalid» en vez de
buscar.

**Comprobación.** Escritura de un nombre parcial en el campo y pulsación directa de *Search*, sin
seleccionar sugerencia.

**Resultado.** La búsqueda **se ejecuta con normalidad** y devuelve resultados. En ningún momento
aparece el mensaje «Invalid».

**Matiz que conviene conservar.** El mensaje «Invalid» sí existe en la aplicación, pero se activa
ante un valor que no corresponde a ningún empleado, no ante un texto parcial legítimo. Confundir
ambos escenarios habría producido un reporte que el desarrollador no habría podido reproducir.

---

## 3. La búsqueda es insensible a los acentos

**Hipótesis.** Una colación de base de datos sensible a diacríticos impediría encontrar a un
empleado llamado `Mónica Núñez` buscando `Monica`.

**Comprobación.** Creación del empleado `Mónica Núñez` y dos búsquedas sobre el mismo listado:

```
GET /api/v2/pim/employees?…&nameOrId=Monica   →  1 resultado
GET /api/v2/pim/employees?…&nameOrId=Mónica   →  1 resultado
```

**Resultado.** Ambas búsquedas devuelven el empleado. La colación de las columnas de nombre
**equipara los diacríticos**, que es el comportamiento correcto.

**Lectura.** Era una hipótesis con fundamento —es un fallo frecuente en aplicaciones diseñadas con
datos en inglés y probadas solo con ellos— y merecía comprobarse. El resultado es que esta
aplicación lo hace bien.

---

## 4. El importe salarial rechaza los valores negativos

**Hipótesis.** El campo *Amount* de un componente salarial aceptaría `-1500`, permitiendo guardar
retribuciones negativas con impacto directo sobre la nómina.

**Comprobación.** Formulario *PIM > Salary > Add* con `-1500` en el campo *Amount*.

**Resultado.** El guardado se rechaza y el mensaje aparece **junto al campo correcto**:

```
Salary Component  →  Required
Currency          →  Required
Amount            →  Should be a number
```

El mensaje de *Amount* es específico del importe negativo: la validación del campo no admite el
signo menos. La hipótesis queda descartada.

**Importancia de haberlo comprobado.** Esta era, sobre el papel, la incidencia de mayor severidad
del ciclo, y era la que sostenía la recomendación de *no apto para release*. Publicarla sin
verificarla habría producido dos daños: una recomendación de release equivocada, y un reporte que el
equipo de desarrollo habría cerrado como no reproducible.

---

## 5 y 6. Los dos hallazgos de paginación no son verificables en este entorno

**Hipótesis.** (a) Al borrar el último registro de la última página, el listado queda vacío sin
retroceder de página. (b) La ordenación por columna se pierde al cambiar de página.

**Impedimento.** Ambas requieren un listado con **más de una página**. La paginación de PIM es de 50
registros y, en el momento de la ejecución, la instancia de demostración contenía **4 empleados**:

```
GET /api/v2/pim/employees?limit=1&offset=0…   →  meta.total = 4
```

La instancia pública se restablece periódicamente y el volumen de datos varía sin aviso — es
exactamente el **riesgo R-01** declarado en el [plan de pruebas](../01-plan-de-pruebas.md#7-análisis-de-riesgos).

**Decisión.** Los casos [CP-019](../02-casos-de-prueba.md#cp-019) y
[CP-020](../02-casos-de-prueba.md#cp-020) se registran como **bloqueados**, no como fallados ni como
superados. Un caso que no ha podido ejecutarse no aporta información sobre la calidad del producto,
y darlo por bueno en cualquiera de los dos sentidos sería inventarse un resultado.

**Descartado deliberadamente:** crear 50 empleados en una instancia pública compartida para forzar
la paginación. Habría contaminado el entorno de todos los demás usuarios de la demo por una
comprobación de severidad Baja. Queda pendiente de un entorno propio, y así se recoge en el
[informe de ejecución](../04-informe-ejecucion.md).

---

## Lo que estas seis comprobaciones dicen del ciclo

De 12 sospechas iniciales, **6 se confirmaron como defectos, 4 resultaron ser comportamiento
correcto y 2 no pudieron comprobarse**. Una tasa de acierto del 50 % sobre las hipótesis
verificables.

No es un mal dato: las hipótesis se formulan precisamente sobre los puntos donde una aplicación
*suele* fallar, y comprobarlas es barato comparado con el coste de un reporte inválido. Lo que sería
un mal dato es haber publicado las doce.

Las cuatro descartadas tienen además algo en común que merece anotarse: **en las cuatro, la
aplicación valida mejor de lo que la hipótesis suponía**, y en tres de ellas la validación está
además en el sitio correcto. Es un contrapeso honesto al hallazgo transversal del ciclo —que la
validación de dominio falta en varios endpoints— y evita que el informe pinte la aplicación peor de
lo que está.
