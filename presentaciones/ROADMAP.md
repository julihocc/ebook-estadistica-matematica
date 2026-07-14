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
- $\checkmark$ **02.01 Introducción a la Probabilidad:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.01_intro_probability.py`.
- $\checkmark$ **02.02 Conjuntos y Particiones:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.02_sets_and_partitions.py`.
- $\checkmark$ **02.03 Fundamentos y Axiomas:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.03_probability_fundamentals.py`.
- $\checkmark$ **02.04 Probabilidad Condicional:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.04_conditional_probability.py`.
- $\checkmark$ **02.05 Teorema de Bayes:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.05_bayes_theorem.py`.
- $\checkmark$ **02.06 Muestreo Aleatorio y TLC:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.06_random_sampling.py`.

### Unidad 2 / Capítulo 03: Variables Aleatorias Discretas (`Avance actual: 4 de 9 secciones completadas`)
- $\checkmark$ **03.01 PMF y Soporte:** 100% completado (`03.01_pmf_y_soporte.tex` ES/EN, `03.01_pmf_and_support.py`).
- $\checkmark$ **03.02 CDF Discreta:** 100% completado (`03.02_cdf_discreta.tex` ES/EN, `03.02_discrete_cdf.py`).
- $\checkmark$ **03.03 Esperanza Matemática, Varianza y Momentos:** 100% completado (`03.03_esperanza_y_varianza.tex` ES/EN, `03.03_expectation_and_variance.py`).
- $\checkmark$ **03.04 Distribuciones de Bernoulli y Binomial:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas 3-3-2-2 en `latex/distribuciones_especiales(p).tex` (Problemas 3.4.1 al 3.4.10) debidamente importados por el libro maestro.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.py` (validación combinatoria con SciPy y Monte Carlo $N=100,000$).
  - *Mazos Beamer:* 20 diapositivas exactas en `presentaciones/es/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.tex` y `en/03.04_bernoulli_binomial.tex`, compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** bajo el tema Metropolis.
  - *Libro Maestro:* Compilado limpiamente (`[Modelación Estadística].tex`) con 518 páginas verificadas.

---

## 3. Guía de Arranque Inmediato para la Próxima Sesión y/o Máquina (`Sección 03.05`)

Cuando un nuevo agente o sesión se inicie en esta u otra computadora con el fin de continuar el proyecto, deberá ejecutar de inmediato la **Sección 03.05: Distribuciones Geométrica y Binomial Negativa** siguiendo este protocolo exacto de 6 pasos:

### Paso 1: Auditoría de Teoría y Creación/Integración de `(p).tex`
1. Consultar el archivo `latex/distribuciones_especiales.tex` (donde se ubica la teoría de distribuciones geométricas y binomiales negativas o de espera).
2. Verificar si en `distribuciones_especiales(p).tex` existen los problemas de la 03.05. Si no existen, agregar los 10 problemas bajo la taxonomía `3-3-2-2` usando los entornos institucionales (`\begin{problema}`, `\begin{sugerencia}`, `\begin{solucion}`):
   - **Nivel Fundamental (3):** Tiempo de espera al primer éxito (PMF geométrica $P(X=k) = q^{k-1}p$), propiedad de pérdida de memoria y cálculo de probabilidades acumuladas sencillas (`3.5.1` a `3.5.3`).
   - **Nivel Operativo (3):** Muestreo hasta obtener $r$ éxitos (Binomial Negativa / Pascal $P(X=k) = \comb{k-1}{r-1}p^r q^{k-r}$), control de calidad industrial con paros de línea e inspección reiterada (`3.5.4` a `3.5.6`).
   - **Nivel Analítico (2):** Deducción formal de esperanza $\mu = 1/p$ (o $r/p$) por diferenciación de series de potencias o suma de geométricas i.i.d., y cálculo de varianza $\sigma^2 = q/p^2$ (`3.5.7` y `3.5.8`).
   - **Nivel Desafiante (2):** Teorema de caracterización de la pérdida de memoria en V.A. discretas ($P(X>m+n \mid X>m) = P(X>n) \iff X \sim \text{Geom}$) y relación asintótica/límite (`3.5.9` y `3.5.10`).
3. Compilar el libro maestro dos veces para comprobar que no se rompen índices ni referencias.

### Paso 2: Desarrollo de Script Python en Inglés (`03.05_geometric_negative_binomial.py`)
Crear el archivo en `presentaciones/code/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.py` con `numpy` y `scipy.stats`:
- **Block 1: Geometric vs. Negative Binomial PMF & CDF Validation:** Verificación de soporte, suma unitaria y relación como suma de $r$ geométricas independientes (`scipy.stats.geom`, `scipy.stats.nbinom`).
- **Block 2: Memoryless Property & Monte Carlo Waiting Times:** Simulación empírica de $N=100,000$ trayectorias de espera demostrando numéricamente la propiedad sin memoria $P(X > m+n \mid X > m) = P(X > n)$.
- **Block 3: Analytical Moments & Dispersion Analysis:** Comparación empírica vs. teórica de la sobre-dispersión (donde $\sigma^2 > \mu$), contrastando con la binomial donde $\sigma^2 < \mu$.

### Paso 3: Construcción de Mazos Beamer en Español e Inglés (`03.05_geometric_negative_binomial.tex`)
1. Crear los mazos espejos de 20 diapositivas en `presentaciones/es/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.tex` y `presentaciones/en/03_discrete_random_variables/03.05_geometric_negative_binomial.tex`.
2. Usar `\date{\vspace{-1.2cm}}` en la portada para absorber el alto de autor e institución sin generar advertencia vertical.
3. Importar los bloques del script con `\lstinputlisting[language=Python, firstline=..., lastline=..., basicstyle=\fontsize{6.3pt}{7.5pt}\ttfamily]{../../code/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.py}`.
4. Ajustar tablas teóricas con `p{width}` explícitos para prevenir `Overfull \hbox`.

### Paso 4: Compilación y Doble Verificación (*Zero Overfull Check*)
Ejecutar los siguientes comandos en la terminal y comprobar que la búsqueda de `Overfull` arroje cero coincidencias en las diapositivas 2+:
```bash
# Para la versión en Español
cd presentations/es/03_variables_aleatorias_discretas
pdflatex -interaction=nonstopmode 03.05_geometric_negative_binomial.tex && pdflatex -interaction=nonstopmode 03.05_geometric_negative_binomial.tex
grep "Overfull" 03.05_geometric_negative_binomial.log

# Para la versión en Inglés
cd ../../en/03_discrete_random_variables
pdflatex -interaction=nonstopmode 03.05_geometric_negative_binomial.tex && pdflatex -interaction=nonstopmode 03.05_geometric_negative_binomial.tex
grep "Overfull" 03.05_geometric_negative_binomial.log
```

### Paso 5: Sincronización de Ebook Principal (`[Modelación Estadística].tex`)
```bash
cd C:/Users/julih/REPOSITORIES/ebook-estadistica-matematica.worktrees/crear-presentaciones/latex
pdflatex -interaction=nonstopmode "[Modelación Estadística].tex" && pdflatex -interaction=nonstopmode "[Modelación Estadística].tex"
```

### Paso 6: Actualización de Documentación y Cierre de Tarea (Sin Auto-Commits)
Actualizar este archivo (`ROADMAP.md`) marcando la 03.05 como completada y apuntando a la 03.06 como el nuevo foco. Verificar con `git status -s` que todos los archivos generados estén limpios y pendientes de confirmación del usuario.

---

## 4. Mapeo Curricular Maestro — Capítulos 03 al 09 (Temas Pendientes)

A continuación se enlistan exhaustivamente todos los temas curriculares que deben desarrollarse de manera sucesiva tras finalizar la Sección 03.05, siguiendo la misma estructura de 3 archivos: cuaderno `(p).tex`, script Python y 2 mazos Beamer ES/EN.

### Capítulo 03: Variables Aleatorias Discretas (Restantes)
- **Sección 03.06:** Distribución Hipergeométrica (`03.06_hypergeometric.py`). *Muestreo sin reemplazo ($N, K, n$), momentos combinatorios y convergencia asintótica a la Binomial.*
- **Sección 03.07:** Distribución de Poisson y Procesos de Poisson (`03.07_poisson_distribution.py`). *Ley de eventos raros ($\lambda=np$), conteo continuo e intervalos de llegada.*
- **Sección 03.08:** Momentos y Funciones Generadoras de Momentos (`03.08_moment_generating_functions.py`). *$M_X(t)=\mathbb{E}[e^{tX}]$, derivadas en el origen ($M_X^{(k)}(0)=\mathbb{E}[X^k]$), unicidad.*
- **Sección 03.09:** Desigualdades Probabilísticas en V.A. Discretas (`03.09_probability_inequalities.py`). *Cotas de Markov ($P(X\ge a)\le \mu/a$) y de Chebyshev ($P(|X-\mu|\ge k\sigma)\le 1/k^2$).*

---

### Unidad 3 / Capítulo 04: Variables Aleatorias Continuas
Directorio base Python: `presentaciones/code/04_variables_aleatorias_continuas/`
- **Sección 04.01:** Función de Densidad de Probabilidad (PDF) y Soporte Continuo (`04.01_pdf_and_support.py`).
- **Sección 04.02:** Función de Distribución Acumulada (CDF) Continua y Cuantiles (`04.02_continuous_cdf.py`).
- **Sección 04.03:** Esperanza Matemática, Varianza y Teorema LOTUS Continuo (`04.03_expectation_and_variance.py`).
- **Sección 04.04:** Distribución Uniforme Continua ($U(a,b)$) (`04.04_uniform_distribution.py`).
- **Sección 04.05:** Distribución Exponencial y Procesos Continuos Sin Memoria (`04.05_exponential_distribution.py`).
- **Sección 04.06:** Distribución Normal / Gaussiana ($N(\mu, \sigma^2)$) y Puntaje $Z$ (`04.06_normal_distribution.py`).
- **Sección 04.07:** Distribuciones Gamma, Beta y Weibull (`04.07_gamma_beta_weibull.py`).

---

### Unidad 4 / Capítulo 05: Distribuciones de Muestreo
Directorio base Python: `presentaciones/code/05_distribuciones_muestreo/`
- **Sección 05.01:** Muestreo Aleatorio Simple, Media y Varianza Muestral Insesgada (`05.01_sample_statistics.py`).
- **Sección 05.02:** Teorema del Límite Central (TLC) Asintótico (`05.02_central_limit_theorem.py`).
- **Sección 05.03:** Distribución Chi-Cuadrada ($\chi^2(k)$) y Varianza Muestral (`05.03_chi_squared_distribution.py`).
- **Sección 05.04:** Distribución $t$ de Student ($t(\nu)$) y Muestras Pequeñas (`05.04_student_t_distribution.py`).
- **Sección 05.05:** Distribución $F$ de Fisher-Snedecor ($F(d_1, d_2)$) (`05.05_fisher_f_distribution.py`).

---

### Unidad 5 / Capítulo 06: Estimación y Ciencia de Datos
Directorio base Python: `presentaciones/code/06_estimacion_estadistica/`
- **Sección 06.01:** Estimación Puntual, Insesgadez, Eficiencia y Consistencia (`06.01_point_estimation_quality.py`).
- **Sección 06.02:** Método de Momentos (MoM) (`06.02_method_of_moments.py`).
- **Sección 06.03:** Estimación por Máxima Verosimilitud (MLE) y Score (`06.03_maximum_likelihood_estimation.py`).
- **Sección 06.04:** Intervalos de Confianza para Medias Poblacionales ($Z$ y $t$) (`06.04_confidence_intervals_means.py`).
- **Sección 06.05:** Intervalos de Confianza para Varianzas ($\chi^2$) y Proporciones (`06.05_confidence_intervals_variances.py`).

---

### Unidad 6 / Capítulo 07: Docimasia (Pruebas de Hipótesis)
Directorio base Python: `presentaciones/code/07_pruebas_hipotesis/`
- **Sección 07.01:** Fundamentos: $H_0$ vs $H_1$, Errores Tipo I y II, y Potencia (`07.01_hypothesis_testing_basics.py`).
- **Sección 07.02:** Pruebas $Z$ y $t$ para Medias de Una y Dos Muestras (`07.02_z_t_tests_means.py`).
- **Sección 07.03:** Pruebas de Bondad de Ajuste $\chi^2$ (`07.03_goodness_of_fit_tests.py`).
- **Sección 07.04:** Tablas de Contingencia y Pruebas de Independencia (`07.04_contingency_tables.py`).

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
- **Sección 09.03:** Diagnóstico de Residuos, Multicolinealidad (VIF) y `scikit-learn` (`09.03_regression_diagnostics.py`).

---

## 5. Referencia de Comandos Rápida para Agentes AI

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
