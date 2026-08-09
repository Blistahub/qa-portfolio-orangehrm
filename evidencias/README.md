# Evidencias

Capturas de pantalla que respaldan cada defecto reportado en [`03-bug-reports/`](../03-bug-reports/).

## Convención de nombres

```
BUG-00X-NN-descripcion-corta.png
```

| Parte | Significado |
| --- | --- |
| `BUG-00X` | Defecto al que pertenece la captura |
| `NN` | Orden dentro de la secuencia del defecto (`01`, `02`, `03`…) |
| `descripcion-corta` | Qué muestra, en minúsculas y separado por guiones |

Ejemplo: `BUG-009-02-joined-date.png`

El prefijo numérico ordena las capturas por sí solo en cualquier explorador de archivos, y el
nombre indica qué contiene sin necesidad de abrirla.

## Qué debe mostrar una captura útil

1. **El estado completo de la pantalla**, no solo el campo. El contexto —la ruta de navegación, el
   nombre del empleado, la pestaña activa— es lo que permite a un desarrollador situarse.
2. **El dato de entrada visible** antes de la acción, y **el resultado** después. Dos capturas
   cuentan una historia que una sola no cuenta.
3. **El resaltado del punto exacto** con un recuadro rojo, cuando la pantalla es densa.
4. **La URL**, siempre que sea relevante para reproducir.
5. Para los defectos con notas de API, la **pestaña *Network* de las DevTools** con la petición
   seleccionada, mostrando el código de estado y el cuerpo. Es la captura que convierte una
   observación de interfaz en un diagnóstico.

## Qué no debe aparecer

- Datos personales reales, propios o de terceros.
- Credenciales distintas de las públicas de la demo (`Admin` / `admin123`), publicadas por el propio
  fabricante en su pantalla de acceso.
- Pestañas, marcadores o notificaciones del navegador ajenas a la prueba.

## Índice de capturas por defecto

Cada reporte lleva en su sección **Evidencia** la tabla de capturas que le corresponde. El total
previsto para este ciclo es de 30 capturas repartidas entre los 12 defectos.
