# Guía de ejecución del ciclo

Runbook operativo para ejecutar el ciclo de pruebas del módulo PIM tal y como está diseñado en la
[matriz de casos](02-casos-de-prueba.md). Su objetivo es que **cualquier persona pueda reproducir el
ciclo completo y llegar a los mismos resultados**, que es la condición que separa un informe de
pruebas de una opinión.

Tiempo estimado del ciclo completo: **6–8 horas**, capturas de evidencia incluidas.

---

## 0. Antes de empezar — criterios de entrada

Comprobar los cuatro criterios del §6.1 del [plan de pruebas](01-plan-de-pruebas.md):

- [ ] La instancia `opensource-demo.orangehrmlive.com` responde y permite iniciar sesión con
      `Admin` / `admin123`.
- [ ] Anotar en el [informe de ejecución](04-informe-ejecucion.md) la **fecha y hora de inicio** y
      la **build exacta** que muestre la instancia. El entorno de demostración se actualiza sin
      aviso: sin este dato, una diferencia entre ciclos es indistinguible de una regresión.
- [ ] Anotar las **versiones de Chrome, Firefox y Edge** utilizadas.
- [ ] Preparar los ficheros de datos de prueba del §5 del plan: `foto-900kb.jpg`,
      `foto-1200kb.jpg`, y las cadenas de 30 y 31 caracteres en un bloc de notas para pegarlas.

## 1. Smoke — el ciclo no arranca si esto falla

Ejecutar en este orden. Si alguno falla, **detener el ciclo** y reportarlo como impedimento:

- [ ] [CP-001](02-casos-de-prueba.md#cp-001) — alta de empleado con datos mínimos
- [ ] [CP-013](02-casos-de-prueba.md#cp-013) — búsqueda por Employee Id
- [ ] [CP-018](02-casos-de-prueba.md#cp-018) — Reset de filtros
- [ ] [CP-026](02-casos-de-prueba.md#cp-026) — persistencia de los cambios en el listado
- [ ] [CP-031](02-casos-de-prueba.md#cp-031) — alta de contacto de emergencia

## 2. Orden de ejecución recomendado

El orden no es el de la numeración, sino el que **minimiza la creación de datos**: cada bloque
reutiliza el empleado creado en el anterior.

| Orden | Bloque | Casos | Notas |
| :---: | --- | --- | --- |
| 1 | Alta de empleado | CP-001 … CP-012 | Crear aquí los empleados que usarán los bloques siguientes. |
| 2 | Listado y búsqueda | CP-013 … CP-021 | CP-019 necesita provocar que la última página tenga un solo registro. |
| 3 | Datos personales | CP-022 … CP-028 | Sobre el empleado creado en CP-001. |
| 4 | Contacto y dependientes | CP-029 … CP-032 | Misma ficha. |
| 5 | Job, Salary, Report-to | CP-033 … CP-036 | CP-033 requiere fecha de nacimiento ya informada (bloque 3). |
| 6 | Transversal | CP-037, CP-038 | Requieren DevTools abiertas. |
| 7 | Cross-browser | Los 15 casos de prioridad Alta | Repetir en Firefox y Edge. |
| 8 | Exploratorio | 2 sesiones de 60 min | Cartas de exploración en el §3.2 del plan. |

**Prioridad Alta primero dentro de cada bloque.** Si el entorno cae a mitad del ciclo (riesgo R-03),
la cobertura crítica ya estará asegurada.

## 3. Durante la ejecución

Por cada caso:

- [ ] Ejecutar los pasos **exactamente como están escritos**. Si hace falta desviarse, el caso está
      mal redactado: corregirlo en `tools/casos.py` y regenerar la matriz.
- [ ] Registrar el resultado real, no el esperado.
- [ ] Si falla: **capturar la evidencia en ese momento**, no al final. El entorno se restablece
      periódicamente (riesgo R-01) y una evidencia no capturada es una evidencia perdida.
- [ ] Si falla: abrir las **DevTools > Network**, localizar la petición implicada y anotar método,
      ruta, código de estado y cuerpo relevante. Esa observación es la que va a la sección *Notas
      técnicas* del reporte.

### Regla sobre los resultados

Un caso que se comporta como se esperaba **se marca Pasa aunque el diseño del caso anticipara un
fallo**, y al revés. La matriz describe lo que *debería* ocurrir; el informe, lo que *ocurre*. Si un
defecto documentado en este repositorio no se reproduce en la ejecución, se retira el reporte y se
actualiza el estado del caso: **no se publica un defecto que no se ha visto**.

## 4. Capturas de evidencia

Cada reporte de defecto lleva en su sección **Evidencia** la tabla de capturas que necesita. Al
adjuntarlas:

- [ ] Nombrarlas según la convención de [`evidencias/README.md`](evidencias/README.md).
- [ ] Guardarlas en `evidencias/`.
- [ ] Sustituir la tabla de capturas pendientes del reporte por las imágenes embebidas:

  ```markdown
  ## Evidencia

  **El formulario acepta y guarda el valor inválido**
  ![Formulario con los valores introducidos](../evidencias/BUG-001-01-formulario.png)

  **El registro resultante en Employee List**
  ![Registro guardado](../evidencias/BUG-001-03-listado.png)
  ```

  Cada imagen con una línea que diga **qué hay que mirar en ella**. Una captura sin pie obliga al
  lector a adivinar qué se le está enseñando.

## 5. Al cerrar el ciclo

- [ ] Actualizar el `Estado` de cada caso en `tools/casos.py` con el resultado real.
- [ ] Regenerar los entregables:

  ```bash
  python tools/generar-matriz.py
  python tools/generar-trazabilidad.py
  ```

- [ ] Actualizar las métricas del [informe de ejecución](04-informe-ejecucion.md) para que cuadren
      con la matriz regenerada.
- [ ] Revisar el veredicto: si desaparece algún defecto de severidad Alta, **la recomendación de
      apto / no apto cambia**. El informe debe seguir a los datos, no al revés.
- [ ] Anotar fecha y hora de cierre del ciclo.
- [ ] Eliminar de la demo los empleados de prueba creados, cuando el caso lo permita.

## 6. Verificación de consistencia del repositorio

Antes de dar el ciclo por cerrado, comprobar que la documentación no se contradice:

- [ ] Cada caso con estado `Falla` tiene un defecto asociado, y ese fichero existe.
- [ ] Cada defecto referencia un caso que existe en la matriz.
- [ ] Los totales del informe coinciden con el resumen de la matriz regenerada.
- [ ] Todas las capturas referenciadas existen en `evidencias/`.

Este último punto está automatizado:

```bash
python tools/verificar.py
```
