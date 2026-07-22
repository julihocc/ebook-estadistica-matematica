# Próximos pasos: cierre de reestructuración y espejo en inglés

**Fecha:** 2026-07-22
**Estado global:** Abierto, en ejecución por etapas.
**Alcance de este documento:** cerrar las tareas que quedaron vivas después de la reestructuración del temario MA1001B, sin modificar `presentaciones/` en esta fase.

## Línea base verificada

La reestructuración del libro en español ya está aplicada. Los archivos de problemas en español usan el estándar vigente de 6 problemas por sección, ordenados por nivel de Bloom, con etiquetas hash `prob:<7-hex>`.

El espejo en inglés sigue abierto y es la deuda principal:

- Archivos de problemas ES: 60.
- Archivos de problemas EN: 52 después del checkpoint 4H.
- Contrapartes exactas EN completas y normalizadas para archivos ES `(p).tex`: 41 de 60 después del checkpoint 4H.
- Contrapartes exactas EN faltantes para archivos ES `(p).tex`: 11 después del checkpoint 4H.
- Contrapartes exactas EN existentes pero todavía no normalizadas contra su fuente ES: 8 después del checkpoint 4H.
- `\input{}` en el maestro ES: 139.
- `\input{}` en el maestro EN: 131 después del checkpoint 4H; la paridad total de 139 entradas queda pendiente de la migración de problemas EN.
- Archivos EN `(p).tex` con encabezados visibles de niveles heredados: 11.
- Archivos EN `(p).tex` con etiquetas numéricas `prob:X.Y.Z` o `prob:en:*`: 1.

Se detectó y corrigió en la etapa 2 un choque de etiqueta de ejemplo:

- `latex/conceptos_estadisticos.tex`
- `latex/distribuciones_muestrales_medias.tex`
- `latex/en_conceptos_estadisticos.tex`
- `latex/en_distribuciones_muestreo_avanzado.tex`

En los cuatro aparecía `\label{exmp:5.1.1}`. No se encontró una referencia viva a esa etiqueta durante el diagnóstico previo. Se reemplazó por etiquetas semánticas compartidas entre ES y EN.

## Plan de cierre por etapas

### 1. Documento rector

**Estado:** Cubierto en esta etapa.

Crear este documento como referencia canónica de las tareas abiertas, con línea base, etapas, criterios de aceptación y backlog explícito.

### 2. Corrección de etiquetas y documentación operativa

**Estado:** Cubierto en esta etapa.

Se cambiaron las etiquetas duplicadas `exmp:5.1.1` por etiquetas semánticas compartidas entre ES y EN:

- `exmp:sample-mean-unbiased`
- `exmp:sample-mean-and-unbiased-variance`

Se actualizaron `CLAUDE.md`, `AGENTS.md` y el encabezado de `docs/plan-renumeracion-temario-MA1001B.md` para reflejar el estado actual:

- El estándar ES vigente es exactamente 6 problemas por archivo `(p).tex`, en orden Bloom, con etiquetas hash.
- El estándar 3-3-2-2 y el diagnóstico de etiquetas numéricas son históricos.
- Los archivos teóricos sin sección propia son parte intencional de la jerarquía actual.
- La brecha EN sigue activa hasta completar este documento.

Se registró el checkpoint en `CHANGELOG.md`.

### 3. Reconstrucción del espejo teórico EN

**Estado:** Cubierto parcialmente en esta etapa.

Se usó el libro ES como fuente canónica para reconstruir el espejo teórico EN. Ahora existen 70 archivos de teoría ES y 70 contrapartes EN. El maestro EN quedó actualizado para usar los archivos de teoría divididos; conserva temporalmente los 29 cuadernos de problemas EN heredados hasta que la etapa 4 cree las 37 contrapartes faltantes.

La secuencia total normalizada de `\input{}` todavía no puede ser idéntica a ES porque faltan los archivos `en_*(p).tex` de la etapa 4.

Se archivaron copias de los paquetes EN previos a la renumeración, junto con sus compañeros de problemas del mismo nombre, en:

`archive/latex/en-pre-syllabus-2026-07-22/`

Paquetes EN teóricos archivados y reutilizados de forma controlada:

- `en_distribuciones_especiales.tex`
- `en_variables_aleatorias_continuas_avanzado.tex`
- `en_distribuciones_muestreo_avanzado.tex`
- `en_estimacion_intervalos_avanzado.tex`
- `en_pruebas_de_hipotesis.tex`
- `en_chi_cuadrada.tex`
- `en_pruebas_hipotesis_avanzadas.tex`
- `en_diseno_experimentos_anova.tex`

El material traducido fiel se reutilizó por división mecánica. Las secciones nuevas desde la reestructuración ES se tradujeron directamente: `en_tecnicas_de_conteo.tex`, `en_relacion_ic_pruebas_hipotesis.tex`, `en_prueba_media_varianza_desconocida.tex`, el bloque de cuadrados latinos/grecolatinos en `en_dbca_cuadrados_latinos.tex`, y `en_diseno_factorial.tex`.

No agregar `_md_entornos` al maestro EN: `_en_entornos.tex` ya incorpora los alias necesarios (`problema`/`problem`, `solucion`/`solution`, `solproblema`/`solproblem`).

### 4. Migración de problemas EN

**Estado:** En ejecución por checkpoints.

Checkpoint 4A cubierto: los 3 cuadernos EN del Capítulo 1 fueron reemplazados por espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_introduccion_estadistica_descriptiva(p).tex`
- `en_medidas_tendencia_central(p).tex`
- `en_medidas_dispersion(p).tex`

Después de este checkpoint, quedan 57 cuadernos EN por normalizar al estándar vivo. La cuenta de contrapartes exactas EN faltantes sigue en 37 porque este checkpoint migró archivos EN que ya existían, no creó todavía los pares ausentes de capítulos posteriores.

Checkpoint 4B cubierto: los 6 cuadernos EN del Capítulo 2 fueron reemplazados o creados como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_conjuntos(p).tex`
- `en_fundamentos_de_probabilidad(p).tex`
- `en_tecnicas_de_conteo(p).tex`
- `en_probabilidad_condicional(p).tex`
- `en_teorema_de_bayes(p).tex`
- `en_muestreo_aleatorio(p).tex`

En este checkpoint se creó la contraparte faltante `en_tecnicas_de_conteo(p).tex` y se agregó al maestro EN inmediatamente después de `en_tecnicas_de_conteo`.

Después de este checkpoint, hay 9 cuadernos EN ya normalizados y quedan 51 cuadernos EN por normalizar al estándar vivo. Las contrapartes exactas EN faltantes bajan de 37 a 36.

Checkpoint 4C cubierto: los 7 cuadernos EN del Capítulo 3 fueron reemplazados o creados como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_variables_aleatorias_discretas(p).tex`
- `en_distribucion_binomial(p).tex`
- `en_distribucion_multinomial(p).tex`
- `en_distribucion_geometrica_binomial_negativa(p).tex`
- `en_distribucion_hipergeometrica(p).tex`
- `en_distribucion_poisson(p).tex`
- `en_variables_discretas_ciencia_datos(p).tex`

En este checkpoint se agregaron al maestro EN las seis entradas de problemas que faltaban después de las secciones nuevas del Capítulo 3: binomial, multinomial, geométrica/binomial negativa, hipergeométrica, Poisson y aplicaciones de variables discretas en ciencia de datos.

Después de este checkpoint, hay 16 cuadernos EN ya normalizados y quedan 44 cuadernos EN por normalizar al estándar vivo. Las contrapartes exactas EN faltantes bajan de 36 a 30.

Checkpoint 4D cubierto: los 2 cuadernos EN heredados del inicio del Capítulo 4 fueron reemplazados como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_variables_aleatorias_continuas(p).tex`
- `en_esperanza_matematica(p).tex`

Este checkpoint no crea contrapartes faltantes nuevas porque ambos archivos ya existían en el maestro EN. Sí reduce la deuda heredada: los archivos EN con encabezados visibles de tiers bajan de 20 a 18 y los archivos EN con etiquetas numéricas o `prob:en:*` bajan de 6 a 4.

Después de este checkpoint, hay 18 cuadernos EN ya normalizados y quedan 42 cuadernos EN por normalizar al estándar vivo. Las contrapartes exactas EN faltantes permanecen en 30.

Checkpoint 4E cubierto: se crearon las 6 contrapartes EN faltantes del resto del Capítulo 4 como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_distribucion_uniforme_continua(p).tex`
- `en_distribucion_normal(p).tex`
- `en_distribuciones_tipo_gamma(p).tex`
- `en_funcion_generadora_momentos(p).tex`
- `en_transformacion_variables(p).tex`
- `en_distribuciones_funciones_variable_aleatoria(p).tex`

En este checkpoint se retiró del maestro EN el bundle heredado `en_variables_aleatorias_continuas_avanzado(p)` y se eliminó el archivo vivo `en_variables_aleatorias_continuas_avanzado(p).tex`, porque sus contenidos ya quedaron reemplazados por los cuadernos de sección correspondientes.

Después de este checkpoint, hay 24 cuadernos EN ya normalizados y quedan 36 cuadernos EN por normalizar al estándar vivo. Las contrapartes exactas EN faltantes bajan de 30 a 24.

Checkpoint 4F cubierto: se crearon o reemplazaron los 6 cuadernos EN del Capítulo 5 como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_distribuciones_muestrales_medias(p).tex`
- `en_distribucion_muestral_chi_cuadrada(p).tex`
- `en_distribucion_muestral_t(p).tex`
- `en_distribucion_muestral_f(p).tex`
- `en_distribuciones_muestreo_ciencia_datos(p).tex`
- `en_estadisticos_z_t(p).tex`

En este checkpoint se retiró del maestro EN el bundle heredado `en_distribuciones_muestreo_avanzado(p)` y se eliminó el archivo vivo `en_distribuciones_muestreo_avanzado(p).tex`, porque sus contenidos ya quedaron reemplazados por los cuadernos de sección correspondientes.

Después de este checkpoint, hay 30 contrapartes exactas EN ya normalizadas contra sus fuentes ES y quedan 30 secciones ES de problemas por cubrir en EN: 19 todavía no tienen contraparte exacta `en_*(p).tex`, y 11 ya tienen archivo EN exacto pero falta normalizarlo contra etiquetas/contenido del ES vigente. Los archivos EN con encabezados visibles heredados bajan de 17 a 15 y los archivos EN con etiquetas numéricas o `prob:en:*` bajan de 3 a 2.

Checkpoint 4G cubierto: se crearon o reemplazaron los 7 cuadernos EN del Capítulo 6 como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_estimacion_puntual(p).tex`
- `en_intervalos_de_confianza(p).tex`
- `en_ic_media_diferencia_medias(p).tex`
- `en_errores_estandar(p).tex`
- `en_ic_proporcion_diferencia_proporciones(p).tex`
- `en_ic_varianza_razon_varianzas(p).tex`
- `en_tamano_muestra_estimacion(p).tex`

En este checkpoint se retiró del maestro EN el bundle heredado `en_estimacion_intervalos_avanzado(p)` y se eliminó el archivo vivo `en_estimacion_intervalos_avanzado(p).tex`, porque sus contenidos ya quedaron reemplazados por los cuadernos de sección correspondientes.

Después de este checkpoint, hay 37 contrapartes exactas EN ya normalizadas contra sus fuentes ES y quedan 23 secciones ES de problemas por cubrir en EN: 14 todavía no tienen contraparte exacta `en_*(p).tex`, y 9 ya tienen archivo EN exacto pero falta normalizarlo contra etiquetas/contenido del ES vigente. Los archivos EN con encabezados visibles heredados bajan de 15 a 12 y los archivos EN con etiquetas numéricas o `prob:en:*` bajan de 2 a 1.

Checkpoint 4H cubierto: se crearon o reemplazaron los 4 cuadernos EN de la primera mitad del Capítulo 7 como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_pruebas_de_hipotesis(p).tex`
- `en_relacion_ic_pruebas_hipotesis(p).tex`
- `en_valores_p_decisiones(p).tex`
- `en_prueba_media_varianza_desconocida(p).tex`

En este checkpoint no se retiró todavía el bundle heredado `en_pruebas_hipotesis_avanzadas(p)`, porque aún respalda secciones posteriores del capítulo que no han recibido contraparte exacta EN.

Después de este checkpoint, hay 41 contrapartes exactas EN ya normalizadas contra sus fuentes ES y quedan 19 secciones ES de problemas por cubrir en EN: 11 todavía no tienen contraparte exacta `en_*(p).tex`, y 8 ya tienen archivo EN exacto pero falta normalizarlo contra etiquetas/contenido del ES vigente. Los archivos EN con encabezados visibles heredados bajan de 12 a 11; los archivos EN con etiquetas numéricas o `prob:en:*` permanecen en 1.

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
