# 02 — Matriz de casos de prueba · Módulo PIM

**38 casos** diseñados sobre el catálogo de [requisitos](00-requisitos.md), siguiendo la
estrategia del [plan de pruebas](01-plan-de-pruebas.md).

> Fichero generado automáticamente por `tools/generar-matriz.py` a partir de `tools/casos.py`.
> No editar a mano: los tres formatos entregables —`.md`, `.csv` y `.xlsx`— salen de la misma
> fuente para que no puedan divergir.

**Otros formatos:** [`02-casos-de-prueba.xlsx`](02-casos-de-prueba.xlsx) ·
[`02-casos-de-prueba.csv`](02-casos-de-prueba.csv)

| Estado | Casos | | Prioridad | Casos | | Técnica de diseño | Casos |
| ------ | ----: | - | --------- | ----: | - | ----------------- | ----: |
| Pasa | 29 | | Alta | 15 | | Particiones de equivalencia | 12 |
| Falla | 6 | | Media | 21 | | Valores límite | 8 |
| Bloqueado | 3 | | Baja | 2 | | Tabla de decisión | 7 |
|  |  | |  |  | | Conjetura de errores | 6 |
|  |  | |  |  | | Transición de estados | 5 |

---

## Resumen de la matriz

| ID | Requisito | Título | Prioridad | Tipo | Técnica | Estado | Defecto |
| -- | --------- | ------ | --------- | ---- | ------- | ------ | ------- |
| `CP-001` | RF-01, RF-09 | [Alta de empleado con los datos mínimos obligatorios](#cp-001) | Alta | Funcional / Smoke | Tabla de decisión (R1) | 🟢 Pasa | — |
| `CP-002` | RF-01 | [El alta sin First Name se rechaza](#cp-002) | Alta | Funcional negativo | Tabla de decisión (R2) | 🟢 Pasa | — |
| `CP-003` | RF-01 | [El alta sin Last Name se rechaza](#cp-003) | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-004` | RF-02 | [First Name admite exactamente 30 caracteres (límite superior)](#cp-004) | Media | Funcional positivo | Valores límite | 🟢 Pasa | — |
| `CP-005` | RF-02 | [First Name no admite 31 caracteres (límite superior + 1)](#cp-005) | Media | Funcional negativo | Valores límite | 🟢 Pasa | — |
| `CP-006` | RF-04 | [El alta con un Employee Id ya existente se rechaza](#cp-006) | Alta | Funcional negativo | Tabla de decisión (R3) | 🟢 Pasa | — |
| `CP-007` | RF-01 | [El alta con nombres compuestos solo por espacios en blanco se rechaza](#cp-007) | Media | Funcional negativo | Conjetura de errores | 🟢 Pasa | — |
| `CP-008` | RF-01 | [Los campos de nombre no admiten dígitos ni caracteres especiales](#cp-008) | Media | Funcional negativo | Particiones de equivalencia | 🔴 Falla | [BUG-001](03-bug-reports/BUG-001.md) |
| `CP-009` | RF-05 | [La foto de perfil por encima de 1 MB se rechaza](#cp-009) | Media | Funcional negativo | Valores límite | 🟢 Pasa | — |
| `CP-010` | RF-06, RF-07, RF-08 | [Alta de empleado con credenciales de acceso válidas](#cp-010) | Alta | Funcional positivo | Tabla de decisión (R4) | 🟢 Pasa | — |
| `CP-011` | RF-08, RF-09 | [Una contraseña que incumple la política no debe dejar el empleado creado](#cp-011) | Alta | Funcional negativo | Tabla de decisión (R5) | 🟢 Pasa | — |
| `CP-012` | RF-07 | [El nombre de usuario por debajo de 5 caracteres se rechaza](#cp-012) | Media | Funcional negativo | Valores límite | 🟢 Pasa | — |
| `CP-013` | RF-10 | [Búsqueda de empleado por Employee Id exacto](#cp-013) | Alta | Funcional / Smoke | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-014` | RF-11 | [El autocompletado de Employee Name sugiere a partir del tercer carácter](#cp-014) | Media | Funcional positivo | Valores límite | 🟢 Pasa | — |
| `CP-015` | RF-11 | [Búsqueda con texto parcial válido sin seleccionar sugerencia](#cp-015) | Media | Usabilidad | Conjetura de errores | 🟢 Pasa | — |
| `CP-016` | RF-12 | [El filtro combinado aplica conjunción lógica entre criterios](#cp-016) | Alta | Funcional positivo | Tabla de decisión | 🟢 Pasa | — |
| `CP-017` | RF-16 | [Búsqueda sin coincidencias muestra «No Records Found»](#cp-017) | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-018` | RF-13 | [El botón Reset limpia todos los filtros y restaura el listado](#cp-018) | Alta | Funcional / Smoke | Transición de estados | 🟢 Pasa | — |
| `CP-019` | RF-14, RF-17 | [Al eliminar el último registro de la última página el listado se reubica](#cp-019) | Media | Funcional negativo | Valores límite | 🟡 Bloqueado | — |
| `CP-020` | RF-15 | [La ordenación por columna se mantiene al cambiar de página](#cp-020) | Baja | Funcional | Transición de estados | 🟡 Bloqueado | — |
| `CP-021` | RF-17 | [Borrado múltiple de empleados con confirmación previa](#cp-021) | Alta | Funcional positivo | Transición de estados | 🟢 Pasa | — |
| `CP-022` | RF-18, RF-22 | [Edición y guardado de los datos personales de un empleado](#cp-022) | Alta | Funcional positivo | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-023` | RF-19, RF-20 | [La fecha de nacimiento con formato inválido se rechaza](#cp-023) | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-024` | RN-01 | [La fecha de nacimiento no admite fechas futuras](#cp-024) | Alta | Funcional negativo | Conjetura de errores | 🔴 Falla | [BUG-006](03-bug-reports/BUG-006.md) |
| `CP-025` | RF-18, RN-04 | [Permiso de conducir con fecha de caducidad pasada](#cp-025) | Baja | Funcional positivo | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-026` | RF-22 | [Los cambios en la ficha se reflejan en el listado de empleados](#cp-026) | Alta | Funcional / Smoke | Transición de estados | 🟢 Pasa | — |
| `CP-027` | RF-10, RF-18 | [Nombres con tildes y caracteres no ASCII: guardado y búsqueda](#cp-027) | Media | Funcional | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-028` | RF-18, RNF-02 | [El contenido con etiquetas HTML se escapa al mostrarse](#cp-028) | Alta | Funcional negativo | Conjetura de errores | 🟢 Pasa | — |
| `CP-029` | RF-23 | [Los campos de teléfono no admiten letras](#cp-029) | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-030` | RF-24 | [El correo electrónico con formato inválido se rechaza](#cp-030) | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-031` | RF-25 | [Alta, edición y borrado de un contacto de emergencia](#cp-031) | Alta | Funcional / Smoke | Transición de estados | 🟢 Pasa | — |
| `CP-032` | RF-26, RN-01 | [Una persona a cargo no admite fecha de nacimiento futura](#cp-032) | Media | Funcional negativo | Conjetura de errores | 🔴 Falla | [BUG-008](03-bug-reports/BUG-008.md) |
| `CP-033` | RN-02 | [La fecha de incorporación no puede ser anterior a la de nacimiento](#cp-033) | Media | Funcional negativo | Tabla de decisión | 🔴 Falla | [BUG-009](03-bug-reports/BUG-009.md) |
| `CP-034` | RF-28, RN-03 | [El importe salarial no admite valores negativos](#cp-034) | Alta | Funcional negativo | Valores límite | 🟢 Pasa | — |
| `CP-035` | RF-29 | [Un empleado no puede asignarse a sí mismo como supervisor](#cp-035) | Media | Funcional negativo | Conjetura de errores | 🔴 Falla | [BUG-011](03-bug-reports/BUG-011.md) |
| `CP-036` | RF-30 | [El adjunto que supera el tamaño máximo configurado se rechaza](#cp-036) | Media | Funcional negativo | Valores límite | 🟡 Bloqueado | — |
| `CP-037` | RNF-01 | [El listado de empleados es operativo en viewport móvil](#cp-037) | Media | Responsive | Particiones de equivalencia | 🟢 Pasa | — |
| `CP-038` | RNF-03 | [Los campos del formulario de alta tienen etiqueta asociada](#cp-038) | Media | Accesibilidad | Particiones de equivalencia | 🔴 Falla | [BUG-012](03-bug-reports/BUG-012.md) |

---

## Detalle de cada caso


### CP-001

**Alta de empleado con los datos mínimos obligatorios**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-01, RF-09 | Alta | Funcional / Smoke | Tabla de decisión (R1) | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: Lucía · Last Name: Herrera

**Pasos**

1. Ir a PIM > Add Employee.
2. Introducir First Name y Last Name.
3. Dejar «Create Login Details» desactivado.
4. Pulsar Save.

**Resultado esperado:** El empleado se crea, aparece el aviso «Successfully Saved» y la aplicación redirige a la ficha del empleado con el Employee Id asignado.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-002

**El alta sin First Name se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-01 | Alta | Funcional negativo | Tabla de decisión (R2) | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: (vacío) · Last Name: Herrera

**Pasos**

1. Ir a PIM > Add Employee.
2. Dejar First Name vacío e introducir solo Last Name.
3. Pulsar Save.

**Resultado esperado:** El empleado no se crea y aparece el mensaje «Required» bajo el campo First Name.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-003

**El alta sin Last Name se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-01 | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: Lucía · Last Name: (vacío)

**Pasos**

1. Ir a PIM > Add Employee.
2. Introducir solo First Name.
3. Pulsar Save.

**Resultado esperado:** El empleado no se crea y aparece el mensaje «Required» bajo el campo Last Name.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-004

**First Name admite exactamente 30 caracteres (límite superior)**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-02 | Media | Funcional positivo | Valores límite | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: Abcdefghijklmnopqrstuvwxyzabcd (30) · Last Name: Herrera

**Pasos**

1. Ir a PIM > Add Employee.
2. Pegar en First Name una cadena de 30 caracteres.
3. Introducir un Last Name válido.
4. Pulsar Save y abrir la ficha creada.

**Resultado esperado:** El empleado se crea y el nombre se almacena y se muestra completo, sin truncar.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-005

**First Name no admite 31 caracteres (límite superior + 1)**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-02 | Media | Funcional negativo | Valores límite | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: Abcdefghijklmnopqrstuvwxyzabcde (31)

**Pasos**

1. Ir a PIM > Add Employee.
2. Pegar en First Name una cadena de 31 caracteres.
3. Observar el contenido del campo.
4. Pulsar Save.

**Resultado esperado:** El campo impide superar los 30 caracteres o el sistema muestra un error de longitud. En ningún caso se guarda un valor truncado en silencio.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-006

**El alta con un Employee Id ya existente se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-04 | Alta | Funcional negativo | Tabla de decisión (R3) | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Existe un empleado con Employee Id conocido.

**Datos de prueba:** Employee Id: (uno ya existente en el listado)

**Pasos**

1. Anotar el Employee Id de un empleado existente desde PIM > Employee List.
2. Ir a PIM > Add Employee.
3. Introducir nombre y apellido válidos.
4. Sustituir el Employee Id autogenerado por el anotado en el paso 1.
5. Pulsar Save.

**Resultado esperado:** El empleado no se crea y se muestra un mensaje indicando que el Employee Id ya está en uso.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-007

**El alta con nombres compuestos solo por espacios en blanco se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-01 | Media | Funcional negativo | Conjetura de errores | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: «   » · Last Name: «   »

**Pasos**

1. Ir a PIM > Add Employee.
2. Introducir tres espacios en First Name y tres en Last Name.
3. Pulsar Save.

**Resultado esperado:** El sistema trata los campos como vacíos y muestra «Required». No se crea un empleado sin nombre visible en el listado.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-008

**Los campos de nombre no admiten dígitos ni caracteres especiales**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-01 | Media | Funcional negativo | Particiones de equivalencia | 🔴 Falla | [BUG-001](03-bug-reports/BUG-001.md) |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: 12345 · Last Name: !@#$%^&*()

**Pasos**

1. Ir a PIM > Add Employee.
2. Introducir en First Name una cadena numérica y en Last Name símbolos.
3. Pulsar Save.
4. Volver a PIM > Employee List y localizar el registro.

**Resultado esperado:** El sistema rechaza la entrada con un mensaje de validación de formato: un nombre de persona no admite dígitos ni símbolos.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-009

**La foto de perfil por encima de 1 MB se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-05 | Media | Funcional negativo | Valores límite | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Fichero de imagen de ~1,2 MB disponible.

**Datos de prueba:** Fichero: foto-1200kb.jpg (1,2 MB)

**Pasos**

1. Ir a PIM > Add Employee.
2. Pulsar sobre el área de la foto y seleccionar el fichero de 1,2 MB.
3. Introducir nombre y apellido válidos.
4. Pulsar Save.

**Resultado esperado:** El sistema rechaza el fichero indicando que se supera el tamaño máximo permitido, y no crea el empleado con una foto inválida.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-010

**Alta de empleado con credenciales de acceso válidas**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-06, RF-07, RF-08 | Alta | Funcional positivo | Tabla de decisión (R4) | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** Usuario: dcoya.test01 · Contraseña: Test1234

**Pasos**

1. Ir a PIM > Add Employee.
2. Introducir nombre y apellido válidos.
3. Activar «Create Login Details».
4. Introducir usuario y contraseña que cumplen la política, estado Enabled.
5. Pulsar Save.
6. Comprobar en Admin > User Management que el usuario aparece.

**Resultado esperado:** El empleado se crea con su usuario asociado y este figura en la lista de usuarios del sistema con estado Enabled.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-011

**Una contraseña que incumple la política no debe dejar el empleado creado**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-08, RF-09 | Alta | Funcional negativo | Tabla de decisión (R5) | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** Usuario: dcoya.test02 · Contraseña: test

**Pasos**

1. Ir a PIM > Add Employee.
2. Introducir nombre y apellido válidos.
3. Activar «Create Login Details».
4. Introducir un usuario válido y la contraseña «test» (incumple la política).
5. Pulsar Save.
6. Ir a PIM > Employee List y buscar el nombre introducido.

**Resultado esperado:** El formulario muestra el error de política de contraseña y NO se crea el empleado: la operación es atómica.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-012

**El nombre de usuario por debajo de 5 caracteres se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-07 | Media | Funcional negativo | Valores límite | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** Usuario: dcoy (4 caracteres) · Contraseña: Test1234

**Pasos**

1. Ir a PIM > Add Employee.
2. Introducir nombre y apellido válidos.
3. Activar «Create Login Details».
4. Introducir un usuario de 4 caracteres y una contraseña válida.
5. Pulsar Save.

**Resultado esperado:** El sistema muestra el mensaje de longitud mínima del nombre de usuario y no crea el registro.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-013

**Búsqueda de empleado por Employee Id exacto**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-10 | Alta | Funcional / Smoke | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Existe un empleado con Employee Id conocido.

**Datos de prueba:** Employee Id: (el del empleado creado en CP-001)

**Pasos**

1. Ir a PIM > Employee List.
2. Introducir el Employee Id en el campo correspondiente.
3. Pulsar Search.

**Resultado esperado:** El listado devuelve únicamente el empleado con ese identificador y el contador indica «(1) Record Found».

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-014

**El autocompletado de Employee Name sugiere a partir del tercer carácter**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-11 | Media | Funcional positivo | Valores límite | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** Texto: «Lu» y después «Luc»

**Pasos**

1. Ir a PIM > Employee List.
2. Escribir dos caracteres en Employee Name y esperar.
3. Escribir un tercer carácter y esperar.

**Resultado esperado:** Con dos caracteres no se despliegan sugerencias; con tres aparece la lista de coincidencias.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-015

**Búsqueda con texto parcial válido sin seleccionar sugerencia**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-11 | Media | Usabilidad | Conjetura de errores | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Existe al menos un empleado cuyo nombre empieza por «Luc».

**Datos de prueba:** Texto: Luc

**Pasos**

1. Ir a PIM > Employee List.
2. Escribir «Luc» en Employee Name sin pulsar ninguna sugerencia.
3. Pulsar Search.

**Resultado esperado:** El sistema busca por coincidencia parcial y devuelve los empleados cuyo nombre contiene el texto, o bien indica con claridad que debe elegirse una sugerencia. No debe etiquetarse como «Invalid» un dato correcto.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-016

**El filtro combinado aplica conjunción lógica entre criterios**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-12 | Alta | Funcional positivo | Tabla de decisión | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** Sub Unit: Engineering · Employment Status: Full-Time Permanent

**Pasos**

1. Ir a PIM > Employee List.
2. Seleccionar una Sub Unit con varios empleados.
3. Seleccionar además un Employment Status.
4. Pulsar Search.
5. Revisar las columnas del resultado.

**Resultado esperado:** Todos los registros devueltos cumplen simultáneamente los dos criterios; ninguno cumple solo uno.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-017

**Búsqueda sin coincidencias muestra «No Records Found»**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-16 | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** Employee Id: ZZ999999

**Pasos**

1. Ir a PIM > Employee List.
2. Introducir un Employee Id inexistente.
3. Pulsar Search.

**Resultado esperado:** Se muestra el aviso «No Records Found», la tabla queda vacía y la cabecera y los filtros siguen operativos.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-018

**El botón Reset limpia todos los filtros y restaura el listado**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-13 | Alta | Funcional / Smoke | Transición de estados | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Hay una búsqueda filtrada aplicada.

**Datos de prueba:** —

**Pasos**

1. Aplicar un filtro por Sub Unit y otro por Employment Status.
2. Pulsar Search y comprobar que el listado se reduce.
3. Pulsar Reset.

**Resultado esperado:** Todos los campos de filtro vuelven a su valor por defecto y el listado muestra de nuevo el total de empleados.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-019

**Al eliminar el último registro de la última página el listado se reubica**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-14, RF-17 | Media | Funcional negativo | Valores límite | 🟡 Bloqueado | — |

**Precondiciones:** Sesión iniciada como Admin. El listado tiene más de una página y la última contiene un único registro eliminable creado para la prueba.

**Datos de prueba:** —

**Pasos**

1. Ir a PIM > Employee List.
2. Navegar hasta la última página de la paginación.
3. Eliminar el único registro que contiene y confirmar.
4. Observar el listado resultante.

**Resultado esperado:** Tras el borrado la aplicación retrocede a la página anterior y muestra registros. No debe quedar una tabla vacía con un total mayor que cero.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-020

**La ordenación por columna se mantiene al cambiar de página**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-15 | Baja | Funcional | Transición de estados | 🟡 Bloqueado | — |

**Precondiciones:** Sesión iniciada como Admin. El listado tiene más de una página.

**Datos de prueba:** Columna: Last Name (A-Z)

**Pasos**

1. Ir a PIM > Employee List.
2. Ordenar por Last Name en orden ascendente.
3. Comprobar el orden de la primera página.
4. Avanzar a la página siguiente y comprobar el orden.

**Resultado esperado:** El criterio de ordenación persiste entre páginas y la secuencia alfabética continúa de forma coherente de una página a la siguiente.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-021

**Borrado múltiple de empleados con confirmación previa**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-17 | Alta | Funcional positivo | Transición de estados | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Existen al menos dos empleados de prueba.

**Datos de prueba:** Empleados creados en CP-001 y CP-004

**Pasos**

1. Ir a PIM > Employee List.
2. Marcar la casilla de dos empleados de prueba.
3. Pulsar «Delete Selected».
4. Confirmar en el diálogo.
5. Buscar de nuevo ambos empleados.

**Resultado esperado:** Se solicita confirmación antes de borrar, ambos registros desaparecen del listado y una búsqueda posterior no los devuelve.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-022

**Edición y guardado de los datos personales de un empleado**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-18, RF-22 | Alta | Funcional positivo | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Existe el empleado de prueba.

**Datos de prueba:** Other Id: OT-0091 · Nationality: Spanish · Marital Status: Single

**Pasos**

1. Abrir la ficha del empleado desde PIM > Employee List.
2. En Personal Details modificar Other Id, Nationality y Marital Status.
3. Pulsar Save.
4. Recargar la página.

**Resultado esperado:** Aparece «Successfully Updated» y los tres valores se conservan tras recargar la página.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-023

**La fecha de nacimiento con formato inválido se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-19, RF-20 | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Date of Birth: 31/02/2020

**Pasos**

1. Situarse en Personal Details.
2. Escribir manualmente una fecha con formato incorrecto en Date of Birth.
3. Pulsar Save.

**Resultado esperado:** Se muestra el mensaje «Should be a valid date in yyyy-dd-mm format» y el valor no se guarda.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-024

**La fecha de nacimiento no admite fechas futuras**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RN-01 | Alta | Funcional negativo | Conjetura de errores | 🔴 Falla | [BUG-006](03-bug-reports/BUG-006.md) |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Date of Birth: 2035-01-01

**Pasos**

1. Situarse en Personal Details.
2. Abrir el selector de Date of Birth y navegar hasta un año futuro.
3. Seleccionar una fecha posterior a hoy.
4. Pulsar Save.

**Resultado esperado:** El sistema rechaza la fecha con un mensaje de validación: una fecha de nacimiento posterior a hoy no es un dato posible.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-025

**Permiso de conducir con fecha de caducidad pasada**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-18, RN-04 | Baja | Funcional positivo | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** License Number: B-4457821 · Expiry Date: 2019-01-15

**Pasos**

1. Situarse en Personal Details.
2. Introducir número de licencia y una fecha de caducidad anterior a hoy.
3. Pulsar Save y recargar.

**Resultado esperado:** El dato se guarda —es un valor histórico legítimo— y el sistema no lo trata como error de validación.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-026

**Los cambios en la ficha se reflejan en el listado de empleados**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-22 | Alta | Funcional / Smoke | Transición de estados | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Existe el empleado de prueba.

**Datos de prueba:** Last Name: Herrera → Herrera-Ruiz

**Pasos**

1. Modificar el Last Name del empleado desde su ficha y guardar.
2. Ir a PIM > Employee List.
3. Buscar el empleado por su Employee Id.

**Resultado esperado:** El listado muestra el apellido actualizado sin necesidad de vaciar la caché ni volver a iniciar sesión.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-027

**Nombres con tildes y caracteres no ASCII: guardado y búsqueda**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-10, RF-18 | Media | Funcional | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: Mónica · Last Name: Núñez

**Pasos**

1. Crear un empleado con acentos en el nombre.
2. Comprobar que la ficha y el listado los muestran correctamente.
3. Buscar el empleado escribiendo el nombre SIN tildes.
4. Buscar el empleado escribiendo el nombre CON tildes.

**Resultado esperado:** El nombre se almacena y se muestra sin corrupción de caracteres, y la búsqueda lo encuentra tanto con tildes como sin ellas.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-028

**El contenido con etiquetas HTML se escapa al mostrarse**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-18, RNF-02 | Alta | Funcional negativo | Conjetura de errores | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** First Name: <b>Lucia</b>

**Pasos**

1. Crear un empleado cuyo First Name contenga una etiqueta HTML.
2. Guardar y abrir la ficha.
3. Consultar el registro en PIM > Employee List.

**Resultado esperado:** El texto se muestra literalmente, tal y como se introdujo, sin interpretarse como marcado. Comprobación del escapado de salida.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-029

**Los campos de teléfono no admiten letras**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-23 | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Mobile: SEIS CINCO DOS

**Pasos**

1. Ir a la pestaña Contact Details.
2. Introducir letras en el campo Mobile.
3. Pulsar Save.

**Resultado esperado:** Se muestra el mensaje «Allows numbers and only + - / ( )» y el valor no se guarda.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-030

**El correo electrónico con formato inválido se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-24 | Media | Funcional negativo | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Work Email: lucia.herrera.empresa.com

**Pasos**

1. Ir a la pestaña Contact Details.
2. Introducir una dirección sin arroba en Work Email.
3. Pulsar Save.

**Resultado esperado:** Se muestra el mensaje «Expected format: admin@example.com» y el valor no se guarda.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-031

**Alta, edición y borrado de un contacto de emergencia**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-25 | Alta | Funcional / Smoke | Transición de estados | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Nombre: Marta Herrera · Relación: Sister · Teléfono: 652489174

**Pasos**

1. Ir a Emergency Contacts y pulsar Add.
2. Rellenar nombre, relación y teléfono, y guardar.
3. Editar el teléfono del contacto creado y guardar.
4. Eliminar el contacto y confirmar.

**Resultado esperado:** El contacto se crea, la edición persiste tras recargar y el borrado lo elimina de la tabla previa confirmación.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-032

**Una persona a cargo no admite fecha de nacimiento futura**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-26, RN-01 | Media | Funcional negativo | Conjetura de errores | 🔴 Falla | [BUG-008](03-bug-reports/BUG-008.md) |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Nombre: Pablo Herrera · Date of Birth: 2035-06-01

**Pasos**

1. Ir a la pestaña Dependents y pulsar Add.
2. Introducir nombre y relación Child.
3. Introducir una fecha de nacimiento posterior a hoy.
4. Pulsar Save.

**Resultado esperado:** El sistema rechaza la fecha con un mensaje de validación, igual que en la ficha del empleado.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-033

**La fecha de incorporación no puede ser anterior a la de nacimiento**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RN-02 | Media | Funcional negativo | Tabla de decisión | 🔴 Falla | [BUG-009](03-bug-reports/BUG-009.md) |

**Precondiciones:** Sesión iniciada como Admin. El empleado tiene fecha de nacimiento informada.

**Datos de prueba:** Date of Birth: 1995-15-06 · Joined Date: 1980-01-10

**Pasos**

1. Comprobar en Personal Details la fecha de nacimiento del empleado.
2. Ir a la pestaña Job.
3. Introducir una Joined Date anterior a esa fecha de nacimiento.
4. Pulsar Save.

**Resultado esperado:** El sistema rechaza la combinación con un mensaje de coherencia entre fechas: nadie se incorpora antes de nacer.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-034

**El importe salarial no admite valores negativos**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-28, RN-03 | Alta | Funcional negativo | Valores límite | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Amount: -1500 · Currency: Euro · Pay Frequency: Monthly

**Pasos**

1. Ir a la pestaña Salary y pulsar Add.
2. Seleccionar componente salarial, divisa y periodicidad.
3. Introducir un importe negativo.
4. Pulsar Save.

**Resultado esperado:** El sistema rechaza el importe con un mensaje de validación. Un salario negativo no es un dato posible.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-035

**Un empleado no puede asignarse a sí mismo como supervisor**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-29 | Media | Funcional negativo | Conjetura de errores | 🔴 Falla | [BUG-011](03-bug-reports/BUG-011.md) |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Supervisor: el mismo empleado de la ficha

**Pasos**

1. Ir a la pestaña Report-to.
2. En «Assigned Supervisors» pulsar Add.
3. Introducir el nombre del propio empleado y seleccionarlo.
4. Elegir el método de reporte y pulsar Save.

**Resultado esperado:** El sistema impide la asignación: crea un ciclo en la jerarquía de supervisión.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-036

**El adjunto que supera el tamaño máximo configurado se rechaza**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RF-30 | Media | Funcional negativo | Valores límite | 🟡 Bloqueado | — |

**Precondiciones:** Sesión iniciada como Admin. Ficha de empleado abierta.

**Datos de prueba:** Fichero por encima del límite de subida de la instancia

**Pasos**

1. Ir a la sección Attachments de la ficha.
2. Pulsar Add y seleccionar un fichero por encima del límite configurado.
3. Introducir un comentario y pulsar Save.

**Resultado esperado:** Se muestra un mensaje indicando el tamaño máximo permitido y el adjunto no se añade a la tabla.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-037

**El listado de empleados es operativo en viewport móvil**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RNF-01 | Media | Responsive | Particiones de equivalencia | 🟢 Pasa | — |

**Precondiciones:** Sesión iniciada como Admin. DevTools en modo dispositivo 360 × 640.

**Datos de prueba:** Viewport: 360 × 640 (Galaxy S20)

**Pasos**

1. Activar la emulación de dispositivo móvil a 360 × 640.
2. Ir a PIM > Employee List.
3. Desplegar el panel de filtros, buscar por Employee Id y revisar el resultado.

**Resultado esperado:** El menú lateral se colapsa, los filtros son accesibles y la tabla se consulta mediante desplazamiento horizontal sin perder columnas ni solaparse los controles.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>

### CP-038

**Los campos del formulario de alta tienen etiqueta asociada**

| Requisito | Prioridad | Tipo | Técnica de diseño | Estado | Defecto |
| --------- | --------- | ---- | ----------------- | ------ | ------- |
| RNF-03 | Media | Accesibilidad | Particiones de equivalencia | 🔴 Falla | [BUG-012](03-bug-reports/BUG-012.md) |

**Precondiciones:** Sesión iniciada como Admin.

**Datos de prueba:** Navegación por teclado + inspector de accesibilidad

**Pasos**

1. Ir a PIM > Add Employee.
2. Recorrer el formulario completo usando únicamente la tecla Tab.
3. Inspeccionar en las DevTools el marcado de cada input y su etiqueta.
4. Comprobar en el árbol de accesibilidad el nombre expuesto de cada campo.

**Resultado esperado:** Cada campo es alcanzable por teclado en orden lógico y expone un nombre accesible mediante label asociado o aria-label.

<sub>[↑ volver al resumen](#resumen-de-la-matriz)</sub>
