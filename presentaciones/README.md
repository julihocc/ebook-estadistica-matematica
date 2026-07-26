# Presentaciones Beamer & Laboratorios de Simulación en Python

Este directorio (`presentaciones/`) contiene las presentaciones interactivas en **LaTeX Beamer** (español e inglés) y los **laboratorios computacionales en Python** complementarios para las clases del libro digital *Modelación Estadística*.

Esta guía constituye el **manual operativo estándar y 100% reproducible** para cualquier agente de inteligencia artificial (o colaborador humano) que trabaje en la creación, modificación, verificación o mantenimiento de las presentaciones y scripts de este proyecto.

### Estado de reconciliación verificado al 2026-07-26 14:24:55 -06:00

- El espejo de cuadernos del libro está cerrado desde el `2026-07-23 11:03:37 -06:00`: existen 60 archivos `(p).tex` ES y 60 contrapartes `en_*(p).tex`, con seis problemas Bloom, seis soluciones y etiquetas hash compartidas por par.
- La matriz canónica de notas ES define el inventario objetivo de 72 secciones activas y un mazo ES por sección; las secciones de problemas quedan fuera de las presentaciones. El detalle está en `docs/matriz-notas-presentaciones-es.md`.
- Verificación física completada el `2026-07-24 11:35:16 -06:00`: hay
  exactamente 72 mazos ES vivos y 8 mazos legado archivados.
- La sincronización de los 21 mazos EN que quedaban parciales quedó cerrada en
  este corte: las 72 filas activas tienen paridad estructural de frames y
  `\lstinputlisting` con su mazo ES. Los 21 mazos EN modificados pasaron doble
  compilación sin errores, referencias indefinidas ni desbordamientos.
- El capítulo 2 usa `02.00_introduccion_probabilidad` y `02.01`–`02.06`, incluyendo los temas promovidos de Fundamentos, Técnicas de conteo y Bayes.
- Los mazos ES se basan en ejemplos y soluciones ya resueltos de teoría; no deben contener bloques `Ejercicio en Clase`, `Problema X.Y.Z`, etiquetas `prob:` ni referencias a `(p)`.
- El piloto `02.03 Técnicas de conteo` queda desarrollado en ES/EN con 22 frames por mazo y doble compilación sin errores ni desbordamientos. No modifica las notas, los archivos `(p)` ni `presentaciones/code/`; sí añade la contraparte EN del piloto.
- El bloque del capítulo 5 (filas 24--26 y 32--33 de la matriz) queda
  desarrollado en ES/EN: cinco pares de mazos, 22 frames por idioma y cero
  listings. Las notas EN de las secciones `section*` correspondientes quedaron
  normalizadas; no se modificaron los archivos `(p)` ni se añadió Python.
- El bloque del capítulo 6 (filas 35, 37, 38 y 40) queda desarrollado en ES/EN:
  cuatro pares de 22 frames, sin listings ni scripts nuevos. La fila 38 ahora
  tiene un mazo EN propio de proporciones; deja de depender del mazo compartido
  de varianzas.
- El bloque del capítulo 7 (filas 42--45, 47--48 y 51--52) queda desarrollado
  en ES/EN: ocho pares de 22 frames, sin listings ni scripts nuevos. La guía EN
  de la fila 45 quedó normalizada a `section*`/`subsection*` para igualar la
  fuente ES. Los logs de contenido no reportan errores, referencias indefinidas,
  etiquetas duplicadas ni desbordamientos; la advertencia de `vbox` restante
  corresponde únicamente a la portada exenta.
- El bloque del capítulo 8 (filas 53, 55--56 y 58--59) queda desarrollado en
  ES/EN: cinco pares de 22 frames, sin listings ni scripts nuevos. Se alinearon
  las secciones y etiquetas EN de efectos de modelo fijo y de bloques; los logs
  de contenido no reportan errores, referencias indefinidas, etiquetas duplicadas
  ni desbordamientos; la advertencia de `vbox` restante corresponde únicamente
  a la portada exenta.
- El bloque del capítulo 9 (filas 62 y 70) queda desarrollado en ES/EN: dos
  pares de 22 frames, sin listings ni scripts nuevos. No se modificaron las
  notas porque ya coincidían estructuralmente; los logs de contenido no reportan
  errores, referencias indefinidas, etiquetas duplicadas ni desbordamientos; la
  advertencia de `vbox` restante corresponde únicamente a la portada exenta.
- La auditoría final encontró y corrigió la única excepción restante: la fila 23
  (Función generadora de momentos) tenía un esqueleto ES y no tenía ruta EN. Ahora
  tiene dos mazos de 22 frames; la ruta EN es `04.08_moment_generating_function`
  para no colisionar con el mazo EN `04.06_exponential_distribution`.
- Las filas 4--6 de las notas EN y sus presentaciones quedaron normalizadas:
  la introducción usa `02.00` sin numerar, conjuntos usa etiquetas `2.1.*` y
  fundamentos usa etiquetas `2.2.*`.
 - Las filas 11, 12 y 16 de las notas EN y sus mazos ya están sincronizadas; las
   diferencias restantes pertenecen a otros mazos EN parciales.
- La fila 18 de las notas EN y su presentación EN conservan la jerarquía y las
  47 etiquetas de ES, con paridad de frames verificada.
- La fila 36 de las notas EN tiene una sola sección y las dos etiquetas de ES;
  su presentación EN quedó en paridad de frames.
- La normalización de notas y presentaciones EN queda cerrada en **72/72
  filas**: no quedan diferencias estructurales frente a ES.
- El primer grupo de mazos EN sincronizado comprende conjuntos y fundamentos:
  ambos pares tienen ahora la misma cantidad de frames y listings que ES y no
  contienen ejercicios heredados. Los cuatro mazos compilaron dos veces sin
  errores ni `Overfull \\hbox`; los avisos de `vbox` se limitan a portadas EN.
 - El segundo grupo del capítulo 2 (condicional, Bayes y muestreo) también quedó
   en paridad exacta de frames y listings con ES. Se retiraron los ejercicios
   heredados; los seis mazos compilaron dos veces sin errores ni `Overfull
   \\hbox`.
 - El primer grupo del capítulo 3 (filas 11, 12 y 16) quedó sincronizado en
   ES/EN: PMF y soporte (14 frames), Bernoulli/binomial (14 frames) y Poisson
   (17 frames), con tres listings compartidos por par. Se retiraron ejercicios
   heredados; los seis mazos compilaron dos veces sin errores, referencias
   indefinidas, etiquetas duplicadas ni desbordamientos de contenido. Solo
   quedaron avisos `vbox` de portada EN; no se modificaron las notas, Python ni
   archivos `(p)`.
 - El segundo grupo del capítulo 3 (filas 13--15 y 17) quedó sincronizado en
   ES/EN: multinomial (14 frames), geométrica/binomial negativa (14),
   hipergeométrica (16) y distribuciones discretas para ciencia de datos (15),
   siempre con tres listings por par. Los ocho mazos compilaron dos veces sin
   errores, referencias indefinidas, etiquetas duplicadas ni desbordamientos de
   contenido; los avisos `vbox` se limitan a portadas EN. No se modificaron
   notas, Python ni archivos `(p)`.
 - El capítulo 1 (filas 1--3) quedó sincronizado en ES/EN: introducción (10
   frames), tendencia central (13) y dispersión (14), con 1, 2 y 2 listings por
   par. Se retiraron ejercicios heredados, se añadieron declaraciones de clase
   ausentes y se compactaron frames EN; los seis mazos compilaron dos veces sin
   errores ni desbordamientos de contenido. Solo quedan avisos `vbox` de
   portada EN; no se modificaron notas, Python ni archivos `(p)`.
 - El capítulo 4 (filas 18--22) quedó sincronizado en ES/EN: PDF y soporte,
   esperanza y varianza, uniforme, normal y gamma/beta/Weibull, con 15 frames y
   3 listings por par. Se retiraron ejercicios heredados y se añadieron los
   desarrollos teóricos faltantes; los diez mazos compilaron dos veces sin
   errores ni desbordamientos de contenido. Solo quedan avisos `vbox` de
   portadas EN; no se modificaron notas, Python ni archivos `(p)`.

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
│       ├── 02.00_introduccion_probabilidad.tex (.pdf)
│       ├── 02.01_conjuntos_y_particiones.tex (.pdf)
│       ├── 02.02_fundamentos_probabilidad.tex (.pdf)
│       ├── 02.03_tecnicas_de_conteo.tex (.pdf)
│       ├── 02.04_probabilidad_condicional.tex (.pdf)
│       ├── 02.05_teorema_bayes.tex (.pdf)
│       └── 02.06_muestreo_aleatorio.tex (.pdf)
└── en/                             ← Presentaciones en inglés (p. ej. en/02_probability_theory/)
    └── 02_probability_theory/
        ├── 02.01_probability_introduction.tex (.pdf)
        ├── 02.02_sets_and_partitions.tex (.pdf)
        ├── 02.03_probability_foundations.tex (.pdf)
        ├── 02.03_counting_techniques.tex (.pdf)
        ├── 02.04_conditional_probability.tex (.pdf)
        ├── 02.05_bayes_theorem.tex (.pdf)
        └── 02.06_random_sampling.tex (.pdf)
```

---

## 2. Las 4 Reglas de Oro del Flujo de Trabajo

### Regla 1: Código de Python Unificado en Inglés (Una Sola Fuente de la Verdad)
- **Prohibido duplicar código:** No se permite crear archivos de simulación independientes en español o por idioma (`*.es.py`, scripts separados en carpetas de idioma, etc.).
- Todo script computacional del proyecto **debe estar redactado exclusivamente en inglés** (comentarios, variables, salidas por consola y docstrings en inglés) y debe ubicarse en `presentaciones/code/<unidad>/<ID>_<nombre_en_ingles>.py`.
- **Librerías permitidas:** Python estándar y `numpy` / `scipy`; la única excepción es `scikit-learn` en el laboratorio 09.10, dedicado a esa biblioteca. No se permiten dependencias gráficas como `matplotlib` ni otras librerías que bloqueen la compilación o la ejecución en terminal.
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

A continuación se presenta el estado finalizado y verificado de las 7 secciones de trabajo correspondientes a la **Unidad 1 / Capítulo 02: Teoría de la Probabilidad** (incluida la introducción sin numerar):

| Sección | Título en Español | Título en Inglés | Script Python (en `code/02_teoria_probabilidad/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **02.00** | [Introducción a la probabilidad](es/02_teoria_probabilidad/02.00_introduccion_probabilidad.tex) ([PDF](es/02_teoria_probabilidad/02.00_introduccion_probabilidad.pdf)) | [Intro to Probability](en/02_probability_theory/02.01_probability_introduction.tex) ([PDF](en/02_probability_theory/02.01_probability_introduction.pdf)) | Sin script dedicado | Completado ES/EN — 9 frames cada uno |
| **02.01** | [Conjuntos y particiones](es/02_teoria_probabilidad/02.01_conjuntos_y_particiones.tex) ([PDF](es/02_teoria_probabilidad/02.01_conjuntos_y_particiones.pdf)) | [Sets and Partitions](en/02_probability_theory/02.02_sets_and_partitions.tex) ([PDF](en/02_probability_theory/02.02_sets_and_partitions.pdf)) | Sin script dedicado | Completado ES/EN — 14 frames, 4 listings |
| **02.02** | [Fundamentos de probabilidad](es/02_teoria_probabilidad/02.02_fundamentos_probabilidad.tex) ([PDF](es/02_teoria_probabilidad/02.02_fundamentos_probabilidad.pdf)) | [Probability Fundamentals](en/02_probability_theory/02.03_probability_foundations.tex) ([PDF](en/02_probability_theory/02.03_probability_foundations.pdf)) | Sin script dedicado | Completado ES/EN — 16 frames, 3 listings |
| **02.03** | [Técnicas de conteo](es/02_teoria_probabilidad/02.03_tecnicas_de_conteo.tex) ([PDF](es/02_teoria_probabilidad/02.03_tecnicas_de_conteo.pdf)) | [Counting Techniques](en/02_probability_theory/02.03_counting_techniques.tex) ([PDF](en/02_probability_theory/02.03_counting_techniques.pdf)) | Sin script dedicado; usa aritmética exacta en las diapositivas | Completado ES/EN — 22 frames cada uno |
| **02.04** | [Probabilidad condicional](es/02_teoria_probabilidad/02.04_probabilidad_condicional.tex) ([PDF](es/02_teoria_probabilidad/02.04_probabilidad_condicional.pdf)) | [Conditional Probability](en/02_probability_theory/02.04_conditional_probability.tex) ([PDF](en/02_probability_theory/02.04_conditional_probability.pdf)) | Sin script dedicado | Completado ES/EN — 16 frames, 4 listings |
| **02.05** | [Teorema de Bayes](es/02_teoria_probabilidad/02.05_teorema_bayes.tex) ([PDF](es/02_teoria_probabilidad/02.05_teorema_bayes.pdf)) | [Bayes Theorem](en/02_probability_theory/02.05_bayes_theorem.tex) ([PDF](en/02_probability_theory/02.05_bayes_theorem.pdf)) | Sin script dedicado | Completado ES/EN — 14 frames, 3 listings |
| **02.06** | [Muestreo aleatorio](es/02_teoria_probabilidad/02.06_muestreo_aleatorio.tex) ([PDF](es/02_teoria_probabilidad/02.06_muestreo_aleatorio.pdf)) | [Random Sampling](en/02_probability_theory/02.06_random_sampling.tex) ([PDF](en/02_probability_theory/02.06_random_sampling.pdf)) | Sin script dedicado | Completado ES/EN — 14 frames, 3 listings |

---

## 5. Catálogo e Índice de Presentaciones --- Capítulo 03 (100% Completado)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 2 / Capítulo 03: Variables Aleatorias Discretas**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/03_variables_aleatorias_discretas/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **03.01** | [03.01 PMF y Soporte](es/03_variables_aleatorias_discretas/03.01_pmf_y_soporte.tex) ([PDF](es/03_variables_aleatorias_discretas/03.01_pmf_y_soporte.pdf)) | [03.01 PMF and Support](en/03_discrete_random_variables/03.01_pmf_and_support.tex) ([PDF](en/03_discrete_random_variables/03.01_pmf_and_support.pdf)) | `03.01_pmf_and_support.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **03.02** | [Mazo ES archivado](../archive/presentaciones-es/03_variables_aleatorias_discretas/03.02_cdf_discreta.tex) | [03.02 Discrete CDF (legado EN)](en/03_discrete_random_variables/03.02_discrete_cdf.tex) | 03.02_discrete_cdf.py | **Archivado: no es sección activa de las notas ES** |
| **03.03** | [Mazo ES archivado](../archive/presentaciones-es/03_variables_aleatorias_discretas/03.03_esperanza_y_varianza.tex) | [03.03 Expectation & Variance (legado EN)](en/03_discrete_random_variables/03.03_expectation_and_variance.tex) | 03.03_expectation_and_variance.py | **Archivado: no es sección activa de las notas ES** |
| **03.04** | [03.04 Bernoulli y Binomial](es/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.tex) ([PDF](es/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.pdf)) | [03.04 Bernoulli & Binomial](en/03_discrete_random_variables/03.04_bernoulli_binomial.tex) ([PDF](en/03_discrete_random_variables/03.04_bernoulli_binomial.pdf)) | `03.04_bernoulli_binomial.py` | $\checkmark$ **Completado** |
| **03.05** | [03.05 Geométrica y Binomial Negativa](es/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.tex) ([PDF](es/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.pdf)) | [03.05 Geometric & Negative Binomial](en/03_discrete_random_variables/03.05_geometric_negative_binomial.tex) ([PDF](en/03_discrete_random_variables/03.05_geometric_negative_binomial.pdf)) | `03.05_geometric_negative_binomial.py` | $\checkmark$ **Completado** |
| **03.06** | [03.06 Hipergeométrica](es/03_variables_aleatorias_discretas/03.06_hipergeometrica.tex) ([PDF](es/03_variables_aleatorias_discretas/03.06_hipergeometrica.pdf)) | [03.06 Hypergeometric](en/03_discrete_random_variables/03.06_hypergeometric.tex) ([PDF](en/03_discrete_random_variables/03.06_hypergeometric.pdf)) | `03.06_hypergeometric.py` | $\checkmark$ **Completado** |
| **03.07** | [03.07 Poisson](es/03_variables_aleatorias_discretas/03.07_poisson_distribution.tex) ([PDF](es/03_variables_aleatorias_discretas/03.07_poisson_distribution.pdf)) | [03.07 Poisson Distribution](en/03_discrete_random_variables/03.07_poisson_distribution.tex) ([PDF](en/03_discrete_random_variables/03.07_poisson_distribution.pdf)) | `03.07_poisson_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **03.08** | [03.08 Multinomial](es/03_variables_aleatorias_discretas/03.08_multinomial_distribution.tex) ([PDF](es/03_variables_aleatorias_discretas/03.08_multinomial_distribution.pdf)) | [03.08 Multinomial Distribution](en/03_discrete_random_variables/03.08_multinomial_distribution.tex) ([PDF](en/03_discrete_random_variables/03.08_multinomial_distribution.pdf)) | `03.08_multinomial_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **03.09** | [Mazo ES archivado](../archive/presentaciones-es/03_variables_aleatorias_discretas/03.09_normal_approximation.tex) | [03.09 Normal Distribution (legado EN)](en/03_discrete_random_variables/03.09_normal_approximation.tex) | 03.09_normal_approximation.py | **Archivado: aproximación subsumida en la teoría activa** |
| **03.10** | [03.10 Discretas en Ciencia de Datos](es/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.tex) ([PDF](es/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.pdf)) | [03.10 Discrete Distributions in Data Science](en/03_discrete_random_variables/03.10_discrete_distributions_data_science.tex) ([PDF](en/03_discrete_random_variables/03.10_discrete_distributions_data_science.pdf)) | `03.10_discrete_distributions_data_science.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 03** |

---

## 5b. Catálogo e Índice de Presentaciones --- Capítulo 04 (catálogo histórico)

### Correspondencia activa corregida — corte 2026-07-24 15:58:15 -06:00

| Fila | Sección ES | Mazo EN | Estado |
| :---: | :--- | :--- | :---: |
| 23 | [04.06 Función generadora de momentos](es/04_variables_aleatorias_continuas/04.06_moment_generating_function.tex) ([PDF](es/04_variables_aleatorias_continuas/04.06_moment_generating_function.pdf)) | [04.08 Moment-generating function](en/04_continuous_random_variables/04.08_moment_generating_function.tex) ([PDF](en/04_continuous_random_variables/04.08_moment_generating_function.pdf)) | ES/EN completos, 22 frames cada uno |

### Catálogo histórico del capítulo 04

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 3 / Capítulo 04: Variables Aleatorias Continuas**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/04_variables_aleatorias_continuas/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **04.01** | [04.01 PDF y Soporte Continuo](es/04_variables_aleatorias_continuas/04.01_pdf_and_support.tex) ([PDF](es/04_variables_aleatorias_continuas/04.01_pdf_and_support.pdf)) | [04.01 PDF and Continuous Support](en/04_continuous_random_variables/04.01_pdf_and_support.tex) ([PDF](en/04_continuous_random_variables/04.01_pdf_and_support.pdf)) | `04.01_pdf_and_support.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 04** |
| **04.02** | [Mazo ES archivado](../archive/presentaciones-es/04_variables_aleatorias_continuas/04.02_continuous_cdf.tex) | [04.02 Continuous CDF (legado EN)](en/04_continuous_random_variables/04.02_continuous_cdf.tex) | 04.02_continuous_cdf.py | **Archivado: contenido integrado en las secciones activas** |
| **04.03** | [04.03 Esperanza y Varianza Continua](es/04_variables_aleatorias_continuas/04.03_expectation_and_variance.tex) ([PDF](es/04_variables_aleatorias_continuas/04.03_expectation_and_variance.pdf)) | [04.03 Continuous Expectation and Variance](en/04_continuous_random_variables/04.03_expectation_and_variance.tex) ([PDF](en/04_continuous_random_variables/04.03_expectation_and_variance.pdf)) | `04.03_expectation_and_variance.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.04** | [04.04 Uniforme Continua](es/04_variables_aleatorias_continuas/04.04_uniform_distribution.tex) ([PDF](es/04_variables_aleatorias_continuas/04.04_uniform_distribution.pdf)) | [04.04 Continuous Uniform Distribution](en/04_continuous_random_variables/04.04_uniform_distribution.tex) ([PDF](en/04_continuous_random_variables/04.04_uniform_distribution.pdf)) | `04.04_uniform_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.05** | [04.05 Normal](es/04_variables_aleatorias_continuas/04.05_normal_distribution.tex) ([PDF](es/04_variables_aleatorias_continuas/04.05_normal_distribution.pdf)) | [04.05 Normal Distribution](en/04_continuous_random_variables/04.05_normal_distribution.tex) ([PDF](en/04_continuous_random_variables/04.05_normal_distribution.pdf)) | `04.05_normal_distribution.py` | $\checkmark$ **Completado (24 diapositivas ES / 20 EN, 0 warnings)** |
| **04.06** | [04.06 Función generadora de momentos](es/04_variables_aleatorias_continuas/04.06_moment_generating_function.tex) ([PDF](es/04_variables_aleatorias_continuas/04.06_moment_generating_function.pdf)) | [04.06 Exponential Distribution (legado EN)](en/04_continuous_random_variables/04.06_exponential_distribution.tex) | — | **Completado ES; el mazo EN conserva una ruta legado** |
| **04.07** | [04.07 Gamma, Beta y Weibull](es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.tex) ([PDF](es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.pdf)) | [04.07 Gamma, Beta, and Weibull Distributions](en/04_continuous_random_variables/04.07_gamma_beta_weibull.tex) ([PDF](en/04_continuous_random_variables/04.07_gamma_beta_weibull.pdf)) | `04.07_gamma_beta_weibull.py` | $\checkmark$ **Completado (23 diapositivas ES / 19 EN, 0 warnings) --- CIERRE DEL CAPÍTULO 04** |

---

## 5c. Catálogo e Índice de Presentaciones --- Capítulo 05 (registro histórico y bloque 1:1)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 4 / Capítulo 05: Distribuciones de Muestreo**:

### Correspondencias activas de las notas ES — corte 2026-07-24 14:51:34 -06:00

Las filas activas y el catálogo histórico que siguen se conservan con su
numeración editorial; la matriz fechada es la autoridad para los conteos
actuales y confirma la paridad de todos los pares.

| Fila | Sección ES | Mazo EN | Estado |
| :---: | :--- | :--- | :---: |
| 24 | [05.00 Introducción inferencial](es/05_distribuciones_muestreo/05.00_introduccion_inferencial.tex) ([PDF](es/05_distribuciones_muestreo/05.00_introduccion_inferencial.pdf)) | [05.00 Inferential Statistics Introduction](en/05_sampling_distributions/05.00_inferential_statistics_introduction.tex) ([PDF](en/05_sampling_distributions/05.00_inferential_statistics_introduction.pdf)) | ES/EN completos, 22 frames cada uno |
| 25 | [05.01 Transformación de variables](es/05_distribuciones_muestreo/05.01_transformacion_variables.tex) ([PDF](es/05_distribuciones_muestreo/05.01_transformacion_variables.pdf)) | [05.01 Variable Transformations](en/05_sampling_distributions/05.01_variable_transformations.tex) ([PDF](en/05_sampling_distributions/05.01_variable_transformations.pdf)) | ES/EN completos, 22 frames cada uno |
| 26 | [05.02 Funciones de variable aleatoria](es/05_distribuciones_muestreo/05.02_distribuciones_funciones.tex) ([PDF](es/05_distribuciones_muestreo/05.02_distribuciones_funciones.pdf)) | [05.02 Distributions of Random-Variable Functions](en/05_sampling_distributions/05.02_distributions_of_random_variable_functions.tex) ([PDF](en/05_sampling_distributions/05.02_distributions_of_random_variable_functions.pdf)) | ES/EN completos, 22 frames cada uno |
| 32 | [05.08 Conceptos fundamentales](es/05_distribuciones_muestreo/05.08_conceptos_estadisticos.tex) ([PDF](es/05_distribuciones_muestreo/05.08_conceptos_estadisticos.pdf)) | [05.08 Fundamental Statistical Concepts](en/05_sampling_distributions/05.08_fundamental_statistical_concepts.tex) ([PDF](en/05_sampling_distributions/05.08_fundamental_statistical_concepts.pdf)) | ES/EN completos, 22 frames cada uno |
| 33 | [05.09 Estadísticos Z y t](es/05_distribuciones_muestreo/05.09_estadisticos_z_t.tex) ([PDF](es/05_distribuciones_muestreo/05.09_estadisticos_z_t.pdf)) | [05.09 Z and t Statistics](en/05_sampling_distributions/05.09_z_and_t_statistics.tex) ([PDF](en/05_sampling_distributions/05.09_z_and_t_statistics.pdf)) | ES/EN completos, 22 frames cada uno |

| Sección | Título en Español | Título en Inglés | Script Python (en `code/05_distribuciones_muestreo/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **05.01** | [05.01 Estadísticos y Varianza Insesgada](es/05_distribuciones_muestreo/05.01_sample_statistics.tex) ([PDF](es/05_distribuciones_muestreo/05.01_sample_statistics.pdf)) | [05.01 Sample Statistics and Unbiased Variance](en/05_sampling_distributions/05.01_sample_statistics.tex) ([PDF](en/05_sampling_distributions/05.01_sample_statistics.pdf)) | `05.01_sample_statistics.py` | $\checkmark$ **Completado (14 frames ES/EN, 3 listings, 0 warnings)** |
| **05.02** | [05.02 TLC Asintótico](es/05_distribuciones_muestreo/05.02_central_limit_theorem.tex) ([PDF](es/05_distribuciones_muestreo/05.02_central_limit_theorem.pdf)) | [05.02 Asymptotic Central Limit Theorem](en/05_sampling_distributions/05.02_central_limit_theorem.tex) ([PDF](en/05_sampling_distributions/05.02_central_limit_theorem.pdf)) | `05.02_central_limit_theorem.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **05.03** | [05.03 Chi-Cuadrada y Varianza Muestral](es/05_distribuciones_muestreo/05.03_chi_squared_distribution.tex) ([PDF](es/05_distribuciones_muestreo/05.03_chi_squared_distribution.pdf)) | [05.03 Chi-Squared Distribution and Sample Variance](en/05_sampling_distributions/05.03_chi_squared_distribution.tex) ([PDF](en/05_sampling_distributions/05.03_chi_squared_distribution.pdf)) | `05.03_chi_squared_distribution.py` | $\checkmark$ **Completado (11 frames ES/EN, 3 listings, 0 warnings)** |
| **05.04** | [05.04 $t$ de Student](es/05_distribuciones_muestreo/05.04_student_t_distribution.tex) ([PDF](es/05_distribuciones_muestreo/05.04_student_t_distribution.pdf)) | [05.04 Student's t-Distribution](en/05_sampling_distributions/05.04_student_t_distribution.tex) ([PDF](en/05_sampling_distributions/05.04_student_t_distribution.pdf)) | `05.04_student_t_distribution.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **05.05** | [05.05 $F$ de Fisher-Snedecor](es/05_distribuciones_muestreo/05.05_fisher_f_distribution.tex) ([PDF](es/05_distribuciones_muestreo/05.05_fisher_f_distribution.pdf)) | [05.05 Fisher-Snedecor F-Distribution](en/05_sampling_distributions/05.05_fisher_f_distribution.tex) ([PDF](en/05_sampling_distributions/05.05_fisher_f_distribution.pdf)) | `05.05_fisher_f_distribution.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |

---

## 5d. Catálogo e Índice de Presentaciones --- Capítulo 06 (registro histórico y bloque 1:1)

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 5 / Capítulo 06: Estimación y su Relación con Ciencia de Datos**:

### Correspondencias activas de las notas ES — corte 2026-07-24 15:07:32 -06:00

| Fila | Sección ES | Mazo EN | Estado |
| :---: | :--- | :--- | :---: |
| 35 | [06.02 Estimación por intervalo](es/06_estimacion_estadistica/06.02_confidence_intervals.tex) ([PDF](es/06_estimacion_estadistica/06.02_confidence_intervals.pdf)) | [06.02 Confidence Intervals](en/06_estimation_data_science/06.02_confidence_intervals.tex) ([PDF](en/06_estimation_data_science/06.02_confidence_intervals.pdf)) | ES/EN completos, 22 frames cada uno |
| 37 | [06.04 Errores estándar](es/06_estimacion_estadistica/06.04_standard_errors.tex) ([PDF](es/06_estimacion_estadistica/06.04_standard_errors.pdf)) | [06.04 Standard Errors](en/06_estimation_data_science/06.04_standard_errors.tex) ([PDF](en/06_estimation_data_science/06.04_standard_errors.pdf)) | ES/EN completos, 22 frames cada uno |
| 38 | [06.05 Estimación de proporciones](es/06_estimacion_estadistica/06.05_confidence_intervals_proportions.tex) ([PDF](es/06_estimacion_estadistica/06.05_confidence_intervals_proportions.pdf)) | [06.05 Proportion Confidence Intervals](en/06_estimation_data_science/06.05_confidence_intervals_proportions.tex) ([PDF](en/06_estimation_data_science/06.05_confidence_intervals_proportions.pdf)) | ES/EN completos, 22 frames cada uno |
| 40 | [06.07 Tamaño de una muestra](es/06_estimacion_estadistica/06.07_sample_size_estimation.tex) ([PDF](es/06_estimacion_estadistica/06.07_sample_size_estimation.pdf)) | [06.07 Sample Size Estimation](en/06_estimation_data_science/06.07_sample_size_estimation.tex) ([PDF](en/06_estimation_data_science/06.07_sample_size_estimation.pdf)) | ES/EN completos, 22 frames cada uno |

El catálogo histórico que sigue conserva laboratorios y mazos previos del
capítulo; la matriz es la autoridad para distinguir las secciones activas.

| Sección | Título en Español | Título en Inglés | Script Python (en `code/06_estimacion_estadistica/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **06.01** | [06.01 Calidad de Estimadores](es/06_estimacion_estadistica/06.01_point_estimation_quality.tex) ([PDF](es/06_estimacion_estadistica/06.01_point_estimation_quality.pdf)) | [06.01 Point Estimation Quality](en/06_estimation_data_science/06.01_point_estimation_quality.tex) ([PDF](en/06_estimation_data_science/06.01_point_estimation_quality.pdf)) | `06.01_point_estimation_quality.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **06.02** | [Mazo ES archivado](../archive/presentaciones-es/06_estimacion_estadistica/06.02_method_of_moments.tex) | [06.02 Method of Moments (legado EN)](en/06_estimation_data_science/06.02_method_of_moments.tex) | 06.02_method_of_moments.py | **Archivado: no es sección activa de las notas ES** |
| **06.03** | [Mazo ES archivado](../archive/presentaciones-es/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.tex) | [06.03 MLE and Score (legado EN)](en/06_estimation_data_science/06.03_maximum_likelihood_estimation.tex) | 06.03_maximum_likelihood_estimation.py | **Archivado: no es sección activa de las notas ES** |
| **06.04** | [06.04 IC para Medias](es/06_estimacion_estadistica/06.04_confidence_intervals_means.tex) ([PDF](es/06_estimacion_estadistica/06.04_confidence_intervals_means.pdf)) | [06.04 Confidence Intervals for Means](en/06_estimation_data_science/06.04_confidence_intervals_means.tex) ([PDF](en/06_estimation_data_science/06.04_confidence_intervals_means.pdf)) | `06.04_confidence_intervals_means.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **06.05** | [06.05 IC para Varianzas y Proporciones](es/06_estimacion_estadistica/06.05_confidence_intervals_variances.tex) ([PDF](es/06_estimacion_estadistica/06.05_confidence_intervals_variances.pdf)) | [06.05 Confidence Intervals for Variances and Proportions](en/06_estimation_data_science/06.05_confidence_intervals_variances.tex) ([PDF](en/06_estimation_data_science/06.05_confidence_intervals_variances.pdf)) | `06.05_confidence_intervals_variances.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |

---

## 5e. Catálogo e Índice de Presentaciones --- Capítulo 07 (catálogo histórico)

### Correspondencias activas de las notas ES — corte 2026-07-24 15:24:57 -06:00

El bloque activo de esta etapa cubre las filas 42--45, 47--48 y 51--52 de la
matriz. Cada par ES/EN tiene 22 frames, cero listings y doble compilación
exitosa; el catálogo histórico de 07.01--07.04 que sigue se conserva sin
renumerarlo.

| Fila | Sección ES | Mazo EN | Estado |
| :---: | :--- | :--- | :---: |
| 42 | [07.02 IC y pruebas](es/07_pruebas_hipotesis/07.02_ci_hypothesis_tests.tex) ([PDF](es/07_pruebas_hipotesis/07.02_ci_hypothesis_tests.pdf)) | [07.02 CI and hypothesis tests](en/07_hypothesis_testing/07.02_ci_hypothesis_tests.tex) ([PDF](en/07_hypothesis_testing/07.02_ci_hypothesis_tests.pdf)) | ES/EN completos, 22 frames cada uno |
| 43 | [07.03 Valores p](es/07_pruebas_hipotesis/07.03_p_values_decisions.tex) ([PDF](es/07_pruebas_hipotesis/07.03_p_values_decisions.pdf)) | [07.03 p-values and decisions](en/07_hypothesis_testing/07.03_p_values_decisions.tex) ([PDF](en/07_hypothesis_testing/07.03_p_values_decisions.pdf)) | ES/EN completos, 22 frames cada uno |
| 44 | [07.04 Prueba t para una media](es/07_pruebas_hipotesis/07.04_one_mean_test.tex) ([PDF](es/07_pruebas_hipotesis/07.04_one_mean_test.pdf)) | [07.04 One-mean t test](en/07_hypothesis_testing/07.04_one_mean_test.tex) ([PDF](en/07_hypothesis_testing/07.04_one_mean_test.pdf)) | ES/EN completos, 22 frames cada uno |
| 45 | [07.05 Guía de pruebas](es/07_pruebas_hipotesis/07.05_hypothesis_testing_guide.tex) ([PDF](es/07_pruebas_hipotesis/07.05_hypothesis_testing_guide.pdf)) | [07.05 Hypothesis testing guide](en/07_hypothesis_testing/07.05_hypothesis_testing_guide.tex) ([PDF](en/07_hypothesis_testing/07.05_hypothesis_testing_guide.pdf)) | ES/EN completos, 22 frames cada uno |
| 47 | [07.07 Pruebas de proporciones](es/07_pruebas_hipotesis/07.07_proportion_tests.tex) ([PDF](es/07_pruebas_hipotesis/07.07_proportion_tests.pdf)) | [07.07 Proportion tests](en/07_hypothesis_testing/07.07_proportion_tests.tex) ([PDF](en/07_hypothesis_testing/07.07_proportion_tests.pdf)) | ES/EN completos, 22 frames cada uno |
| 48 | [07.08 Pruebas de varianzas](es/07_pruebas_hipotesis/07.08_variance_tests.tex) ([PDF](es/07_pruebas_hipotesis/07.08_variance_tests.pdf)) | [07.08 Variance tests](en/07_hypothesis_testing/07.08_variance_tests.tex) ([PDF](en/07_hypothesis_testing/07.08_variance_tests.pdf)) | ES/EN completos, 22 frames cada uno |
| 51 | [07.11 Pruebas de homogeneidad](es/07_pruebas_hipotesis/07.11_homogeneity_tests.tex) ([PDF](es/07_pruebas_hipotesis/07.11_homogeneity_tests.pdf)) | [07.11 Homogeneity tests](en/07_hypothesis_testing/07.11_homogeneity_tests.tex) ([PDF](en/07_hypothesis_testing/07.11_homogeneity_tests.pdf)) | ES/EN completos, 22 frames cada uno |
| 52 | [07.12 Pruebas de varias proporciones](es/07_pruebas_hipotesis/07.12_multiple_proportions.tex) ([PDF](es/07_pruebas_hipotesis/07.12_multiple_proportions.pdf)) | [07.12 Multiple-proportion tests](en/07_hypothesis_testing/07.12_multiple_proportions.tex) ([PDF](en/07_hypothesis_testing/07.12_multiple_proportions.pdf)) | ES/EN completos, 22 frames cada uno |

### Catálogo histórico del capítulo 07

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 6 / Capítulo 07: Docimasia (Pruebas de Hipótesis)**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/07_pruebas_hipotesis/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **07.01** | [07.01 Fundamentos de Docimasia](es/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.tex) ([PDF](es/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.pdf)) | [07.01 Hypothesis Testing Foundations](en/07_hypothesis_testing/07.01_hypothesis_testing_basics.tex) ([PDF](en/07_hypothesis_testing/07.01_hypothesis_testing_basics.pdf)) | `07.01_hypothesis_testing_basics.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **07.02** | [07.02 Pruebas $Z$/$t$ para Medias](es/07_pruebas_hipotesis/07.02_z_t_tests_means.tex) ([PDF](es/07_pruebas_hipotesis/07.02_z_t_tests_means.pdf)) | [07.02 Z/t Tests for Means](en/07_hypothesis_testing/07.02_z_t_tests_means.tex) ([PDF](en/07_hypothesis_testing/07.02_z_t_tests_means.pdf)) | `07.02_z_t_tests_means.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **07.03** | [07.03 Bondad de Ajuste $\chi^2$](es/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.tex) ([PDF](es/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.pdf)) | [07.03 Chi-Squared Goodness-of-Fit](en/07_hypothesis_testing/07.03_goodness_of_fit_tests.tex) ([PDF](en/07_hypothesis_testing/07.03_goodness_of_fit_tests.pdf)) | `07.03_goodness_of_fit_tests.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **07.04** | [07.04 Contingencia e Independencia](es/07_pruebas_hipotesis/07.04_contingency_tables.tex) ([PDF](es/07_pruebas_hipotesis/07.04_contingency_tables.pdf)) | [07.04 Contingency Tables and Independence](en/07_hypothesis_testing/07.04_contingency_tables.tex) ([PDF](en/07_hypothesis_testing/07.04_contingency_tables.pdf)) | `07.04_contingency_tables.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |

---

## 5f. Catálogo e Índice de Presentaciones --- Capítulo 08 (catálogo histórico)

### Correspondencias activas de las notas ES — corte 2026-07-24 15:41:01 -06:00

El bloque activo cubre las filas 53, 55--56 y 58--59 de la matriz. Cada par
ES/EN tiene 22 frames, cero listings y doble compilación exitosa; el catálogo
histórico de 08.01--08.02 que sigue se conserva sin renumerarlo.

| Fila | Sección ES | Mazo EN | Estado |
| :---: | :--- | :--- | :---: |
| 53 | [08.01 Estrategias de experimentación](es/08_diseno_experimentos/08.01_experimental_strategies.tex) ([PDF](es/08_diseno_experimentos/08.01_experimental_strategies.pdf)) | [08.01 Experimental strategies](en/08_experimental_design/08.01_experimental_strategies.tex) ([PDF](en/08_experimental_design/08.01_experimental_strategies.pdf)) | ES/EN completos, 22 frames cada uno |
| 55 | [08.03 Efectos de modelo fijo](es/08_diseno_experimentos/08.03_fixed_effects.tex) ([PDF](es/08_diseno_experimentos/08.03_fixed_effects.pdf)) | [08.03 Fixed-effect effects](en/08_experimental_design/08.03_fixed_effects.tex) ([PDF](en/08_experimental_design/08.03_fixed_effects.pdf)) | ES/EN completos, 22 frames cada uno |
| 56 | [08.04 Comparaciones post-hoc](es/08_diseno_experimentos/08.04_post_hoc_comparisons.tex) ([PDF](es/08_diseno_experimentos/08.04_post_hoc_comparisons.pdf)) | [08.04 Post-hoc comparisons](en/08_experimental_design/08.04_post_hoc_comparisons.tex) ([PDF](en/08_experimental_design/08.04_post_hoc_comparisons.pdf)) | ES/EN completos, 22 frames cada uno |
| 58 | [08.06 Bloques y cuadrados latinos](es/08_diseno_experimentos/08.06_randomized_blocks_latin_squares.tex) ([PDF](es/08_diseno_experimentos/08.06_randomized_blocks_latin_squares.pdf)) | [08.06 Blocks and Latin squares](en/08_experimental_design/08.06_randomized_blocks_latin_squares.tex) ([PDF](en/08_experimental_design/08.06_randomized_blocks_latin_squares.pdf)) | ES/EN completos, 22 frames cada uno |
| 59 | [08.07 Diseños factoriales](es/08_diseno_experimentos/08.07_factorial_designs.tex) ([PDF](es/08_diseno_experimentos/08.07_factorial_designs.pdf)) | [08.07 Factorial designs](en/08_experimental_design/08.07_factorial_designs.tex) ([PDF](en/08_experimental_design/08.07_factorial_designs.pdf)) | ES/EN completos, 22 frames cada uno |

### Catálogo histórico del capítulo 08

A continuación se presenta el avance y estado verificado de las secciones correspondientes a la **Unidad 7 / Capítulo 08: Elementos de Diseño de Experimentos (ANOVA)**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/08_diseno_experimentos/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **08.01** | [08.01 ANOVA de un Factor](es/08_diseno_experimentos/08.01_one_way_anova.tex) ([PDF](es/08_diseno_experimentos/08.01_one_way_anova.pdf)) | [08.01 One-Way ANOVA](en/08_experimental_design/08.01_one_way_anova.tex) ([PDF](en/08_experimental_design/08.01_one_way_anova.pdf)) | `08.01_one_way_anova.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **08.02** | [08.02 Supuestos del ANOVA](es/08_diseno_experimentos/08.02_anova_assumptions.tex) ([PDF](es/08_diseno_experimentos/08.02_anova_assumptions.pdf)) | [08.02 ANOVA Assumptions](en/08_experimental_design/08.02_anova_assumptions.tex) ([PDF](en/08_experimental_design/08.02_anova_assumptions.pdf)) | `08.02_anova_assumptions.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |

---

## 5g. Catálogo e Índice de Presentaciones --- Capítulo 09 (catálogo histórico)

### Correspondencias activas de las notas ES — corte 2026-07-24 15:49:29 -06:00

El bloque activo cubre las filas 62 y 70 de la matriz. Cada par ES/EN tiene
22 frames, cero listings y doble compilación exitosa; el catálogo histórico de
las demás secciones 09.01--09.11 que sigue se conserva sin renumerarlo.

| Fila | Sección ES | Mazo EN | Estado |
| :---: | :--- | :--- | :---: |
| 62 | [09.02 Introducción a la regresión](es/09_regresiones/09.02_regresiones_lineales_section.tex) ([PDF](es/09_regresiones/09.02_regresiones_lineales_section.pdf)) | [09.02 Introduction to linear regression](en/09_regressions/09.02_regresiones_lineales_section.tex) ([PDF](en/09_regressions/09.02_regresiones_lineales_section.pdf)) | ES/EN completos, 22 frames cada uno |
| 70 | [09.11 Resumen de modelos](es/09_regresiones/09.11_model_summary.tex) ([PDF](es/09_regresiones/09.11_model_summary.pdf)) | [09.11 Model summary](en/09_regressions/09.11_model_summary.tex) ([PDF](en/09_regressions/09.11_model_summary.pdf)) | ES/EN completos, 22 frames cada uno |

### Catálogo histórico del capítulo 09

A continuación se presenta el avance y estado verificado de las secciones correspondientes al **Tema complementario / Capítulo 09: Regresiones Lineales y Múltiples**. No constituye una Unidad 8 del programa oficial: las siete unidades oficiales corresponden a los capítulos 02–08. Una versión anterior de este capítulo agrupó 7 archivos de teoría en una sola sección 09.01; se corrigió a la estructura 1:1 de 12 secciones que se muestra abajo (detalle completo en `ROADMAP.md`).

| Sección | Título en Español | Título en Inglés | Script Python (en `code/09_regresiones/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **09.01** | [09.01 Correlación](es/09_regresiones/09.01_correlation.tex) ([PDF](es/09_regresiones/09.01_correlation.pdf)) | [09.01 Correlation](en/09_regressions/09.01_correlation.tex) ([PDF](en/09_regressions/09.01_correlation.pdf)) | `09.01_correlation.py` | $\checkmark$ **Completado (15 diapositivas ES / 15 EN, 0 warnings) --- APERTURA DEL CAPÍTULO 09** |
| **09.02** | [09.02 Introducción a la Regresión](es/09_regresiones/09.02_introduction_to_regression.tex) ([PDF](es/09_regresiones/09.02_introduction_to_regression.pdf)) | [09.02 Introduction to Regression](en/09_regressions/09.02_introduction_to_regression.tex) ([PDF](en/09_regressions/09.02_introduction_to_regression.pdf)) | `09.02_introduction_to_regression.py` | $\checkmark$ **Completado (15 diapositivas ES / 15 EN, 0 warnings)** |
| **09.03** | [09.03 Matemáticas de la Regresión](es/09_regresiones/09.03_mathematics_of_regression.tex) ([PDF](es/09_regresiones/09.03_mathematics_of_regression.pdf)) | [09.03 Mathematics of Regression](en/09_regressions/09.03_mathematics_of_regression.tex) ([PDF](en/09_regressions/09.03_mathematics_of_regression.pdf)) | `09.03_mathematics_of_regression.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **09.04** | [09.04 Regresión sobre Datos Simulados](es/09_regresiones/09.04_regression_on_simulated_data.tex) ([PDF](es/09_regresiones/09.04_regression_on_simulated_data.pdf)) | [09.04 Regression on Simulated Data](en/09_regressions/09.04_regression_on_simulated_data.tex) ([PDF](en/09_regressions/09.04_regression_on_simulated_data.pdf)) | `09.04_regression_on_simulated_data.py` | $\checkmark$ **Completado (13 diapositivas ES / 13 EN, 0 warnings)** |
| **09.05** | [09.05 Coeficientes Óptimos](es/09_regresiones/09.05_optimal_coefficients_and_tests.tex) ([PDF](es/09_regresiones/09.05_optimal_coefficients_and_tests.pdf)) | [09.05 Optimal Coefficients](en/09_regressions/09.05_optimal_coefficients_and_tests.tex) ([PDF](en/09_regressions/09.05_optimal_coefficients_and_tests.pdf)) | `09.05_optimal_coefficients_and_tests.py` | $\checkmark$ **Completado (12 frames ES/EN, 3 listings, 0 warnings)** |
| **09.06** | [09.06 Implementación con statsmodels](es/09_regresiones/09.06_implementation_with_statsmodels.tex) ([PDF](es/09_regresiones/09.06_implementation_with_statsmodels.pdf)) | [09.06 Implementation with statsmodels](en/09_regressions/09.06_implementation_with_statsmodels.tex) ([PDF](en/09_regressions/09.06_implementation_with_statsmodels.pdf)) | `09.06_statsmodels_style_summary.py` | $\checkmark$ **Completado (13 diapositivas ES / 13 EN, 0 warnings)** |
| **09.07** | [09.07 Regresión Lineal Múltiple](es/09_regresiones/09.07_multiple_linear_regression.tex) ([PDF](es/09_regresiones/09.07_multiple_linear_regression.pdf)) | [09.07 Multiple Linear Regression](en/09_regressions/09.07_multiple_linear_regression.tex) ([PDF](en/09_regressions/09.07_multiple_linear_regression.pdf)) | `09.07_multiple_linear_regression.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **09.08** | [09.08 Validación de Modelos](es/09_regresiones/09.08_model_validation.tex) ([PDF](es/09_regresiones/09.08_model_validation.pdf)) | [09.08 Model Validation](en/09_regressions/09.08_model_validation.tex) ([PDF](en/09_regressions/09.08_model_validation.pdf)) | `09.08_model_validation.py` | $\checkmark$ **Completado (13 diapositivas ES / 13 EN, 0 warnings)** |
| **09.09** | [09.09 Diagnóstico de Regresión](es/09_regresiones/09.09_regression_diagnostics.tex) ([PDF](es/09_regresiones/09.09_regression_diagnostics.pdf)) | [09.09 Regression Diagnostics](en/09_regressions/09.09_regression_diagnostics.tex) ([PDF](en/09_regressions/09.09_regression_diagnostics.pdf)) | `09.09_regression_diagnostics.py` | $\checkmark$ **Completado (13 frames ES/EN, 3 listings, 0 warnings)** |
| **09.10** | [09.10 Regresión con scikit-learn](es/09_regresiones/09.10_scikit_learn_regression.tex) ([PDF](es/09_regresiones/09.10_scikit_learn_regression.pdf)) | [09.10 Regression with scikit-learn](en/09_regressions/09.10_scikit_learn_regression.tex) ([PDF](en/09_regressions/09.10_scikit_learn_regression.pdf)) | `09.10_scikit_learn_regression.py` | $\checkmark$ **Completado (12 frames ES/EN, 3 listings, 0 warnings; excepción de dependencia documentada)** |
| **09.11** | [09.11 Variables Categóricas y Muda](es/09_regresiones/09.11_categorical_dummy_variables.tex) ([PDF](es/09_regresiones/09.11_categorical_dummy_variables.pdf)) | [09.11 Categorical and Dummy Variables](en/09_regressions/09.11_categorical_dummy_variables.tex) ([PDF](en/09_regressions/09.11_categorical_dummy_variables.pdf)) | `09.11_categorical_dummy_variables.py` | $\checkmark$ **Completado (12 frames ES/EN, 3 listings, 0 warnings)** |
| **09.12** | [Mazo ES archivado](../archive/presentaciones-es/09_regresiones/09.12_nonlinear_polynomial_regression.tex) | [09.12 Nonlinear Transformations (legado EN)](en/09_regressions/09.12_nonlinear_polynomial_regression.tex) | 09.12_nonlinear_polynomial_regression.py | **Archivado: no es sección activa de las notas ES** |

---

## 6. Próximo Trabajo y Hoja de Ruta (`ROADMAP.md`)

Los Capítulos 04 (Variables Aleatorias Continuas), 05 (Distribuciones de Muestreo), 06 (Estimación y su Relación con Ciencia de Datos), 07 (Docimasia --- Pruebas de Hipótesis), 08 (Elementos de Diseño de Experimentos --- ANOVA) y 09 (Regresiones Lineales y Múltiples) están 100% completos. El Capítulo 09 quedó estructurado en 12 secciones 1:1 con sus archivos de teoría fuente (09.01 Correlación hasta 09.12 Transformaciones No Lineales y Regresión Polinomial), tras corregir una discrepancia estructural documentada antes del 2026-07-23 (ver nota en la Sección 5g arriba y el detalle completo en `ROADMAP.md`). Para conocer el estado detallado de cada sección y el trabajo pendiente en capítulos futuros, consulta el documento oficial de planificación:
👉 **[presentaciones/ROADMAP.md](ROADMAP.md)**.
