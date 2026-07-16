# ROADMAP: Ebook "Modelación Estadística" --- Presentaciones Beamer & Laboratorios Python

## 1. Visión y Objetivos del Subproyecto

Este subproyecto tiene como objetivo construir **presentaciones didácticas de alta calidad en formato Beamer (Español e Inglés)** y **laboratorios computacionales reproducibles en Python** para cada una de las secciones teóricas del libro de texto *Modelación Estadística* (cuyo archivo maestro es `latex/[Modelación Estadística].tex`).

### Las 4 Reglas de Oro para Todo Agente y Sesión de Trabajo

1. **Estricta Política de No-Commits Automáticos (`No-Auto-Commit Policy`):**
   Ningún agente de IA debe ejecutar comandos `git commit` o `git push` por su cuenta. Todos los archivos creados o modificados deben permanecer en el árbol de trabajo (*working tree*) para revisión y validación de estilo por parte del autor (`Juliho Castillo Colmenares`).
2. **Purity Tipográfica y Política Cero Desbordamientos (*Zero Overfull Policy*):**
   Cada presentación Beamer en español (`es/`) e inglés (`en/`) debe compilarse obligatoriamente **dos veces** con `pdflatex -interaction=nonstopmode`. Es un requisito de aceptación que el archivo de registro (`.log`) arroje **exactamente 0 `Overfull \vbox` y 0 `Overfull \hbox`** en todas las diapositivas de contenido (páginas 2 a $N$). La portada en la página 1 (`\begin{frame}[plain]`) está exenta del aviso `\vbox` de centrado vertical propio de `beamerthememetropolis`.
3. **Taxonomía Institucional del Libro ("3-3-2-2"):**
   Antes o en paralelo con el desarrollo del mazo Beamer, el cuaderno complementario del libro en `latex/<seccion>(p).tex` debe contar con **exactamente 10 problemas resueltos y fundamentados** en cuatro niveles:
   - `\subsubsection*{Nivel 1: Fundamental (Conceptos básicos y directos)}` $\to$ **3 problemas**.
   - `\subsubsection*{Nivel 2: Operativo (Cálculo e implementación técnica)}` $\to$ **3 problemas**.
   - `\subsubsection*{Nivel 3: Analítico (Demostraciones y modelación matemática)}` $\to$ **2 problemas**.
   - `\subsubsection*{Nivel 4: Desafiante (Problemas avanzados o retos de ingeniería)}` $\to$ **2 problemas**.
4. **Única Fuente de Verdad Computacional (*Single Source of Truth*):**
   Todo el código Python reside exclusivamente en `presentaciones/code/<unidad>/<ID>_<name_in_english>.py` usando solo bibliotecas base (`numpy`, `scipy`) e **inglés estricto en variables y comentarios**. Ambos mazos Beamer (ES y EN) importan exactamente estas líneas con `\lstinputlisting[language=Python, ...]` dentro de entornos `[fragile]`.

---

## 2. Estado Finalizado y Verificado al Cierre de Sesión

### Unidad 1 / Capítulo 02: Teoría de la Probabilidad (`100% COMPLETADA`)
- $\checkmark$ **02.01 Introducción a la Probabilidad:** Mazos ES/EN de 20 diapositivas (`0 overfulls` reportados en sesión previa), sin script computacional dedicado.
- $\checkmark$ **02.02 Conjuntos y Particiones:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.02_sets_partitions.py`.
- $\checkmark$ **02.03 Fundamentos y Axiomas:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.03_probability_axioms.py`.
- $\checkmark$ **02.04 Probabilidad Condicional:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.04_conditional_probability.py`.
- $\checkmark$ **02.05 Teorema de Bayes:** 100% completado (Remediación modular total bajo el Estándar de Oro).
  - *Cuaderno de Problemas:* 10 problemas en `latex/teorema_de_bayes(p).tex` organizados bajo la taxonomía 3-3-2-2 (Problemas 2.5.1 al 2.5.10).
  - *Laboratorio Python:* `presentaciones/code/02_teoria_probabilidad/02.05_bayes_theorem.py` (simulación de test médico diagnóstico y VPP empírico vs. teórico, evaluación exacta de clasificador Naive Bayes anti-spam, y actualización bayesiana secuencial a lo largo de observaciones iterativas).
  - *Mazos Beamer:* 22 diapositivas pedagógicas simétricas en `presentaciones/es/02_teoria_probabilidad/02.05_teorema_bayes.tex` y `en/02_probability_theory/02.05_bayes_theorem.tex` (revelado progresivo `\pause`, puente computacional Python en 4 diapositivas sin truncar, 4 problemas en clase desarrollados en Enunciado $\to$ Resolución para cada nivel de la taxonomía, cero marcado informal y compilación certificada con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **02.06 Muestreo Aleatorio y TLC:** 100% completado (Remediación modular total bajo el Estándar de Oro).
  - *Cuaderno de Problemas:* 10 problemas en `latex/muestreo_aleatorio(p).tex` organizados bajo la taxonomía 3-3-2-2.
  - *Laboratorio Python:* `presentaciones/code/02_teoria_probabilidad/02.06_random_sampling.py` (simulación MAS con vs sin reemplazo, verificación empírica de FPC, evolución del error en LGN con cota de Chebyshev, y estandarización CLT en población exponencial $N=50,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas simétricas en `presentaciones/es/02_teoria_probabilidad/02.06_muestreo_aleatorio.tex` y `en/02_probability_theory/02.06_random_sampling.tex` (revelado progresivo `\pause`, puente computacional Python de 4 diapositivas, 4 problemas en clase desarrollados en Enunciado $\to$ Resolución, cero marcado informal y compilación certificada con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).

### Unidad 2 / Capítulo 03: Variables Aleatorias Discretas (`Avance actual: 10 de 10 secciones completadas --- 100% FINALIZADO`)
- $\checkmark$ **03.01 PMF y Soporte:** 100% completado (Remediación modular total).
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_discretas(p).tex` (Problemas 3.1.1 al 3.1.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.01_pmf_and_support.py` (normalización polinomial, probabilidad condicional en soporte discreto, simulación Monte Carlo de suma de dados y transformación no lineal $|X-1|$ con sumas por preimágenes).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.01_pmf_y_soporte.tex` y `en/03_discrete_random_variables/03.01_pmf_and_support.tex` (revelado progresivo `\pause`, puente numérico Python en 4 diapositivas, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución para cada nivel de la taxonomía, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.02 CDF Discreta:** 100% completado (Remediación modular total).
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_discretas(p).tex` (Problemas 3.2.1 al 3.2.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.02_discrete_cdf.py` (construcción de CDF, operador de diferencia $\Delta F$ para recuperar PMF, probabilidades de intervalos y simulación empírica ECDF con $N=100,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.02_cdf_discreta.tex` (revelado progresivo `\pause`, puente numérico Python en 4 diapositivas, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución para cada nivel de la taxonomía, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.03 Esperanza Matemática, Varianza y Momentos:** 100% completado (Remediación modular total).
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_discretas(p).tex` (Problemas 3.3.1 al 3.3.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.03_expectation_and_variance.py` (cálculo de momentos exactos, LOTUS, estandarización Z y simulación Monte Carlo de LLN con $N=100,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.03_esperanza_y_varianza.tex` (revelado progresivo `\pause`, puente numérico Python en 4 diapositivas, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución para cada nivel de la taxonomía, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.04 Distribuciones de Bernoulli y Binomial:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.4.1 al 3.4.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.py` (validación vectorizada en numpy/scipy y simulación Monte Carlo $N=100,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.tex` (revelado progresivo `\pause`, puente numérico Python tras teoría, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.05 Distribuciones Geométrica y Binomial Negativa:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.5.1 al 3.5.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.py` (validación combinatoria con SciPy y Monte Carlo $N=250,000$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.tex` y `presentaciones/en/03_discrete_random_variables/03.05_geometric_negative_binomial.tex` (revelado progresivo `\pause`, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.06 Distribución Hipergeométrica:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.6.1 al 3.6.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.06_hypergeometric.py` (validación PMF, FPCF con Monte Carlo $N=250,000$ y prueba exacta de Fisher).
  - *Mazos Beamer:* mazos ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.06_hipergeometrica.tex` y `presentaciones/en/03_discrete_random_variables/03.06_hypergeometric.tex`, compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`**.
  - *Libro Maestro:* Compilado limpiamente (`[Modelación Estadística].tex`).
- $\checkmark$ **03.07 Distribución de Poisson y Procesos de Llegada:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.7.1 al 3.7.10): cálculo directo de PMF, equidispersión, ley de eventos raros, aditividad, deducción analítica de momentos y propiedad condicional binomial en suma de Poisson.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.07_poisson_distribution.py` (validación de PMF y equidispersión, ley de eventos raros Binomial $\to$ Poisson con TVD, aditividad y distribución condicional binomial verificada por simulación Monte Carlo con $N=250,000$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.07_poisson_distribution.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.07_poisson_distribution.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 552 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **03.08 Distribución Multinomial y Ensayos Politómicos:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.8.1 al 3.8.10): coeficientes multinomiales, probabilidades conjuntas, marginales binomiales, simulación de ensayos politómicos, covarianzas negativas, deducción de momentos factoriales, distribuciones condicionales y aplicación a tablas de contingencia.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.08_multinomial_distribution.py` (validación de PMF multinomial y normalización, simulación Monte Carlo de covarianzas con $N=250,000$ verificando $\cov(X_i, X_j) = -n p_i p_j$, distribución condicional multinomial en sub-vector verificada con filtro de 43{,}324 muestras de 500,000 simulaciones).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.08_multinomial_distribution.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.08_multinomial_distribution.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 560 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **03.09 Distribución Normal y Aproximación Continua:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.9.1 al 3.9.10): PDF Normal y estandarización $Z$, cálculo de probabilidades con la regla 68-95-99.7, aproximación Binomial-Normal con corrección de Yates, Poisson-Normal con $\lambda \ge 30$, deducción del Teorema de De Moivre-Laplace vía MGF, MGF de la Normal, TLC aplicado a sumas de Poisson y Exponential.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.09_normal_approximation.py` (verificación de PDF Normal con integración numérica $\int f = 1$, estandarización $Z$ y regla empírica, aproximación Binomial-Normal con y sin Yates mostrando reducción de error de $0.0112$ a $0.0021$, Poisson-Normal con error $< 0.001$, TLC para suma de 50 exponenciales verificado por Monte Carlo con $N=250{,}000$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.09_normal_approximation.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.09_normal_approximation.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 568 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **03.10 Distribuciones Discretas en Ciencia de Datos:** 100% completado (**CIERRE DEL CAPÍTULO 03**).
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.10.1 al 3.10.10): MLE de Poisson, detección de sobredispersión por cociente $D = s^{2}/\bar{x}$, intervalos de Wald/exacto/bootstrap, ajuste de Binomial Negativa por momentos, comparación de modelos vía AIC/BIC, test de razón de verosimilitud de Wilks, modelo jerárquico Poisson-Gamma, inferencia en confiabilidad exponencial.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.py` (ajuste MLE de Poisson y Binomial Negativa con $\Delta$AIC $= 16.21$ a favor de NegBin, test de Wilks con $\Lambda = 45.34$ y $p < 10^{-6}$ para $n = 200$ de NegBin, intervalos de Wald/exacto/bootstrap para $\lambda$ Poisson con 12 meses de reclamaciones, bootstrap de parámetros de Binomial Negativa con $B = 10{,}000$ muestras).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.10_discrete_distributions_data_science.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 576 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.02 Función de Distribución Acumulada Continua y Cuantiles:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_continuas(p).tex` (Problemas 4.2.1 al 4.2.10): CDF exponencial, cuantiles, método de inversión, prueba de Kolmogorov-Smirnov, log-normal, propiedades axiomáticas de $F$.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.02_continuous_cdf.py` (validación de propiedades de CDF; cuantiles por inversión numérica; método de inversión verificado con KS test $p > 0.4$; test KS aplicado a $n = 50$ muestras Uniform).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.02_continuous_cdf.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.02_continuous_cdf.tex` (20 frames), compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 590 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.03 Esperanza Matemática, Varianza y Teorema LOTUS Continuo:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/esperanza_matematica(p).tex` (Problemas 4.3.1 al 4.3.10): esperanza y varianza de PDF triangular, momentos de Exponential, asimetría y curtosis, LOTUS, linealidad, ley total de varianza, propagación de incertidumbre.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.03_expectation_and_variance.py` (verificación de momentos para Triangular, Uniform, Exponential, Normal; LOTUS para $\E[\sqrt{X}] = 0.8$ y $\E[\log X] = -0.5$; asimetría $\gamma_{1} = 2$ y curtosis $\gamma_{2} = 6$ de Exponential; Monte Carlo con $N = 250{,}000$ confirma valores teóricos; ley total de varianza validada en modelo jerárquico).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.03_expectation_and_variance.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.03_expectation_and_variance.tex` (20 frames), compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 596 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.04 Distribución Uniforme Continua $U(a, b)$:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_continuas_avanzado(p).tex` (Problemas 4.4.1 al 4.4.10): PDF y CDF de $U(2, 8)$, momentos, propiedad de no-falta-de-memoria, cuantiles, simulación Monte Carlo, método de inversión, máxima entropía, orden estadísticas, MLE de midrange, y prueba de Kolmogorov-Smirnov.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.04_uniform_distribution.py` (validación de $\int f = 1$; comparación de CDF manual vs SciPy con tolerancia $0$; cuantiles por inversión numérica; Monte Carlo con $N = 100{,}000$ verifica $\E[X] \approx 0.5$ y $\Var(X) \approx 0.0833$; máxima entropía verificada: Uniform(0,1) tiene $h = 0 > -0.125 = h(\text{Beta}(2,2))$; prueba KS distingue correctamente muestras Uniform de Exponential).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.04_uniform_distribution.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.04_uniform_distribution.tex` (20 frames), compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 602 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.05 Distribución Exponencial y Procesos sin Memoria:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_continuas_avanzado(p).tex` (Problemas 4.5.1 al 4.5.10): PDF y CDF exponencial, momentos, conexión con proceso de Poisson, propiedad de falta de memoria, cuantiles, MLE $\hat{\lambda} = 1/\bar{X}$, distribución Erlang, sistemas de confiabilidad en serie, y sistema de colas M/M/1.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.05_exponential_distribution.py` (verificación de $\int f = 1$; propiedad de falta de memoria con tolerancia $< 10^{-15}$; MLE con $n = 50$ muestras produce $\hat{\lambda} = 2.36 \pm 0.37$ con CI bootstrap al 95\% $[1.82, 3.27]$; Erlang$(5, 1)$ verificada con KS test $p = 0.46$; sistema de $n = 10$ componentes en serie con MTTF = 100 h; sistema M/M/1 con $\rho = 0.833$, $L = 5$ y $W = 1$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.05_exponential_distribution.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.05_exponential_distribution.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 608 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.06 Distribución Normal / Gaussiana y Puntaje $Z$:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_continuas_avanzado(p).tex` (Problemas 4.6.1 al 4.6.10): PDF y CDF Normal, estandarización al puntaje $Z$, regla 68-95-99.7, prueba $Z$ de una muestra, deducción de MGF Normal, suma de normales independientes, Teorema del Límite Central, y aproximación Binomial-Normal con corrección de Yates.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.06_normal_distribution.py` (validación de $\int f = 1$ con tolerancia $< 10^{-7}$; estandarización $Z$ verificada con tolerancia $< 10^{-16}$ para 6 puntos; regla 68-95-99.7 confirmada; cuantiles $z_{0.025} = -1.96$, $z_{0.975} = 1.96$; prueba $Z$ con $Z = 1.5$, $p = 0.134$; TLC verificado: suma de 30 uniformes $\sim N(15, 2.5)$ con KS $p = 0.71$; aproximación Binomial-Normal con error $0.001$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.06_normal_distribution.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.06_normal_distribution.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 614 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.07 Distribuciones Gamma, Beta y Weibull:** 100% completado (**CIERRE DEL CAPÍTULO 04**).
  - *Teoría del Libro Maestro:* Se auditó la subsección Gamma existente en `latex/variables_aleatorias_continuas_avanzado.tex` y se agregaron las subsecciones nuevas `Distribución beta` y `Distribución Weibull` (con sus espejos en `latex/en_variables_aleatorias_continuas_avanzado.tex`), ya que solo la teoría Gamma preexistía en el libro maestro.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/variables_aleatorias_continuas_avanzado(p).tex` (Problemas 4.7.1 al 4.7.10): PDF y normalización Gamma, casos particulares Exponencial y Chi-cuadrada, momentos vía MGF, PDF y momentos Beta, actualización bayesiana conjugada y propiedad de simetría, confiabilidad y tasa de falla Weibull, comparación de lotes Weibull, conexión Gamma-Chi-cuadrada, y proceso de reemplazo Gamma/Erlang vs. Weibull.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.py` (validación de $\int f = 1$ para Gamma, Beta y Weibull vía `scipy.integrate.quad`; propiedad aditiva de Erlang con $P(T>1.5)=0.1736$; casos particulares Exponencial y Chi-cuadrada verificados exactos contra SciPy; momentos Beta$(3,5)$ exactos; propiedad de simetría Beta verificada numéricamente; actualización bayesiana Beta$(2,2) \to$ Beta$(16,8)$; comparación de funciones de riesgo Weibull para $\beta=1$ vs. $\beta=2$).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.tex` (23 frames) y `presentaciones/en/04_continuous_random_variables/04.07_gamma_beta_weibull.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 622 páginas (`[Modelación Estadística].tex`).

### Unidad 4 / Capítulo 05: Distribuciones de Muestreo (`Avance actual: 5 de 5 secciones completadas --- 100% FINALIZADO`)
- $\checkmark$ **05.01 Muestreo Aleatorio Simple, Media y Varianza Muestral Insesgada:** 100% completado (**APERTURA DEL CAPÍTULO 05**).
  - *Teoría del Libro Maestro:* Se auditó `latex/distribuciones_muestreo_avanzado.tex` (ES) y su espejo `latex/en_distribuciones_muestreo_avanzado.tex` (EN) — la subsección "Distribuciones muestrales de medias" ya cubría $E(\bar X)=\mu$ y $\Var(\bar X)=\sigma^2/n$, pero no la insesgadez de la varianza muestral. Se agregó la subsección nueva "Estadísticos y Varianza Muestral Insesgada" con la definición formal de estadístico, la corrección de Bessel y su demostración completa.
  - *Cuaderno de Problemas:* Se creó `latex/distribuciones_muestreo_avanzado(p).tex` (no existía previamente) con 10 problemas 3-3-2-2 (Problemas 5.1.1 al 5.1.10): media/varianza muestral, distinción estadístico vs. parámetro, derivación de $\Var(\bar X)=\sigma^2/n$, comparación de estimadores sesgado/insesgado, demostración formal de $E(S^2)=\sigma^2$, consistencia de $\bar X$, fórmula abreviada de $S^2$, y corrección por población finita (FPC). Archivo conectado al libro maestro vía `\input{distribuciones_muestreo_avanzado(p)}`.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.01_sample_statistics.py` (verificación Monte Carlo de $E(S^2)=\sigma^2$ vs. estimador sesgado con $N=200{,}000$ muestras; distribución muestral de $\bar X$ verificada para $n=25,100,400$; corrección por población finita verificada empíricamente por muestreo sin reemplazo, FPC teórica $\approx 31.50$ vs. empírica $\approx 31.61$).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.01_sample_statistics.tex` (18 frames) y `presentaciones/en/05_sampling_distributions/05.01_sample_statistics.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 628 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (448 páginas) sin errores.
  - *Correcciones adicionales aplicadas durante esta sesión (fuera del alcance directo de 05.01, pero bloqueaban una compilación limpia del libro maestro):* se definieron los comandos `\E` y `\Prob` (faltantes) en `latex/_pe_comandos.tex`, eliminando cientos de errores "Undefined control sequence" en problemas de capítulos previos; se corrigió un `\begin{align*}`/`\end{itemize}` mal balanceado en `latex/distribuciones_especiales(p).tex`; se reemplazaron caracteres Unicode sin soporte (ideogramas chinos accidentales y ✓ literal) por `\checkmark` en `latex/distribuciones_especiales(p).tex` y `latex/variables_aleatorias_continuas(p).tex`. El libro maestro compila ahora con **0 errores de LaTeX** (`! ...`) de punta a punta.
- $\checkmark$ **05.02 Teorema del Límite Central Asintótico:** 100% completado.
  - *Teoría del Libro Maestro:* Nueva subsección "Teorema del Límite Central: Convergencia Asintótica" agregada a `latex/distribuciones_muestreo_avanzado.tex` (ES) y su espejo `latex/en_distribuciones_muestreo_avanzado.tex` (EN) — convergencia en distribución formal, demostración completa vía FGM (siguiendo el mismo método usado como ejercicio en la 04.06), y el teorema de Berry-Esseen para la tasa de convergencia $O(1/\sqrt n)$. El TLC introductorio de `muestreo_aleatorio.tex` (usado en 02.06) se dejó sin cambios, ya que este tratamiento es deliberadamente más riguroso y complementario.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_muestreo_avanzado(p).tex` (Problemas 5.2.1 al 5.2.10): aplicación directa del TLC, identificación de $Z_n$, heurística $n\ge30$ vs. Berry-Esseen, TLC para sumas (reclamaciones de seguros), cota de Berry-Esseen numérica, TLC para proporciones muestrales, demostración FGM para la Exponencial, derivación de $n$ mínimo a partir de Berry-Esseen, aproximación Binomial-Normal con corrección de Yates, y TLC combinado con la FPC de la Sección 05.01.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.02_central_limit_theorem.py` (convergencia verificada vía prueba de Kolmogorov-Smirnov desde una población Exponencial fuertemente asimétrica para $n=5,30,100$; tasa de Berry-Esseen verificada empíricamente con razones observadas $\approx 0.53$ y $\approx 0.55$ contra la razón teórica $0.5$; aplicaciones a sumas de reclamaciones de seguros y proporciones muestrales, con verificación cruzada Monte Carlo).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.02_central_limit_theorem.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.02_central_limit_theorem.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 632 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (450 páginas) sin errores.
- $\checkmark$ **05.03 Distribución Chi-Cuadrada y Varianza Muestral:** 100% completado.
  - *Teoría del Libro Maestro:* La subsección "Distribución $\chi^2$" en `latex/distribuciones_muestreo_avanzado.tex` (ES) y su espejo EN ya cubría definición, propiedades y la observación de que $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, pero sin PDF explícita ni demostración. Se agregó la densidad formal, el **Teorema de Fisher** completo (independencia de $\bar X$ y $S^2$, más el resultado chi-cuadrada) con bosquejo de demostración vía transformación ortogonal (Teorema de Cochran), y un ejemplo resuelto.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_muestreo_avanzado(p).tex` (Problemas 5.3.1 al 5.3.10): propiedades básicas, definición vía suma de normales al cuadrado, aplicación directa del estadístico $(n-1)S^2/\sigma^2$, reproductividad, MGF vía la conexión Gamma (Sección 04.07), prueba de hipótesis para $\sigma^2$, derivación algebraica de $E(\chi^2_\nu)=\nu$ y $\Var(\chi^2_\nu)=2\nu$, demostración de reproductividad vía MGF, y la descomposición $T=Z/\sqrt{\chi^2_{n-1}/(n-1)}$ que anticipa la distribución $t$ de Student (05.04).
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.03_chi_squared_distribution.py` (propiedades y conexión Gamma verificadas exactas; reproductividad verificada por KS test $p=0.908$; Teorema de Fisher verificado con correlación$(\bar X, S^2)\approx 0.004$ y KS test $p=0.517$ contra $\chi^2_9$; cobertura empírica del intervalo de confianza para $\sigma^2$ de $94.87\%$ vs. $95\%$ nominal).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.03_chi_squared_distribution.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.03_chi_squared_distribution.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 636 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (450 páginas) sin errores.
- $\checkmark$ **05.04 Distribución $t$ de Student y Muestras Pequeñas:** 100% completado.
  - *Teoría del Libro Maestro:* La subsección "Distribución $t$ de Student" en `latex/distribuciones_muestreo_avanzado.tex` (ES) y su espejo EN ya cubría definición, PDF, propiedades y la observación del estadístico $t$, pero le faltaba la aplicación práctica central: el intervalo de confianza para $\mu$ con $\sigma$ desconocida. Se agregó el teorema del intervalo de confianza, una observación sobre por qué el ajuste importa más en muestras pequeñas, y un ejemplo resuelto comparando el intervalo $t$ contra el (incorrecto) intervalo $z$.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_muestreo_avanzado(p).tex` (Problemas 5.4.1 al 5.4.10): propiedades de la $t$, construcción de intervalos de confianza, comparación de cuantiles $t$ vs. $z$, prueba $t$ de una muestra, derivación analítica de $\Var(T)=\nu/(\nu-2)$, convergencia a la Normal vía Slutsky, muestras pareadas, y determinación iterativa de tamaño de muestra.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.04_student_t_distribution.py` (varianza y convergencia de cuantiles verificadas exactas; comparación de intervalos $t$ vs. $z$ mostrando una diferencia del $17.7\%$ para $n=9$; prueba $t$ de una muestra; cobertura empírica del IC del $95.09\%$ vs. $95\%$ nominal).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.04_student_t_distribution.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.04_student_t_distribution.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 640 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (452 páginas) sin errores.
- $\checkmark$ **05.05 Distribución $F$ de Fisher-Snedecor:** 100% completado (**CIERRE DEL CAPÍTULO 05**).
  - *Teoría del Libro Maestro:* La subsección "Distribución $F$ de Snedecor" en `latex/distribuciones_muestreo_avanzado.tex` (ES) y su espejo EN ya era muy completa (definición, PDF, propiedades, prueba de igualdad de varianzas, y un ANOVA completamente resuelto). Se agregó el **intervalo de confianza para $\sigma_1^2/\sigma_2^2$** y la **identidad $T^2\sim F_{1,\nu}$**, que conecta formalmente las tres distribuciones del capítulo ($\chi^2$, $t$, $F$).
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_muestreo_avanzado(p).tex` (Problemas 5.5.1 al 5.5.10): propiedades básicas, propiedad recíproca, prueba $F$ de varianzas, ANOVA a partir de estadísticos resumidos, intervalo de confianza para el cociente de varianzas, demostración de $T^2\sim F_{1,\nu}$, derivación de $E(F)=d_2/(d_2-2)$, un ANOVA completo con datos crudos, y un problema de decisión que conecta la prueba $F$ con la elección entre prueba $t$ agrupada o de Welch.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.05_fisher_f_distribution.py` (propiedades, recíproco y la identidad $T^2\sim F_{1,\nu}$ verificados vía KS test; prueba $F$ e IC para $\sigma_1^2/\sigma_2^2$ con cobertura empírica de $94.97\%$; ANOVA completo verificado exacto contra `scipy.stats.f_oneway`).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.05_fisher_f_distribution.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.05_fisher_f_distribution.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 644 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (452 páginas) sin errores.

### Unidad 5 / Capítulo 06: Estimación y su Relación con Ciencia de Datos (`Avance actual: 5 de 5 secciones completadas --- 100% FINALIZADO`)
- $\checkmark$ **06.01 Estimación Puntual, Insesgadez, Eficiencia y Consistencia:** 100% completado (**APERTURA DEL CAPÍTULO 06**).
  - *Teoría del Libro Maestro:* `latex/estimacion_puntual.tex` (ES) y `latex/en_estimacion_puntual.tex` (EN) ya contenían un desarrollo extenso y avanzado de MLE y Método de Momentos, pero el texto introductorio hacía referencia a una "sección anterior" que definía los criterios de calidad de un estimador — contenido que en realidad nunca se había escrito. Se agregó la subsección faltante "Criterios de Calidad de un Estimador Puntual": definición formal de estimador, sesgo, ECM con demostración de la descomposición sesgo-varianza, eficiencia relativa, la Cota Inferior de Cramér-Rao, y consistencia (con la vía práctica vía Chebyshev).
  - *Cuaderno de Problemas:* 10 problemas nuevos 3-3-2-2 (Problemas 6.1.1 al 6.1.10) agregados a `latex/estimacion_puntual(p).tex` (que ya contenía 10 problemas avanzados preexistentes sobre MLE/MoM/Cramér-Rao/Rao-Blackwell, dejados intactos): insesgadez de combinaciones lineales, cálculo numérico de sesgo y ECM, eficiencia relativa, insesgadez asintótica, consistencia vía Chebyshev, derivación de la CRLB para la media normal, y el estimador de encogimiento (\emph{shrinkage}) óptimo que minimiza el ECM.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.01_point_estimation_quality.py` (descomposición sesgo-varianza-ECM y eficiencia relativa $\bar X$ vs. $T_1$ ($\text{Ef}\approx 16.07$, teórico $n=16$); estimador de encogimiento óptimo $c^*\approx 0.643$ con reducción de ECM del $35.7\%$, verificado por búsqueda en malla; consistencia de la proporción muestral verificada vía cota de Chebyshev vs. Monte Carlo).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.01_point_estimation_quality.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.01_point_estimation_quality.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 650 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (454 páginas) sin errores.
- $\checkmark$ **06.02 Método de Momentos (MoM):** 100% completado.
  - *Teoría del Libro Maestro:* La subsección "Método de Momentos (MoM)" en `latex/estimacion_puntual.tex` (ES) y su espejo EN ya tenía definición, teorema del procedimiento general, y un ejemplo resuelto (Gamma). Se agregó un segundo ejemplo ("el caso delicado" $U(-\theta,\theta)$, donde el primer momento no identifica al parámetro) y una observación de propiedades/limitaciones del MoM (consistencia vía LGN, menor eficiencia que MLE, posibilidad de estimaciones inadmisibles).
  - *Cuaderno de Problemas:* 10 problemas nuevos 3-3-2-2 (Problemas 6.2.1 al 6.2.10) agregados a `latex/estimacion_puntual(p).tex`: MoM para Poisson, Geométrica, Uniforme de dos parámetros, Binomial, Beta, consistencia vía LGN, MoM sin forma cerrada para Weibull, y comparación MoM vs. MLE para la Gamma.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.02_method_of_moments.py` (estimadores cerrados de la Gamma verificados exactos; el caso delicado $U(-\theta,\theta)$ verificado; eficiencia relativa MLE/MoM $\approx 1.14$ confirmando que el MLE es más eficiente, vía comparación Monte Carlo contra `scipy.stats.gamma.fit`).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.02_method_of_moments.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.02_method_of_moments.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 654 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (454 páginas) sin errores.
- $\checkmark$ **06.03 Estimación por Máxima Verosimilitud (MLE) y Score:** 100% completado.
  - *Teoría del Libro Maestro:* La subsección MLE en `latex/estimacion_puntual.tex` (ES) y su espejo EN ya tenía definición, ecuación de score (mencionada informalmente), dos ejemplos (Bernoulli, Normal) y propiedades asintóticas listadas sin demostración. Se agregó la subsubsección formal "La Función de Score y Normalidad Asintótica": definición de la función de score, sus propiedades (media cero con demostración, identidad de la información), y el Teorema de Normalidad Asintótica del MLE, conectado explícitamente con la Cota de Cramér-Rao de la Sección 06.01.
  - *Cuaderno de Problemas:* 10 problemas nuevos 3-3-2-2 (Problemas 6.3.1 al 6.3.10) agregados a `latex/estimacion_puntual(p).tex`: score y su media cero para la Exponencial, Información de Fisher, normalidad asintótica aplicada a la Poisson, MLE de la Geométrica vía score, demostración general de la identidad de la información, score vectorial para la Normal, MLE de la distribución Rayleigh, y el método delta para $\hat\sigma_{MLE}=\sqrt{\hat\sigma^2_{MLE}}$.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.py` (propiedades del score verificadas para la Exponencial; normalidad asintótica del MLE de Poisson verificada vía Monte Carlo con IC aproximado $[3.133, 3.867]$; MLE de Rayleigh y método delta verificados con varianzas empíricas que coinciden con las teóricas).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.03_maximum_likelihood_estimation.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 658 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (456 páginas) sin errores.
- $\checkmark$ **06.04 Intervalos de Confianza para Medias Poblacionales ($Z$ y $t$):** 100% completado.
  - *Teoría del Libro Maestro:* `latex/intervalos_de_confianza.tex` (ES) y su espejo EN eran de estilo histórico/conceptual (pruebas de hipótesis, valores-$p$, colas) sin fórmula explícita de IC para $\mu$; el archivo `latex/estimacion_intervalos_avanzado.tex` ya contenía teoría rigurosa avanzada (diferencia de medias, proporciones, varianzas, tamaño de muestra) pero asumía que el caso de una sola muestra ya había sido cubierto. Se agregó la subsección faltante "Construcción del Intervalo de Confianza para una Media Poblacional": los teoremas formales del IC con $Z$ (σ conocida) y con $t$ (σ desconocida), la estructura común "estimador ± margen de error", y un ejemplo resuelto comparando ambos casos.
  - *Cuaderno de Problemas:* Se auditó `latex/intervalos_de_confianza(p).tex` y se encontró que **ya contenía un cuaderno completo 3-3-2-2** (10 problemas con etiquetas descriptivas `prob-ic-*`) cubriendo exactamente el tema de 06.04: IC básico con $Z$, decisión $Z$ vs. $t$, tamaño de muestra, varianza agrupada, aproximación de Welch, y una demostración epistemológica rigurosa de la interpretación frecuentista. No se creó un cuaderno nuevo para evitar duplicar contenido ya completo y de alta calidad.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.04_confidence_intervals_means.py` (comparación IC $Z$ vs. $t$ verificada exacta; IC de diferencia de medias con varianza agrupada verificado idéntico a la solución existente; cobertura frecuentista verificada vía Monte Carlo con $100{,}000$ repeticiones, $94.96\%$ vs. $95\%$ nominal).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.04_confidence_intervals_means.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.04_confidence_intervals_means.tex` (19 frames), citando los problemas existentes `prob-ic-1`, `prob-ic-6`, `prob-ic-analit-pooled` y `prob-ic-desaf-epistemologia`, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 660 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (456 páginas) sin errores.
- $\checkmark$ **06.05 Intervalos de Confianza para Varianzas y Proporciones:** 100% completado (**CIERRE DEL CAPÍTULO 06**).
  - *Teoría del Libro Maestro:* `latex/estimacion_intervalos_avanzado.tex` (ES) y su espejo EN ya contenían teoremas rigurosos y completos para IC de varianza ($\chi^2$), razón de varianzas ($F$), proporción (Wald) y diferencia de proporciones, además de fórmulas de tamaño de muestra. Se agregó el **Intervalo de Wilson (Score)** explícito, que la observación existente solo mencionaba por nombre sin dar su fórmula, junto con una explicación de por qué mantiene mejor cobertura real que Wald.
  - *Cuaderno de Problemas:* Se auditó `latex/estimacion_intervalos_avanzado(p).tex` y se confirmó que **ya contenía un cuaderno 3-3-2-2 completo y de nivel avanzado** (10 problemas) cubriendo IC para varianza, razón de varianzas, diferencia de proporciones A/B, tamaño de muestra, y dos problemas desafiantes de gran calidad (transformación de Fisher para correlación, método delta para cocientes de medias). No se creó un cuaderno nuevo para evitar duplicar contenido ya excelente.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.05_confidence_intervals_variances.py` (IC $\chi^2$ para varianza verificado exacto; comparación Wald vs. Wilson mostrando que Wilson nunca cruza el $0$; IC $F$ para razón de varianzas y prueba A/B verificados idénticos a las soluciones existentes; IC de Fisher para correlación exacto; **estudio de cobertura Monte Carlo revelando que Wald solo cubre 87.65\% cuando el nominal es 95\%, mientras Wilson cubre 95.64\%** --- confirmación numérica contundente de por qué Wilson es preferible).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.05_confidence_intervals_variances.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.05_confidence_intervals_variances.tex` (20 frames), citando los problemas existentes `prob:ic_varianza`, `prob:dif_proporciones_ab`, `prob:ic_razon_varianzas` y `prob:ic-desaf-fisher`, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 660 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (458 páginas) sin errores.

### Unidad 6 / Capítulo 07: Docimasia (Pruebas de Hipótesis) (`Avance actual: 4 de 4 secciones completadas --- 100% FINALIZADO`)
- $\checkmark$ **07.01 Fundamentos: $H_0$ vs. $H_1$, Errores Tipo I y II, y Potencia:** 100% completado (**APERTURA DEL CAPÍTULO 07**).
  - *Teoría del Libro Maestro:* `latex/pruebas_de_hipotesis.tex` (ES) y su espejo EN ya contenían un desarrollo completo (notación formal, tipos de prueba, errores Tipo I/II, nivel de significación, valor-$p$, regla de decisión, ejemplo íntegro), pero carecían de una fórmula formal para relacionar potencia con tamaño de muestra. Se agregó la subsección faltante "Potencia y Tamaño de Muestra": el teorema del tamaño de muestra $n=((Z_\alpha+Z_\beta)\sigma/(\mu_a-\mu_0))^2$ para una prueba $Z$ de una cola, con una observación sobre el *trade-off* triangular entre $\alpha$, $\beta$ y $n$.
  - *Cuaderno de Problemas:* **No existía un archivo `(p).tex` para esta sección** (a diferencia de `chi_cuadrada(p).tex` y `pruebas_hipotesis_avanzadas(p).tex`, que sí existían). Se creó desde cero `latex/pruebas_de_hipotesis(p).tex` y su espejo `latex/en_pruebas_de_hipotesis(p).tex` con 10 problemas nuevos 3-3-2-2 (Problemas 7.1.1 al 7.1.10): formulación de $H_0/H_a$, interpretación de errores Tipo I/II en contexto médico, prueba $Z$ completa, cálculo de $\beta$ y potencia, tamaño de muestra para potencia objetivo, deducción de la función de potencia general, tasa de error familiar (FWER) y corrección de Bonferroni, el Lema de Neyman-Pearson (optimalidad UMP del test $Z$), y la deducción rigurosa de la fórmula de tamaño de muestra desde las definiciones puras de $\alpha$ y $\beta$. Se conectó (`\input`) al libro maestro ES y EN justo después de `pruebas_de_hipotesis`.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.py` (tasa de Error Tipo I verificada vía Monte Carlo con 200,000 réplicas, $0.0503$ vs. $\alpha=0.05$ nominal; potencia analítica y empírica coincidentes para $\mu_a=108$; tamaño de muestra $n=31$ verificado empíricamente alcanzando potencia $0.9073$ vs. objetivo $0.90$, mientras $n=30$ se queda corto).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.01_hypothesis_testing_basics.tex` (17 frames), citando los problemas nuevos 7.1.1, 7.1.5, 7.1.7 y 7.1.9, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente (668 páginas ES); también se recompiló `[Statistical Modeling].tex` sin errores. Nota: se encontró un bloqueo transitorio de archivo (SumatraPDF con el PDF abierto) durante la primera compilación posterior a los cambios de la Sección 07.03; se resolvió reintentando la compilación.
- $\checkmark$ **07.02 Pruebas $Z$ y $t$ para Medias de Una y Dos Muestras:** 100% completado.
  - *Teoría del Libro Maestro:* `latex/pruebas_hipotesis_avanzadas.tex` (ES) y su espejo EN ya contenían teoremas rigurosos completos para los cuatro casos de comparación de dos medias (varianzas conocidas, varianza agrupada, Welch, pareadas), además de pruebas de proporciones, varianzas y homogeneidad. No se requirió teoría nueva.
  - *Cuaderno de Problemas:* Se auditó `latex/pruebas_hipotesis_avanzadas(p).tex` y se confirmó que **ya contenía un cuaderno 3-3-2-2 completo y de nivel avanzado** (10 problemas con etiquetas descriptivas `prob:doc_*`) cubriendo dos medias, proporciones, varianzas, homogeneidad y Marascuilo. No se creó un cuaderno nuevo para evitar duplicar contenido ya completo.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.02_z_t_tests_means.py` (prueba $t$ de una muestra verificada contra `scipy.stats.ttest_1samp`; comparación directa de varianza agrupada vs. Welch bajo homoscedasticidad y heteroscedasticidad, verificada contra `scipy.stats.ttest_ind`; prueba $t$ pareada verificada contra `scipy.stats.ttest_rel`).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.02_z_t_tests_means.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.02_z_t_tests_means.tex` (17 frames), citando los problemas existentes `prob:doc_dos_medias_iguales`, `prob:doc_welch_hetero`, `prob:doc_errores_potencia_muestra` y `prob:doc_desaf_lrt_wilks`, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* No requirió recompilación (no se modificó el libro maestro en esta sección); verificado indirectamente en la recompilación final del capítulo.
- $\checkmark$ **07.03 Pruebas de Bondad de Ajuste $\chi^2$:** 100% completado.
  - *Teoría del Libro Maestro:* `latex/chi_cuadrada.tex` (ES) y su espejo EN ya contenían la introducción, el estadístico, la distribución $\chi^2$ y un ejemplo de bondad de ajuste (dado), pero carecían de un teorema formal para la prueba de bondad de ajuste y la Regla de Cochran. Se agregó la subsección "Prueba formal de bondad de ajuste": el teorema con $\nu=k-1-m$ grados de libertad (donde $m$ es el número de parámetros estimados de la muestra), y una observación formalizando la Regla de Cochran (ningún $E_i<1$; máximo 20\% de celdas con $E_i<5$) y el procedimiento de fusión de celdas.
  - *Cuaderno de Problemas:* Se auditó `latex/chi_cuadrada(p).tex` y se confirmó que **ya contenía un cuaderno 3-3-2-2 completo** (10 problemas, mezclando bondad de ajuste e independencia) con etiquetas `prob:3.9.*` y `prob:chi-*`. No se creó un cuaderno nuevo; se seleccionaron los 4 problemas de sabor "bondad de ajuste" para esta sección (3.9.1, 3.9.2, chi-analit-poisson, chi-desaf-teorema-pearson), dejando los de sabor "independencia/homogeneidad" para la Sección 07.04.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.py` (bondad de ajuste uniforme verificada contra `scipy.stats.chisquare`; ajuste Poisson con $\hat\lambda$ estimado y grados de libertad corregidos ($\nu=k-1-m$) verificado contra `scipy.stats.chisquare(ddof=1)`; violación de la Regla de Cochran detectada y corregida mediante fusión de celdas, con el estadístico recalculado).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.03_goodness_of_fit_tests.tex` (17 frames), citando los problemas existentes 3.9.1, 3.9.2, chi-analit-poisson y chi-desaf-teorema-pearson, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente tras agregar el teorema formal y la Regla de Cochran; también se recompiló `[Statistical Modeling].tex` sin errores.
- $\checkmark$ **07.04 Tablas de Contingencia y Pruebas de Independencia:** 100% completado (**CIERRE DEL CAPÍTULO 07**).
  - *Teoría del Libro Maestro:* `latex/chi_cuadrada.tex` (independencia) y `latex/pruebas_hipotesis_avanzadas.tex` (homogeneidad, Marascuilo) ya contenían teoría rigurosa y completa para esta sección (diferencia conceptual independencia vs. homogeneidad, estadístico común, procedimiento post-hoc de Marascuilo). No se requirió teoría nueva.
  - *Cuaderno de Problemas:* Se reutilizaron los problemas de sabor "independencia/homogeneidad" ya existentes en `latex/chi_cuadrada(p).tex` (3.9.3, 3.9.5, chi-analit-homogeneidad-z, chi-desaf-contingencia-2x2) y `latex/pruebas_hipotesis_avanzadas(p).tex` (`prob:homogeneidad_contingencia`), citándolos directamente sin duplicar contenido.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.04_contingency_tables.py` (prueba de independencia en tabla $4\times3$ verificada contra `scipy.stats.chi2_contingency`; prueba de homogeneidad en 3 cohortes independientes con la misma fórmula pero diseño muestral distinto; **identidad exacta $Z^2=\chi^2$ verificada numéricamente a precisión de máquina** ($|\chi^2-Z^2|<10^{-10}$) en una tabla $2\times2$ de ensayo clínico).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.04_contingency_tables.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.04_contingency_tables.tex` (17 frames), citando los problemas existentes 3.9.3, 3.9.5 y las secciones analítica/desafiante de contingencia $2\times2$, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente (`[Modelación Estadística].tex` y `[Statistical Modeling].tex`), confirmando **0 errores y 0 referencias indefinidas** tras el cierre completo del Capítulo 07.

---

## 3. Plan de Armonización Estructural y Curricular (Notas y Presentaciones ES/EN)


Para resolver definitivamente la discrepancia de numeración reportada y asegurar la paridad bilingüe de todo el ecosistema (*tufte-book* en ES/EN + Beamer ES/EN + Python), se establece la siguiente hoja de ruta en 3 fases de ejecución estricta:

### Fase 1: Reordenamiento y Formalización en las Notas Maestras (`latex/`)
1. **Versión en Español (`latex/distribuciones_especiales.tex`):**
   Reordenar los bloques teóricos dentro del archivo para que la progresión de secciones sea estrictamente consecutiva y coincida con el orden pedagógico de las distribuciones discretas:
   - **Sección 3.1:** Funciones de masa de probabilidad discretas (PMF y soporte) (`variables_aleatorias_discretas.tex`)
   - **Sección 3.2:** Función de distribución acumulada para variables aleatorias discretas (CDF) (`variables_aleatorias_discretas.tex`)
   - **Sección 3.3:** Esperanza matemática y varianza en variables aleatorias discretas (`variables_aleatorias_discretas.tex`)
   - **Sección 3.4:** Distribución Binomial y Bernoulli (`distribuciones_especiales.tex`)
   - **Sección 3.5:** Distribuciones Geométrica y Binomial Negativa (`distribuciones_especiales.tex` --- *Traslado inmediato después de Binomial*)
   - **Sección 3.6:** Distribución Hipergeométrica (`distribuciones_especiales.tex` --- *Traslado tras Geométrica*)
   - **Sección 3.7:** Distribución de Poisson (`distribuciones_especiales.tex`)
   - **Sección 3.8:** Distribución Multinomial (`distribuciones_especiales.tex`)
   - **Sección 3.9:** Distribución Normal y aproximación continua (`distribuciones_especiales.tex`)
   - **Sección 3.10:** Distribuciones discretas en ciencia de datos (`distribuciones_especiales.tex`)
2. **Versión en Inglés (`latex/en_variables_aleatorias_discretas.tex` y `en_distribuciones_especiales.tex`):**
   Aplicar la misma jerarquía y reordenamiento en las notas en inglés (`[Statistical Modeling].tex`):
   - Elevar `Discrete Probability Functions` a **Section 3.1** y `Distribution Functions` a **Section 3.2**.
   - Redactar e integrar **Section 3.3:** `Mathematical Expectation and Variance of Discrete Random Variables`.
   - Reordenar `en_distribuciones_especiales.tex` en **Sections 3.4 a 3.10** en simetría 1:1 exacta con la versión en español.
3. **Certificación de Compilación del Libro:** Compilar dos veces tanto `[Modelación Estadística].tex` como `[Statistical Modeling].tex` para validar las tablas de contenido (`.toc`) y las referencias cruzadas.

### Fase 2: Renombramiento y Alinear Títulos en Mazos Beamer (`presentaciones/`)
1. Auditores y ajuste de subtítulos (`\subtitle{Sección 03.XX --- ...}`) en los mazos existentes `03.01` a `03.06` en las carpetas `presentaciones/es/03_variables_aleatorias_discretas/` y `presentaciones/en/03_discrete_random_variables/`.
2. Verificar que los identificadores de archivo (`03.01` a `03.06`) mapeen en simetría total 1:1 con las Secciones 3.1 a 3.6 formalizadas en la Fase 1.

### Fase 3: Desarrollo Curricular de las Secciones Faltantes (03.07 a 03.10)
Con el nuevo ordenamiento consolidado, el desarrollo de temas restantes del Capítulo 3 abarcará los siguientes 4 módulos, cada uno ejecutado bajo la estructura de oro (**10 Problemas 3-3-2-2 en `(p).tex` ES/EN $\to$ Script Python en inglés $\to$ 22 Slides Beamer ES/EN con 0 Overfulls**):
- **Sección 03.07:** Distribución de Poisson y Procesos de Llegada (`03.07_poisson_distribution.py`, mazos ES/EN de 22 diapositivas).
- **Sección 03.08:** Distribución Multinomial y Ensayos Politómicos (`03.08_multinomial_distribution.py`, mazos ES/EN de 22 diapositivas).
- **Sección 03.09:** Distribución Normal y Aproximación Continua de Variables Discretas (`03.09_normal_approximation.py`, mazos ES/EN de 22 diapositivas).
- **Sección 03.10:** Distribuciones Discretas en Ciencia de Datos y Casos Prácticos (`03.10_discrete_distributions_data_science.py`, mazos ES/EN de 22 diapositivas).

---

## 4. Guía de Arranque Inmediato para la Próxima Sesión y/o Máquina (`Sección 04.07`) --- COMPLETADA

**Estado: ejecutada y cerrada.** La Sección 04.07 (Distribuciones Gamma, Beta y Weibull) fue completada siguiendo el protocolo de 6 pasos descrito abajo, cerrando el Capítulo 04 al 100%. Esta guía se conserva como referencia histórica del protocolo aplicado; la próxima sesión debe iniciar la **Sección 05.01** (ver Sección 5 de este documento, Unidad 4 / Capítulo 05).

<details>
<summary>Protocolo de 6 pasos ejecutado para la 04.07 (referencia histórica)</summary>

**Secciones 04.01 a 04.06 del Capítulo 04 completadas.** Cuando un nuevo agente o sesión se inicie en esta u otra computadora con el fin de continuar el proyecto, deberá ejecutar de inmediato la **Sección 04.07: Distribuciones Gamma, Beta y Weibull**, siguiendo este protocolo exacto de 6 pasos:

### Paso 1: Auditoría de Teoría y Creación/Integración de `(p).tex`
1. Consultar el archivo `latex/variables_aleatorias_continuas_avanzado.tex` (donde se ubica la teoría de las distribuciones Gamma, Beta y Weibull).
2. Verificar si en `variables_aleatorias_continuas_avanzado(p).tex` existen los problemas de la 04.07. Si no existen, agregar los 10 problemas bajo la taxonomía `3-3-2-2` usando los entornos institucionales (`\begin{problema}`, `\begin{sugerencia}`, `\begin{solucion}`):
   - **Nivel Fundamental (3):** Definición de Gamma($\alpha, \lambda$) con PDF $f(x) = \frac{\lambda^{\alpha}}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}$, casos particulares (Exponencial, Chi-cuadrada), y momentos (`4.7.1` a `4.7.3`).
   - **Nivel Operativo (3):** Distribución Beta($\alpha, \beta$) en $[0, 1]$, cálculo de esperanza y varianza, y aplicación a proporciones (`4.7.4` a `4.7.6`).
   - **Nivel Analítico (2):** Distribución Weibull con PDF $f(t) = \frac{\beta}{\eta}(t/\eta)^{\beta-1} e^{-(t/\eta)^{\beta}}$ y aplicación a análisis de confiabilidad (`4.7.7` y `4.7.8`).
   - **Nivel Desafiante (2):** Conexión Gamma-Chi-cuadrada, y aplicación a procesos Gamma para análisis de tasas de fallo (`4.7.9` y `4.7.10`).
3. Compilar el libro maestro dos veces para comprobar que no se rompen índices ni referencias.

### Paso 2: Desarrollo de Script Python en Inglés (`04.07_gamma_beta_weibull.py`)
Crear el archivo en `presentaciones/code/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.py` con `numpy` y `scipy.stats`:
- **Block 1: Gamma Distribution & Erlang:** Verificación de $\int f(x)\,dx = 1$ con `scipy.integrate.quad`; relación Gamma-Erlang; casos particulares Exponential y Chi-squared.
- **Block 2: Beta Distribution & Moments:** Cálculo de esperanza y varianza para Beta($\alpha, \beta$); verificación de la simetría Beta($\alpha, \beta$) = $1 - $ Beta($\beta, \alpha$); aplicación a prior bayesiano.
- **Block 3: Weibull & Reliability Analysis:** Distribución Weibull con tasa de fallo variable; aplicación a sistemas con Weibull(shape=$\beta$); comparación de funciones de hazard.

### Paso 3: Construcción de Mazos Beamer en Español e Inglés (`04.07_gamma_beta_weibull.tex`)
1. Crear los mazos espejos en `presentaciones/es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.07_gamma_beta_weibull.tex` (20 frames).
2. Usar `\date{\vspace{-1.2cm}}` en la portada ES y `\date{\vspace{-1.5cm}}` en la portada EN.
3. Importar los bloques del script con `\lstinputlisting[language=Python, ...]{../../code/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.py}`.
4. Ajustar tablas teóricas y espaciados para prevenir `Overfull`.

### Paso 4: Compilación y Doble Verificación (*Zero Overfull Check*)
Ejecutar los siguientes comandos en la terminal y comprobar que la búsqueda de `Overfull` arroje cero coincidencias en las diapositivas 2+:
```bash
cd presentaciones/es/04_variables_aleatorias_continuas
pdflatex -interaction=nonstopmode 04.07_gamma_beta_weibull.tex && pdflatex -interaction=nonstopmode 04.07_gamma_beta_weibull.tex
grep "Overfull" 04.07_gamma_beta_weibull.log

cd ../../en/04_continuous_random_variables
pdflatex -interaction=nonstopmode 04.07_gamma_beta_weibull.tex && pdflatex -interaction=nonstopmode 04.07_gamma_beta_weibull.tex
grep "Overfull" 04.07_gamma_beta_weibull.log
```

### Paso 5: Sincronización de Ebook Principal (`[Modelación Estadística].tex`)
```bash
cd C:/Users/julih/REPOSITORIES/ebook-estadistica-matematica.worktrees/crear-presentaciones/latex
pdflatex -interaction=nonstopmode "[Modelación Estadística].tex" && pdflatex -interaction=nonstopmode "[Modelación Estadística].tex"
```

### Paso 6: Actualización de Documentación y Cierre de Tarea (Sin Auto-Commits)
Al completar la 04.07, el Capítulo 04 estará 100% finalizado. Actualizar este archivo (`ROADMAP.md`) marcando la 04.07 como completada, y verificar con `git status -s` que todos los archivos generados estén limpios y pendientes de confirmación del usuario.

</details>

---

## 5. Mapeo Curricular Maestro — Capítulos 03 al 09 (Temas Pendientes)

A continuación se enlistan exhaustivamente todos los temas curriculares que deben desarrollarse de manera sucesiva tras finalizar la Sección 03.06, siguiendo la misma estructura de 3 archivos: cuaderno `(p).tex`, script Python y 2 mazos Beamer ES/EN.

### Capítulo 03: Variables Aleatorias Discretas (Restantes)
- **Sección 03.07:** Distribución de Poisson y Procesos de Llegada (`03.07_poisson_distribution.py`). *Ley de eventos raros ($\lambda=np$), conteo continuo e intervalos de llegada.*
- **Sección 03.08:** Distribución Multinomial y Ensayos Politómicos (`03.08_multinomial_distribution.py`). *Probabilidades conjuntas, covarianzas negativas entre categorías.*
- **Sección 03.09:** Distribución Normal y Aproximación Continua de Variables Discretas (`03.09_normal_approximation.py`). *Teorema de De Moivre-Laplace y corrección por continuidad de Yates.*
- **Sección 03.10:** Distribuciones Discretas en Ciencia de Datos y Casos Prácticos (`03.10_discrete_distributions_data_science.py`). *Ajuste por máxima verosimilitud MLE y modelado empirico.*

---

### Unidad 3 / Capítulo 04: Variables Aleatorias Continuas (`Avance actual: 7 de 7 secciones completadas --- 100% FINALIZADO`)
Directorio base Python: `presentaciones/code/04_variables_aleatorias_continuas/`
- $\checkmark$ **04.01 Función de Densidad (PDF) y Soporte Continuo:** 100% completado.
- **Sección 04.02:** Función de Distribución Acumulada (CDF) Continua y Cuantiles (`04.02_continuous_cdf.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 04.03:** Esperanza Matemática, Varianza y Teorema LOTUS Continuo (`04.03_expectation_and_variance.py`).
- **Sección 04.03:** Esperanza Matemática, Varianza y Teorema LOTUS Continuo (`04.03_expectation_and_variance.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 04.04:** Distribución Uniforme Continua ($U(a,b)$) (`04.04_uniform_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 04.05:** Distribución Exponencial y Procesos Continuos Sin Memoria (`04.05_exponential_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 04.06:** Distribución Normal / Gaussiana ($N(\mu, \sigma^2)$) y Puntaje $Z$ (`04.06_normal_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 04.07:** Distribuciones Gamma, Beta y Weibull (`04.07_gamma_beta_weibull.py`). **100% COMPLETADO** — ver descripción detallada arriba.

---

### Unidad 4 / Capítulo 05: Distribuciones de Muestreo
Directorio base Python: `presentaciones/code/05_distribuciones_muestreo/`
- **Sección 05.01:** Muestreo Aleatorio Simple, Media y Varianza Muestral Insesgada (`05.01_sample_statistics.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 05.02:** Teorema del Límite Central (TLC) Asintótico (`05.02_central_limit_theorem.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 05.03:** Distribución Chi-Cuadrada ($\chi^2(k)$) y Varianza Muestral (`05.03_chi_squared_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 05.04:** Distribución $t$ de Student ($t(\nu)$) y Muestras Pequeñas (`05.04_student_t_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 05.05:** Distribución $F$ de Fisher-Snedecor ($F(d_1, d_2)$) (`05.05_fisher_f_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.

---

### Unidad 5 / Capítulo 06: Estimación y Ciencia de Datos
Directorio base Python: `presentaciones/code/06_estimacion_estadistica/`
- **Sección 06.01:** Estimación Puntual, Insesgadez, Eficiencia y Consistencia (`06.01_point_estimation_quality.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 06.02:** Método de Momentos (MoM) (`06.02_method_of_moments.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 06.03:** Estimación por Máxima Verosimilitud (MLE) y Score (`06.03_maximum_likelihood_estimation.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 06.04:** Intervalos de Confianza para Medias Poblacionales ($Z$ y $t$) (`06.04_confidence_intervals_means.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 06.05:** Intervalos de Confianza para Varianzas ($\chi^2$) y Proporciones (`06.05_confidence_intervals_variances.py`). **100% COMPLETADO** — ver descripción detallada arriba.

---

### Unidad 6 / Capítulo 07: Docimasia (Pruebas de Hipótesis) (`Avance actual: 4 de 4 secciones completadas --- 100% FINALIZADO`)
Directorio base Python: `presentaciones/code/07_pruebas_hipotesis/`
- **Sección 07.01:** Fundamentos: $H_0$ vs $H_1$, Errores Tipo I y II, y Potencia (`07.01_hypothesis_testing_basics.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 07.02:** Pruebas $Z$ y $t$ para Medias de Una y Dos Muestras (`07.02_z_t_tests_means.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 07.03:** Pruebas de Bondad de Ajuste $\chi^2$ (`07.03_goodness_of_fit_tests.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 07.04:** Tablas de Contingencia y Pruebas de Independencia (`07.04_contingency_tables.py`). **100% COMPLETADO** --- ver descripción detallada arriba.

---

### Unidad 7 / Capítulo 08: Elementos de Diseño de Experimentos (ANOVA)
Directorio base Python: `presentaciones/code/08_diseno_experimentos/`
- **Sección 08.01:** Análisis de Varianza de un Factor (ANOVA 1-Way) y Prueba $F$ (`08.01_one_way_anova.py`).
- **Sección 08.02:** Supuestos del ANOVA, Prueba de Levene/Bartlett y Diagnóstico (`08.02_anova_assumptions.py`).

---

### Tema Complementario / Capítulo 09: Regresiones Lineales y Múltiples
Directorio base Python: `presentaciones/code/09_regresiones/`
- **Sección 09.01:** Regresión Lineal Simple (OLS) y Coeficiente de Determinación $R^2$ (`09.01_simple_linear_regression.py`).
- **Sección 09.02:** Regresión Lineal Múltiple, Ecuación Normal y Regularización Ridge/Lasso (`09.02_multiple_linear_regression.py`).
- **Sección 09.03:** Diagnóstico de Residuos, Multicolinealidad (VIF) y Supuestos Clásicos (`09.03_regression_diagnostics.py`).
- **Sección 09.04:** Validación de Modelos, $k$-fold Cross-Validation y `scikit-learn` (`09.04_model_validation.py`).

---

## 6. Referencia de Comandos Rápida para Agentes AI

```bash
# Compilar libro maestro
cd C:/Users/julih/REPOSITORIES/ebook-estadistica-matematica.worktrees/crear-presentaciones/latex
pdflatex -interaction=nonstopmode "[Modelación Estadística].tex" && pdflatex -interaction=nonstopmode "[Modelación Estadística].tex"

# Verificación de Overfull en una presentación (ejemplo ES)
cd C:/Users/julih/REPOSITORIES/ebook-estadistica-matematica.worktrees/crear-presentaciones/presentaciones/es/<capitulo>
pdflatex -interaction=nonstopmode <seccion>.tex && pdflatex -interaction=nonstopmode <seccion>.tex
grep "Overfull" <seccion>.log

# Revisar archivos modificados sin commit
git status -s
```
