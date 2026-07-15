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

### Unidad 2 / Capítulo 03: Variables Aleatorias Discretas (`Avance actual: 9 de 10 secciones completadas`)
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

---

## 3. Plan de Armonización Estructural y Curricular (Notas y Presentaciones ES/EN)

Nota operativa: existe un borrador local complementario en `presentaciones/plan-maestro-reestructuracion-pedagogica.md`. Ese archivo debe revisarse antes de ejecutar reestructuraciones mayores de los capítulos 04 al 09; mientras no esté aprobado, no sustituye a este `ROADMAP.md`.

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

## 4. Guía de Arranque Inmediato para la Próxima Sesión y/o Máquina (`Sección 03.10`)

Cuando un nuevo agente o sesión se inicie en esta u otra computadora con el fin de continuar el proyecto, deberá ejecutar de inmediato la **Sección 03.10: Distribuciones Discretas en Ciencia de Datos y Casos Prácticos** siguiendo este protocolo exacto de 6 pasos:

### Paso 1: Auditoría de Teoría y Creación/Integración de `(p).tex`
1. Consultar el archivo `latex/distribuciones_especiales.tex` (donde se ubica la teoría de aplicaciones de distribuciones discretas en ciencia de datos).
2. Verificar si en `distribuciones_especiales(p).tex` existen los problemas de la 03.10. Si no existen, agregar los 10 problemas bajo la taxonomía `3-3-2-2` usando los entornos institucionales (`\begin{problema}`, `\begin{sugerencia}`, `\begin{solucion}`):
   - **Nivel Fundamental (3):** Ajuste de distribuciones por máxima verosimilitud (MLE), comparación de modelos Poisson vs. Binomial Negativa, detección de sobredispersión (`3.10.1` a `3.10.3`).
   - **Nivel Operativo (3):** Estimación de parámetros con datos empíricos, bootstrap e intervalos de confianza para $\lambda$ y $p$, validación cruzada de modelos (`3.10.4` a `3.10.6`).
   - **Nivel Analítico (2):** Función de log-verosimilitud negativa, criterios de información AIC/BIC, y likelihood ratio test (`3.10.7` y `3.10.8`).
   - **Nivel Desafiante (2):** Regresión de Poisson y Binomial Negativa, predicción con incertidumbre, y aplicación a un caso real de detección de fraude o análisis de churn (`3.10.9` y `3.10.10`).
3. Compilar el libro maestro dos veces para comprobar que no se rompen índices ni referencias.

### Paso 2: Desarrollo de Script Python en Inglés (`03.10_discrete_distributions_data_science.py`)
Crear el archivo en `presentaciones/code/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.py` con `numpy` y `scipy.stats`:
- **Block 1: MLE Fitting & Overdispersion Detection:** Ajuste de Poisson y Binomial Negativa a datos de conteo empíricos; cálculo del índice de dispersión $D = s^{2}/\bar{x}$.
- **Block 2: Likelihood Ratio Test & Information Criteria:** Comparación de modelos vía log-verosimilitud, AIC, BIC, y test de sobredispersión.
- **Block 3: Confidence Intervals & Bootstrap:** Intervalos de confianza para $\lambda$ Poisson, intervalos bootstrap no paramétricos, y aplicación a un dataset sintético de churn.

### Paso 3: Construcción de Mazos Beamer en Español e Inglés (`03.10_discrete_distributions_data_science.tex`)
1. Crear los mazos espejos en `presentaciones/es/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.10_discrete_distributions_data_science.tex` (20 frames).
2. Usar `\date{\vspace{-1.2cm}}` en la portada ES y `\date{\vspace{-1.5cm}}` en la portada EN.
3. Importar los bloques del script con `\lstinputlisting[language=Python, ...]{../../code/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.py}`.
4. Ajustar tablas teóricas y espaciados para prevenir `Overfull`.

### Paso 4: Compilación y Doble Verificación (*Zero Overfull Check*)
Ejecutar los siguientes comandos en la terminal y comprobar que la búsqueda de `Overfull` arroje cero coincidencias en las diapositivas 2+:
```bash
cd presentaciones/es/03_variables_aleatorias_discretas
pdflatex -interaction=nonstopmode 03.10_discrete_distributions_data_science.tex && pdflatex -interaction=nonstopmode 03.10_discrete_distributions_data_science.tex
grep "Overfull" 03.10_discrete_distributions_data_science.log

cd ../../en/03_discrete_random_variables
pdflatex -interaction=nonstopmode 03.10_discrete_distributions_data_science.tex && pdflatex -interaction=nonstopmode 03.10_discrete_distributions_data_science.tex
grep "Overfull" 03.10_discrete_distributions_data_science.log
```

### Paso 5: Sincronización de Ebook Principal (`[Modelación Estadística].tex`)
```bash
cd C:/Users/julih/REPOSITORIES/ebook-estadistica-matematica.worktrees/crear-presentaciones/latex
pdflatex -interaction=nonstopmode "[Modelación Estadística].tex" && pdflatex -interaction=nonstopmode "[Modelación Estadística].tex"
```

### Paso 6: Actualización de Documentación y Cierre de Tarea (Sin Auto-Commits)
Actualizar este archivo (`ROADMAP.md`) marcando la 03.10 como completada y verificando que el Capítulo 03 (Variables Aleatorias Discretas) esté 100% finalizado. Verificar con `git status -s` que todos los archivos generados estén limpios y pendientes de confirmación del usuario.

---

## 5. Mapeo Curricular Maestro — Capítulos 03 al 09 (Temas Pendientes)

A continuación se enlistan exhaustivamente todos los temas curriculares que deben desarrollarse de manera sucesiva tras finalizar la Sección 03.06, siguiendo la misma estructura de 3 archivos: cuaderno `(p).tex`, script Python y 2 mazos Beamer ES/EN.

### Capítulo 03: Variables Aleatorias Discretas (Restantes)
- **Sección 03.07:** Distribución de Poisson y Procesos de Llegada (`03.07_poisson_distribution.py`). *Ley de eventos raros ($\lambda=np$), conteo continuo e intervalos de llegada.*
- **Sección 03.08:** Distribución Multinomial y Ensayos Politómicos (`03.08_multinomial_distribution.py`). *Probabilidades conjuntas, covarianzas negativas entre categorías.*
- **Sección 03.09:** Distribución Normal y Aproximación Continua de Variables Discretas (`03.09_normal_approximation.py`). *Teorema de De Moivre-Laplace y corrección por continuidad de Yates.*
- **Sección 03.10:** Distribuciones Discretas en Ciencia de Datos y Casos Prácticos (`03.10_discrete_distributions_data_science.py`). *Ajuste por máxima verosimilitud MLE y modelado empirico.*

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
