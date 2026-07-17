# Changelog

Este changelog resume la evolución del repositorio a partir del historial de Git.
Como el proyecto no usa versiones ni tags de lanzamiento, los cambios se agrupan
por fechas e hitos editoriales.

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
