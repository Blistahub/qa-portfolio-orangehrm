# 01 — Plan de pruebas · Módulo PIM (OrangeHRM OS)

| Campo                | Valor                                                        |
| -------------------- | ------------------------------------------------------------ |
| **Proyecto**         | Portfolio de QA manual — OrangeHRM OS                        |
| **Aplicación (SUT)** | OrangeHRM OS 5.x — `opensource-demo.orangehrmlive.com`        |
| **Módulo**           | PIM — *Personal Information Management*                       |
| **Versión del plan** | 1.0                                                           |
| **Autor**            | David Coya Moreno — QA Tester                                 |
| **Estado**           | Aprobado para ejecución                                       |

---

## 1. Objetivo

Verificar que el módulo PIM permite dar de alta, consultar, modificar y eliminar empleados de forma
correcta, y que valida los datos de entrada antes de persistirlos, con el fin de emitir una
**recomendación fundamentada sobre si el módulo es apto para su paso a producción**.

El objetivo secundario, y explícito en un portfolio, es dejar constancia del método: cómo se
delimita el alcance, cómo se derivan los casos de una técnica de diseño concreta y cómo se
documenta un defecto de forma que un desarrollador pueda corregirlo sin volver a preguntar.

---

## 2. Alcance

### 2.1 Qué entra en el alcance

| Área                              | Funcionalidad cubierta                                                            |
| --------------------------------- | ---------------------------------------------------------------------------------- |
| **PIM > Add Employee**            | Alta de empleado, validación de campos obligatorios y de longitud, *Employee Id*, foto de perfil, creación opcional de credenciales de acceso. |
| **PIM > Employee List**           | Búsqueda simple y combinada, autocompletado, *Reset*, paginación, ordenación, listado vacío, borrado individual y múltiple. |
| **PIM > Personal Details**        | Edición y persistencia de datos personales, validación de fecha de nacimiento y de permiso de conducir, campos personalizados. |
| **PIM > Contact Details**         | Validación de teléfonos y correo electrónico.                                      |
| **PIM > Emergency Contacts / Dependents** | Alta, edición y borrado de registros dependientes de la ficha.               |
| **PIM > Job / Salary / Report-to**| Coherencia de fechas de incorporación, importes salariales y jerarquía de supervisión. |
| **PIM > Attachments**             | Adjuntado de ficheros y límite de tamaño.                                          |
| **Transversal**                   | Compatibilidad Chrome / Firefox / Edge, comportamiento responsive, accesibilidad básica de formularios, tiempos de respuesta percibidos. |

### 2.2 Qué NO entra en el alcance — y por qué

Delimitar es la mitad del trabajo. Cada exclusión lleva su motivo:

| Excluido                                                       | Motivo                                                                                                        |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Módulos Leave, Time, Recruitment, Performance, Admin, Directory, Buzz, Claim y Maintenance | Un módulo cubierto en profundidad aporta más información de calidad que veinte casos dispersos por toda la aplicación. Se cubrirán en iteraciones posteriores. |
| Autenticación y gestión de sesión                              | Es precondición de todos los casos, no objeto de prueba. Un fallo de login **bloquea** la ejecución y se reporta como impedimento, no como defecto de PIM. |
| Vista *My Info* (rol ESS sobre la propia ficha)                | El demo público no permite crear un usuario ESS operativo con credenciales conocidas y estables; sin eso los resultados no serían reproducibles por un tercero. Se documenta como **riesgo R-04**. |
| Pruebas de carga, estrés y rendimiento medido                  | Lanzar carga contra una instancia pública compartida de terceros es abuso de un servicio ajeno, con independencia de que sea un entorno de demostración. Solo se registra el tiempo de respuesta **percibido** durante la ejecución funcional. |
| Pruebas de seguridad ofensiva (SQLi, XSS, fuerza bruta, escaneo de puertos) | No se dispone de autorización escrita del propietario del sistema. Sin permiso explícito no se ejecutan. |
| Pruebas de instalación, migración y actualización              | No hay acceso al servidor ni a la base de datos de la instancia de demostración.                              |
| Verificación en base de datos con SQL                          | Sin acceso al motor de datos. La integridad se verifica indirectamente a través de la interfaz y de las respuestas de la API interna observadas en el navegador. |
| Automatización de la regresión                                 | Fuera del alcance de **este** repositorio por decisión de diseño: se aborda en el proyecto `qa-portfolio-playwright-saucedemo`. |
| Localización e internacionalización completa                   | Solo se prueba el idioma por defecto (inglés). Las incidencias de traducción se anotan como observación, no como defecto. |

> **Nota ética y legal.** Todas las pruebas se ejecutan contra la instancia pública que OrangeHRM
> publica expresamente para demostración y aprendizaje, exclusivamente de forma manual y a través de
> la interfaz de usuario, a un ritmo equivalente al de un usuario real. No se ejecutan scripts
> automatizados, escáneres ni pruebas de carga contra ella. Los datos que se crean se eliminan al
> terminar cuando el caso lo permite.

---

## 3. Estrategia de pruebas

### 3.1 Niveles

| Nivel                | Aplicación en este proyecto                                                     |
| -------------------- | -------------------------------------------------------------------------------- |
| Unitario / integración | Fuera de alcance: no hay acceso al código fuente desplegado.                    |
| **Sistema**          | Nivel principal. Se prueba el módulo PIM completo a través de la interfaz.        |
| **Aceptación**       | Validación de los flujos de negocio de extremo a extremo (alta → consulta → modificación → baja). |

### 3.2 Tipos de prueba

| Tipo               | Alcance en este plan                                                                          |
| ------------------ | ----------------------------------------------------------------------------------------------- |
| **Funcional**      | Núcleo del plan. Verificación de cada requisito del catálogo `RF-01 … RF-30`.                     |
| **Smoke**          | Subconjunto de 5 casos críticos (`CP-001`, `CP-013`, `CP-018`, `CP-026`, `CP-031`) ejecutado antes de cualquier ciclo completo. Si falla uno, el ciclo no arranca. |
| **Regresión**      | Reejecución de los casos de prioridad Alta tras cada corrección de defecto.                     |
| **Exploratorio**   | Dos sesiones cronometradas de 60 min con carta de exploración: (1) validaciones de formulario en la ficha del empleado, (2) coherencia de datos entre listado y ficha. Los hallazgos se convierten en casos formales o en defectos. |
| **Cross-browser**  | Los casos de prioridad Alta se ejecutan en Chrome, Firefox y Edge; el resto solo en Chrome.      |
| **Responsive**     | Los casos `CP-032` y `CP-033` en viewport móvil 360 × 640 px.                                    |
| **Accesibilidad**  | Comprobación básica de etiquetado de formularios y navegación por teclado (`RNF-03`). No se realiza auditoría WCAG completa. |
| **Retest**         | Verificación dirigida de cada defecto corregido antes de darlo por cerrado.                      |

### 3.3 Técnicas de diseño de casos

Los casos no se improvisan: cada uno declara la técnica de la que se deriva.

| Técnica                        | Dónde se aplica                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Particiones de equivalencia**| Campos de texto libre (nombres, teléfono, correo): una clase válida y las clases inválidas relevantes, un caso por clase en lugar de multiplicar entradas equivalentes. |
| **Análisis de valores límite** | Longitudes de campo (30 caracteres en nombres, 5–40 en usuario, 8 en contraseña) y tamaño de fichero (1 MB): se prueba `mín-1`, `mín`, `máx`, `máx+1`. |
| **Tabla de decisión**          | Reglas de negocio con varias condiciones combinadas: alta de empleado con y sin credenciales de acceso, y filtrado combinado del listado. Ver §3.4. |
| **Transición de estados**      | Ciclo de vida del registro: *inexistente → creado → modificado → eliminado*, incluida la transición inválida (consultar un empleado ya eliminado). |
| **Conjetura de errores**       | Basada en la experiencia: fechas futuras, importes negativos, espacios en blanco al inicio y final, caracteres Unicode, doble envío del formulario. |

### 3.4 Tabla de decisión — alta de empleado

| Condición                              | R1 | R2 | R3 | R4 | R5 |
| -------------------------------------- | -- | -- | -- | -- | -- |
| First Name y Last Name informados      | Sí | No | Sí | Sí | Sí |
| Employee Id único                      | Sí | –  | No | Sí | Sí |
| *Create Login Details* activado        | No | –  | –  | Sí | Sí |
| Credenciales válidas (usuario + política de contraseña) | – | – | – | Sí | No |
| **Resultado esperado**                 | Alta correcta sin acceso | Error: campo obligatorio | Error: Id duplicado | Alta correcta con acceso | Error: credenciales inválidas, **sin crear el empleado** |
| **Caso que la cubre**                  | CP-001 | CP-002 | CP-006 | CP-010 | CP-011 |

La regla **R5** es la interesante: comprueba que un fallo en el segundo bloque del formulario no deja
un empleado creado a medias. Es el tipo de caso que solo aparece si se modela la tabla.

---

## 4. Entorno de pruebas

| Elemento              | Detalle                                                                              |
| --------------------- | -------------------------------------------------------------------------------------- |
| **URL**               | `https://opensource-demo.orangehrmlive.com`                                            |
| **Versión**           | OrangeHRM OS 5.x — la build concreta se anota en el informe de ejecución en el momento del ciclo. |
| **Credenciales**      | `Admin` / `admin123` (rol Administrador, publicadas por el propio fabricante en la pantalla de acceso). |
| **Sistema operativo** | Windows 11 Pro 24H2                                                                    |
| **Navegadores**       | Google Chrome (estable), Mozilla Firefox (estable), Microsoft Edge (estable)           |
| **Resoluciones**      | Escritorio 1920 × 1080 · Móvil emulado 360 × 640 (Chrome DevTools, perfil Galaxy S20)  |
| **Herramientas**      | DevTools del navegador (pestaña *Network* para inspeccionar el contrato de la API interna), ShareX para captura de evidencias, Markdown + Excel para la documentación. |

### 4.1 Condición del entorno y su efecto sobre los resultados

La instancia es **pública, compartida y se restablece periódicamente**. Esto tiene tres consecuencias
que condicionan la lectura de los resultados y que se declaran por adelantado:

1. Otros usuarios modifican los datos simultáneamente, de modo que ningún caso puede depender de un
   registro concreto preexistente. **Cada caso crea los datos que necesita.**
2. El restablecimiento periódico elimina los registros de prueba, por lo que un defecto debe poder
   reproducirse **desde cero** siguiendo sus pasos. Todos los defectos de este repositorio están
   escritos con esa condición.
3. No hay control de versiones del entorno: una diferencia de comportamiento entre dos ciclos puede
   deberse a una actualización de la demo y no a una regresión. Se mitiga anotando fecha y hora de
   cada ejecución.

---

## 5. Datos de prueba

| Conjunto                | Contenido                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------ |
| **Empleado válido**     | `Nombre: Lucia · Apellido: Herrera · Employee Id: autogenerado`                       |
| **Cadena de 30 caracteres** | `Abcdefghijklmnopqrstuvwxyzabcd` (límite exacto)                                   |
| **Cadena de 31 caracteres** | `Abcdefghijklmnopqrstuvwxyzabcde` (límite + 1)                                     |
| **Cadenas inválidas**   | `12345`, `!@#$%^&*()`, `   ` (solo espacios), `<script>alert(1)</script>` (usada únicamente para comprobar el **escapado en la salida**, no como prueba de intrusión) |
| **Fechas**              | Válida `1995-15-06` · Futura `2035-01-01` · Formato inválido `31/02/2020`             |
| **Ficheros**            | `foto-900kb.jpg` (bajo el límite) · `foto-1200kb.jpg` (sobre el límite) · `documento.exe` (extensión no permitida) |
| **Credenciales**        | Usuario `dcoya.test01` · Contraseñas: válida `Test1234`, corta `Test12`, sin dígito `testtesting` |

Los datos se generan en el momento de la ejecución. Cuando un caso requiere un nombre único se le
añade un sufijo numérico correlativo para evitar colisiones con otros usuarios de la demo.

---

## 6. Criterios de entrada y salida

### 6.1 Criterios de entrada — el ciclo no arranca sin esto

- La instancia responde y permite autenticarse con el usuario Admin.
- Los 5 casos de smoke se ejecutan correctamente.
- La matriz de casos está revisada y cada caso tiene requisito asociado.
- El entorno y los navegadores están en las versiones declaradas en §4.

### 6.2 Criterios de salida — el ciclo se cierra con esto

- ≥ 95 % de los casos planificados ejecutados (ni bloqueados ni pendientes).
- 100 % de los casos de prioridad **Alta** ejecutados y con resultado registrado.
- **0 defectos abiertos de severidad Crítica o Alta.**
- Todos los defectos de severidad Media abiertos cuentan con análisis de impacto y decisión
  documentada de aceptarlos o corregirlos.
- Informe de ejecución emitido, con recomendación explícita de apto / no apto para release.

### 6.3 Criterios de suspensión y reanudación

Se **suspende** el ciclo si la instancia deja de estar disponible más de 30 minutos, si un defecto
Crítico impide ejecutar más del 30 % de los casos restantes, o si el entorno se restablece a mitad de
un ciclo invalidando los datos en curso. Se **reanuda** cuando el entorno vuelve a cumplir los
criterios de entrada, reejecutando los casos afectados desde el principio.

---

## 7. Análisis de riesgos

| ID   | Riesgo                                                                | Prob. | Impacto | Mitigación                                                                                     |
| ---- | --------------------------------------------------------------------- | ----- | ------- | ------------------------------------------------------------------------------------------------ |
| R-01 | El entorno de demostración se restablece durante el ciclo y se pierden los datos de prueba. | Alta  | Medio   | Cada caso es autosuficiente y crea sus propios datos. La evidencia se captura en el momento del hallazgo, no al final. |
| R-02 | Otros usuarios de la demo pública modifican registros y contaminan los resultados. | Alta  | Medio   | No se usan registros preexistentes como precondición. Los nombres llevan sufijo propio.         |
| R-03 | La instancia no está disponible o responde con lentitud.              | Media | Alto    | Se ejecuta primero el bloque de casos de prioridad Alta, para asegurar la cobertura crítica.    |
| R-04 | Sin usuario ESS estable, no puede verificarse la segregación de permisos por rol. | Alta  | Medio   | Se excluye del alcance de forma explícita (§2.2) y se declara como hueco de cobertura conocido en el informe. |
| R-05 | Ausencia de especificación formal: un comportamiento inesperado puede ser intencionado. | Alta  | Alto    | Los requisitos se derivan y se documentan (`00-requisitos.md`). Los defectos que dependen de una regla no documentada se marcan como *requiere confirmación de negocio*. |
| R-06 | Sin acceso a la base de datos, no puede confirmarse la integridad real de los datos persistidos. | Alta  | Medio   | Verificación indirecta mediante la interfaz y la inspección de las respuestas de la API interna en las DevTools. |
| R-07 | Sesgo del propio tester: se prueba mejor lo que se conoce y se repiten los mismos patrones. | Media | Medio   | Las técnicas de diseño formales (§3.3) obligan a cubrir clases de entrada que la intuición omite; las sesiones exploratorias se ejecutan con carta y tiempo fijo. |

---

## 8. Entregables

| Entregable                 | Fichero                                                        |
| -------------------------- | ---------------------------------------------------------------- |
| Catálogo de requisitos     | [`00-requisitos.md`](00-requisitos.md)                            |
| Plan de pruebas            | `01-plan-de-pruebas.md` (este documento)                          |
| Matriz de casos de prueba  | [`02-casos-de-prueba.md`](02-casos-de-prueba.md) · `.xlsx` · `.csv`|
| Reportes de defecto        | [`03-bug-reports/`](03-bug-reports/)                              |
| Informe de ejecución       | [`04-informe-ejecucion.md`](04-informe-ejecucion.md)              |
| Matriz de trazabilidad     | [`05-matriz-trazabilidad.md`](05-matriz-trazabilidad.md)          |
| Evidencias                 | [`evidencias/`](evidencias/)                                      |

## 9. Roles

Proyecto individual de portfolio. **David Coya Moreno** asume el diseño del plan, el diseño y la
ejecución de los casos, el reporte de defectos y la emisión del informe.

En un equipo real, el rol de **triaje y priorización** correspondería al QA Lead junto con el Product
Owner, y la decisión de *release* al PO. En este documento la recomendación de apto / no apto se
emite como **recomendación técnica del QA**, que es exactamente el alcance que le corresponde: el QA
informa del riesgo, no decide el negocio.
