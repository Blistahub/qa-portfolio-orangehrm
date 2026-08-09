# 05 — Matriz de trazabilidad

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
| Requisitos declarados | 40 |
| Requisitos con al menos un caso | 34 (85,0 %) |
| Requisitos sin cobertura | 6 |
| Requisitos verificados sin incidencias | 17 |
| Requisitos con al menos un defecto abierto | 16 |

## Requisito → Casos → Defectos

| Requisito | Descripción | Casos que lo verifican | Defectos | Resultado |
| --- | --- | --- | --- | --- |
| **RF-01** | Alta de empleado; First Name y Last Name obligatorios | [CP-001](02-casos-de-prueba.md#cp-001) · [CP-002](02-casos-de-prueba.md#cp-002) · [CP-003](02-casos-de-prueba.md#cp-003) · [CP-007](02-casos-de-prueba.md#cp-007) · [CP-008](02-casos-de-prueba.md#cp-008) | [BUG-001](03-bug-reports/BUG-001.md) | 🔴 Incumplido |
| **RF-02** | Campos de nombre con máximo de 30 caracteres | [CP-004](02-casos-de-prueba.md#cp-004) · [CP-005](02-casos-de-prueba.md#cp-005) | — | 🟢 Verificado |
| **RF-03** | Employee Id correlativo autogenerado y editable | — | — | ⚪ Sin cobertura |
| **RF-04** | Employee Id único en el sistema | [CP-006](02-casos-de-prueba.md#cp-006) | — | 🟢 Verificado |
| **RF-05** | Foto de perfil de hasta 1 MB | [CP-009](02-casos-de-prueba.md#cp-009) | — | 🟢 Verificado |
| **RF-06** | Creación opcional de credenciales de acceso | [CP-010](02-casos-de-prueba.md#cp-010) | — | 🟢 Verificado |
| **RF-07** | Nombre de usuario de 5 a 40 caracteres y único | [CP-010](02-casos-de-prueba.md#cp-010) · [CP-012](02-casos-de-prueba.md#cp-012) | — | 🟢 Verificado |
| **RF-08** | Política mínima de contraseña | [CP-010](02-casos-de-prueba.md#cp-010) · [CP-011](02-casos-de-prueba.md#cp-011) | [BUG-002](03-bug-reports/BUG-002.md) | 🔴 Incumplido |
| **RF-09** | Confirmación y redirección tras guardar | [CP-001](02-casos-de-prueba.md#cp-001) · [CP-011](02-casos-de-prueba.md#cp-011) | [BUG-002](03-bug-reports/BUG-002.md) | 🔴 Incumplido |
| **RF-10** | Filtros del listado de empleados | [CP-013](02-casos-de-prueba.md#cp-013) · [CP-027](02-casos-de-prueba.md#cp-027) | [BUG-007](03-bug-reports/BUG-007.md) | 🔴 Incumplido |
| **RF-11** | Autocompletado de Employee Name | [CP-014](02-casos-de-prueba.md#cp-014) · [CP-015](02-casos-de-prueba.md#cp-015) | [BUG-003](03-bug-reports/BUG-003.md) | 🔴 Incumplido |
| **RF-12** | Conjunción lógica entre criterios de filtro | [CP-016](02-casos-de-prueba.md#cp-016) | — | 🟢 Verificado |
| **RF-13** | Reset de filtros | [CP-018](02-casos-de-prueba.md#cp-018) | — | 🟢 Verificado |
| **RF-14** | Paginación de 50 registros y total de resultados | [CP-019](02-casos-de-prueba.md#cp-019) | [BUG-004](03-bug-reports/BUG-004.md) | 🔴 Incumplido |
| **RF-15** | Ordenación por columnas | [CP-020](02-casos-de-prueba.md#cp-020) | [BUG-005](03-bug-reports/BUG-005.md) | 🔴 Incumplido |
| **RF-16** | Aviso «No Records Found» | [CP-017](02-casos-de-prueba.md#cp-017) | — | 🟢 Verificado |
| **RF-17** | Borrado individual y múltiple con confirmación | [CP-019](02-casos-de-prueba.md#cp-019) · [CP-021](02-casos-de-prueba.md#cp-021) | [BUG-004](03-bug-reports/BUG-004.md) | 🔴 Incumplido |
| **RF-18** | Edición de datos personales | [CP-022](02-casos-de-prueba.md#cp-022) · [CP-025](02-casos-de-prueba.md#cp-025) · [CP-027](02-casos-de-prueba.md#cp-027) · [CP-028](02-casos-de-prueba.md#cp-028) | [BUG-007](03-bug-reports/BUG-007.md) | 🔴 Incumplido |
| **RF-19** | Formato de fecha yyyy-dd-mm | [CP-023](02-casos-de-prueba.md#cp-023) | — | 🟢 Verificado |
| **RF-20** | Rechazo de fechas con formato inválido | [CP-023](02-casos-de-prueba.md#cp-023) | — | 🟢 Verificado |
| **RF-21** | Custom Fields según configuración de PIM | — | — | ⚪ Sin cobertura |
| **RF-22** | Persistencia y coherencia con el listado | [CP-022](02-casos-de-prueba.md#cp-022) · [CP-026](02-casos-de-prueba.md#cp-026) | — | 🟢 Verificado |
| **RF-23** | Teléfonos: solo dígitos y + - / ( ) | [CP-029](02-casos-de-prueba.md#cp-029) | — | 🟢 Verificado |
| **RF-24** | Correo electrónico con formato válido | [CP-030](02-casos-de-prueba.md#cp-030) | — | 🟢 Verificado |
| **RF-25** | Contactos de emergencia | [CP-031](02-casos-de-prueba.md#cp-031) | — | 🟢 Verificado |
| **RF-26** | Personas a cargo (Dependents) | [CP-032](02-casos-de-prueba.md#cp-032) | [BUG-008](03-bug-reports/BUG-008.md) | 🔴 Incumplido |
| **RF-27** | Datos de puesto (Job) | — | — | ⚪ Sin cobertura |
| **RF-28** | Componentes salariales | [CP-034](02-casos-de-prueba.md#cp-034) | [BUG-010](03-bug-reports/BUG-010.md) | 🔴 Incumplido |
| **RF-29** | Jerarquía Report-to sin ciclos | [CP-035](02-casos-de-prueba.md#cp-035) | [BUG-011](03-bug-reports/BUG-011.md) | 🔴 Incumplido |
| **RF-30** | Adjuntos con límite de tamaño | [CP-036](02-casos-de-prueba.md#cp-036) | — | 🟡 No verificado |
| **RN-01** | Fecha de nacimiento no posterior a hoy | [CP-024](02-casos-de-prueba.md#cp-024) · [CP-032](02-casos-de-prueba.md#cp-032) | [BUG-006](03-bug-reports/BUG-006.md) · [BUG-008](03-bug-reports/BUG-008.md) | 🔴 Incumplido |
| **RN-02** | Incorporación no anterior al nacimiento | [CP-033](02-casos-de-prueba.md#cp-033) | [BUG-009](03-bug-reports/BUG-009.md) | 🔴 Incumplido |
| **RN-03** | Importe salarial no negativo | [CP-034](02-casos-de-prueba.md#cp-034) | [BUG-010](03-bug-reports/BUG-010.md) | 🔴 Incumplido |
| **RN-04** | Vigencia del permiso de conducir | [CP-025](02-casos-de-prueba.md#cp-025) | — | 🟢 Verificado |
| **RN-05** | Borrado sin registros huérfanos | — | — | ⚪ Sin cobertura |
| **RNF-01** | Usabilidad en escritorio y móvil | [CP-037](02-casos-de-prueba.md#cp-037) | — | 🟢 Verificado |
| **RNF-02** | Mensajes de validación específicos del campo | [CP-028](02-casos-de-prueba.md#cp-028) | — | 🟢 Verificado |
| **RNF-03** | Campos con nombre accesible | [CP-038](02-casos-de-prueba.md#cp-038) | [BUG-012](03-bug-reports/BUG-012.md) | 🔴 Incumplido |
| **RNF-04** | Tiempo de respuesta < 3 s | — | — | ⚪ Sin cobertura |
| **RNF-05** | Equivalencia entre navegadores | — | — | ⚪ Sin cobertura |

## Cobertura inversa: todo caso responde a un requisito

Los 38 casos de la matriz declaran requisito asociado. **No hay casos huérfanos**, es
decir, ninguno prueba algo que no esté en el catálogo. Es la comprobación complementaria a la
anterior y la que evita el problema opuesto al hueco de cobertura: gastar esfuerzo de prueba en
comportamiento que nadie ha pedido.

## Huecos de cobertura declarados

- **RF-03** — Instancia pública compartida: la correlatividad del Id no es verificable de forma reproducible.
- **RF-21** — Requiere alterar la configuración global de PIM en un entorno compartido con otros usuarios. Descartado por criterio.
- **RF-27** — Cubierto parcialmente por CP-033 (coherencia de fechas). Los catálogos de puesto y categoría quedan para el ciclo 2.
- **RN-05** — No verificable sin acceso a la base de datos (riesgo R-06).
- **RNF-04** — Solo se registra el tiempo percibido; medir sobre una instancia pública compartida no daría cifras válidas.
- **RNF-05** — Cubierto transversalmente por la estrategia (los 15 casos de prioridad Alta se ejecutaron en 3 navegadores), sin caso dedicado.

Declarar los huecos es parte del entregable. Una matriz que muestre el 100 % de cobertura sin
explicar cómo lo consigue es menos fiable que una que reconoce sus límites: en la práctica, el 100 %
se obtiene casi siempre relajando lo que se considera «cubierto».
