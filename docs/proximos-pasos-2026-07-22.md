# Próximos pasos: cierre de reestructuración y espejo en inglés

**Fecha:** 2026-07-22
**Estado global:** Abierto, en ejecución por etapas.
**Alcance de este documento:** cerrar las tareas que quedaron vivas después de la reestructuración del temario MA1001B, sin modificar `presentaciones/` en esta fase.

## Línea base verificada

La reestructuración del libro en español ya está aplicada. Los archivos de problemas en español usan el estándar vigente de 6 problemas por sección, ordenados por nivel de Bloom, con etiquetas hash `prob:<7-hex>`.

El espejo en inglés sigue abierto y es la deuda principal:

- Archivos de problemas ES: 60.
- Archivos de problemas EN: 29.
- Contrapartes exactas EN faltantes para archivos ES `(p).tex`: 37.
- `\input{}` en el maestro ES: 139.
- `\input{}` en el maestro EN: 77.
- Archivos EN `(p).tex` con encabezados visibles de niveles heredados: 29.
- Archivos EN `(p).tex` con etiquetas numéricas `prob:X.Y.Z`: 14.

También queda un choque de etiqueta de ejemplo:

- `latex/conceptos_estadisticos.tex`
- `latex/distribuciones_muestrales_medias.tex`
- `latex/en_conceptos_estadisticos.tex`
- `latex/en_distribuciones_muestreo_avanzado.tex`

En los cuatro aparece `\label{exmp:5.1.1}`. No se encontró una referencia viva a esa etiqueta durante el diagnóstico previo, pero debe corregirse antes de compilar para evitar advertencias de etiquetas duplicadas.

## Plan de cierre por etapas

### 1. Documento rector

**Estado:** Cubierto en esta etapa.

Crear este documento como referencia canónica de las tareas abiertas, con línea base, etapas, criterios de aceptación y backlog explícito.

### 2. Corrección de etiquetas y documentación operativa

**Estado:** Pendiente.

Cambiar las etiquetas duplicadas `exmp:5.1.1` por etiquetas semánticas compartidas entre ES y EN:

- `exmp:sample-mean-unbiased`
- `exmp:sample-mean-and-unbiased-variance`

Actualizar `CLAUDE.md`, `AGENTS.md` y el encabezado de `docs/plan-renumeracion-temario-MA1001B.md` para reflejar el estado actual:

- El estándar ES vigente es exactamente 6 problemas por archivo `(p).tex`, en orden Bloom, con etiquetas hash.
- El estándar 3-3-2-2 y el diagnóstico de etiquetas numéricas son históricos.
- Los archivos teóricos sin sección propia son parte intencional de la jerarquía actual.
- La brecha EN sigue activa hasta completar este documento.

Registrar el checkpoint en `CHANGELOG.md`.

### 3. Reconstrucción del espejo teórico EN

**Estado:** Pendiente.

Usar el libro ES como fuente canónica. El maestro EN debe quedar con la misma secuencia normalizada de `\input{}` que el maestro ES para los capítulos 1-9, cambiando solamente el prefijo `en_` y la infraestructura propia del idioma.

Archivar los paquetes EN previos a la renumeración, junto con sus compañeros de problemas del mismo nombre, en:

`archive/latex/en-pre-syllabus-2026-07-22/`

Paquetes EN teóricos identificados para archivo y reutilización controlada:

- `en_distribuciones_especiales.tex`
- `en_variables_aleatorias_continuas_avanzado.tex`
- `en_distribuciones_muestreo_avanzado.tex`
- `en_estimacion_intervalos_avanzado.tex`
- `en_pruebas_de_hipotesis.tex`
- `en_chi_cuadrada.tex`
- `en_pruebas_hipotesis_avanzadas.tex`
- `en_diseno_experimentos_anova.tex`

El material traducido que siga siendo fiel se puede reutilizar. Lo que falte o haya cambiado después de la reestructuración ES debe traducirse desde el contenido ES actual.

No agregar `_md_entornos` al maestro EN: `_en_entornos.tex` ya incorpora los alias necesarios (`problema`/`problem`, `solucion`/`solution`, `solproblema`/`solproblem`).

### 4. Migración de problemas EN

**Estado:** Pendiente.

Crear una contraparte `en_*(p).tex` por cada uno de los 60 archivos ES de problemas.

Cada par ES/EN debe cumplir:

- 6 problemas y 6 soluciones.
- Orden Bloom: `Remember`, `Understand`, `Apply`, `Analyze`, `Evaluate`, `Create`.
- Comentarios invisibles de nivel.
- Misma lista de etiquetas hash que el archivo ES correspondiente.
- Sin encabezados visibles heredados `Fundamental/Operational/Analytical/Challenging`.
- Sin etiquetas numéricas ni etiquetas descriptivas heredadas en archivos EN vivos.

Los problemas EN adicionales que no correspondan al par ES vigente deben quedar solo en el archivo histórico, no en el maestro vivo.

### 5. Verificación final

**Estado:** Pendiente.

Antes de cerrar la tarea:

- Comparar secuencias normalizadas de `\input{}` entre maestros ES y EN.
- Confirmar 60 archivos ES `(p).tex` y 60 archivos EN `en_*(p).tex`.
- Validar cada par ES/EN de problemas: 6 enunciados, 6 soluciones, orden Bloom idéntico, etiquetas idénticas.
- Confirmar unicidad de etiquetas en cada maestro compilable.
- Compilar dos veces:
  - `latex/[Modelación Estadística].tex`
  - `latex/[Statistical Modeling].tex`
- Exigir 0 errores LaTeX, 0 referencias indefinidas y 0 advertencias de etiquetas multiplicadas.
- Ejecutar `git diff --check`.
- Confirmar que no se agregaron `.log` ni cambios ajenos.

Los artefactos de build se actualizan si cambian por convención del repositorio, pero no se hace `git commit` ni `git push`.

## Backlog separado

Estas tareas quedan registradas, pero fuera del alcance de este cierre:

- Solape de captions en tablas anchas con `tufte-book`.
- Diferencia de orden de la distribución exponencial entre libro y presentaciones.
- Inexactitudes en `presentaciones/ROADMAP.md` sobre frames y estado de avance.

Antes de tocar `presentaciones/` en una tarea futura, leer obligatoriamente:

- `presentaciones/README.md`
- `presentaciones/ROADMAP.md`
- `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md`

## Criterio de cierre

La tarea se considera cerrada solo cuando el libro ES y el espejo EN compilan sin errores ni advertencias críticas, tienen estructura paralela, tienen 60 pares de problemas con etiquetas compartidas, y la documentación de operación ya no contradice el estado vivo del repositorio.
