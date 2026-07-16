# Changelog

Este changelog resume la evolución del repositorio a partir del historial de Git.
Como el proyecto no usa versiones ni tags de lanzamiento, los cambios se agrupan
por fechas e hitos editoriales.

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
