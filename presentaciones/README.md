# Presentaciones Beamer & Laboratorios de Simulación en Python

Este directorio (`presentaciones/`) contiene las presentaciones interactivas en **LaTeX Beamer** (español e inglés) y los **laboratorios computacionales en Python** complementarios para las clases del libro digital *Modelación Estadística*.

Esta guía constituye el **manual operativo estándar y 100% reproducible** para cualquier agente de inteligencia artificial (o colaborador humano) que trabaje en la creación, modificación, verificación o mantenimiento de las presentaciones y scripts de este proyecto.

### Estado documental verificado al 2026-07-23 11:17:26 -06:00

- El espejo de cuadernos del libro está cerrado desde el `2026-07-23 11:03:37 -06:00`: existen 60 archivos `(p).tex` ES y 60 contrapartes `en_*(p).tex`, con seis problemas Bloom, seis soluciones y etiquetas hash compartidas por par.
- El árbol de presentaciones contiene 54 mazos ES y 54 mazos EN (`.tex` y `.pdf`), además de 53 scripts Python en inglés bajo `presentaciones/code/`.
- Esta reconciliación actualiza únicamente documentación; no modifica `presentaciones/es/`, `presentaciones/en/` ni `presentaciones/code/`.

---

## 1. Arquitectura y Estructura del Directorio

```text
presentaciones/
├── _preambulo_beamer.tex           ← Preámbulo compartido en español (tema Metropolis, colores, paquetes)
├── _comandos_beamer.tex            ← Comandos matemáticos e institucionales en español
├── _en_preambulo_beamer.tex        ← Preámbulo compartido en inglés
├── _en_comandos_beamer.tex         ← Comandos matemáticos en inglés
├── README.md                       ← Esta guía y catálogo operativo de presentaciones
├── ROADMAP.md                      ← Hoja de ruta, trabajo pendiente y planificación de capítulos
├── code/                           ← ÚNICA FUENTE DE LA VERDAD para código de simulación (en inglés)
│   ├── 02_teoria_probabilidad/
│   │   ├── 02.02_sets_partitions.py
│   │   ├── 02.03_probability_axioms.py
│   │   ├── 02.04_conditional_probability.py
│   │   ├── 02.05_bayes_theorem.py
│   │   └── 02.06_random_sampling.py
│   ├── 03_variables_aleatorias_discretas/
│   │   ├── 03.01_pmf_and_support.py
│   │   ├── 03.02_discrete_cdf.py
│   │   ├── 03.03_expectation_and_variance.py
│   │   ├── 03.04_bernoulli_binomial.py
│   │   ├── 03.05_geometric_negative_binomial.py
│   │   ├── 03.06_hypergeometric.py
│   │   ├── 03.07_poisson_distribution.py
│   │   ├── 03.08_multinomial_distribution.py
│   │   ├── 03.09_normal_approximation.py
│   │   └── 03.10_discrete_distributions_data_science.py
│   └── <proximas_unidades>/
├── es/                             ← Presentaciones en español (p. ej. es/02_teoria_probabilidad/)
│   └── 02_teoria_probabilidad/
│       ├── 02.01_introduccion_probabilidad.tex (.pdf)
│       ├── 02.02_conjuntos_y_particiones.tex (.pdf)
│       ├── 02.03_fundamentos_probabilidad.tex (.pdf)
│       ├── 02.04_probabilidad_condicional.tex (.pdf)
│       ├── 02.05_teorema_bayes.tex (.pdf)
│       └── 02.06_muestreo_aleatorio.tex (.pdf)
└── en/                             ← Presentaciones en inglés (p. ej. en/02_probability_theory/)
    └── 02_probability_theory/
        ├── 02.01_probability_introduction.tex (.pdf)
        ├── 02.02_sets_and_partitions.tex (.pdf)
        ├── 02.03_probability_foundations.tex (.pdf)
        ├── 02.04_conditional_probability.tex (.pdf)
        ├── 02.05_bayes_theorem.tex (.pdf)
        └── 02.06_random_sampling.tex (.pdf)
```

---

## 2. Las 4 Reglas de Oro del Flujo de Trabajo

### Regla 1: Código de Python Unificado en Inglés (Una Sola Fuente de la Verdad)
- **Prohibido duplicar código:** No se permite crear archivos de simulación independientes en español o por idioma (`*.es.py`, scripts separados en carpetas de idioma, etc.).
- Todo script computacional del proyecto **debe estar redactado exclusivamente en inglés** (comentarios, variables, salidas por consola y docstrings en inglés) y debe ubicarse en `presentaciones/code/<unidad>/<ID>_<nombre_en_ingles>.py`.
- **Librerías permitidas:** Única y exclusivamente `python` estándar y `numpy` / `scipy` (sin dependencias que requieran entornos virtuales complejos o interfaces gráficas como `matplotlib` que bloqueen compilación o terminal).
- **Importación en Beamer:** Tanto la presentación en **español** como la presentación en **inglés** referencian exactamente el mismo script mediante `\lstinputlisting`:
  ```latex
  \lstinputlisting[language=Python, firstline=10, lastline=28, basicstyle=\fontsize{5.2pt}{6.1pt}\ttfamily]{../../code/02_teoria_probabilidad/02.06_random_sampling.py}
  ```

### Regla 2: Política de Cero Advertencias de Desbordamiento (*Zero Overfull Warning Policy*)
- Al compilar cualquier presentación Beamer en PDF mediante `pdflatex`, **ninguna diapositiva de contenido (páginas 2 en adelante) debe generar advertencias `Overfull \vbox` ni `Overfull \hbox`**.
- La portada (página 1) utiliza la convención estándar de Metropolis `\begin{frame}[plain] \titlepage \end{frame}`.
- **Técnicas obligatorias de prevención y corrección:**
  1. Uso del entorno de dos columnas `\begin{columns}[T]` para equilibrar la alineación vertical superior.
  2. Uso de tamaños de fuente compactos en el texto: `\small`, `\footnotesize`, `\scriptsize`.
  3. Control vertical fino entre bloques con `\vspace{-0.1cm}`, `\vspace{-0.15cm}` o `\vspace{-0.2cm}`.
  4. Reducción en la separación de listas: `\begin{itemize} \itemsep=0.03cm ... \end{itemize}`.
  5. En bloques de código largo, usar `\fontsize{5.0pt}{5.8pt}\selectfont` o dividir el laboratorio en múltiples diapositivas (p. ej., *Lab Python 1/4*, *2/4*, *3/4*, *4/4*).

### Regla 3: Identidad Institucional y Metadatos
Toda presentación (`.tex`) debe encabezarse estrictamente con los siguientes metadatos institucionales del autor y los archivos preámbulo compartidos del idioma correspondiente.

Plantilla en español:
```latex
% !TeX program = pdflatex
\documentclass[aspectratio=169,xcolor={dvipsnames,table}]{beamer}

\input{../../_preambulo_beamer}
\input{../../_comandos_beamer}

\title{Título del Tema}
\subtitle{Sección XX.YY --- Subtítulo del Tema}
\author[J. Castillo Colmenares]{Juliho Castillo Colmenares}
\institute[Tec de Monterrey]{Tecnológico de Monterrey}
\date{}
```

Plantilla en inglés:
```latex
% !TeX program = pdflatex
\documentclass[aspectratio=169,xcolor={dvipsnames,table}]{beamer}

\input{../../_en_preambulo_beamer}
\input{../../_en_comandos_beamer}

\title{Topic Title}
\subtitle{Section XX.YY --- Topic Subtitle}
\author[J. Castillo Colmenares]{Juliho Castillo Colmenares}
\institute[Tec de Monterrey]{Tecnológico de Monterrey}
\date{}
```
Los bloques institucionales en los preámbulos compartidos configuran la paleta oficial: **TecRojo (`#EC2661`)** y **TecAzul (`#1A2E51`)**.

### Regla 4: Cuadernos de Problemas y Taxonomía de Bloom
Cuando se cree o actualice una presentación, se debe verificar el cuaderno de ejercicios complementario correspondiente (`latex/<seccion>(p).tex`) sin convertirlo en material de ejercicios sin resolver dentro del mazo.
El estándar vigente exige cobertura de los seis niveles de Bloom, en este orden: **Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear**. Cada archivo vivo contiene como mínimo un problema por nivel (la convención actual normalmente produce seis problemas), comentarios LaTeX invisibles para documentar el nivel, y etiquetas `prob:<7-hex>` compartidas exactamente con su contraparte ES/EN.
Las soluciones deben enlazar explícitamente su problema mediante `\begin{solproblema}[prob:<tag>]`. Los mazos Beamer reutilizan ejemplos `\ejemplo`/`\solucion` ya resueltos en la teoría; el cuaderno `(p).tex` queda como práctica autónoma.

> **Referencia histórica no normativa.** La distribución de 10 problemas `3-3-2-2` con niveles visibles fue la convención anterior al 2026-07-20. No se debe aplicar a archivos nuevos ni usarla para evaluar el estado actual.

---

## 3. Checklist Reproducible de 6 Pasos para Añadir o Actualizar una Sección

Cualquier agente que trabaje en una nueva sección del libro (p. ej. Capítulo 03 en adelante) debe ejecutar y validar los siguientes pasos en orden cronológico exacto:

- [ ] **Paso 1: Auditoría de Teoría en LaTeX Maestro**
  - Abrir y leer `latex/<seccion>.tex` (o el capítulo correspondiente) para entender las fórmulas, definiciones, teoremas y notación exacta utilizada en el texto principal.
- [ ] **Paso 2: Cuaderno de Ejercicios (`(p).tex`) e Integración al Libro**
  - Verificar la existencia de `latex/<seccion>(p).tex`. Si no existe o no cubre los seis niveles de Bloom, redactar/completar al menos un problema por nivel, con sus soluciones detalladas en los entornos institucionales (`\begin{problema}`, `\begin{sugerencia}`, `\begin{solucion}`), comentarios de nivel invisibles y etiquetas hash sin colisión.
  - Asegurar que `\input{<seccion>(p)}` esté declarado en `latex/[Modelación Estadística].tex`.
  - Compilar el libro principal en la terminal: `cd latex && pdflatex "[Modelación Estadística].tex" && pdflatex "[Modelación Estadística].tex"`.
- [ ] **Paso 3: Desarrollo del Script de Simulación Python en Inglés**
  - Crear el archivo del laboratorio computacional en `presentaciones/code/<unidad>/<XX.YY_nombre>.py`.
  - Estructurar el script con bloques numerados (p. ej., `--- 1. Simulation A ---`, `--- 2. Convergence B ---`) y funciones claras de verificación que arrojen resultados numéricos por consola equivalentes a las demostraciones analíticas.
  - Ejecutar y probar el script en terminal para verificar sintaxis y precisión: `python <script>.py`.
- [ ] **Paso 4: Redacción de Presentaciones Beamer (ES / EN)**
  - Crear o actualizar el archivo en español `presentaciones/es/<unidad>/<seccion>.tex` siguiendo los cinco bloques y las 22 diapositivas de contenido definidos en las especificaciones; el Bloque IV debe reutilizar ejemplos resueltos de la teoría, no problemas `(p).tex` sin resolver.
  - Crear o actualizar la versión en inglés `presentaciones/en/<unidad>/<section>.tex` manteniendo simetría total y la misma importación al script `.py` en inglés.
- [ ] **Paso 5: Compilación Doble y Verificación Cero Advertencias (*Zero Overfull Check*)**
  - Compilar ambas presentaciones dos veces desde sus respectivos directorios:
    ```bash
    cd presentaciones/es/<unidad>/ && pdflatex -interaction=nonstopmode <archivo>.tex && pdflatex -interaction=nonstopmode <archivo>.tex
    cd ../../en/<unidad>/ && pdflatex -interaction=nonstopmode <archivo>.tex && pdflatex -interaction=nonstopmode <archivo>.tex
    ```
  - **Revisar el archivo de registro (`<archivo>.log`)**: Buscar `Overfull \vbox` o `Overfull \hbox`. Si aparecen en las páginas 2 a N, ajustar márgenes verticalmente (`\vspace`), reducir fuente del bloque de código (`\fontsize{..}{..}\selectfont`) o reestructurar columnas hasta obtener 0 advertencias de contenido.
- [ ] **Paso 6: Cierre de Cambios y Actualización de Documentación**
  - Hacer un `git status` para comprobar que se generaron los `.tex`, `.pdf`, `.py` y el `(p).tex`.
  - Actualizar el registro en `CHANGELOG.md` y verificar/actualizar el catálogo e índice en este archivo y en `ROADMAP.md`.
  - No ejecutar `git commit` ni `git push` automáticamente; dejar los cambios en el árbol de trabajo para revisión del autor.

---

## 4. Catálogo e Índice de Presentaciones --- Capítulo 02 (100% Completado)

A continuación se presenta el estado finalizado y verificado de las 6 secciones correspondientes a la **Unidad 1 / Capítulo 02: Teoría de la Probabilidad**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/02_teoria_probabilidad/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **02.01** | [02.01 Introducción a la Probabilidad](es/02_teoria_probabilidad/02.01_introduccion_probabilidad.tex) ([PDF](es/02_teoria_probabilidad/02.01_introduccion_probabilidad.pdf)) | [02.01 Intro to Probability](en/02_probability_theory/02.01_probability_introduction.tex) ([PDF](en/02_probability_theory/02.01_probability_introduction.pdf)) | Sin script dedicado | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.02** | [02.02 Conjuntos y Particiones](es/02_teoria_probabilidad/02.02_conjuntos_y_particiones.tex) ([PDF](es/02_teoria_probabilidad/02.02_conjuntos_y_particiones.pdf)) | [02.02 Sets and Partitions](en/02_probability_theory/02.02_sets_and_partitions.tex) ([PDF](en/02_probability_theory/02.02_sets_and_partitions.pdf)) | `02.02_sets_partitions.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.03** | [02.03 Fundamentos y Axiomas](es/02_teoria_probabilidad/02.03_fundamentos_probabilidad.tex) ([PDF](es/02_teoria_probabilidad/02.03_fundamentos_probabilidad.pdf)) | [02.03 Probability Fundamentals](en/02_probability_theory/02.03_probability_foundations.tex) ([PDF](en/02_probability_theory/02.03_probability_foundations.pdf)) | `02.03_probability_axioms.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.04** | [02.04 Probabilidad Condicional](es/02_teoria_probabilidad/02.04_probabilidad_condicional.tex) ([PDF](es/02_teoria_probabilidad/02.04_probabilidad_condicional.pdf)) | [02.04 Conditional Probability](en/02_probability_theory/02.04_conditional_probability.tex) ([PDF](en/02_probability_theory/02.04_conditional_probability.pdf)) | `02.04_conditional_probability.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.05** | [02.05 Teorema de Bayes](es/02_teoria_probabilidad/02.05_teorema_bayes.tex) ([PDF](es/02_teoria_probabilidad/02.05_teorema_bayes.pdf)) | [02.05 Bayes' Theorem](en/02_probability_theory/02.05_bayes_theorem.tex) ([PDF](en/02_probability_theory/02.05_bayes_theorem.pdf)) | `02.05_bayes_theorem.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.06** | [02.06 Muestreo y TLC](es/02_teoria_probabilidad/02.06_muestreo_aleatorio.tex) ([PDF](es/02_teoria_probabilidad/02.06_muestreo_aleatorio.pdf)) | [02.06 Random Sampling & CLT](en/02_probability_theory/02.06_random_sampling.tex) ([PDF](en/02_probability_theory/02.06_random_sampling.pdf)) | `02.06_random_sampling.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |

---

## 5. Catálogo e Índice de Presentaciones --- Capítulo 03 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 2 / Capítulo 03: Variables Aleatorias Discretas**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/03_variables_aleatorias_discretas/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **03.01** | [03.01 PMF y Soporte](es/03_variables_aleatorias_discretas/03.01_pmf_y_soporte.tex) ([PDF](es/03_variables_aleatorias_discretas/03.01_pmf_y_soporte.pdf)) | [03.01 PMF and Support](en/03_discrete_random_variables/03.01_pmf_and_support.tex) ([PDF](en/03_discrete_random_variables/03.01_pmf_and_support.pdf)) | `03.01_pmf_and_support.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **03.02** | [03.02 CDF Discreta](es/03_variables_aleatorias_discretas/03.02_cdf_discreta.tex) ([PDF](es/03_variables_aleatorias_discretas/03.02_cdf_discreta.pdf)) | [03.02 Discrete CDF](en/03_discrete_random_variables/03.02_discrete_cdf.tex) ([PDF](en/03_discrete_random_variables/03.02_discrete_cdf.pdf)) | `03.02_discrete_cdf.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **03.03** | [03.03 Esperanza y Varianza](es/03_variables_aleatorias_discretas/03.03_esperanza_y_varianza.tex) ([PDF](es/03_variables_aleatorias_discretas/03.03_esperanza_y_varianza.pdf)) | [03.03 Expectation & Variance](en/03_discrete_random_variables/03.03_expectation_and_variance.tex) ([PDF](en/03_discrete_random_variables/03.03_expectation_and_variance.pdf)) | `03.03_expectation_and_variance.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **03.04** | [03.04 Bernoulli y Binomial](es/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.tex) ([PDF](es/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.pdf)) | [03.04 Bernoulli & Binomial](en/03_discrete_random_variables/03.04_bernoulli_binomial.tex) ([PDF](en/03_discrete_random_variables/03.04_bernoulli_binomial.pdf)) | `03.04_bernoulli_binomial.py` | $\checkmark$ **Completado** |
| **03.05** | [03.05 Geométrica y Binomial Negativa](es/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.tex) ([PDF](es/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.pdf)) | [03.05 Geometric & Negative Binomial](en/03_discrete_random_variables/03.05_geometric_negative_binomial.tex) ([PDF](en/03_discrete_random_variables/03.05_geometric_negative_binomial.pdf)) | `03.05_geometric_negative_binomial.py` | $\checkmark$ **Completado** |
| **03.06** | [03.06 Hipergeométrica](es/03_variables_aleatorias_discretas/03.06_hipergeometrica.tex) ([PDF](es/03_variables_aleatorias_discretas/03.06_hipergeometrica.pdf)) | [03.06 Hypergeometric](en/03_discrete_random_variables/03.06_hypergeometric.tex) ([PDF](en/03_discrete_random_variables/03.06_hypergeometric.pdf)) | `03.06_hypergeometric.py` | $\checkmark$ **Completado** |
| **03.07** | [03.07 Poisson](es/03_variables_aleatorias_discretas/03.07_poisson_distribution.tex) ([PDF](es/03_variables_aleatorias_discretas/03.07_poisson_distribution.pdf)) | [03.07 Poisson Distribution](en/03_discrete_random_variables/03.07_poisson_distribution.tex) ([PDF](en/03_discrete_random_variables/03.07_poisson_distribution.pdf)) | `03.07_poisson_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **03.08** | [03.08 Multinomial](es/03_variables_aleatorias_discretas/03.08_multinomial_distribution.tex) ([PDF](es/03_variables_aleatorias_discretas/03.08_multinomial_distribution.pdf)) | [03.08 Multinomial Distribution](en/03_discrete_random_variables/03.08_multinomial_distribution.tex) ([PDF](en/03_discrete_random_variables/03.08_multinomial_distribution.pdf)) | `03.08_multinomial_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **03.09** | [03.09 Normal](es/03_variables_aleatorias_discretas/03.09_normal_approximation.tex) ([PDF](es/03_variables_aleatorias_discretas/03.09_normal_approximation.pdf)) | [03.09 Normal Distribution](en/03_discrete_random_variables/03.09_normal_approximation.tex) ([PDF](en/03_discrete_random_variables/03.09_normal_approximation.pdf)) | `03.09_normal_approximation.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **03.10** | [03.10 Discretas en Ciencia de Datos](es/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.tex) ([PDF](es/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.pdf)) | [03.10 Discrete Distributions in Data Science](en/03_discrete_random_variables/03.10_discrete_distributions_data_science.tex) ([PDF](en/03_discrete_random_variables/03.10_discrete_distributions_data_science.pdf)) | `03.10_discrete_distributions_data_science.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 03** |

---

## 5b. Catálogo e Índice de Presentaciones --- Capítulo 04 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 3 / Capítulo 04: Variables Aleatorias Continuas**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/04_variables_aleatorias_continuas/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **04.01** | [04.01 PDF y Soporte Continuo](es/04_variables_aleatorias_continuas/04.01_pdf_and_support.tex) ([PDF](es/04_variables_aleatorias_continuas/04.01_pdf_and_support.pdf)) | [04.01 PDF and Continuous Support](en/04_continuous_random_variables/04.01_pdf_and_support.tex) ([PDF](en/04_continuous_random_variables/04.01_pdf_and_support.pdf)) | `04.01_pdf_and_support.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 04** |
| **04.02** | [04.02 CDF Continua y Cuantiles](es/04_variables_aleatorias_continuas/04.02_continuous_cdf.tex) ([PDF](es/04_variables_aleatorias_continuas/04.02_continuous_cdf.pdf)) | [04.02 Continuous CDF and Quantiles](en/04_continuous_random_variables/04.02_continuous_cdf.tex) ([PDF](en/04_continuous_random_variables/04.02_continuous_cdf.pdf)) | `04.02_continuous_cdf.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.03** | [04.03 Esperanza y Varianza Continua](es/04_variables_aleatorias_continuas/04.03_expectation_and_variance.tex) ([PDF](es/04_variables_aleatorias_continuas/04.03_expectation_and_variance.pdf)) | [04.03 Continuous Expectation and Variance](en/04_continuous_random_variables/04.03_expectation_and_variance.tex) ([PDF](en/04_continuous_random_variables/04.03_expectation_and_variance.pdf)) | `04.03_expectation_and_variance.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.04** | [04.04 Uniforme Continua](es/04_variables_aleatorias_continuas/04.04_uniform_distribution.tex) ([PDF](es/04_variables_aleatorias_continuas/04.04_uniform_distribution.pdf)) | [04.04 Continuous Uniform Distribution](en/04_continuous_random_variables/04.04_uniform_distribution.tex) ([PDF](en/04_continuous_random_variables/04.04_uniform_distribution.pdf)) | `04.04_uniform_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.05** | [04.05 Exponencial](es/04_variables_aleatorias_continuas/04.05_exponential_distribution.tex) ([PDF](es/04_variables_aleatorias_continuas/04.05_exponential_distribution.pdf)) | [04.05 Exponential Distribution](en/04_continuous_random_variables/04.05_exponential_distribution.tex) ([PDF](en/04_continuous_random_variables/04.05_exponential_distribution.pdf)) | `04.05_exponential_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.06** | [04.06 Normal](es/04_variables_aleatorias_continuas/04.06_normal_distribution.tex) ([PDF](es/04_variables_aleatorias_continuas/04.06_normal_distribution.pdf)) | [04.06 Normal Distribution](en/04_continuous_random_variables/04.06_normal_distribution.tex) ([PDF](en/04_continuous_random_variables/04.06_normal_distribution.pdf)) | `04.06_normal_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.07** | [04.07 Gamma, Beta y Weibull](es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.tex) ([PDF](es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.pdf)) | [04.07 Gamma, Beta, and Weibull Distributions](en/04_continuous_random_variables/04.07_gamma_beta_weibull.tex) ([PDF](en/04_continuous_random_variables/04.07_gamma_beta_weibull.pdf)) | `04.07_gamma_beta_weibull.py` | $\checkmark$ **Completado (23 diapositivas ES / 19 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 04** |

---

## 5c. Catálogo e Índice de Presentaciones --- Capítulo 05 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 4 / Capítulo 05: Distribuciones de Muestreo**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/05_distribuciones_muestreo/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **05.01** | [05.01 Estadísticos y Varianza Insesgada](es/05_distribuciones_muestreo/05.01_sample_statistics.tex) ([PDF](es/05_distribuciones_muestreo/05.01_sample_statistics.pdf)) | [05.01 Sample Statistics and Unbiased Variance](en/05_sampling_distributions/05.01_sample_statistics.tex) ([PDF](en/05_sampling_distributions/05.01_sample_statistics.pdf)) | `05.01_sample_statistics.py` | $\checkmark$ **Completado (18 diapositivas ES / 19 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 05** |
| **05.02** | [05.02 TLC Asintótico](es/05_distribuciones_muestreo/05.02_central_limit_theorem.tex) ([PDF](es/05_distribuciones_muestreo/05.02_central_limit_theorem.pdf)) | [05.02 Asymptotic Central Limit Theorem](en/05_sampling_distributions/05.02_central_limit_theorem.tex) ([PDF](en/05_sampling_distributions/05.02_central_limit_theorem.pdf)) | `05.02_central_limit_theorem.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings)** |
| **05.03** | [05.03 Chi-Cuadrada y Varianza Muestral](es/05_distribuciones_muestreo/05.03_chi_squared_distribution.tex) ([PDF](es/05_distribuciones_muestreo/05.03_chi_squared_distribution.pdf)) | [05.03 Chi-Squared Distribution and Sample Variance](en/05_sampling_distributions/05.03_chi_squared_distribution.tex) ([PDF](en/05_sampling_distributions/05.03_chi_squared_distribution.pdf)) | `05.03_chi_squared_distribution.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings)** |
| **05.04** | [05.04 $t$ de Student](es/05_distribuciones_muestreo/05.04_student_t_distribution.tex) ([PDF](es/05_distribuciones_muestreo/05.04_student_t_distribution.pdf)) | [05.04 Student's t-Distribution](en/05_sampling_distributions/05.04_student_t_distribution.tex) ([PDF](en/05_sampling_distributions/05.04_student_t_distribution.pdf)) | `05.04_student_t_distribution.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings)** |
| **05.05** | [05.05 $F$ de Fisher-Snedecor](es/05_distribuciones_muestreo/05.05_fisher_f_distribution.tex) ([PDF](es/05_distribuciones_muestreo/05.05_fisher_f_distribution.pdf)) | [05.05 Fisher-Snedecor F-Distribution](en/05_sampling_distributions/05.05_fisher_f_distribution.tex) ([PDF](en/05_sampling_distributions/05.05_fisher_f_distribution.pdf)) | `05.05_fisher_f_distribution.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 05** |

---

## 5d. Catálogo e Índice de Presentaciones --- Capítulo 06 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 5 / Capítulo 06: Estimación y su Relación con Ciencia de Datos**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/06_estimacion_estadistica/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **06.01** | [06.01 Calidad de Estimadores](es/06_estimacion_estadistica/06.01_point_estimation_quality.tex) ([PDF](es/06_estimacion_estadistica/06.01_point_estimation_quality.pdf)) | [06.01 Point Estimation Quality](en/06_estimation_data_science/06.01_point_estimation_quality.tex) ([PDF](en/06_estimation_data_science/06.01_point_estimation_quality.pdf)) | `06.01_point_estimation_quality.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 06** |
| **06.02** | [06.02 Método de Momentos](es/06_estimacion_estadistica/06.02_method_of_moments.tex) ([PDF](es/06_estimacion_estadistica/06.02_method_of_moments.pdf)) | [06.02 Method of Moments](en/06_estimation_data_science/06.02_method_of_moments.tex) ([PDF](en/06_estimation_data_science/06.02_method_of_moments.pdf)) | `06.02_method_of_moments.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings)** |
| **06.03** | [06.03 MLE y Score](es/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.tex) ([PDF](es/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.pdf)) | [06.03 MLE and Score](en/06_estimation_data_science/06.03_maximum_likelihood_estimation.tex) ([PDF](en/06_estimation_data_science/06.03_maximum_likelihood_estimation.pdf)) | `06.03_maximum_likelihood_estimation.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings)** |
| **06.04** | [06.04 IC para Medias](es/06_estimacion_estadistica/06.04_confidence_intervals_means.tex) ([PDF](es/06_estimacion_estadistica/06.04_confidence_intervals_means.pdf)) | [06.04 Confidence Intervals for Means](en/06_estimation_data_science/06.04_confidence_intervals_means.tex) ([PDF](en/06_estimation_data_science/06.04_confidence_intervals_means.pdf)) | `06.04_confidence_intervals_means.py` | $\checkmark$ **Completado (17 diapositivas ES / 19 EN, 0 warnings)** |
| **06.05** | [06.05 IC para Varianzas y Proporciones](es/06_estimacion_estadistica/06.05_confidence_intervals_variances.tex) ([PDF](es/06_estimacion_estadistica/06.05_confidence_intervals_variances.pdf)) | [06.05 Confidence Intervals for Variances and Proportions](en/06_estimation_data_science/06.05_confidence_intervals_variances.tex) ([PDF](en/06_estimation_data_science/06.05_confidence_intervals_variances.pdf)) | `06.05_confidence_intervals_variances.py` | $\checkmark$ **Completado (17 diapositivas ES / 20 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 06** |

---

## 5e. Catálogo e Índice de Presentaciones --- Capítulo 07 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 6 / Capítulo 07: Docimasia (Pruebas de Hipótesis)**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/07_pruebas_hipotesis/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **07.01** | [07.01 Fundamentos de Docimasia](es/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.tex) ([PDF](es/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.pdf)) | [07.01 Hypothesis Testing Foundations](en/07_hypothesis_testing/07.01_hypothesis_testing_basics.tex) ([PDF](en/07_hypothesis_testing/07.01_hypothesis_testing_basics.pdf)) | `07.01_hypothesis_testing_basics.py` | $\checkmark$ **Completado (17 diapositivas ES / 17 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 07** |
| **07.02** | [07.02 Pruebas $Z$/$t$ para Medias](es/07_pruebas_hipotesis/07.02_z_t_tests_means.tex) ([PDF](es/07_pruebas_hipotesis/07.02_z_t_tests_means.pdf)) | [07.02 Z/t Tests for Means](en/07_hypothesis_testing/07.02_z_t_tests_means.tex) ([PDF](en/07_hypothesis_testing/07.02_z_t_tests_means.pdf)) | `07.02_z_t_tests_means.py` | $\checkmark$ **Completado (17 diapositivas ES / 17 EN, 0 warnings)** |
| **07.03** | [07.03 Bondad de Ajuste $\chi^2$](es/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.tex) ([PDF](es/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.pdf)) | [07.03 Chi-Squared Goodness-of-Fit](en/07_hypothesis_testing/07.03_goodness_of_fit_tests.tex) ([PDF](en/07_hypothesis_testing/07.03_goodness_of_fit_tests.pdf)) | `07.03_goodness_of_fit_tests.py` | $\checkmark$ **Completado (17 diapositivas ES / 17 EN, 0 warnings)** |
| **07.04** | [07.04 Contingencia e Independencia](es/07_pruebas_hipotesis/07.04_contingency_tables.tex) ([PDF](es/07_pruebas_hipotesis/07.04_contingency_tables.pdf)) | [07.04 Contingency Tables and Independence](en/07_hypothesis_testing/07.04_contingency_tables.tex) ([PDF](en/07_hypothesis_testing/07.04_contingency_tables.pdf)) | `07.04_contingency_tables.py` | $\checkmark$ **Completado (17 diapositivas ES / 17 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 07** |

---

## 5f. Catálogo e Índice de Presentaciones --- Capítulo 08 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 7 / Capítulo 08: Elementos de Diseño de Experimentos (ANOVA)**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/08_diseno_experimentos/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **08.01** | [08.01 ANOVA de un Factor](es/08_diseno_experimentos/08.01_one_way_anova.tex) ([PDF](es/08_diseno_experimentos/08.01_one_way_anova.pdf)) | [08.01 One-Way ANOVA](en/08_experimental_design/08.01_one_way_anova.tex) ([PDF](en/08_experimental_design/08.01_one_way_anova.pdf)) | `08.01_one_way_anova.py` | $\checkmark$ **Completado (17 diapositivas ES / 17 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 08** |
| **08.02** | [08.02 Supuestos del ANOVA](es/08_diseno_experimentos/08.02_anova_assumptions.tex) ([PDF](es/08_diseno_experimentos/08.02_anova_assumptions.pdf)) | [08.02 ANOVA Assumptions](en/08_experimental_design/08.02_anova_assumptions.tex) ([PDF](en/08_experimental_design/08.02_anova_assumptions.pdf)) | `08.02_anova_assumptions.py` | $\checkmark$ **Completado (17 diapositivas ES / 17 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 08** |

---

## 5g. Catálogo e Índice de Presentaciones --- Capítulo 09 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes al **Tema complementario / Capítulo 09: Regresiones Lineales y Múltiples**. No constituye una Unidad 8 del programa oficial: las siete unidades oficiales corresponden a los capítulos 02–08. Una versión anterior de este capítulo agrupó 7 archivos de teoría en una sola sección 09.01; se corrigió a la estructura 1:1 de 12 secciones que se muestra abajo (detalle completo en `ROADMAP.md`).

| Sección | Título en Español | Título en Inglés | Script Python (en `code/09_regresiones/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **09.01** | [09.01 Correlación](es/09_regresiones/09.01_correlation.tex) ([PDF](es/09_regresiones/09.01_correlation.pdf)) | [09.01 Correlation](en/09_regressions/09.01_correlation.tex) ([PDF](en/09_regressions/09.01_correlation.pdf)) | `09.01_correlation.py` | $\checkmark$ **Completado (15 diapositivas ES / 15 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 09** |
| **09.02** | [09.02 Introducción a la Regresión](es/09_regresiones/09.02_introduction_to_regression.tex) ([PDF](es/09_regresiones/09.02_introduction_to_regression.pdf)) | [09.02 Introduction to Regression](en/09_regressions/09.02_introduction_to_regression.tex) ([PDF](en/09_regressions/09.02_introduction_to_regression.pdf)) | `09.02_introduction_to_regression.py` | $\checkmark$ **Completado (15 diapositivas ES / 15 EN, 0 warnings)** |
| **09.03** | [09.03 Matemáticas de la Regresión](es/09_regresiones/09.03_mathematics_of_regression.tex) ([PDF](es/09_regresiones/09.03_mathematics_of_regression.pdf)) | [09.03 Mathematics of Regression](en/09_regressions/09.03_mathematics_of_regression.tex) ([PDF](en/09_regressions/09.03_mathematics_of_regression.pdf)) | `09.03_mathematics_of_regression.py` | $\checkmark$ **Completado (19 diapositivas ES / 19 EN, 0 warnings)** |
| **09.04** | [09.04 Regresión sobre Datos Simulados](es/09_regresiones/09.04_regression_on_simulated_data.tex) ([PDF](es/09_regresiones/09.04_regression_on_simulated_data.pdf)) | [09.04 Regression on Simulated Data](en/09_regressions/09.04_regression_on_simulated_data.tex) ([PDF](en/09_regressions/09.04_regression_on_simulated_data.pdf)) | `09.04_regression_on_simulated_data.py` | $\checkmark$ **Completado (13 diapositivas ES / 13 EN, 0 warnings)** |
| **09.05** | [09.05 Coeficientes Óptimos](es/09_regresiones/09.05_optimal_coefficients_and_tests.tex) ([PDF](es/09_regresiones/09.05_optimal_coefficients_and_tests.pdf)) | [09.05 Optimal Coefficients](en/09_regressions/09.05_optimal_coefficients_and_tests.tex) ([PDF](en/09_regressions/09.05_optimal_coefficients_and_tests.pdf)) | `09.05_optimal_coefficients_and_tests.py` | $\checkmark$ **Completado (16 diapositivas ES / 16 EN, 0 warnings)** |
| **09.06** | [09.06 Implementación con statsmodels](es/09_regresiones/09.06_implementation_with_statsmodels.tex) ([PDF](es/09_regresiones/09.06_implementation_with_statsmodels.pdf)) | [09.06 Implementation with statsmodels](en/09_regressions/09.06_implementation_with_statsmodels.tex) ([PDF](en/09_regressions/09.06_implementation_with_statsmodels.pdf)) | `09.06_statsmodels_style_summary.py` | $\checkmark$ **Completado (13 diapositivas ES / 13 EN, 0 warnings)** |
| **09.07** | [09.07 Regresión Lineal Múltiple](es/09_regresiones/09.07_multiple_linear_regression.tex) ([PDF](es/09_regresiones/09.07_multiple_linear_regression.pdf)) | [09.07 Multiple Linear Regression](en/09_regressions/09.07_multiple_linear_regression.tex) ([PDF](en/09_regressions/09.07_multiple_linear_regression.pdf)) | `09.07_multiple_linear_regression.py` | $\checkmark$ **Completado (21 diapositivas ES / 21 EN, 0 warnings)** |
| **09.08** | [09.08 Validación de Modelos](es/09_regresiones/09.08_model_validation.tex) ([PDF](es/09_regresiones/09.08_model_validation.pdf)) | [09.08 Model Validation](en/09_regressions/09.08_model_validation.tex) ([PDF](en/09_regressions/09.08_model_validation.pdf)) | `09.08_model_validation.py` | $\checkmark$ **Completado (13 diapositivas ES / 13 EN, 0 warnings)** |
| **09.09** | [09.09 Diagnóstico de Regresión](es/09_regresiones/09.09_regression_diagnostics.tex) ([PDF](es/09_regresiones/09.09_regression_diagnostics.pdf)) | [09.09 Regression Diagnostics](en/09_regressions/09.09_regression_diagnostics.tex) ([PDF](en/09_regressions/09.09_regression_diagnostics.pdf)) | `09.09_regression_diagnostics.py` | $\checkmark$ **Completado (21 diapositivas ES / 21 EN, 0 warnings)** |
| **09.10** | [09.10 Regresión con scikit-learn](es/09_regresiones/09.10_scikit_learn_regression.tex) ([PDF](es/09_regresiones/09.10_scikit_learn_regression.pdf)) | [09.10 Regression with scikit-learn](en/09_regressions/09.10_scikit_learn_regression.tex) ([PDF](en/09_regressions/09.10_scikit_learn_regression.pdf)) | `09.10_scikit_learn_regression.py` | $\checkmark$ **Completado (20 diapositivas ES / 20 EN, 0 warnings)** |
| **09.11** | [09.11 Variables Categóricas y Muda](es/09_regresiones/09.11_categorical_dummy_variables.tex) ([PDF](es/09_regresiones/09.11_categorical_dummy_variables.pdf)) | [09.11 Categorical and Dummy Variables](en/09_regressions/09.11_categorical_dummy_variables.tex) ([PDF](en/09_regressions/09.11_categorical_dummy_variables.pdf)) | `09.11_categorical_dummy_variables.py` | $\checkmark$ **Completado (20 diapositivas ES / 20 EN, 0 warnings)** |
| **09.12** | [09.12 Transformaciones No Lineales](es/09_regresiones/09.12_nonlinear_polynomial_regression.tex) ([PDF](es/09_regresiones/09.12_nonlinear_polynomial_regression.pdf)) | [09.12 Nonlinear Transformations](en/09_regressions/09.12_nonlinear_polynomial_regression.tex) ([PDF](en/09_regressions/09.12_nonlinear_polynomial_regression.pdf)) | `09.12_nonlinear_polynomial_regression.py` | $\checkmark$ **Completado (19 diapositivas ES / 19 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 09** |

---

## 6. Próximo Trabajo y Hoja de Ruta (`ROADMAP.md`)

Los Capítulos 04 (Variables Aleatorias Continuas), 05 (Distribuciones de Muestreo), 06 (Estimación y su Relación con Ciencia de Datos), 07 (Docimasia --- Pruebas de Hipótesis), 08 (Elementos de Diseño de Experimentos --- ANOVA) y 09 (Regresiones Lineales y Múltiples) están 100% completos. El Capítulo 09 quedó estructurado en 12 secciones 1:1 con sus archivos de teoría fuente (09.01 Correlación hasta 09.12 Transformaciones No Lineales y Regresión Polinomial), tras corregir una discrepancia estructural documentada antes del 2026-07-23 (ver nota en la Sección 5g arriba y el detalle completo en `ROADMAP.md`). Para conocer el estado detallado de cada sección y el trabajo pendiente en capítulos futuros, consulta el documento oficial de planificación:
👉 **[presentaciones/ROADMAP.md](ROADMAP.md)**.
