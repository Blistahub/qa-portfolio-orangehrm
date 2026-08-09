# 00 — Catálogo de requisitos (módulo PIM)

**Aplicación bajo prueba (SUT):** OrangeHRM OS 5.x — instancia pública de demostración
**Módulo:** PIM — *Personal Information Management* (gestión de empleados)
**Autor:** David Coya Moreno

---

## Nota metodológica

OrangeHRM OS no publica una especificación funcional formal de su módulo PIM. Los requisitos de
este catálogo se han **derivado por ingeniería inversa** a partir de tres fuentes, en este orden de
prioridad:

1. La documentación de usuario oficial de OrangeHRM (guía del módulo PIM y de configuración).
2. El comportamiento observado de la interfaz: campos obligatorios marcados con `*`, mensajes de
   validación mostrados por la propia aplicación, y límites de longitud aplicados por los `input`.
3. Las respuestas de la API interna `/web/index.php/api/v2/pim/*` inspeccionadas con las DevTools
   del navegador, que revelan el contrato real de cada operación.

**Esto es una limitación conocida y se declara de forma explícita.** Un requisito derivado no es
un requisito acordado: cuando el comportamiento observado y el comportamiento razonable divergen,
el defecto se reporta como *"requiere confirmación de negocio"* en lugar de darlo por cerrado. Esa
distinción está marcada en la columna correspondiente de cada defecto.

En un proyecto real esta sección se sustituiría por los enlaces a las historias de usuario de Jira
o a la especificación de requisitos del cliente. Se mantiene aquí porque el objetivo del portfolio
es mostrar el **método de trazabilidad**, no inventar una especificación que no existe.

---

## Convención de identificadores

| Prefijo | Significado                                                      |
| ------- | ---------------------------------------------------------------- |
| `RF-nn` | Requisito funcional                                              |
| `RNF-nn`| Requisito no funcional (usabilidad, accesibilidad, rendimiento)  |
| `RN-nn` | Regla de negocio (condiciona el resultado de un requisito)       |

Cada caso de prueba de [`02-casos-de-prueba.md`](02-casos-de-prueba.md) declara el requisito que
cubre. Cada defecto de [`03-bug-reports/`](03-bug-reports/) declara el requisito que incumple. La
[matriz de trazabilidad](05-matriz-trazabilidad.md) cierra el círculo: requisito → casos → defectos.

---

## 1. Alta de empleado (*PIM > Add Employee*)

| ID     | Requisito                                                                                                                       | Origen |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- | ------ |
| RF-01  | El sistema permite dar de alta un empleado. *First Name* y *Last Name* son obligatorios; *Middle Name* es opcional.              | UI (`*`) |
| RF-02  | Los campos de nombre admiten un máximo de 30 caracteres cada uno.                                                                | UI (`maxlength`) |
| RF-03  | El sistema asigna automáticamente un *Employee Id* correlativo, editable por el usuario en el momento del alta.                  | UI |
| RF-04  | El *Employee Id* debe ser único en el sistema. Un identificador ya existente se rechaza con un mensaje de validación.            | Doc. oficial |
| RF-05  | El alta permite adjuntar una foto de perfil de hasta 1 MB en formato de imagen.                                                  | UI (mensaje) |
| RF-06  | El alta permite crear opcionalmente credenciales de acceso (*Create Login Details*) con usuario, contraseña y estado.            | UI |
| RF-07  | El nombre de usuario debe tener entre 5 y 40 caracteres y ser único en el sistema.                                               | UI (mensaje) |
| RF-08  | La contraseña debe cumplir la política mínima: 8 caracteres, al menos un número y al menos una letra minúscula.                  | UI (mensaje) |
| RF-09  | Tras guardar correctamente, el sistema redirige a la ficha del empleado creado y muestra confirmación *"Successfully Saved"*.    | UI |

## 2. Listado y búsqueda de empleados (*PIM > Employee List*)

| ID     | Requisito                                                                                                                       | Origen |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- | ------ |
| RF-10  | El listado permite filtrar por nombre de empleado, *Employee Id*, estado de empleo, *Include* (activos / pasados), sub-unidad y supervisor. | UI |
| RF-11  | El campo *Employee Name* ofrece autocompletado a partir del tercer carácter y exige seleccionar una de las sugerencias.          | UI |
| RF-12  | El filtro combina los criterios introducidos mediante conjunción lógica (AND).                                                   | Comportamiento |
| RF-13  | El botón *Reset* limpia todos los filtros y restaura el listado completo.                                                        | UI |
| RF-14  | El listado se pagina de 50 en 50 registros y muestra el total de resultados encontrados.                                         | UI |
| RF-15  | El listado permite ordenar por las columnas *First (& Middle) Name*, *Last Name*, *Id*, *Job Title*, *Employment Status* y *Sub Unit*. | UI |
| RF-16  | Una búsqueda sin coincidencias muestra el aviso *"No Records Found"* y no deja la tabla en estado inconsistente.                 | UI |
| RF-17  | El listado permite eliminar empleados de forma individual o múltiple, siempre con confirmación previa.                           | UI |

## 3. Ficha del empleado — datos personales (*PIM > Personal Details*)

| ID     | Requisito                                                                                                                       | Origen |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- | ------ |
| RF-18  | La ficha permite editar nombre, *Employee Id*, *Other Id*, número y fecha de caducidad del permiso de conducir, nacionalidad, estado civil, fecha de nacimiento y sexo. | UI |
| RF-19  | La fecha de nacimiento se introduce en formato `yyyy-dd-mm` (formato por defecto de la instancia) mediante campo de texto o selector de calendario. | UI |
| RF-20  | El sistema rechaza fechas con formato inválido mostrando *"Should be a valid date in yyyy-dd-mm format"*.                        | UI (mensaje) |
| RF-21  | La sección *Custom Fields* muestra únicamente los campos personalizados definidos en *PIM > Configuration*.                      | Doc. oficial |
| RF-22  | Los cambios guardados persisten tras recargar la página y son visibles en el listado de empleados.                               | Comportamiento |

## 4. Ficha del empleado — resto de secciones

| ID     | Requisito                                                                                                                       | Origen |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- | ------ |
| RF-23  | *Contact Details*: los campos de teléfono admiten exclusivamente dígitos y los símbolos `+ - / ( ) espacio`.                     | UI (mensaje) |
| RF-24  | *Contact Details*: el campo de correo electrónico exige un formato de dirección válido y no admite duplicados entre empleados.   | UI (mensaje) |
| RF-25  | *Emergency Contacts*: permite añadir, editar y eliminar contactos de emergencia con nombre, relación y teléfono.                 | UI |
| RF-26  | *Dependents*: permite registrar personas a cargo con nombre, relación y fecha de nacimiento.                                     | UI |
| RF-27  | *Job*: permite registrar fecha de incorporación, puesto, categoría, sub-unidad, ubicación y estado de empleo.                    | UI |
| RF-28  | *Salary*: permite añadir componentes salariales con importe, divisa y periodicidad de pago.                                      | UI |
| RF-29  | *Report-to*: permite asignar supervisores y subordinados, sin que un empleado pueda ser supervisor de sí mismo.                  | Doc. oficial |
| RF-30  | *Attachments*: permite adjuntar ficheros con un comentario descriptivo, respetando el tamaño máximo configurado.                 | UI |

## 5. Reglas de negocio

| ID     | Regla                                                                                                                            |
| ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| RN-01  | Un empleado no puede tener fecha de nacimiento posterior a la fecha actual.                                                       |
| RN-02  | Un empleado no puede tener fecha de incorporación anterior a su fecha de nacimiento.                                              |
| RN-03  | Un importe salarial no puede ser negativo.                                                                                        |
| RN-04  | La fecha de caducidad del permiso de conducir posterior a hoy indica permiso vigente; anterior, permiso caducado.                  |
| RN-05  | Eliminar un empleado no debe dejar registros huérfanos ni romper las jerarquías *Report-to* en las que participaba.               |

> **RN-01, RN-02, RN-03 y RN-05 no están documentadas por el fabricante.** Se han formulado como
> reglas de negocio *esperables* en cualquier ERP de RRHH y los defectos derivados de ellas se
> reportan marcados como **requiere confirmación de negocio**. Esta distinción es deliberada: un
> tester no convierte su expectativa en un requisito del cliente.

## 6. Requisitos no funcionales

| ID      | Requisito                                                                                                                       |
| ------- | ------------------------------------------------------------------------------------------------------------------------------- |
| RNF-01  | La interfaz es utilizable en resoluciones de escritorio (≥ 1366 px) y en móvil (360 × 640 px) sin pérdida de funcionalidad.       |
| RNF-02  | Los mensajes de validación son específicos del campo que los origina y se muestran junto a él.                                    |
| RNF-03  | Los campos de formulario tienen etiqueta asociada mediante `for`/`id` o `aria-label`, de modo que un lector de pantalla los anuncie. |
| RNF-04  | Las operaciones de listado y guardado responden en menos de 3 segundos en condiciones normales de uso.                            |
| RNF-05  | La aplicación se comporta de forma equivalente en Chrome, Firefox y Edge (última versión estable).                                |
