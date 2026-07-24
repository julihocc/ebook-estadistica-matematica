# Próximos pasos: cierre de reestructuración y espejo en inglés

## Verificación posterior a los commits — 2026-07-24 12:50:34 -06:00

La rama quedó limpia después de registrar la implementación. `git log` confirmó
los siguientes commits locales, todos del 2026-07-24 entre `12:42:34` y
`12:43:32 -06:00`:

- `73d5a71` (12:42:34): documentación operativa y especificaciones.
- `c6db7bb` (12:42:44): PDF principal ES regenerado.
- `6d86c54` (12:42:48): archivo de mazos ES legado.
- `0195e36` (12:42:53): actualización del capítulo 1.
- `147e779` (12:42:57): actualización del capítulo 2 y PDFs 02.00–02.03.
- `f35341f` (12:43:02): actualización del capítulo 3 y retiro de stubs.
- `7fd0981` (12:43:07): actualización del capítulo 4 y retiro de stubs.
- `945635e` (12:43:11): actualización del capítulo 5.
- `076c246` (12:43:17): actualización del capítulo 6 y retiro de stubs.
- `11bad58` (12:43:21): actualización del capítulo 7.
- `bf09a2b` (12:43:26): actualización del capítulo 8.
- `a59cc86` (12:43:32): actualización del capítulo 9 y retiro del stub 09.12.

La comparación desde `734388e` abarcó 164 rutas: 144 de `presentaciones/es/`
y 8 documentales, sin cambios en `presentaciones/en/`,
`presentaciones/code/` ni archivos `.log`. Las dos alternativas técnicas
previstas ya estaban cerradas: captions ANOVA en `84f4718` y compatibilidad de
`scipy.stats.kstest` en `e243847`. Por tanto, no se selecciona un nuevo
pendiente técnico dentro de esta etapa; cualquier trabajo adicional requiere
un nuevo alcance y fecha de inicio.

## Cierre final documentado — 2026-07-24 11:54:02 -06:00

La verificación posterior a la actualización del catálogo mantuvo 72 mazos ES,
72 filas de matriz y 8 mazos legado archivados. Los enlaces relativos de los
documentos operativos actualizados pasan la comprobación. En ese corte todavía
no se había creado commit ni hecho push; el registro posterior aparece arriba.

## Verificación física ES completada — 2026-07-24 11:35:16 -06:00

- Se confirmaron 72 comandos `\section`/`\section*` activos de teoría en las
  fuentes ES y 72 filas en la matriz.
- Existen exactamente 72 mazos ES físicos, uno por fila de la matriz; no hay
  duplicados ni mazos asociados a secciones `(p)`.
- Se archivaron 8 mazos legado fuera del árbol vivo. Los 72 mazos compilaron
  dos veces con código `0`; no hubo errores, referencias indefinidas,
  etiquetas duplicadas ni desbordamientos en páginas de contenido.
- Se eliminaron bloques de ejercicios y referencias a problemas de los mazos;
  se conservan únicamente exposiciones teóricas y desarrollos ya resueltos.
- Esta etapa modificó notas ES, mazos ES, matriz, PDFs generados y archivo
  histórico; no modificó `presentaciones/en/` ni `presentaciones/code/`.
- No se creó commit ni se hizo `git push`.

## Registro de implementación — 2026-07-23 17:32:50 -06:00

Se promovieron Fundamentos de probabilidad y el Teorema de Bayes a secciones
propias de las notas ES. La estructura pedagógica de la Unidad 1 queda
1.1–1.6, mientras que la transcripción oficial MA1001B conserva sus cuatro
subtemas. La matriz `docs/matriz-notas-presentaciones-es.md` registra 72
secciones activas y su correspondencia prevista con mazos ES.

Los mazos españoles del capítulo 2 usan `02.00`–`02.06`; se añadió el mazo de
Técnicas de conteo. Los bloques de problemas no forman parte de los mazos:
deben usarse únicamente ejemplos y soluciones ya resueltos en teoría. Esta
etapa no modifica `presentaciones/en/` ni `presentaciones/code/`, y no cambia
el contenido matemático ni los archivos `(p)`.

La auditoría física y la compilación doble quedaron completadas el
`2026-07-24 11:35:16 -06:00`; el párrafo conserva el registro del estado
previo y ya no representa una tarea abierta.

**Fecha:** 2026-07-22
**Estado global:** Cerrado el 2026-07-23 11:03:37 -06:00, tras completar los checkpoints 4J y 4K y la verificación final.
**Alcance de este documento:** cerrar las tareas que quedaron vivas después de la reestructuración del temario MA1001B. La reconciliación puede modificar documentación operativa, captions de tablas ANOVA y nombres/rutas de mazos y scripts, pero no cambia contenido matemático ni lógica ejecutable de Python.

## Reconciliación ANOVA y orden de distribuciones verificada al 2026-07-23 12:16:14 -06:00

- Las tablas ANOVA anchas de `efectos_modelo_fijo` y `dbca_cuadrados_latinos`, en ES y EN, usan `table*` con `[htbp]`; captions y labels preceden al `tabular`. La inspección visual de las páginas 320/330 ES y 300/309 EN confirmó que no hay solapamiento con los encabezados.
- El libro y sus maestros conservan la secuencia canónica `Uniforme → Normal → Gamma`, con Exponencial como subsección de Gamma.
- Los mazos y scripts de variables continuas siguen ahora `04.05 Normal → 04.06 Exponencial → 04.07 Gamma`. El mazo 04.06 es una extracción pedagógica de la subsección Exponencial del libro; no implica una sección independiente en el maestro.
- Se actualizaron `presentaciones/README.md`, `presentaciones/ROADMAP.md`, títulos, agendas y rutas `\lstinputlisting`; no se alteraron problemas Bloom/hash ni entradas `\input{}` de los maestros.
- Los maestros compilaron dos pasadas (`ES=0,0`, `EN=0,0`) y los 14 mazos del capítulo 04 compilaron dos pasadas cada uno (`0,0`). Los únicos desbordamientos detectados están en portadas, no en contenido.
- Pendiente técnico fechado: el script `presentaciones/code/04_variables_aleatorias_continuas/04.05_normal_distribution.py` falla en la llamada `scipy.stats.kstest` con la API instalada; corregir esa compatibilidad requiere una modificación de lógica Python y queda fuera de esta etapa.
- Commits locales relacionados: `84f4718` (captions ANOVA) y `810bc25` (renumeración y catálogos). No se hizo `git push`.

## Cierre de compatibilidad del laboratorio Normal verificado al 2026-07-23 14:47:30 -06:00

- Se reemplazó la llamada string-based de `scipy.stats.kstest` por una CDF normal explícita con `loc=theo_mean` y `scale=\sqrt{theo_var}`; la prueba estadística y sus parámetros no cambiaron.
- `04.05_normal_distribution.py` y `04.06_exponential_distribution.py` terminaron con código de salida `0`; el laboratorio Normal reportó `D=0.0014`, `p=0.7069`.
- El estado activo de `presentaciones/README.md` y `presentaciones/ROADMAP.md` ya no declara pendientes ANOVA, de orden de distribuciones ni de compatibilidad Python.
- No se modificaron mazos Beamer, maestros LaTeX ni cuadernos Bloom/hash.

## Reconciliación documental de presentaciones verificada al 2026-07-23 11:17:26 -06:00

- `presentaciones/README.md`, `presentaciones/ROADMAP.md` y `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md` ya describen la convención vigente de seis niveles Bloom, etiquetas `prob:<7-hex>` y soluciones enlazadas.
- El catálogo ES actualizado refleja 72 mazos y 72 PDF; las cifras EN y de
  scripts de ese corte se conservan como historial porque esta etapa no tocó
  `presentaciones/en/` ni `presentaciones/code/`.
- Las referencias activas a 10 problemas `3-3-2-2`, a la antigua Unidad 8 y a bundles retirados fueron corregidas o marcadas como historial anterior al 2026-07-20.
- Esa etapa fue exclusivamente documental y no modificó `presentaciones/es/`, `presentaciones/en/` ni `presentaciones/code/`.
- El backlog de esa fecha (solapamiento de captions y diferencia de orden de Exponencial) quedó resuelto el 2026-07-23 12:16:14 -06:00; permanece únicamente la incompatibilidad técnica de `scipy.stats.kstest` descrita arriba.

## Cierre verificado el 2026-07-23 11:03:37 -06:00

- Checkpoint 4J completado en `cd2abf4`: seis contrapartes EN de diseño experimental, maestro EN actualizado y bundle `en_diseno_experimentos_anova(p).tex` retirado del árbol vivo.
- Checkpoint 4K completado en `534f156`: siete contrapartes EN de regresión normalizadas con seis problemas Bloom y etiquetas compartidas.
- El bundle `en_distribuciones_especiales(p).tex` se retiró del maestro y del árbol vivo; su copia histórica ya existía en `archive/latex/en-pre-syllabus-2026-07-22/`.
- Estado vivo: 60 archivos ES `(p).tex`, 60 archivos EN `en_*(p).tex`, 139 entradas `\input{}` en cada maestro y 0 objetivos faltantes.
- La secuencia de etiquetas de los 60 pares coincide; cada archivo contiene 6 enunciados, 6 soluciones y los seis niveles Bloom.
- El maestro EN compiló tres pasadas tras 4J y tres pasadas tras 4K, sin errores LaTeX, referencias indefinidas ni etiquetas multiplicadas.
- `presentaciones/` no se modificó y no se hizo `git push`.

## Bitácora de progreso registrada el 2026-07-22 17:04 -06:00

Entre el checkpoint 4F y el corte documentado el 2026-07-22 17:04 -06:00 se avanzó el cierre del espejo EN hasta el checkpoint 4I, con verificación incremental y commits locales por bloques revisables:

- `c8712a1` — `Completes EN checkpoint 4G migration`: migración de los 7 cuadernos EN del Capítulo 6 / Estimación, retiro de `en_estimacion_intervalos_avanzado(p).tex`, actualización del maestro EN y verificación de compilación.
- `393207a` — `Advances EN Chapter 7 problem migration`: migración de los 4 cuadernos EN de la primera mitad del Capítulo 7 / Pruebas de hipótesis.
- `a8db919` — `Completes EN Chapter 7 problem migration`: migración de los 6 cuadernos EN restantes del Capítulo 7, retiro de `en_pruebas_hipotesis_avanzadas(p).tex`, actualización del maestro EN y verificación de compilación.

Estado verificado al 2026-07-22 17:04 -06:00:

- 47 de 60 secciones ES de problemas ya tienen contraparte EN exacta normalizada.
- Quedan 13 secciones por cubrir: 6 sin contraparte exacta EN y 7 con archivo EN existente pero todavía heredado.
- El maestro EN tiene 135 entradas `\input{}` y 0 objetivos faltantes.
- Quedan 2 referencias a nombres de bundles heredados de problemas en el maestro EN: `en_distribuciones_especiales(p)` y `en_diseno_experimentos_anova(p)`.
- No se tocó `presentaciones/`.
- No se hizo `git push`.

Pendientes identificados al 2026-07-22 17:04 -06:00 (resueltos al 2026-07-23 11:03:37 -06:00):

1. **Checkpoint 4J — Capítulo 8 / Diseño experimental.** Crear las 6 contrapartes EN faltantes y conectarlas al maestro EN inmediatamente después de sus archivos teóricos:
   - `en_estrategias_experimentacion(p).tex`
   - `en_anova_un_factor(p).tex`
   - `en_efectos_modelo_fijo(p).tex`
   - `en_adecuacion_modelo_anova(p).tex`
   - `en_cuadrados_latinos_grecolatinos(p).tex`
   - `en_diseno_factorial(p).tex`
   Al cubrir este bloque debe retirarse del maestro EN y del árbol vivo `en_diseno_experimentos_anova(p).tex`.
2. **Checkpoint 4K — Capítulo 9 / Regresiones.** Normalizar los 7 cuadernos EN que ya existen pero siguen heredados, verificando etiquetas contra sus fuentes ES:
   - `en_regresiones_lineales(p).tex`
   - `en_regresion_multiple(p).tex`
   - `en_validacion_modelo(p).tex`
   - `en_supuestos_regresion(p).tex`
   - `en_regresion_scikit(p).tex`
   - `en_otros_problemas_categoricas(p).tex`
   - `en_otros_problemas_transformaciones(p).tex`
3. **Revisión puntual de bundle vivo restante.** Confirmar en el cierre final si `en_distribuciones_especiales(p).tex` debe conservarse como contraparte válida del archivo ES homónimo o archivarse/retirarse si queda fuera de la estructura paralela final.
4. **Verificación final completa.** Cuando los 60 pares estén normalizados: comparar secuencias de `\input{}` ES/EN, confirmar unicidad de etiquetas, compilar ES y EN, ejecutar `git diff --check`, revisar que no haya `.log` agregados ni cambios ajenos, y actualizar la documentación de operación si el estado vivo ya no coincide con notas históricas.

## Línea base histórica verificada al 2026-07-22 17:04 -06:00

La reestructuración del libro en español ya está aplicada. Los archivos de problemas en español usan el estándar vigente de 6 problemas por sección, ordenados por nivel de Bloom, con etiquetas hash `prob:<7-hex>`.

En ese corte, el espejo en inglés seguía abierto y constituía la deuda principal:

- Archivos de problemas ES: 60.
- Archivos de problemas EN: 56 después del checkpoint 4I.
- Contrapartes exactas EN completas y normalizadas para archivos ES `(p).tex`: 47 de 60 después del checkpoint 4I.
- Contrapartes exactas EN faltantes para archivos ES `(p).tex`: 6 después del checkpoint 4I.
- Contrapartes exactas EN existentes pero todavía no normalizadas contra su fuente ES: 7 después del checkpoint 4I.
- `\input{}` en el maestro ES: 139.
- `\input{}` en el maestro EN: 135 después del checkpoint 4I; la paridad total de 139 entradas queda pendiente de la migración de problemas EN.
- Archivos EN `(p).tex` con encabezados visibles de niveles heredados: 9.
- Archivos EN `(p).tex` con etiquetas numéricas `prob:X.Y.Z` o `prob:en:*`: 1.

Se detectó y corrigió en la etapa 2 un choque de etiqueta de ejemplo:

- `latex/conceptos_estadisticos.tex`
- `latex/distribuciones_muestrales_medias.tex`
- `latex/en_conceptos_estadisticos.tex`
- `latex/en_distribuciones_muestreo_avanzado.tex`

En los cuatro aparecía `\label{exmp:5.1.1}`. No se encontró una referencia viva a esa etiqueta durante el diagnóstico previo. Se reemplazó por etiquetas semánticas compartidas entre ES y EN.

## Plan de cierre por etapas

### 1. Documento rector

**Estado:** Cubierto antes del cierre del 2026-07-23 11:03:37 -06:00.

Crear este documento como referencia canónica de las tareas abiertas, con línea base, etapas, criterios de aceptación y backlog explícito.

### 2. Corrección de etiquetas y documentación operativa

**Estado:** Cubierto antes del cierre del 2026-07-23 11:03:37 -06:00.

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

**Estado:** Cubierto parcialmente en la línea base del 2026-07-22 17:04 -06:00; completado en el cierre del 2026-07-23 11:03:37 -06:00.

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

### 4. Registro histórico de la migración de problemas EN (completado el 2026-07-23 11:03:37 -06:00)

**Estado:** Completado por checkpoints al 2026-07-23 11:03:37 -06:00.

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

Checkpoint 4I cubierto: se crearon o reemplazaron los 6 cuadernos EN restantes del Capítulo 7 como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES:

- `en_prueba_dos_medias(p).tex`
- `en_prueba_proporciones(p).tex`
- `en_prueba_varianzas(p).tex`
- `en_chi_cuadrada(p).tex`
- `en_pruebas_independencia(p).tex`
- `en_pruebas_homogeneidad_varias_proporciones(p).tex`

En este checkpoint se retiró del maestro EN el bundle heredado `en_pruebas_hipotesis_avanzadas(p)` y se eliminó el archivo vivo `en_pruebas_hipotesis_avanzadas(p).tex`, porque sus contenidos ya quedaron reemplazados por los cuadernos de sección correspondientes.

Después de este checkpoint, hay 47 contrapartes exactas EN ya normalizadas contra sus fuentes ES y quedan 13 secciones ES de problemas por cubrir en EN: 6 todavía no tienen contraparte exacta `en_*(p).tex`, y 7 ya tienen archivo EN exacto pero falta normalizarlo contra etiquetas/contenido del ES vigente. Los archivos EN con encabezados visibles heredados bajan de 11 a 9; los archivos EN con etiquetas numéricas o `prob:en:*` permanecen en 1.

El requisito de cierre fue crear una contraparte `en_*(p).tex` por cada uno de los 60 archivos ES de problemas; quedó cumplido el 2026-07-23 11:03:37 -06:00.

Cada par ES/EN debe cumplir:

- 6 problemas y 6 soluciones.
- Orden Bloom: `Remember`, `Understand`, `Apply`, `Analyze`, `Evaluate`, `Create`.
- Comentarios invisibles de nivel.
- Misma lista de etiquetas hash que el archivo ES correspondiente.
- Sin encabezados visibles heredados `Fundamental/Operational/Analytical/Challenging`.
- Sin etiquetas numéricas ni etiquetas descriptivas heredadas en archivos EN vivos.

Los problemas EN adicionales que no correspondan al par ES vigente deben quedar solo en el archivo histórico, no en el maestro vivo.

### 5. Verificación final (completada el 2026-07-23 11:03:37 -06:00)

**Estado:** Completada el 2026-07-23 11:03:37 -06:00.

Verificaciones realizadas para cerrar la tarea:

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

Los artefactos de build se actualizan si cambian por convención del repositorio. Los commits se hacen por chunks revisables cuando el usuario lo solicita; no se hace `git push` sin instrucción explícita.

## Backlog histórico separado al 2026-07-23 11:17:26 -06:00

Estas tareas describían el estado previo y quedaron resueltas al 2026-07-23 14:47:30 -06:00:

- Solape de captions en tablas anchas con `tufte-book`.
- Diferencia de orden de la distribución exponencial entre libro y presentaciones.
- Las inexactitudes de `presentaciones/ROADMAP.md` sobre frames y estado de avance quedaron corregidas en las reconciliaciones del 2026-07-23 12:16:14 y 14:47:30 -06:00.

Antes de tocar `presentaciones/` en una tarea futura, leer obligatoriamente:

- `presentaciones/README.md`
- `presentaciones/ROADMAP.md`
- `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md`

## Criterio de cierre

La tarea se considera cerrada solo cuando el libro ES y el espejo EN compilan sin errores ni advertencias críticas, tienen estructura paralela, tienen 60 pares de problemas con etiquetas compartidas, y la documentación de operación ya no contradice el estado vivo del repositorio.
