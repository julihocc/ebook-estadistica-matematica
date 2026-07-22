# Changelog

Este changelog resume la evolución del repositorio a partir del historial de Git.
Como el proyecto no usa versiones ni tags de lanzamiento, los cambios se agrupan
por fechas e hitos editoriales.

## 2026-07-22 (documentación de cierre y corrección de etiqueta duplicada)

### Añadido / Corregido
- Creado `docs/proximos-pasos-2026-07-22.md` como documento rector de cierre por etapas: línea base verificada, brecha del espejo EN, tareas pendientes, criterios de aceptación y backlog separado para `presentaciones/`/tablas.
- Corregida la colisión preexistente de `\label{exmp:5.1.1}` en ES y EN. Las etiquetas vivas ahora son semánticas y compartidas por idioma: `exmp:sample-mean-unbiased` para el ejemplo de media muestral insesgada y `exmp:sample-mean-and-unbiased-variance` para el ejemplo de media y varianza muestral insesgada.
- Sincronizados `CLAUDE.md`, `AGENTS.md` y el encabezado de `docs/plan-renumeracion-temario-MA1001B.md` para indicar que la convención ES vigente es 6 problemas Bloom con etiquetas hash, que el diagnóstico 3-3-2-2/numérico es histórico para ES, y que el espejo EN sigue abierto hasta completar el plan de cierre.
- Reconstruido el espejo teórico EN a partir de los bundles heredados y del contenido ES nuevo: existen 70 archivos de teoría ES y 70 contrapartes EN; el maestro `latex/[Statistical Modeling].tex` ahora usa los archivos de teoría divididos y conserva temporalmente los 29 cuadernos de problemas EN heredados hasta la migración de problemas.
- Copiados al archivo histórico `archive/latex/en-pre-syllabus-2026-07-22/` los 8 bundles EN previos a la renumeración y sus 8 compañeros `(p).tex`. Los bundles teóricos sin contraparte viva fueron retirados de `latex/` tras generar sus archivos divididos.
- Migrado el checkpoint 4A de problemas EN: los 3 cuadernos del Capítulo 1 (`en_introduccion_estadistica_descriptiva(p).tex`, `en_medidas_tendencia_central(p).tex`, `en_medidas_dispersion(p).tex`) ahora son espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES, sin encabezados visibles heredados ni etiquetas `prob:en:*`.
- Migrado el checkpoint 4B de problemas EN: los 6 cuadernos del Capítulo 2 (`en_conjuntos(p).tex`, `en_fundamentos_de_probabilidad(p).tex`, `en_tecnicas_de_conteo(p).tex`, `en_probabilidad_condicional(p).tex`, `en_teorema_de_bayes(p).tex`, `en_muestreo_aleatorio(p).tex`) ahora son espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES. Se creó `en_tecnicas_de_conteo(p).tex` y se agregó al maestro `latex/[Statistical Modeling].tex`.
- Migrado el checkpoint 4C de problemas EN: los 7 cuadernos del Capítulo 3 (`en_variables_aleatorias_discretas(p).tex`, `en_distribucion_binomial(p).tex`, `en_distribucion_multinomial(p).tex`, `en_distribucion_geometrica_binomial_negativa(p).tex`, `en_distribucion_hipergeometrica(p).tex`, `en_distribucion_poisson(p).tex`, `en_variables_discretas_ciencia_datos(p).tex`) ahora son espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES. Se agregaron al maestro EN las 6 entradas de problemas que faltaban en las secciones nuevas del capítulo.
- Migrado el checkpoint 4D de problemas EN: los 2 cuadernos heredados del inicio del Capítulo 4 (`en_variables_aleatorias_continuas(p).tex`, `en_esperanza_matematica(p).tex`) ahora son espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES, sin encabezados visibles heredados ni etiquetas numéricas.
- Migrado el checkpoint 4E de problemas EN: creados los 6 cuadernos faltantes del resto del Capítulo 4 (`en_distribucion_uniforme_continua(p).tex`, `en_distribucion_normal(p).tex`, `en_distribuciones_tipo_gamma(p).tex`, `en_funcion_generadora_momentos(p).tex`, `en_transformacion_variables(p).tex`, `en_distribuciones_funciones_variable_aleatoria(p).tex`) como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES. Se retiró del maestro EN y del árbol vivo el bundle heredado `en_variables_aleatorias_continuas_avanzado(p).tex`.
- Migrado el checkpoint 4F de problemas EN: creados o reemplazados los 6 cuadernos del Capítulo 5 (`en_distribuciones_muestrales_medias(p).tex`, `en_distribucion_muestral_chi_cuadrada(p).tex`, `en_distribucion_muestral_t(p).tex`, `en_distribucion_muestral_f(p).tex`, `en_distribuciones_muestreo_ciencia_datos(p).tex`, `en_estadisticos_z_t(p).tex`) como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES. Se retiró del maestro EN y del árbol vivo el bundle heredado `en_distribuciones_muestreo_avanzado(p).tex`.
- Migrado el checkpoint 4G de problemas EN: creados o reemplazados los 7 cuadernos del Capítulo 6 (`en_estimacion_puntual(p).tex`, `en_intervalos_de_confianza(p).tex`, `en_ic_media_diferencia_medias(p).tex`, `en_errores_estandar(p).tex`, `en_ic_proporcion_diferencia_proporciones(p).tex`, `en_ic_varianza_razon_varianzas(p).tex`, `en_tamano_muestra_estimacion(p).tex`) como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES. Se retiró del maestro EN y del árbol vivo el bundle heredado `en_estimacion_intervalos_avanzado(p).tex`.
- Migrado el checkpoint 4H de problemas EN: creados o reemplazados los 4 cuadernos de la primera mitad del Capítulo 7 (`en_pruebas_de_hipotesis(p).tex`, `en_relacion_ic_pruebas_hipotesis(p).tex`, `en_valores_p_decisiones(p).tex`, `en_prueba_media_varianza_desconocida(p).tex`) como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES. Se conserva temporalmente el bundle heredado `en_pruebas_hipotesis_avanzadas(p).tex` hasta migrar las secciones restantes del capítulo.
- Migrado el checkpoint 4I de problemas EN: creados o reemplazados los 6 cuadernos restantes del Capítulo 7 (`en_prueba_dos_medias(p).tex`, `en_prueba_proporciones(p).tex`, `en_prueba_varianzas(p).tex`, `en_chi_cuadrada(p).tex`, `en_pruebas_independencia(p).tex`, `en_pruebas_homogeneidad_varias_proporciones(p).tex`) como espejos de 6 problemas Bloom/hash con las mismas etiquetas que sus fuentes ES. Se retiró del maestro EN y del árbol vivo el bundle heredado `en_pruebas_hipotesis_avanzadas(p).tex`.

### Verificación
- Confirmado que no quedan ocurrencias de `\label{exmp:5.1.1}` en `latex/`.
- Confirmado que las dos etiquetas nuevas aparecen una vez por idioma y no se referencian desde otros archivos.
- Confirmado que el maestro EN no apunta a `\input{}` faltantes y que no quedan archivos de teoría ES sin contraparte `en_`.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 3 cuadernos EN del Capítulo 1.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 6 cuadernos EN del Capítulo 2.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 7 cuadernos EN del Capítulo 3.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 2 cuadernos EN heredados del inicio del Capítulo 4.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 6 cuadernos EN nuevos del resto del Capítulo 4.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 6 cuadernos EN del Capítulo 5.
- Después del checkpoint 4F, el maestro EN tiene 124 entradas `\input{}` sin objetivos faltantes; 30 de 60 secciones ES de problemas tienen contraparte EN exacta normalizada, 19 contrapartes exactas EN siguen faltantes y 11 archivos EN exactos siguen pendientes de normalización.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 7 cuadernos EN del Capítulo 6.
- Después del checkpoint 4G, el maestro EN tiene 128 entradas `\input{}` sin objetivos faltantes; 37 de 60 secciones ES de problemas tienen contraparte EN exacta normalizada, 14 contrapartes exactas EN siguen faltantes y 9 archivos EN exactos siguen pendientes de normalización.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 4 cuadernos EN de la primera mitad del Capítulo 7.
- Después del checkpoint 4H, el maestro EN tiene 131 entradas `\input{}` sin objetivos faltantes; 41 de 60 secciones ES de problemas tienen contraparte EN exacta normalizada, 11 contrapartes exactas EN siguen faltantes y 8 archivos EN exactos siguen pendientes de normalización.
- Confirmada la paridad de etiquetas, conteos de 6 problemas/6 soluciones y ausencia de tiers visibles heredados en los 6 cuadernos EN restantes del Capítulo 7.
- Después del checkpoint 4I, el maestro EN tiene 135 entradas `\input{}` sin objetivos faltantes; 47 de 60 secciones ES de problemas tienen contraparte EN exacta normalizada, 6 contrapartes exactas EN siguen faltantes y 7 archivos EN exactos siguen pendientes de normalización.
- No se tocó `presentaciones/`. Los checkpoints se committearon localmente por bloques revisables cuando el usuario lo solicitó; no se hizo `git push`.

## 2026-07-22 (migración de los 21 cuadernos `(p).tex` restantes a la convención Bloom + hash-labels)

### Añadido / Corregido
- **Migración del segundo lote de cuadernos de problemas a la convención decidida el 2026-07-18** (ver esa entrada): 21 archivos `latex/*(p).tex` que ya eran un archivo por tema pero seguían en la convención vieja (banners visibles `Nivel Fundamental/Operativo/Analítico/Desafiante` 3-3-2-2, en su mayoría etiquetas numéricas `prob:X.Y.Z`) se modernizaron a la convención nueva (6 problemas por archivo, uno por nivel de la Taxonomía de Bloom documentado como comentario LaTeX invisible `% <Nivel>`, y etiquetas hasheadas `prob:<7 hex>` verificadas sin colisión contra el `.aux`). Es la continuación directa del primer lote de 8 archivos "_avanzado"/bundle ya migrado y commiteado por el usuario en la sesión anterior (commits `13b41c5`…`bfbd7b9`, no documentados hasta ahora en este changelog).
  - **Cap. 1 (Estadística Descriptiva, 3 archivos):** `introduccion_estadistica_descriptiva(p).tex`, `medidas_tendencia_central(p).tex`, `medidas_dispersion(p).tex`.
  - **Unidad 1 / Cap. 2 (Teoría de Probabilidad, 5 archivos):** `conjuntos(p).tex`, `fundamentos_de_probabilidad(p).tex`, `probabilidad_condicional(p).tex`, `teorema_de_bayes(p).tex`, `muestreo_aleatorio(p).tex`.
  - **Cap. 3 (Variables Aleatorias Discretas, 1 archivo):** `variables_aleatorias_discretas(p).tex`.
  - **Cap. 4 (Variables Aleatorias Continuas, 2 archivos):** `variables_aleatorias_continuas(p).tex`, `esperanza_matematica(p).tex`.
  - **Cap. 5 (Distribuciones de Muestreo, 1 archivo):** `estadisticos_z_t(p).tex`.
  - **Cap. 6 (Estimación, 2 archivos):** `estimacion_puntual(p).tex`, `intervalos_de_confianza(p).tex`.
  - **Cap. 9 (Regresiones Lineales y Múltiples, 7 archivos):** `regresiones_lineales(p).tex`, `regresion_multiple(p).tex`, `validacion_modelo(p).tex`, `supuestos_regresion(p).tex`, `regresion_scikit(p).tex`, `otros_problemas_categoricas(p).tex`, `otros_problemas_transformaciones(p).tex`.
- **3 casos de consolidación genuina** (a diferencia del primer lote, donde el patrón dominante era dividir un archivo en varios): `variables_aleatorias_discretas(p).tex` (30 problemas en 3 subsecciones viejas → 6, cubriendo temáticamente las 3 subsecciones de una sola `\section` de teoría), `variables_aleatorias_continuas(p).tex` (20→6), y `estimacion_puntual(p).tex` (40 problemas en 3 subsecciones → 6, aprovechando para cubrir por primera vez con un problema nuevo la subsección "Los métodos de estimación puntual en Ciencia de Datos", que no tenía ningún problema en la convención vieja).
- **Hallazgos estructurales preexistentes, documentados pero no corregidos (fuera de alcance):** `fundamentos_de_probabilidad.tex`, `teorema_de_bayes.tex` y `estadisticos_z_t.tex` no poseen una `\section` propia (los dos primeros son `\subsection` huérfanas que heredan la numeración de la sección anterior; el tercero usa `\section*` sin numerar), de modo que sus cuadernos migrados aterrizan bajo el encabezado impreso de la sección numerada previa (`conjuntos.tex` §2.1 y `probabilidad_condicional.tex` §2.3, respectivamente, y `distribuciones_muestreo_ciencia_datos.tex` §5.7 para el tercero) en vez de bajo un encabezado propio — mismatch de contenido/título preexistente en la teoría, no introducido por esta migración.
- **Defecto de comillas rectas corregido** en 4 de los archivos nuevos (mismo patrón de corrupción bajo `babel`-español ya documentado el 2026-07-20): `fundamentos_de_probabilidad(p).tex` (texto introductorio heredado verbatim del archivo viejo), `esperanza_matematica(p).tex`, `regresion_scikit(p).tex` y `otros_problemas_transformaciones(p).tex`. Corregido reemplazando por `\emph{}` o comillas tipográficas LaTeX según el caso.
- **Inconsistencia numérica detectada en el archivo viejo y evitada, no corregida en la fuente:** el problema del Estadístico $C_p$ de Mallows en `validacion_modelo(p).tex` (original, ya sobrescrito) tenía una solución con una línea de aritmética repetida tres veces cuyo resultado numérico ($C_p=-20.75$) contradice la propia interpretación del texto ("un valor cercano a $p=3$ indica ausencia de sesgo"). En vez de propagar el error a la convención nueva, se excluyó ese problema del pool de reutilización y se sustituyó por otro problema del mismo archivo viejo (comparación de modelos por validación cruzada de 10 pliegues) para completar los 6 niveles de Bloom.
- Los 7 archivos de Cap. 9 preservan la excepción estructural ya existente antes de esta tarea: cada uno vive en su propia `\section` numerada dedicada exclusivamente a problemas (patrón `Problemas resueltos de ...` del capítulo suplementario). `regresiones_lineales(p).tex` en particular respalda una cadena de 6 archivos de teoría (`correlacion`, `introduccion_regresiones_lineales`, `regresiones_lineales`, `matematicas_regresiones`, `simulacion_regresion`, `valores_optimos`, `implementacion_regresion`) y por eso conserva su propio `\section` sin asterisco (en vez de `\section*{Problemas}`, usado en los otros 20 archivos del lote); `otros_problemas_categoricas(p).tex` y `otros_problemas_transformaciones(p).tex` siguen compartiendo la única `\section` de `otros_problemas.tex`, aterrizando consecutivamente bajo el mismo número de sección.

### Verificación
- Cada uno de los 21 archivos: libro maestro ES recompilado dos veces (`pdflatex -interaction=nonstopmode`) tras la edición, **0 errores, 0 referencias indefinidas nuevas** (única preexistente tolerada en todo el log: `exmp:5.1.1`, fuera de alcance).
- Exactamente 6 `\begin{problema}` y 6 `\begin{solproblema}[prob:<hash>]` confirmados por archivo (`grep` dedicado), un nivel de Bloom cada uno en orden Recordar→Crear; cada hash de 7 hex verificado individualmente sin colisión contra el `.aux` compilado antes de escribirse en el archivo.
- Verificación visual (renderizado a imagen con `pdftoppm`) de al menos una página por archivo migrado, confirmando ausencia de banners de nivel visibles, comillas corruptas y desbordes de tabla/columna.
- `git status --short latex/` inspeccionado tras cada archivo: únicamente el archivo `.tex` modificado más el PDF recompilado, sin archivos nuevos en los 21 casos (a diferencia del primer lote, donde 8 archivos se dividían en 34).
- **Sin `git commit` en ningún punto de la sesión** — el diff completo de los 21 archivos queda staged para revisión del usuario, siguiendo la misma convención que la sesión de migración anterior.

## 2026-07-20 (continuación 3 — división de los 8 archivos de teoría que agrupaban varias secciones)

### Corregido
- **Causa raíz del desfase de numeración y de los encabezados "Problemas" duplicados**: se detectó que 8 archivos de teoría en los capítulos 3-8 agrupaban entre 2 y 7 `\section` reales cada uno en un único archivo, sin ningún `\input` que las separara físicamente (36 secciones en total): `distribuciones_especiales.tex`, `variables_aleatorias_continuas_avanzado.tex`, `distribuciones_muestreo_avanzado.tex`, `estimacion_intervalos_avanzado.tex`, `pruebas_de_hipotesis.tex`, `chi_cuadrada.tex`, `pruebas_hipotesis_avanzadas.tex` y `diseno_experimentos_anova.tex`. Esto era la causa estructural de que los cuadernos de problemas nuevos creados hoy mismo (`relacion_ic_pruebas_hipotesis(p).tex`, `cuadrados_latinos_grecolatinos(p).tex`) no pudieran aterrizar en su sección correcta, y de que dos de ellos (`cuadrados_latinos_grecolatinos(p)` y `diseno_factorial(p)`) quedaran apilados uno justo después del otro, produciendo dos encabezados "Problemas" seguidos en el PDF bajo la sección 8.6.
- **Los 8 archivos se dividieron en un archivo por sección real** (34 archivos nuevos con nombre descriptivo por tema, 2 archivos conservados — `pruebas_de_hipotesis.tex` y `chi_cuadrada.tex` — recortados a su primera sección únicamente), preservando el contenido exactamente (mismos `\label`, mismas fórmulas; verificado con conteo de `\label{` idéntico antes/después en cada uno de los 8 grupos). La división por sí sola no altera ningún número de sección ni página (confirmado comparando el `.toc` completo contra una línea base tomada antes de empezar: 0 diferencias tras cada división aislada).
- **Los 3 cuadernos de problemas nuevos de hoy se reubicaron** para quedar inmediatamente después de su propio archivo de sección:
  - `relacion_ic_pruebas_hipotesis(p).tex`: de continuación de 7.3 → **7.2.1-7.2.6** (limpio, sección dedicada).
  - `cuadrados_latinos_grecolatinos(p).tex`: de continuación de 8.6 → **8.5.1-8.5.6** (limpio, sección dedicada).
  - `diseno_factorial(p).tex`: permanece en 8.6, pero ahora **en solitario** (8.6.1-8.6.6) sin el cuaderno de cuadrados latinos apilado encima — resuelto el síntoma de los dos encabezados "Problemas" duplicados.
  - Se eliminaron los comentarios de limitación de numeración añadidos hoy en los 2 primeros archivos, ya que la limitación que documentaban dejó de existir.
  - Los 8 cuadernos de problemas **preexistentes** de estos grupos (`distribuciones_especiales(p)`, `variables_aleatorias_continuas_avanzado(p)`, `distribuciones_muestreo_avanzado(p)`, `estimacion_intervalos_avanzado(p)`, `pruebas_de_hipotesis(p)`, `chi_cuadrada(p)`, `pruebas_hipotesis_avanzadas(p)`, `diseno_experimentos_anova(p)`) **no se movieron ni se migraron**: mantienen su posición relativa (después del último archivo nuevo de su grupo) y, por tanto, su número de sección compilado exactamente igual que antes de esta división. Migrar su contenido a la convención de 1-archivo-por-sección queda para la tarea grande ya diferida.
- **Defecto de comillas rectas corregido**: se encontró que los 5 cuadernos de problemas escritos hoy usaban comillas rectas (`"..."`) en vez de comillas tipográficas LaTeX (`` `` ... '' ``), lo cual bajo el paquete `babel` en español se interpreta como un atajo de shorthand y produce texto corrupto en el PDF compilado (ej. `"continuidad"` renderizaba como `çontinuidad.es`). Corregido en los 5 archivos (32 pares de comillas reemplazados), verificado visualmente en las páginas afectadas tras recompilar.

### Verificación
- Libro maestro ES recompilado dos veces después de cada una de las 8 divisiones: **0 errores, 0 referencias indefinidas** en cada paso.
- `grep "multiply defined"` solo reporta la colisión preexistente `exmp:5.1.1` (fuera de alcance) — 0 colisiones nuevas introducidas por la división.
- Conteo de `\label{` idéntico entre cada archivo original y la suma de sus archivos divididos, confirmando cero pérdida de contenido en los 8 grupos.
- `.toc` comparado contra línea base antes/después de cada división: idéntico salvo en los 3 puntos de reubicación intencional (7.2, 8.5, 8.6), donde el cambio de página es el esperado por el contenido reinsertado.
- Verificación visual (renderizado a imagen con `pdftoppm`) de las páginas 533-540 (frontera 8.5/8.6): confirmado un solo encabezado "Problemas" por sección, numeración `Problema 8.5.x`/`8.6.x` correcta, y comillas tipográficas correctamente renderizadas.
- No se tocó ningún cuaderno de problemas preexistente (aparte de eliminar los 2 comentarios de limitación ya obsoletos). No se hizo `git commit`.

## 2026-07-20 (continuación 2 — diagnóstico de cuadernos de problemas, corrección de colisión y cierre de 5 huecos de cobertura)

### Añadido
- **Diagnóstico completo de los 19 archivos `latex/*(p).tex` de los capítulos 2-8** (`docs/diagnostico-cuadernos-problemas-2026-07-20.md`), solicitado antes de decidir cómo continuar tras la renumeración de teoría. Extraído directamente del `.aux` compilado: **255 de 315 etiquetas `\label{prob:X.Y.Z}` con nombre numérico (81 %) compilan con un número de sección distinto al que su nombre sugiere**; **5 secciones sin ningún problema** (2.2 Técnicas de conteo, 7.2 Relación IC↔pruebas, 7.4 Prueba $t$ con varianza desconocida, y dentro de 8.5 los subtemas de cuadrados latinos/grecolatinos, más 8.6 Diseños factoriales); y una **colisión activa de etiquetas** (ver abajo). El documento incluye tabla maestra por archivo, mapa de cobertura por sección, aclaración sobre los rótulos "Sección XX.YY" (pertenecen a la numeración de los mazos de `presentaciones/`, no al temario), contraste convención vieja/nueva, y 4 rutas de ejecución posibles.
- **5 cuadernos de problemas nuevos**, uno por cada sección sin cobertura, cerrando exactamente los huecos identificados en el diagnóstico:
  1. `tecnicas_de_conteo(p).tex` (2.2) — aterriza limpio en 2.2.1-2.2.6.
  2. `relacion_ic_pruebas_hipotesis(p).tex` (temáticamente 7.2) — aterriza como continuación de 7.3, no de 7.2, porque `pruebas_de_hipotesis.tex` agrupa sus 3 secciones (7.1-7.3) en un único archivo sin separación física de `\input`; documentado con un comentario al inicio del archivo. Dividir esa teoría queda fuera de alcance de esta tarea.
  3. `prueba_media_varianza_desconocida(p).tex` (7.4) — aterriza limpio en 7.4.1-7.4.6. Se añadió `\label{sec:relacion-ic-pruebas}` a la sección 7.2 en `pruebas_de_hipotesis.tex` (no existía) para permitir referencias `\ref{}` futuras.
  4. `cuadrados_latinos_grecolatinos(p).tex` (temáticamente 8.5) — aterriza como continuación de 8.6, no de 8.5, por la misma razón estructural que el caso 7.2: `diseno_experimentos_anova.tex` agrupa 8.1-8.6 en un único archivo. Documentado igual con comentario al inicio.
  5. `diseno_factorial(p).tex` (8.6) — aterriza en la misma sección 8.6 (continuación numérica del archivo anterior, 8.6.7-8.6.12); en este caso el aterrizaje es temáticamente correcto, ya que sí trata de diseños factoriales.
- **Refinamiento de la convención de cuadernos de problemas decidida el 2026-07-18** (Regla de Oro 4 de `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md`, actualizada), aplicado a los 5 archivos nuevos y documentado hacia adelante:
  - **Categorización por los 6 niveles de la Taxonomía de Bloom** (Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear) en vez de por dificultad (Fundamental/Operativo/Analítico/Desafiante). Cada uno de los 5 archivos nuevos tiene exactamente 6 problemas, uno por nivel, con el nivel documentado como comentario LaTeX invisible (`% Recordar`, etc.).
  - **Etiquetas `\label` con tag hasheado corto** (`prob:<7 hex>`, derivado de `sha1sum` sobre una semilla determinista `"<archivo>-p-<índice>"`, verificado contra el `.aux` para evitar colisiones) en vez de nombres numéricos o semánticos. Motivo explícito del usuario: mantener nombres significativos "ha sido un dolor de cabeza" y los nombres numéricos son la causa directa del desfase de Fase D.
  - Los 19 archivos `(p).tex` existentes **no se migran** a esta convención en esta tarea — queda pendiente en la reorganización completa, diferida.

### Corregido
- **Colisión activa de etiquetas `prob:3.9.1`-`prob:3.9.5`**, duplicadas entre `distribuciones_especiales(p).tex` y `chi_cuadrada(p).tex` (y su espejo `en_chi_cuadrada(p).tex`). Como `chi_cuadrada` se procesa después en el `\input`, sus valores ganaban la resolución de `\ref`, causando que las Soluciones de `distribuciones_especiales(p).tex` (que citan `\ref{prob:3.9.1}`...`\ref{prob:3.9.5}` internamente) imprimieran el número de un problema de `chi_cuadrada` completamente distinto (bondad de ajuste/independencia) en vez del propio. Corregido renombrando las 5 etiquetas de `chi_cuadrada(p).tex`/`en_chi_cuadrada(p).tex` a tags hasheados (`prob:3f1ec07`, `prob:d4859df`, `prob:da2eb15`, `prob:d6f0154`, `prob:f622374`), sin tocar `distribuciones_especiales(p).tex`, que ahora vuelve a resolver sus propias citas correctamente (verificado contra el `.aux`: `prob:3.9.1`→`3.7.51`, ..., `prob:3.9.5`→`3.7.55`, cada una única).

### Verificación
- Libro maestro ES recompilado dos veces después de cada uno de los 6 cambios (colisión + 5 archivos nuevos): **0 errores, 0 referencias indefinidas** en cada paso.
- `grep "multiply defined"` solo reporta la colisión preexistente y no relacionada `exmp:5.1.1` (fuera de alcance) — 0 colisiones nuevas.
- Los 30 tags hasheados nuevos (5 de la corrección + 25 de los 5 archivos, 6 c/u) verificados individualmente contra el `.aux` antes de usarse: 0 colisiones.
- No se tocó ningún `(p).tex` existente más allá de los 2 renombrados (`chi_cuadrada(p).tex`, `en_chi_cuadrada(p).tex`). No se tocó `presentaciones/*.tex`. No se hizo `git commit`.

## 2026-07-20 (continuación — redacción del contenido nuevo diferido)

### Añadido
- **Redacción de los 5 bloques de contenido matemático nuevo que quedaron como stub `% TODO(contenido-nuevo)` tras la ejecución de la renumeración del temario** (ver entrada anterior de esta misma fecha). Cada bloque sigue el estilo ya establecido del libro (`definición → teorema/propiedad → ejemplo resuelto`), sin código Python nuevo:
  1. **1.2 Técnicas de conteo** (`tecnicas_de_conteo.tex`, nuevo contenido): principio de multiplicación, permutaciones ($P(n,r)$), combinaciones y coeficiente binomial (reutilizando `\comb{n}{r}` ya definido en `_pe_comandos.tex`), cerrando con un ejemplo de probabilidad clásica (probabilidad de una flor en póker) que combina ambos conceptos.
  2. **6.2 Relación entre intervalos de confianza y pruebas de hipótesis** (`pruebas_de_hipotesis.tex`): se añadió el teorema de equivalencia IC↔prueba de dos colas ($\text{Rechazar } H_0 \iff \theta_0 \notin \text{IC}_{(1-\alpha)100\%}$) a continuación de la regla de decisión por valor p ya existente.
  3. **6.4 Pruebas relacionadas con una media, varianza desconocida** (`prueba_media_varianza_desconocida.tex`): prueba $t$ para una media reutilizando la distribución $t$ ya desarrollada en el capítulo de distribuciones de muestreo, con ejemplo resuelto completo (patrón "Paso 1 a Paso 5" ya usado en 6.1/6.3).
  4. **7.5 (ampliación) Cuadrados latinos y cuadrados grecolatinos** (`diseno_experimentos_anova.tex`): definiciones formales, modelo aditivo y tabla ANOVA para ambos diseños, usando como plantilla la tabla ANOVA de DBCA ya presente en el mismo archivo; se documentó la condición de no-existencia para $n=6$ en cuadrados grecolatinos.
  5. **7.6 Introducción a diseños factoriales** (`diseno_experimentos_anova.tex`, sección nueva al final del archivo): diseño factorial completo, efectos principales e interacción, modelo con interacción, tabla ANOVA de dos factores, y un ejemplo ilustrativo con datos de tiempos de entrenamiento de un modelo de ML bajo dos algoritmos y dos tamaños de lote (sin código Python).
  - **Referencias cruzadas añadidas para evitar números hardcodeados**: se agregó `\label{sec:distribucion-t}` a la sección de la distribución $t$ (`distribuciones_muestreo_avanzado.tex`) y `\label{sec:prueba-t-media}` a la nueva sección 6.4, y ambas se citan mutuamente vía `\ref{}`. De paso se corrigió una referencia de prosa preexistente y ya desactualizada en `distribuciones_muestreo_avanzado.tex` ("la prueba-$t$ (sección 3.6)") para que apunte a `\ref{sec:prueba-t-media}` en vez de a un número fijo — el número "3.6" ya no correspondía a ninguna sección real tras la renumeración de la entrada anterior.
  - **Verificado**: libro completo recompilado dos veces sin errores, 0 referencias indefinidas, 0 etiquetas `\label` duplicadas nuevas (las únicas colisiones "multiply defined" en el log son las preexistentes `exmp:5.1.1` y `prob:3.9.x`), 0 comentarios `% TODO(contenido-nuevo)` restantes en todo `latex/`, y el conteo de secciones numeradas por capítulo (2→4, 3→7, 4→6, 5→7, 6→8, 7→12, 8→7, incluyendo las secciones `Problemas resueltos` preexistentes) permanece idéntico al de la entrada anterior — la redacción no alteró la estructura, solo llenó los stubs. Además se inspeccionaron visualmente (renderizado a imagen con `pdftoppm`) todas las páginas con contenido nuevo (69-71, 453, 462-464, 521-525): todas compilan sin desbordes ni solapamientos.
  - **Hallazgo colateral, no corregido (fuera de alcance)**: al intentar homogeneizar el estilo de las nuevas tablas ANOVA de 7.5/7.6 con el de las tablas preexistentes (`\begin{table}[h!]...\caption{...}\label{...}`, como `tab:anova_dbca`), se detectó que ese patrón produce una superposición visual entre el `\caption` y la fila de encabezado de la tabla cuando el float cae al inicio de una página nueva — defecto que también afecta a las tablas preexistentes `tab:anova_un_factor` (p. 516) y `tab:anova_dbca` (p. 521), por lo que es un problema estructural de la clase `tufte-book`/mecanismo de captions del libro, no algo introducido en esta sesión. Se revirtió el cambio de estilo en las 2 tablas nuevas de cuadrado latino/factorial, dejándolas como `\begin{center}...\end{center}` sin `\caption`/`\label` (como ya estaban), que sí renderizan limpio. Pendiente de una revisión aparte del mecanismo de `\caption` en tablas anchas si se desea que las 4 tablas ANOVA del libro (2 preexistentes + 2 nuevas) tengan numeración y captions consistentes.

## 2026-07-20

### Corregido
- **Ejecución de la renumeración del temario MA1001B (Caps. 2-8 del libro maestro en español) — plan de `docs/plan-renumeracion-temario-MA1001B.md` ejecutado.** El plan, documentado el 2026-07-18 como "planeado, sin ejecutar", fue auditado contra el estado real de los 20 archivos afectados y contra el orden real de `\input` del maestro antes de ejecutarse; la auditoría encontró y resolvió tres problemas que el plan original no contemplaba:
  1. **El Capítulo 7 (Docimasia) era numéricamente imposible tal como estaba planeado**: el plan asignaba a `chi_cuadrada.tex` los números 6.8-6.9 y a `pruebas_hipotesis_avanzadas.tex` los números 6.5-6.7 *y* 6.10-6.11, pero `chi_cuadrada.tex` estaba `\input`ado *antes* que `pruebas_hipotesis_avanzadas.tex` en el maestro, y LaTeX numera por orden físico de aparición. Se resolvió partiendo `pruebas_hipotesis_avanzadas.tex` en dos archivos (`pruebas_hipotesis_avanzadas.tex` con 6.5-6.7, y el nuevo `pruebas_homogeneidad_varias_proporciones.tex` con 6.10-6.11) intercalados alrededor de `chi_cuadrada.tex` (dividido internamente en 6.8 "Pruebas de bondad de ajuste" y 6.9 "Pruebas de independencia", con `\label{sec:3.9}` repuntado y una nueva `\label{sec:independencia}` para las 3 referencias externas afectadas).
  2. **Conflicto entre el plan y la Fase E (2026-07-18)**: el plan pedía fusionar "Distribución Exponencial" de vuelta como subsección de "3.5 Distribuciones de tipo gamma", revirtiendo la promoción a `\section` independiente que la Fase E había hecho para alinear el libro con el orden de los mazos de `presentaciones/` (Uniforme→Exponencial→Normal). Por decisión explícita del usuario se siguió el plan al pie de la letra (fusión en 3.5); el libro ES vuelve a divergir del orden de los mazos 04.04-04.06 — pendiente de reconciliación futura si se retoma el trabajo de `presentaciones/`.
  3. **Auditoría de `\label`/`\ref` ampliada**: se confirmó mediante un inventario completo de `latex/*.tex` que las únicas referencias cruzadas entre archivos afectadas por el plan eran las 3 ya identificadas hacia `sec:3.9`; no se encontraron más labels en riesgo.
  - **Alcance de la ejecución**: solo reestructuración (retitular, fusionar, dividir, promover/degradar `\section`/`\subsection`, mover contenido dentro y entre archivos). Los 5 bloques de contenido matemático nuevo que pedía el plan original (1.2 Técnicas de conteo, 6.2 puente IC↔pruebas de hipótesis, 6.4 prueba t con varianza desconocida, 7.5 cuadrados latinos/grecolatinos, 7.6 diseños factoriales) se dejaron como `\section`/`\subsection` con título y número correctos más un comentario `% TODO(contenido-nuevo)`, sin redactar el contenido — pendientes para una tarea de redacción separada.
  - **Resultado verificado**: capítulos 2-8 del libro maestro ES recompilados dos veces sin errores y sin referencias indefinidas; cada capítulo muestra exactamente el número de secciones numeradas de su unidad correspondiente del temario (Cap. 2→4, Cap. 3→7, Cap. 4→6, Cap. 5→7, Cap. 6→7, Cap. 7→11, Cap. 8→6), más las secciones `\section*` esperadas y las secciones `Problemas resueltos` preexistentes (fuera de alcance, sin tocar). Archivos nuevos: `tecnicas_de_conteo.tex`, `prueba_media_varianza_desconocida.tex`, `pruebas_homogeneidad_varias_proporciones.tex`.
  - **Fuera de alcance, sin tocar**: `latex/en_*.tex` (mirror en inglés, queda desalineado de la nueva estructura ES hasta que se ejecute un plan equivalente), `presentaciones/`, los archivos `(p).tex` de problemas, y el label duplicado preexistente `exmp:5.1.1` (`conceptos_estadisticos.tex` / `distribuciones_muestreo_avanzado.tex`, no relacionado con este trabajo).
  - **Efecto colateral corregido durante la misma ejecución**: convertir un `\section` a `\section*` (introducciones sin numerar, guía de apoyo, comparaciones múltiples) deja sus `\subsection` hijas sin contexto de numeración propio, por lo que en la tabla de contenidos aparecían visualmente anidadas bajo la última `\section` numerada que las precedía físicamente (p. ej., los pasos de `guia_prueba_hipotesis.tex` aparecían colgando de "6.4 Pruebas relacionadas con una media", una sección nueva vacía). Se corrigió marcando también como `\subsection*` las subsecciones de los 6 bloques `\section*` afectados (`introduccion_probabilidad.tex`, `introduccion_estadistica_inferencial.tex`, `conceptos_estadisticos.tex`, `estadisticos_z_t.tex`, `guia_prueba_hipotesis.tex`, y el bloque "Comparaciones múltiples y pruebas post-hoc" de `diseno_experimentos_anova.tex`), sin alterar contenido. Verificado contra el `.toc` recompilado: las secciones numeradas por capítulo no cambiaron.

## 2026-07-18

### Decidido (pendiente de ejecución)
- **Reorganización de cuadernos de problemas y contenido de práctica en los mazos — decisión de alcance, no ejecutada aún.** Durante la Fase G (mapeo estricto 1 mazo = 1 `\section`), el usuario pidió replantear dos convenciones establecidas desde las Fases A/B y codificadas como estándar oficial en `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md` (Regla de Oro 1/Bloque IV y Regla de Oro 4):
  1. **Cuadernos de problemas por sección, no por capítulo:** cada `\section` real debe tener su propio archivo `(p).tex` individual (ya implícito en la redacción original de la Regla de Oro 4, pero nunca implementado así — hoy un archivo cubre varias secciones de un capítulo).
  2. **Cantidad de problemas flexible, no fija:** se abandona la taxonomía rígida de 10 problemas (3-3-2-2). Nueva guía: 3-6 problemas por sección, priorizando variedad sobre alcanzar un conteo, ordenados de menor a mayor dificultad.
  3. **Dificultad como comentario interno, no como encabezado visible:** los banners `\subsection*{Nivel Fundamental}` etc. se convierten en comentarios LaTeX (`% Nivel Fundamental`) que no aparecen en el PDF compilado.
  4. **Mazos: reemplazar "Ejercicio en Clase" (citar problema del cuaderno) por ejemplos resueltos ya existentes en la teoría** (`\ejemplo`/`\solucion` reutilizados, sin crear contenido nuevo), con el mismo nivel de detalle (par de diapositivas Enunciado→Resolución paso a paso).
  5. **Alcance retroactivo:** aplica a los capítulos ya reestructurados esta sesión (Cap. 3-5, vía Fases C/E/G1-G3) y hacia adelante (Cap. 6-9, Fase F).
  - Se actualizó `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md` (Regla de Oro 1/Bloque IV, Regla de Oro 4) para reflejar las nuevas reglas como estándar oficial vigente.
  - **Efecto colateral esperado, no verificado aún:** al ubicar cada archivo de problemas justo después de su sección real en el `\input`, el bug de numeración pospuesto en Fase D podría resolverse automáticamente (el contador `[section]` heredaría el número correcto sin necesitar `\subsection*` con asterisco) — pendiente de confirmar contra el `.aux` al ejecutar.
  - **Estado: solo documentado, sin ejecutar.** El usuario pidió ir despacio y confirmar el plan por escrito antes de tocar ningún archivo de problemas o mazo existente. La ejecución se retomará un paso a la vez, empezando por un piloto en una sola sección pequeña.

### Corregido
- **Divergencia estructural ES/EN del libro maestro — Fase C (Nivel 1) completa:** el usuario reportó que, pese a las Fases A/B, el desalineamiento entre las notas ES y EN seguía presente y que las tablas de contenido tampoco coincidían con los slides. Una nueva auditoría confirmó que las Fases A/B nunca compararon la estructura real de `\section`/`\subsection` (solo paridad de problemas y frames de teoría en slides), y encontró divergencias genuinas de tabla de contenidos:
  - `en_variables_aleatorias_discretas.tex` (Cap. 3) tenía solo 2 `\section`s (PMF+CDF fusionadas) donde ES tiene 3 (PMF, CDF, Esperanza/Varianza); se dividió para igualar la estructura ES.
  - `en_distribuciones_especiales.tex` (Cap. 3) colapsaba las 7 distribuciones de ES en 1 solo `\section` con 11 `\subsection`s; se dividió en 7 `\section`s (uno por distribución), preservando el contenido ya traducido.
  - `en_diseno_experimentos_anova.tex` (Cap. 8) carecía por completo de la sección "Verificación de supuestos en ANOVA" (homoscedasticidad/Bartlett-Levene, normalidad de residuos, independencia) — contenido de teoría totalmente ausente en el libro EN aunque el mazo `en/08.02_anova_assumptions.tex` (17 diapositivas) ya la necesitaba y existía. Se tradujo y agregó. Además, se detectó que el resto del archivo estaba igualmente colapsado (1 `\section` envolvente con 4 `\subsection`s); se promovieron a 4 `\section`es reales, quedando 5 en total, igual que ES.
  - `regresion_multiple.tex` (ES, Cap. 9): se corrigió un typo preexistente de un solo idioma — dos subsecciones tituladas "Modelo 3" (la segunda debía decir "Modelo 4"); el EN correspondiente ya estaba bien numerado.
  - Verificación: ambos libros maestros recompilados múltiples veces, 0 errores y 0 referencias indefinidas en cada paso; conteos de `\section` confirmados idénticos ES/EN en los Caps. 3 y 8 (antes 2 vs 3, y 1 vs 5 respectivamente).
  - **Hallazgo adicional descubierto durante esta fase, no reportado originalmente por el usuario:** los números de problema impresos en el PDF no coinciden con lo que citan los mazos de slides (ej. mazo cita "Problema 3.5.2", el PDF real imprime "3.10.11"), causado por el uso de `\subsection*` con asterisco (que no avanza el contador real de LaTeX) para organizar sub-temas dentro de varios archivos `(p).tex`. Confirmado contra el `.aux` compilado. Afecta 7 pares de archivos ES+EN en 5 capítulos (3, 4, 5, 6, 8); no afecta Caps. 1, 2, 7, 9.
  - Próximos pasos aprobados por el usuario (Fases E, F — ver plan): reordenar el libro para que coincida con el orden ya establecido en los mazos de slides (Caps. 3, 4, 6), y cerrar los huecos de cobertura donde el libro tiene contenido sin ningún mazo correspondiente (Caps. 4, 5, 6, 7, 8).

- **Fase D (Nivel 4, numeración de problemas) — investigada y POSPUESTA:** se prototipó el fix del hallazgo anterior en `variables_aleatorias_continuas(p).tex`/`en_...` (Cap. 4), insertando un `\section` real antes de cada bloque de problemas. Resultado: `\label{prob:4.1.1}` compiló como `4.2.1` (no `4.1.1`), confirmado contra el `.aux` — el número heredado depende de cuántas secciones reales de teoría preceden al archivo de problemas en el `\input`, no del número "intencionado" en la etiqueta. Se descubrió, además, que la opción de "reestructurar la teoría para que cada tema tenga su propia sección" es contraproducente: dividir la teoría en más secciones reales aleja aún más el número impreso del valor intencionado (aritmética simple del orden de `\input`, no una suposición). Tras corregir este análisis, se decidió posponer la Fase D por completo; se revirtió el cambio de prueba (confirmado limpio contra `git diff`) y se recompilaron ambos libros maestros: 0 errores, 0 referencias indefinidas. El hallazgo y las 3 opciones reales de solución (re-citar mazos al número real, forzar `\setcounter` por bloque, o aceptar el desfase) quedan documentados en el plan para retomarse en una tarea futura separada.

- **Fase E (Nivel 2, reordenar el libro al orden de los mazos) completa:** el libro maestro ordenaba los temas de forma distinta al orden ya establecido en los mazos de slides desde hace tiempo (Caps. 3, 4, 6). Antes de mover nada, se auditó (E1) todo `latex/` en busca de `\label`/`\ref` internos y citas de prosa hardcodeadas — ningún `\ref` se rompía en ninguno de los 3 casos, y los mazos nunca referencian el libro (son unidades de compilación independientes), pero se encontraron 2 complicaciones estructurales reales:
  - **Cap. 3** (`distribuciones_especiales.tex`/`en_...`): se reordenaron las 7 secciones a Binomial→Geométrica/BinNeg→Hipergeométrica→Poisson→Multinomial→Normal→CienciaDatos. Se detectó que la subsección "Problemas Resueltos" (con ejemplos de Normal y Poisson) estaba anidada dentro de Multinomial; movida junto con Multinomial habría creado una referencia hacia adelante a la sección Normal antes de que existiera en el documento reordenado. Se reubicó como última subsección de la nueva sección Normal.
  - **Cap. 4** (`variables_aleatorias_continuas_avanzado.tex`/`en_...`): Exponencial no era una sección independiente, sino un caso particular anidado dentro de "Distribuciones de tipo gamma" (definida como Gamma(1,β)), que además vive después de Normal. Por decisión explícita del usuario, se promovió Exponencial a `\subsection` propia con una definición autocontenida (sin presuponer Gamma), colocada entre Uniforme y Normal — coincidiendo con el orden de los mazos (04.04→04.05→04.06). La antigua subsubsección dentro de Gamma se reemplazó por una nota breve de conexión hacia atrás, sin duplicar la etiqueta `eq:2.8.8`.
  - **Cap. 6** (`estimacion_puntual.tex`/`en_...`): se intercambiaron Método de Momentos (MoM) y Máxima Verosimilitud (MLE) para que MoM quede primero. Se detectó y corrigió una cita de prosa ambigua dependiente de posición ("como se demostró en la sección anterior", sobre el sesgo $n$ vs. $n-1$ del estimador de varianza) que, tras el intercambio, habría apuntado incorrectamente a la sección de MoM; se reescribió para referenciar explícitamente el capítulo de distribuciones muestrales.
  - Verificación en los 3 casos: diff de líneas ordenadas contra la versión previa en git (sin pérdida de contenido, solo reordenamiento/reescrituras puntuales documentadas), conteo de `\label{}` idéntico antes/después, y recompilación de ambos libros maestros 3 veces cada uno: 0 errores, 0 referencias indefinidas.
  - Efecto secundario no solicitado: al reescribir por completo los 2 archivos de Cap. 4 para reordenarlos, se normalizó su estilo de acentos de escape LaTeX (`\'o`) a caracteres UTF-8 literales (`ó`), igual que el resto del libro — cambio cosmético/de codificación, sin alterar contenido.

## 2026-07-18 (continuación — Fase B)

### Corregido
- **Reconstrucción de los mazos Beamer EN estructuralmente divergentes de ES — Fase B completa:** continuación directa de la Fase A (alineación del libro maestro, ver entrada 2026-07-17). Una auditoría estructural de los 54 pares de mazos había clasificado 26 mazos EN como divergentes de su espejo ES: 5 con reconstrucción severa de la sección de ejercicios (Cap. 03, secciones 03.02-03.06) y 21 con frames de teoría condensados o completamente ausentes (cola del Cap. 03 y Caps. 04-06 completos). Se ejecutó en 6 sub-fases (B1-B6), verificando y recompilando cada mazo individualmente antes de continuar a la siguiente.
  - **B1 (03.02-03.06):** se reconstruyó la sección de ejercicios de los 5 mazos, reemplazando el patrón incorrecto (mezcla de problemas sin separar Enunciado/Resolución, o listados en bloque de 10 problemas) por el patrón estándar de 4 ejercicios "Classroom Exercise" citando los mismos números de problema que ES; en 03.02 además se eliminaron 2 frames de teoría que no existían en la fuente ES.
  - **B2 (03.07-03.10):** se restauraron frames de teoría completamente ausentes en EN: Función Generadora de Probabilidades y Función Generadora de Momentos (03.07), Marginal Binomial Reduction (03.08), Regla Empírica 68-95-99.7 (03.09), y Motivación + Binomial Negativa con interpretación jerárquica Poisson-Gamma (03.10). Se detectó y corrigió, fuera del alcance original, que `\bm{...}` nunca había sido definido en ningún preámbulo del proyecto (bug preexistente que rompía la compilación de 03.08 en ambos idiomas independientemente de esta tarea); se agregó `\usepackage{bm}` a `_preambulo_beamer.tex` y `_en_preambulo_beamer.tex`. También se corrigió una corrupción de codificación en el ES de 03.10 (caracteres chinos mezclados accidentalmente en el texto de motivación).
  - **B3 (04.01-04.07, Variables Aleatorias Continuas):** se restauró el frame de Motivación en los 7 mazos (ausente en todos) y, en los 5 primeros, un frame de teoría adicional por mazo con contenido que no aparecía en ningún otro frame de EN (propiedad fundamental y esperanza continua; propiedades axiomáticas de la CDF; linealidad de esperanza y varianza incluyendo $\Var(X+Y)=\Var(X)+\Var(Y)+2\cov(X,Y)$; ausencia de falta de memoria en la Uniforme, con corrección de una fórmula garabateada; demostración completa de la propiedad de falta de memoria de la Exponencial).
  - **B4 (05.01-05.05, Distribuciones Muestrales):** gap más leve de las tres fases — en los 5 mazos, todo frame de teoría de ES ya tenía equivalente 1:1 en EN; solo se restauró el frame de Motivación, ausente en los 5.
  - **B5 (06.01-06.05, Estimación Puntual):** mismo patrón que B4 — se restauró únicamente el frame de Motivación en 4 de los 5 mazos; 06.05 ya lo tenía y no requirió cambios (verificado por `git diff` vacío).
  - **B6 (verificación final):** recompilación doble de los 26 mazos tocados en B1-B5 más los 9 mazos ya tocados en fases previas del Cap. 03 (sin regresiones), y recompilación doble del libro maestro completo ES y EN. **Verificación agregada final:** ES y EN mantienen exactamente **483 problemas cada uno** (paridad confirmada, incluyendo la resolución de un falso positivo de conteo causado por 6 archivos preexistentes de Caps. 01-02 que usan el nombre de entorno `problem` en vez de `problema`, inconsistencia no relacionada con esta tarea); 0 errores y 0 referencias indefinidas en ambos libros maestros; 0 `Overfull \vbox`/`\hbox` de contenido en los 26 mazos reconstruidos (solo el Overfull de portada, exento por convención).
  - **Hallazgo pendiente de decisión del usuario, fuera de alcance de esta tarea:** `presentaciones/ROADMAP.md` contiene conteos de frames y afirmaciones de "0 Overfull"/"100% completado" para varios de estos mazos que no coinciden con el estado real de los archivos, de forma inconsistente y anterior a esta sesión (algunos ya coincidían, otros no) — no se modificó ese archivo porque el estado de completitud de los capítulos no cambió (solo su fidelidad), pero se documenta aquí para que el usuario decida si amerita una reconciliación separada.
  - `es/01_estadistica_descriptiva/01.01_introduccion.tex` carece de la línea `\documentclass{beamer}`, un defecto preexistente no relacionado detectado durante una recompilación de control en B2; no corregido por estar fuera de alcance.

## 2026-07-17

### Corregido
- **Alineación del libro maestro en inglés (`latex/[Statistical Modeling].tex`) con la fuente en español (`latex/[Modelación Estadística].tex`) — Fase A completa:** se detectó que el libro maestro EN no estaba fielmente alineado con la fuente ES, afectando la fidelidad de los slides en ambos idiomas. Una auditoría estructural de los 9 capítulos encontró: (1) 7 archivos de cuaderno de problemas "(p)" en inglés completamente inexistentes, con 270 problemas en español sin ningún equivalente EN, concentrados en los Capítulos 02-05; (2) `en_estimacion_puntual(p).tex` (Cap. 06) con solo 10 de 40 problemas (faltaban 3 lotes completos, Secciones 06.01-06.03); (3) `en_variables_aleatorias_discretas.tex` (Cap. 03) con una sección de teoría entera faltante ("Esperanza matemática y varianza en variables aleatorias discretas"); (4) una línea de preámbulo (`\input{_md_entornos}`) ausente en el master EN, investigada y confirmada como **falso positivo** (`_en_entornos.tex` ya fusiona esos entornos en inglés; agregar la línea habría causado conflicto de `\newtheorem` duplicado).
  - Se agregó la sección de teoría faltante a `en_variables_aleatorias_discretas.tex`.
  - Se crearon 7 archivos de cuaderno de problemas nuevos, traducidos fielmente del español preservando cifras, etiquetas `\label` y conteo exacto de problemas: `en_muestreo_aleatorio(p).tex` (10), `en_esperanza_matematica(p).tex` (10), `en_variables_aleatorias_discretas(p).tex` (30, 3 subsecciones), `en_variables_aleatorias_continuas(p).tex` (20), `en_variables_aleatorias_continuas_avanzado(p).tex` (40), `en_distribuciones_muestreo_avanzado(p).tex` (50), y `en_distribuciones_especiales(p).tex` (70, 7 subsecciones, el más grande, traducido en 7 partes paralelas por sección y ensamblado).
  - Se completó `en_estimacion_puntual(p).tex` agregando los 30 problemas faltantes (Secciones 06.01-06.03).
  - Cada archivo fue verificado independientemente (no solo por el proceso de traducción): conteo de `\begin{problema}`/`\begin{solucion}`/`\begin{sugerencia}` idéntico al original ES, diff vacío entre las listas ordenadas de `\label{prob:...}`, y verificación puntual de valores numéricos críticos (p. ej. la Paradoja de San Petersburgo, cifras financieras).
  - El libro maestro EN se recompiló dos veces después de cada adición individual (11 verificaciones incrementales), confirmando **0 errores y 0 referencias indefinidas** en cada paso.
  - **Verificación final agregada:** el libro maestro ES y el EN contienen ahora exactamente **483 problemas cada uno** (paridad total confirmada por conteo automatizado), y ambos recompilan limpiamente de punta a punta.
  - Próximo paso (Fase B, pendiente): reconstruir los mazos Beamer EN que resultaron estructuralmente divergentes de sus espejos ES durante esta misma auditoría (Capítulo 3, secciones 03.02-03.06 con patrón de ejercicios incorrecto; Capítulos 03 cola, 04, 05 y 06 con frames de teoría condensados/faltantes).

## 2026-07-16

### Corregido
- **Corrupción de codificación en `latex/diseno_experimentos_anova.tex`**: 33 instancias del macro `\textbf{` habían perdido el carácter `\` y quedado como un carácter tabulador literal seguido de `extbf{` (corrupción a nivel de bytes, probablemente de una sustitución automática defectuosa en una sesión anterior). No producía errores de compilación, pero renderizaba texto literal "extbf{...}" en el PDF en lugar de negritas. Corregido programáticamente; el libro maestro se recompiló dos veces confirmando **0 errores y 0 referencias indefinidas**.

### Añadido
- **Sección 08.01: Análisis de Varianza de un Factor (ANOVA 1-Way) y Prueba $F$ (Apertura del Capítulo 08)**:
  - Teoría (fundamentos del DoE, modelo lineal del ANOVA, partición de sumas de cuadrados, estadístico $F$, post-hoc LSD/Tukey/Bonferroni, DBCA) ya existía de forma completa y rigurosa en `latex/diseno_experimentos_anova.tex` y su espejo EN; no se requirió teoría nueva.
  - Se auditó `latex/diseno_experimentos_anova(p).tex` y se confirmó un cuaderno 3-3-2-2 completo (10 problemas, auto-numerados 8.6.1 a 8.6.10); se citaron los Problemas 8.6.3, 8.6.5, 8.6.8 y 8.6.9 sin duplicar contenido.
  - Script de laboratorio en Python `presentaciones/code/08_diseno_experimentos/08.01_one_way_anova.py` (descomposición SCT=SCTR+SCE verificada contra `scipy.stats.f_oneway`, HSD de Tukey vía `scipy.stats.studentized_range`, y Diseño en Bloques Completos al Azar con cálculo de Eficiencia Relativa del bloqueo).
  - Mazos Beamer bilingües en `presentaciones/es/08_diseno_experimentos/08.01_one_way_anova.tex` (17 diapositivas) y `presentaciones/en/08_experimental_design/08.01_one_way_anova.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 08 (Elementos de Diseño de Experimentos --- ANOVA) inicia su desarrollo: 1 de 2 secciones completadas.
- **Sección 08.02: Supuestos del ANOVA, Prueba de Levene/Bartlett y Diagnóstico (Cierre del Capítulo 08)**:
  - Teoría de verificación de supuestos (homoscedasticidad vía Bartlett/Levene, normalidad de residuos vía Shapiro-Wilk, independencia, ANOVA de Welch y Kruskal-Wallis como alternativas) ya existía de forma completa en `latex/diseno_experimentos_anova.tex` y su espejo EN; no se requirió teoría nueva.
  - Se detectó que solo 1 de los 10 problemas existentes abordaba específicamente la verificación de supuestos; se agregaron 3 problemas nuevos (Problemas 8.6.11 a 8.6.13, ES y EN) sobre el estadístico de Bartlett, la Prueba de Levene como ANOVA sobre desviaciones absolutas, y la demostración formal de la equivalencia algebraica entre Levene y el ANOVA de un factor.
  - Script de laboratorio en Python `presentaciones/code/08_diseno_experimentos/08.02_anova_assumptions.py` (Bartlett y Levene verificados contra `scipy.stats.bartlett`/`scipy.stats.levene`, Shapiro-Wilk sobre residuos de un ANOVA, y comparación de ANOVA paramétrico vs. Kruskal-Wallis sobre datos asimétricos).
  - Mazos Beamer bilingües en `presentaciones/es/08_diseno_experimentos/08.02_anova_assumptions.tex` (17 diapositivas) y `presentaciones/en/08_experimental_design/08.02_anova_assumptions.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 08 (Elementos de Diseño de Experimentos --- ANOVA) queda 100% finalizado (2 de 2 secciones).
- **Sección 09.01: Regresión Lineal Simple (MCO) y Coeficiente $R^2$ (Apertura del Capítulo 09)**:
  - Teoría (motivación vía correlación, modelo lineal poblacional, derivación de las ecuaciones normales de Gauss, descomposición SCT=SCR+SCE, propiedades de $R^2$ incluyendo $R^2=r^2$ y el $R^2$ ajustado, prueba de significancia $t$ para la pendiente) ya existía de forma completa en siete archivos (`latex/correlacion.tex`, `introduccion_regresiones_lineales.tex`, `regresiones_lineales.tex`, `matematicas_regresiones.tex`, `simulacion_regresion.tex`, `valores_optimos.tex`, `implementacion_regresion.tex`) y sus espejos EN; no se requirió teoría nueva.
  - Se auditó `latex/regresiones_lineales(p).tex` y se confirmó un cuaderno 3-3-2-2 completo (10 problemas, auto-numerados 9.8.1 a 9.8.10); se citaron los Problemas 9.8.1, 9.8.5, 9.8.7 y 9.8.9 sin duplicar contenido.
  - Script de laboratorio en Python `presentaciones/code/09_regresiones/09.01_simple_linear_regression.py` (estimación MCO verificada contra `scipy.stats.linregress`, descomposición SCT=SCR+SCE con verificación de la identidad $R^2=r^2$ contra `np.corrcoef`, y prueba $t$ de significancia de la pendiente con intervalos de confianza/predicción del 95\%).
  - Mazos Beamer bilingües en `presentaciones/es/09_regresiones/09.01_simple_linear_regression.tex` (17 diapositivas) y `presentaciones/en/09_regressions/09.01_simple_linear_regression.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 09 (Regresiones Lineales y Múltiples) inicia su desarrollo: 1 de 4 secciones completadas.
- **Sección 09.02: Regresión Lineal Múltiple, Ecuación Normal y Regularización Ridge/Lasso**:
  - `latex/regresion_multiple.tex` y su espejo EN ya cubrían la introducción a la regresión múltiple, selección de variables y el diagnóstico VIF, pero carecían de la Ecuación Normal en notación matricial y de Ridge/Lasso --- ambos nombrados explícitamente en el título de la sección y ya citados por el cuaderno de problemas. Se agregaron dos subsecciones nuevas: la Ecuación Normal de Gauss ($\hat{\boldsymbol\beta}=(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}$) con la Matriz Sombrero, y la regularización Ridge/Lasso con sus funciones objetivo penalizadas.
  - Se auditó `latex/regresion_multiple(p).tex` y se confirmó un cuaderno 3-3-2-2 completo (10 problemas, auto-numerados 9.10.1 a 9.10.10); se citaron los Problemas 9.10.1, 9.10.4, 9.10.7 y 9.10.9 sin duplicar contenido.
  - Script de laboratorio en Python `presentaciones/code/09_regresiones/09.02_multiple_linear_regression.py` (solución matricial verificada contra `np.linalg.lstsq` con verificación de simetría/idempotencia de la Matriz Sombrero; Ridge con solución cerrada mostrando contracción de coeficientes; Lasso implementado desde cero por descenso de coordenadas, mostrando sparsity progresiva).
  - Mazos Beamer bilingües en `presentaciones/es/09_regresiones/09.02_multiple_linear_regression.tex` (17 diapositivas) y `presentaciones/en/09_regressions/09.02_multiple_linear_regression.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 09 (Regresiones Lineales y Múltiples): 2 de 4 secciones completadas.
- **Sección 09.03: Diagnóstico de Residuos, Multicolinealidad (VIF) y Supuestos Clásicos**:
  - Teoría (supuestos clásicos, análisis de residuos, gráficas Q-Q/escala, Durbin-Watson, Breusch-Pagan, transformaciones correctivas, Distancia de Cook) ya existía de forma completa en `latex/supuestos_regresion.tex` y su espejo EN; el diagnóstico de VIF ya vivía en `latex/regresion_multiple.tex` (Sección 09.02). No se requirió teoría nueva.
  - **No existía un cuaderno de problemas para esta sección.** Se creó desde cero `latex/supuestos_regresion(p).tex` y su espejo `latex/en_supuestos_regresion(p).tex` con 10 problemas nuevos 3-3-2-2 (auto-numerados 9.14.1 a 9.14.10), conectados al libro maestro ES y EN.
  - Script de laboratorio en Python `presentaciones/code/09_regresiones/09.03_regression_diagnostics.py` (Durbin-Watson y Breusch-Pagan implementados desde cero sin `statsmodels`; VIF verificado exactamente contra $\text{diag}(\mathbf{R}^{-1})$; Distancia de Cook detectando observaciones influyentes por alto apalancamiento y por residuo grande).
  - Mazos Beamer bilingües en `presentaciones/es/09_regresiones/09.03_regression_diagnostics.tex` (17 diapositivas) y `presentaciones/en/09_regressions/09.03_regression_diagnostics.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 09 (Regresiones Lineales y Múltiples): 3 de 4 secciones completadas.

### Corregido
- **Corrección estructural del Capítulo 09 (Regresiones Lineales y Múltiples):** las entradas anteriores de este changelog describían una Sección 09.01 que agrupaba **7 archivos de teoría distintos** (`correlacion`, `introduccion_regresiones_lineales`, `regresiones_lineales`, `matematicas_regresiones`, `simulacion_regresion`, `valores_optimos`, `implementacion_regresion`) en un solo mazo Beamer de 17 diapositivas, violando la regla estructural del proyecto de que cada archivo/sección de las notas debe tener su propio mazo 1:1 (ya establecida y verificada empíricamente en los Capítulos 01-08). Se corrigió dividiendo esa sección en 6 mazos independientes (09.01-09.06) y renumerando las 2 secciones que ya eran 1:1 correctas: la antigua **09.02 (Regresión Múltiple) → 09.07**, y la antigua **09.03 (Diagnóstico de Regresión) → 09.09**, actualizando en ambas sus referencias cruzadas internas, la diapositiva "Hoja de Ruta" y el cierre "Perspectiva Modular" para la numeración final de 12 secciones. Los archivos huérfanos `introduccion_regresiones_lineales.tex` (superado por `regresiones_lineales.tex`) y `resumen_modelo.tex` (28 líneas de puro resumen ya cubierto por 09.07/09.09) no reciben mazo propio, siguiendo el mismo patrón de huérfanos ya documentado en el Capítulo 05.

### Añadido
- **Secciones 09.01-09.06, 09.08 y 09.10-09.12 del Capítulo 09 (Regresiones Lineales y Múltiples), completando la estructura correcta de 12 secciones:**
  - **09.01 Correlación como Premisa de la Regresión** (apertura del capítulo) y **09.02 Introducción a la Regresión Lineal**: mazos conceptuales/motivacionales respaldados por `latex/correlacion.tex` y `latex/regresiones_lineales.tex` respectivamente; sin ejercicios numéricos propios, citan hacia adelante a las secciones donde comienza la práctica. Scripts `09.01_correlation.py` y `09.02_introduction_to_regression.py`.
  - **09.03 Matemáticas de la Regresión**: respaldada por `latex/matematicas_regresiones.tex`; cita los Problemas 9.8.7, 9.8.9 y 9.8.10 de `latex/regresiones_lineales(p).tex` (partición $R^2=r^2$ y deducción de ecuaciones normales/insesgo). Script `09.03_mathematics_of_regression.py`.
  - **09.04 Regresión sobre Datos Simulados** y **09.06 Implementación con `statsmodels`**: mazos íntegramente demostrativos respaldados por `latex/simulacion_regresion.tex` e `latex/implementacion_regresion.tex`; el laboratorio Python de cada uno (comparación recta ajustada vs. recta poblacional verdadera; comparación motor manual vs. `model.summary()`) constituye el ejercicio resuelto completo. Scripts `09.04_regression_on_simulated_data.py` y `09.06_statsmodels_style_summary.py`.
  - **09.05 Coeficientes Óptimos, Pruebas $t$/$F$ y RSE**: respaldada por `latex/valores_optimos.tex`; cita los Problemas 9.8.4 y 9.8.6 de `latex/regresiones_lineales(p).tex`. Script `09.05_optimal_coefficients_and_tests.py`.
  - **09.08 Validación de Modelos y $k$-fold Cross-Validation**: respaldada por `latex/validacion_modelo.tex` (ya completa); mazo demostrativo (detección de sobreajuste, $k$-fold desde cero) que aprovecha `latex/validacion_modelo(p).tex`, ya conectado al libro maestro, sin necesidad de crear un cuaderno nuevo. Script `09.08_model_validation.py`.
  - **09.10 Regresión con `scikit-learn`**: respaldada por `latex/regresion_scikit.tex`; cuaderno nuevo `latex/regresion_scikit(p).tex` (10 problemas 3-3-2-2, 9.17.1-9.17.10). Script `09.10_scikit_learn_regression.py` --- **única excepción documentada en todo el proyecto a la regla numpy/scipy**: usa `sklearn` real (`LinearRegression`, `train_test_split`, `RFE`) porque el tema de la sección es la propia librería.
  - **09.11 Variables Categóricas y Variables Muda** y **09.12 Transformaciones No Lineales y Regresión Polinomial** (cierre del capítulo): ambas dividen conceptualmente `latex/otros_problemas.tex`; cuadernos nuevos `latex/otros_problemas_categoricas(p).tex` (9.19.1-9.19.10) y `latex/otros_problemas_transformaciones(p).tex` (9.20.1-9.20.10). Scripts `09.11_categorical_dummy_variables.py` y `09.12_nonlinear_polynomial_regression.py` (regresión polinomial vía expansión $Z=X^2$, Prueba $F$ Parcial, multicolinealidad polinomial).
  - Los 9 mazos nuevos y los 2 renumerados (09.07, 09.09) fueron compilados dos veces cada uno en ES y EN (24 compilaciones dobles), confirmando **0 errores, 0 referencias indefinidas y 0 `Overfull \vbox`/`\hbox`** en contenido (portada exenta). Se verificó además que el bloque de 12 ítems de la diapositiva "Hoja de Ruta" es idéntico en los 12 mazos por idioma, y que cada cierre "Perspectiva Modular"/"Modular Perspective" apunta correctamente a la sección siguiente real.
  - El libro maestro (`[Modelación Estadística].tex` y `[Statistical Modeling].tex`) fue recompilado dos veces al cierre del capítulo, confirmando **0 errores y 0 referencias indefinidas**.
  - Capítulo 09 (Regresiones Lineales y Múltiples) queda **100% finalizado (12 de 12 secciones)**.

## 2026-07-15

### Añadido
- **Sección 04.07: Distribuciones Gamma, Beta y Weibull (Cierre del Capítulo 04)**:
  - Teoría nueva de las distribuciones Beta y Weibull agregada a `latex/variables_aleatorias_continuas_avanzado.tex` y su espejo `latex/en_variables_aleatorias_continuas_avanzado.tex` (la teoría Gamma ya existía; se auditó y se dejó sin cambios de fondo).
  - 10 problemas bajo la taxonomía 3-3-2-2 (Problemas 4.7.1 a 4.7.10) en `latex/variables_aleatorias_continuas_avanzado(p).tex`.
  - Script de laboratorio en Python `presentaciones/code/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.py` (propiedad aditiva de Erlang, casos particulares Exponencial/Chi-cuadrada, momentos y simetría de la Beta, actualización bayesiana conjugada, y análisis de confiabilidad Weibull).
  - Mazos Beamer bilingües en `presentaciones/es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.tex` (23 diapositivas) y `presentaciones/en/04_continuous_random_variables/04.07_gamma_beta_weibull.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 04 (Variables Aleatorias Continuas) queda 100% finalizado (7 de 7 secciones).
- **Corrección de bugs preexistentes de compilación en el libro maestro** (no relacionados con la 04.07, detectados al recompilar el libro completo):
  - Definidos los comandos `\E` y `\Prob` (faltantes) en `latex/_pe_comandos.tex`, eliminando cientos de errores "Undefined control sequence" que afectaban prácticamente todos los capítulos que usan esperanza/probabilidad matemática.
  - Corregido un `\begin{align*}`/`\end{itemize}` mal balanceado en `latex/distribuciones_especiales(p).tex` (Problema 3.5.9).
  - Reemplazados caracteres Unicode sin soporte en pdflatex (ideogramas chinos accidentales y el símbolo ✓ literal) por `\checkmark` en `latex/distribuciones_especiales(p).tex` y `latex/variables_aleatorias_continuas(p).tex`.
  - El libro maestro (`[Modelación Estadística].tex`) compila ahora de punta a punta con **0 errores de LaTeX**.
- **Sección 05.01: Muestreo Aleatorio Simple, Media y Varianza Muestral Insesgada (Apertura del Capítulo 05)**:
  - Nueva subsección "Estadísticos y Varianza Muestral Insesgada" (definición formal de estadístico, corrección de Bessel y demostración de $E(S^2)=\sigma^2$) agregada a `latex/distribuciones_muestreo_avanzado.tex` y su espejo `latex/en_distribuciones_muestreo_avanzado.tex`.
  - Creado `latex/distribuciones_muestreo_avanzado(p).tex` (no existía) con 10 problemas 3-3-2-2 (Problemas 5.1.1 a 5.1.10), conectado al libro maestro.
  - Script de laboratorio en Python `presentaciones/code/05_distribuciones_muestreo/05.01_sample_statistics.py` (insesgadez de $S^2$ vía Monte Carlo, distribución muestral de la media, y corrección por población finita).
  - Mazos Beamer bilingües en `presentaciones/es/05_distribuciones_muestreo/05.01_sample_statistics.tex` (18 diapositivas) y `presentaciones/en/05_sampling_distributions/05.01_sample_statistics.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 05 (Distribuciones de Muestreo) inicia su desarrollo: 1 de 5 secciones completadas.
- **Sección 05.02: Teorema del Límite Central Asintótico**:
  - Nueva subsección "Teorema del Límite Central: Convergencia Asintótica" (convergencia en distribución, demostración vía FGM, teorema de Berry-Esseen) agregada a `latex/distribuciones_muestreo_avanzado.tex` y su espejo `latex/en_distribuciones_muestreo_avanzado.tex`.
  - 10 problemas bajo la taxonomía 3-3-2-2 (Problemas 5.2.1 a 5.2.10) en `latex/distribuciones_muestreo_avanzado(p).tex`.
  - Script de laboratorio en Python `presentaciones/code/05_distribuciones_muestreo/05.02_central_limit_theorem.py` (convergencia vía prueba KS desde una población Exponencial asimétrica, verificación empírica de la tasa de Berry-Esseen, TLC para sumas y proporciones).
  - Mazos Beamer bilingües en `presentaciones/es/05_distribuciones_muestreo/05.02_central_limit_theorem.tex` (17 diapositivas) y `presentaciones/en/05_sampling_distributions/05.02_central_limit_theorem.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 05 (Distribuciones de Muestreo): 2 de 5 secciones completadas.
- **Sección 05.03: Distribución Chi-Cuadrada y Varianza Muestral**:
  - Densidad formal, el Teorema de Fisher (independencia de $\bar X$ y $S^2$; $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$) con bosquejo de demostración, y un ejemplo resuelto, agregados a `latex/distribuciones_muestreo_avanzado.tex` y su espejo `latex/en_distribuciones_muestreo_avanzado.tex`.
  - 10 problemas bajo la taxonomía 3-3-2-2 (Problemas 5.3.1 a 5.3.10) en `latex/distribuciones_muestreo_avanzado(p).tex`, incluyendo la descomposición que anticipa la distribución $t$ de Student.
  - Script de laboratorio en Python `presentaciones/code/05_distribuciones_muestreo/05.03_chi_squared_distribution.py` (propiedades, reproductividad, Teorema de Fisher, y cobertura del intervalo de confianza para $\sigma^2$, todos verificados vía Monte Carlo/KS test).
  - Mazos Beamer bilingües en `presentaciones/es/05_distribuciones_muestreo/05.03_chi_squared_distribution.tex` (17 diapositivas) y `presentaciones/en/05_sampling_distributions/05.03_chi_squared_distribution.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 05 (Distribuciones de Muestreo): 3 de 5 secciones completadas.
- **Sección 05.04: Distribución $t$ de Student y Muestras Pequeñas**:
  - Teorema del intervalo de confianza para $\mu$ con $\sigma$ desconocida, observación sobre su relevancia en muestras pequeñas, y ejemplo resuelto comparando el intervalo $t$ contra el (incorrecto) intervalo $z$, agregados a `latex/distribuciones_muestreo_avanzado.tex` y su espejo `latex/en_distribuciones_muestreo_avanzado.tex`.
  - 10 problemas bajo la taxonomía 3-3-2-2 (Problemas 5.4.1 a 5.4.10) en `latex/distribuciones_muestreo_avanzado(p).tex`.
  - Script de laboratorio en Python `presentaciones/code/05_distribuciones_muestreo/05.04_student_t_distribution.py` (propiedades y convergencia de la $t$, comparación de intervalos $t$ vs. $z$, prueba $t$ de una muestra, cobertura empírica del IC).
  - Mazos Beamer bilingües en `presentaciones/es/05_distribuciones_muestreo/05.04_student_t_distribution.tex` (17 diapositivas) y `presentaciones/en/05_sampling_distributions/05.04_student_t_distribution.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 05 (Distribuciones de Muestreo): 4 de 5 secciones completadas.
- **Sección 05.05: Distribución $F$ de Fisher-Snedecor (Cierre del Capítulo 05)**:
  - Intervalo de confianza para $\sigma_1^2/\sigma_2^2$ y la identidad $T^2\sim F_{1,\nu}$ agregados a `latex/distribuciones_muestreo_avanzado.tex` y su espejo `latex/en_distribuciones_muestreo_avanzado.tex` (la teoría base de $F$, prueba de varianzas y ANOVA ya existía y era sólida).
  - 10 problemas bajo la taxonomía 3-3-2-2 (Problemas 5.5.1 a 5.5.10) en `latex/distribuciones_muestreo_avanzado(p).tex`, incluyendo un ANOVA completo con datos crudos.
  - Script de laboratorio en Python `presentaciones/code/05_distribuciones_muestreo/05.05_fisher_f_distribution.py` (propiedades, recíproco, identidad $T^2\sim F_{1,\nu}$, prueba $F$ con IC, y ANOVA verificado contra `scipy.stats.f_oneway`).
  - Mazos Beamer bilingües en `presentaciones/es/05_distribuciones_muestreo/05.05_fisher_f_distribution.tex` (17 diapositivas) y `presentaciones/en/05_sampling_distributions/05.05_fisher_f_distribution.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 05 (Distribuciones de Muestreo) queda 100% finalizado (5 de 5 secciones).
- **Sección 06.01: Estimación Puntual, Insesgadez, Eficiencia y Consistencia (Apertura del Capítulo 06)**:
  - Nueva subsección "Criterios de Calidad de un Estimador Puntual" (sesgo, ECM con descomposición sesgo-varianza, eficiencia relativa, Cota de Cramér-Rao, consistencia) agregada a `latex/estimacion_puntual.tex` y su espejo `latex/en_estimacion_puntual.tex`, que ya contenían un desarrollo extenso de MLE y Método de Momentos pero carecían de esta base teórica previa.
  - 10 problemas nuevos bajo la taxonomía 3-3-2-2 (Problemas 6.1.1 a 6.1.10) agregados a `latex/estimacion_puntual(p).tex`, que ya contenía 10 problemas avanzados preexistentes sobre MLE/MoM/Cramér-Rao/Rao-Blackwell (dejados intactos).
  - Script de laboratorio en Python `presentaciones/code/06_estimacion_estadistica/06.01_point_estimation_quality.py` (descomposición sesgo-varianza-ECM, eficiencia relativa, estimador de encogimiento óptimo, y consistencia vía Chebyshev).
  - Mazos Beamer bilingües en `presentaciones/es/06_estimacion_estadistica/06.01_point_estimation_quality.tex` (17 diapositivas) y `presentaciones/en/06_estimation_data_science/06.01_point_estimation_quality.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 06 (Estimación y su Relación con Ciencia de Datos) inicia su desarrollo: 1 de 5 secciones completadas.
- **Sección 06.02: Método de Momentos (MoM)**:
  - Segundo ejemplo ("caso delicado" $U(-\theta,\theta)$) y observación de propiedades/limitaciones agregados a `latex/estimacion_puntual.tex` y su espejo `latex/en_estimacion_puntual.tex`.
  - 10 problemas nuevos bajo la taxonomía 3-3-2-2 (Problemas 6.2.1 a 6.2.10) en `latex/estimacion_puntual(p).tex`.
  - Script de laboratorio en Python `presentaciones/code/06_estimacion_estadistica/06.02_method_of_moments.py` (MoM para la Gamma, el caso delicado, y comparación de eficiencia MoM vs. MLE).
  - Mazos Beamer bilingües en `presentaciones/es/06_estimacion_estadistica/06.02_method_of_moments.tex` (17 diapositivas) y `presentaciones/en/06_estimation_data_science/06.02_method_of_moments.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 06 (Estimación y su Relación con Ciencia de Datos): 2 de 5 secciones completadas.
- **Sección 06.03: Estimación por Máxima Verosimilitud (MLE) y Score**:
  - Nueva subsubsección "La Función de Score y Normalidad Asintótica" (definición del score, media cero con demostración, identidad de la información, Teorema de Normalidad Asintótica del MLE conectado con Cramér-Rao) agregada a `latex/estimacion_puntual.tex` y su espejo `latex/en_estimacion_puntual.tex`.
  - 10 problemas nuevos bajo la taxonomía 3-3-2-2 (Problemas 6.3.1 a 6.3.10) en `latex/estimacion_puntual(p).tex`, incluyendo el MLE de la distribución Rayleigh y el método delta.
  - Script de laboratorio en Python `presentaciones/code/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.py` (propiedades del score, normalidad asintótica vía Monte Carlo, MLE de Rayleigh y método delta).
  - Mazos Beamer bilingües en `presentaciones/es/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.tex` (17 diapositivas) y `presentaciones/en/06_estimation_data_science/06.03_maximum_likelihood_estimation.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 06 (Estimación y su Relación con Ciencia de Datos): 3 de 5 secciones completadas.
- **Sección 06.04: Intervalos de Confianza para Medias Poblacionales ($Z$ y $t$)**:
  - Nueva subsección "Construcción del Intervalo de Confianza para una Media Poblacional" (teoremas para $Z$ y $t$, estructura común, ejemplo resuelto) agregada a `latex/intervalos_de_confianza.tex` y su espejo `latex/en_intervalos_de_confianza.tex`.
  - Se auditó `latex/intervalos_de_confianza(p).tex` y se confirmó que ya contenía un cuaderno 3-3-2-2 completo y de alta calidad para este tema exacto; no se creó un cuaderno duplicado.
  - Script de laboratorio en Python `presentaciones/code/06_estimacion_estadistica/06.04_confidence_intervals_means.py` (IC $Z$ vs. $t$, IC de diferencia de medias con varianza agrupada, cobertura frecuentista vía Monte Carlo).
  - Mazos Beamer bilingües en `presentaciones/es/06_estimacion_estadistica/06.04_confidence_intervals_means.tex` (17 diapositivas) y `presentaciones/en/06_estimation_data_science/06.04_confidence_intervals_means.tex` (19 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 06 (Estimación y su Relación con Ciencia de Datos): 4 de 5 secciones completadas.
- **Sección 06.05: Intervalos de Confianza para Varianzas y Proporciones (Cierre del Capítulo 06)**:
  - Intervalo de Wilson (Score) explícito para una proporción, con explicación de su ventaja de cobertura sobre Wald, agregado a `latex/estimacion_intervalos_avanzado.tex` y su espejo `latex/en_estimacion_intervalos_avanzado.tex`.
  - Se auditó `latex/estimacion_intervalos_avanzado(p).tex` y se confirmó que ya contenía un cuaderno 3-3-2-2 completo y avanzado (incluyendo la transformación de Fisher para correlación y el método delta) para este tema; no se creó un cuaderno duplicado.
  - Script de laboratorio en Python `presentaciones/code/06_estimacion_estadistica/06.05_confidence_intervals_variances.py` (IC $\chi^2$ y $F$, IC de Fisher para correlación, y un estudio de cobertura Monte Carlo mostrando que Wald cubre solo $87.65\%$ vs. el $95.64\%$ de Wilson frente a un nominal del $95\%$).
  - Mazos Beamer bilingües en `presentaciones/es/06_estimacion_estadistica/06.05_confidence_intervals_variances.tex` (17 diapositivas) y `presentaciones/en/06_estimation_data_science/06.05_confidence_intervals_variances.tex` (20 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 06 (Estimación y su Relación con Ciencia de Datos) queda 100% finalizado (5 de 5 secciones).
- **Sección 07.01: Fundamentos de Pruebas de Hipótesis (Apertura del Capítulo 07)**:
  - Nueva subsección "Potencia y Tamaño de Muestra" (teorema del tamaño de muestra $n=((Z_\alpha+Z_\beta)\sigma/(\mu_a-\mu_0))^2$ y observación del *trade-off* $\alpha$-$\beta$-$n$) agregada a `latex/pruebas_de_hipotesis.tex` y su espejo `latex/en_pruebas_de_hipotesis.tex`.
  - Creado desde cero `latex/pruebas_de_hipotesis(p).tex` y su espejo `latex/en_pruebas_de_hipotesis(p).tex` (no existía cuaderno de problemas para esta sección) con 10 problemas 3-3-2-2 (Problemas 7.1.1 a 7.1.10), incluyendo el Lema de Neyman-Pearson y la deducción rigurosa de la fórmula de tamaño de muestra; conectado (`\input`) al libro maestro ES y EN.
  - Script de laboratorio en Python `presentaciones/code/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.py` (tasa de Error Tipo I verificada vía Monte Carlo, función de potencia, y verificación empírica del tamaño de muestra para una potencia objetivo).
  - Mazos Beamer bilingües en `presentaciones/es/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.tex` (17 diapositivas) y `presentaciones/en/07_hypothesis_testing/07.01_hypothesis_testing_basics.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 07 (Docimasia --- Pruebas de Hipótesis) inicia su desarrollo: 1 de 4 secciones completadas.
- **Sección 07.02: Pruebas $Z$ y $t$ para Medias de Una y Dos Muestras**:
  - Se auditó `latex/pruebas_hipotesis_avanzadas.tex` y se confirmó que ya contenía teoremas rigurosos completos para los cuatro casos de comparación de dos medias; no se requirió teoría nueva.
  - Se auditó `latex/pruebas_hipotesis_avanzadas(p).tex` y se confirmó que ya contenía un cuaderno 3-3-2-2 completo y avanzado; no se creó un cuaderno duplicado.
  - Script de laboratorio en Python `presentaciones/code/07_pruebas_hipotesis/07.02_z_t_tests_means.py` (prueba $t$ de una muestra, comparación varianza agrupada vs. Welch, y prueba $t$ pareada, todas verificadas contra `scipy.stats`).
  - Mazos Beamer bilingües en `presentaciones/es/07_pruebas_hipotesis/07.02_z_t_tests_means.tex` (17 diapositivas) y `presentaciones/en/07_hypothesis_testing/07.02_z_t_tests_means.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 07: 2 de 4 secciones completadas.
- **Sección 07.03: Pruebas de Bondad de Ajuste $\chi^2$**:
  - Nueva subsección "Prueba formal de bondad de ajuste" (teorema con $\nu=k-1-m$ y formalización de la Regla de Cochran) agregada a `latex/chi_cuadrada.tex` y su espejo `latex/en_chi_cuadrada.tex`.
  - Se auditó `latex/chi_cuadrada(p).tex` y se confirmó que ya contenía un cuaderno 3-3-2-2 completo (mezclando bondad de ajuste e independencia); se citaron los problemas de sabor "bondad de ajuste" sin duplicar contenido.
  - Script de laboratorio en Python `presentaciones/code/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.py` (bondad de ajuste uniforme y Poisson con parámetro estimado, y detección/corrección de la violación de la Regla de Cochran mediante fusión de celdas).
  - Mazos Beamer bilingües en `presentaciones/es/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.tex` (17 diapositivas) y `presentaciones/en/07_hypothesis_testing/07.03_goodness_of_fit_tests.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 07: 3 de 4 secciones completadas.
- **Sección 07.04: Tablas de Contingencia y Pruebas de Independencia (Cierre del Capítulo 07)**:
  - Teoría de independencia y homogeneidad ya existía de forma rigurosa en `latex/chi_cuadrada.tex` y `latex/pruebas_hipotesis_avanzadas.tex`; no se requirió teoría nueva.
  - Se reutilizaron los problemas de sabor "independencia/homogeneidad" ya existentes en `latex/chi_cuadrada(p).tex` y `latex/pruebas_hipotesis_avanzadas(p).tex`, citándolos sin duplicar contenido.
  - Script de laboratorio en Python `presentaciones/code/07_pruebas_hipotesis/07.04_contingency_tables.py` (prueba de independencia y de homogeneidad, y verificación numérica a precisión de máquina de la identidad exacta $Z^2=\chi^2$ en tablas $2\times2$).
  - Mazos Beamer bilingües en `presentaciones/es/07_pruebas_hipotesis/07.04_contingency_tables.tex` (17 diapositivas) y `presentaciones/en/07_hypothesis_testing/07.04_contingency_tables.tex` (17 diapositivas), certificados con **0 `Overfull \vbox`/`\hbox`** en contenido.
  - Capítulo 07 (Docimasia --- Pruebas de Hipótesis) queda 100% finalizado (4 de 4 secciones).

## 2026-07-14

### Añadido
- **Presentaciones Beamer del Capítulo 02 (Teoría de la Probabilidad --- 100% Finalizado)**:
  - Creadas las 12 presentaciones interactivas en LaTeX Beamer (6 en español en `presentaciones/es/02_teoria_probabilidad/` y 6 en inglés en `presentaciones/en/02_probability_theory/`) para las Secciones 02.01 a 02.06.
  - Estructuración estándar de 20 diapositivas por sección (portada `[plain]`, hoja de ruta, motivación, desarrollo teórico, 4 diapositivas de laboratorio en Python, 4 diapositivas de ejercicios por niveles y puente didáctico).
  - Optimización vertical estricta para garantizar **cero advertencias `Overfull \vbox` y `Overfull \hbox`** en todas las diapositivas de contenido (páginas 2 a 20).
- **Laboratorios de Simulación Computacional en Python (`numpy`/`scipy`)**:
  - Creados los 6 scripts de simulación y comprobación de probabilidad unificados **únicamente en inglés** dentro de `presentaciones/code/02_teoria_probabilidad/` (`02.01_intro_probability.py` a `02.06_random_sampling.py`).
  - Integración en vivo de los laboratorios en las diapositivas Beamer (ES y EN) mediante `\lstinputlisting`.
- **Cuadernos de Problemas (`(p).tex`) e Integración en Libro Maestro**:
  - Creados y afinados los ejercicios del Capítulo 02 bajo la taxonomía institucional de dificultad **3-3-2-2** (3 Fundamental, 3 Operativo, 2 Analítico, 2 Desafiante).
- **Documentación Reproducible del Flujo de Trabajo**:
  - Creado `presentaciones/README.md` como instructivo de 4 reglas de oro y checklist paso a paso para la compilación sin errores de presentaciones Beamer.
  - Creado `presentaciones/ROADMAP.md` con el desglose exacto de trabajo pendiente para la Unidad 2 / Capítulo 03 (Variables Aleatorias Discretas).

## 2026-07-13

### Cambiado
- Adscripción del autor en la portada (`\publisher`) actualizada de
  `www.optimum.mx` a Tecnológico de Monterrey, Escuela de Ingeniería y
  Ciencias, Campus Ciudad de México, con correo de contacto
  `julihocc@tec.mx`.
- Paleta de colores del libro (encabezados, entornos `solucion` y
  `algoritmo`) ajustada para acercarse a los colores institucionales del
  Tecnológico de Monterrey.

## 2026-07-12

### Cambiado
- Estandarización de la estructura de problemas en los 16 archivos `(p).tex`
  del libro a un esquema de dificultad por niveles ("3-3-2-2"): 3 problemas
  de Nivel Fundamental, 3 de Nivel Operativo, 2 de Nivel Analítico y 2 de
  Nivel Desafiante, en cada tema. Aplicado a:
  - Estadística descriptiva: `medidas_dispersion(p)`,
    `medidas_tendencia_central(p)`.
  - Teoría de probabilidad: `conjuntos(p)`, `fundamentos_de_probabilidad(p)`,
    `probabilidad_condicional(p)`, `teorema_de_bayes(p)`.
  - Estimación e intervalos: `estadisticos_z_t(p)`,
    `estimacion_intervalos_avanzado(p)`, `estimacion_puntual(p)`,
    `intervalos_de_confianza(p)`.
  - Chi-cuadrada, hipótesis y ANOVA: `chi_cuadrada(p)`,
    `diseno_experimentos_anova(p)`, `pruebas_hipotesis_avanzadas(p)`.
  - Regresión lineal, múltiple y validación de modelos:
    `regresion_multiple(p)`, `regresiones_lineales(p)`,
    `validacion_modelo(p)`.
- Actualización de artefactos de compilación con el PDF resultante de 444
  páginas.

## 2026-07-10

### Añadido
- Ejemplos de código en `code/` para los temas de chi-cuadrada, distribuciones
  continuas avanzadas, distribuciones especiales, distribuciones de muestreo,
  estadísticos `z`/`t` y regresión.
- Scripts auxiliares `fix_regresion2.py` y `limpieza_final.py` para limpieza y
  ajuste de contenido.

### Cambiado
- Integración de listados externos de Python dentro del ebook mediante
  `\lstinputlisting`.
- Corrección de referencias internas tras la renumeración del capítulo 3
  (`sec:3.8` → `sec:3.9`).
- Actualización de artefactos de compilación, incluyendo el PDF principal del
  libro.

## 2026-07-09

### Añadido
- `AGENTS.md` con instrucciones de compilación y convenciones editoriales del
  repositorio.
- `docs/MA1001B - Analítico.pdf` como referencia del programa/sílabo.
- Nuevo tema de distribuciones continuas avanzadas: uniforme, normal, gamma y
  familia FGM.
- Nueva sección de distribuciones de muestreo avanzadas.

### Cambiado
- Mejora integral de los capítulos 1 a 4:
  - Capítulo 1: estadística descriptiva.
  - Capítulo 2: probabilidad.
  - Capítulo 3: estadística inferencial.
  - Capítulo 4: regresiones lineales.
- Expansión del capítulo 2 con distribuciones geométrica, binomial negativa,
  hipergeométrica y aplicaciones a ciencia de datos.
- Migración de los capítulos 1 a 4 al sistema unificado de numeración
  `[cap.sec.item]`.
- Migración de archivos huérfanos (`pe-*.tex` y `probabilidad-basica.tex`) al
  mismo esquema de numeración.

### Mantenimiento
- Validación final de compilación limpia sin advertencias por etiquetas
  duplicadas.
- Ajustes en `.gitattributes` para retirar la configuración de Git LFS para
  archivos PDF, después de una configuración transitoria.
- Registro de sesión añadido al repositorio.

## 2021-10-24 a 2021-08-02

### Cambiado
- Corrección del teorema 2.2.6.
- Incorporación de la carpeta de soluciones.
- Ajuste de enlaces o referencia institucional a `optimum.mx`.

### Notas
- Este tramo contiene un commit con mensaje poco descriptivo (`No recuerdo que
  hice`), por lo que el cambio exacto no puede reconstruirse con confianza
  solo a partir del mensaje.

## 2021-07-18 a 2021-07-02

### Fundación del proyecto
- Creación inicial del repositorio y del `README.md`.
- Adopción de la licencia CC BY 4.0.
- Incorporación de la base LaTeX del libro y consolidación del contenido dentro
  de `latex/`.
- Renombrado y normalización temprana de nombres de archivo.
- Cambio editorial del título de la sección de conteo a notación de conjuntos.
- Inclusión del primer ejercicio publicado en YouTube.
- Primeros merges sobre `main` durante la etapa de arranque.

## Lectura general de la historia

La historia del repositorio muestra dos etapas claras:

1. **2021:** arranque del libro, definición de licencia, estructura LaTeX base
   y primeras decisiones editoriales.
2. **2026:** reactivación intensa del proyecto con expansión del contenido,
   unificación de numeración, mejora de capítulos, incorporación de ejemplos de
   código y actualización del PDF final.
