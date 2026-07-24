# ROADMAP: Ebook "Modelación Estadística" --- Presentaciones Beamer & Laboratorios Python

## 1. Visión y Objetivos del Subproyecto

Este subproyecto tiene como objetivo construir **presentaciones didácticas de alta calidad en formato Beamer (Español e Inglés)** y **laboratorios computacionales reproducibles en Python** para cada una de las secciones teóricas del libro de texto *Modelación Estadística* (cuyo archivo maestro es `latex/[Modelación Estadística].tex`).

### Las 4 Reglas de Oro para Todo Agente y Trabajo Documentado

1. **Estricta Política de No-Commits Automáticos (`No-Auto-Commit Policy`):**
   Ningún agente de IA debe ejecutar comandos `git commit` o `git push` por su cuenta. Todos los archivos creados o modificados deben permanecer en el árbol de trabajo (*working tree*) para revisión y validación de estilo por parte del autor (`Juliho Castillo Colmenares`).
2. **Purity Tipográfica y Política Cero Desbordamientos (*Zero Overfull Policy*):**
   Cada presentación Beamer en español (`es/`) e inglés (`en/`) debe compilarse obligatoriamente **dos veces** con `pdflatex -interaction=nonstopmode`. Es un requisito de aceptación que el archivo de registro (`.log`) arroje **exactamente 0 `Overfull \vbox` y 0 `Overfull \hbox`** en todas las diapositivas de contenido (páginas 2 a $N$). La portada en la página 1 (`\begin{frame}[plain]`) está exenta del aviso `\vbox` de centrado vertical propio de `beamerthememetropolis`.
3. **Taxonomía vigente de los cuadernos de práctica:**
   Cada `latex/<seccion>(p).tex` vivo debe cubrir los seis niveles de Bloom en orden **Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear**, con comentarios de nivel invisibles, etiquetas `prob:<7-hex>` y soluciones enlazadas mediante `\begin{solproblema}[prob:<tag>]`. El cuaderno es práctica autónoma; el Bloque IV de los mazos reutiliza ejemplos `\ejemplo`/`\solucion` ya resueltos en la teoría.
   - La convención anterior de 10 problemas `3-3-2-2` y niveles visibles se conserva solo como referencia histórica anterior al 2026-07-20.
4. **Única Fuente de Verdad Computacional (*Single Source of Truth*):**
   Todo el código Python reside exclusivamente en `presentaciones/code/<unidad>/<ID>_<name_in_english>.py` usando solo bibliotecas base (`numpy`, `scipy`) e **inglés estricto en variables y comentarios**. Ambos mazos Beamer (ES y EN) importan exactamente estas líneas con `\lstinputlisting[language=Python, ...]` dentro de entornos `[fragile]`.

---

## 2. Estado vigente verificado al 2026-07-24 17:34:27 -06:00

- El cierre del espejo EN del libro quedó confirmado el `2026-07-23 11:03:37 -06:00`: 60 archivos ES `(p).tex`, 60 archivos EN `en_*(p).tex`, seis problemas y seis soluciones por par, orden Bloom y etiquetas hash idénticas.
- Los maestros ES y EN tienen 139 entradas `\input{}` sin objetivos faltantes; la secuencia paralela del contenido está verificada.
- El árbol de presentaciones contiene 72 mazos ES físicos, uno por cada sección
  activa de teoría; el espejo EN y los 53 scripts Python no se modificaron en
  esta etapa.
- Esta actualización corrige una incompatibilidad de API en el script Normal y reconcilia documentación; no modifica el contenido de `presentaciones/es/` ni `presentaciones/en/`.

### Normalización de notas EN del capítulo 2 — 2026-07-24 16:05:21 -06:00

- Las filas 4--6 de `docs/matriz-notas-presentaciones-es.md` ya tienen el mismo
  tipo de sección y etiquetas que las notas ES: `section*`/`subsection*`, `2.1.*`
  y `2.2.*`, respectivamente.
- Los maestros ES y EN pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas ni etiquetas duplicadas.
- Este subbloque solo modifica notas EN y documentación. La paridad de frames
  de los mazos EN de las filas 5--6 queda como pendiente operativo posterior;
  no se añadieron scripts ni se tocaron archivos `(p)`.

### Normalización de notas EN del capítulo 3 — 2026-07-24 16:15:12 -06:00

- Las notas EN de discretas y Poisson ya coinciden con sus fuentes ES en
  jerarquía y etiquetas; Poisson conserva además los nueve listings y todos los
  ejemplos y desarrollos de aproximación normal y problemas resueltos.
- Los maestros ES y EN pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas ni etiquetas duplicadas.
- La presentación EN de las filas 11 y 16 conserva una diferencia histórica de
  frames y queda como el siguiente trabajo de sincronización de mazos; no se
  modificaron Beamer, Python ni archivos `(p)`.

### Normalización de notas EN de la fila 18 — 2026-07-24 16:18:42 -06:00

- `en_variables_aleatorias_continuas.tex` coincide con ES en jerarquía y en sus
  47 etiquetas.
- Los maestros pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas ni etiquetas duplicadas.
- La presentación EN de la fila 18 conserva una diferencia histórica de frames
  y queda para la sincronización de mazos; no se modificaron Beamer ni Python.

### Normalización de notas EN de la fila 36 — 2026-07-24 16:21:29 -06:00

- `en_ic_media_diferencia_medias.tex` ya tiene una sola sección y las dos
  etiquetas de su fuente ES.
- Los maestros pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas ni etiquetas duplicadas. No se modificaron Beamer ni
  Python.

### Cierre de normalización de notas EN — 2026-07-24 16:26:30 -06:00

- Las 72 filas de la matriz ya tienen correspondencia estructural y de etiquetas
  entre las notas ES y EN.
- Los maestros pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas ni etiquetas duplicadas.
- El trabajo pendiente se limita a sincronizar frames de mazos EN; no quedan
  notas EN parciales, y no se modificaron scripts ni archivos `(p)`.

### Primer grupo de mazos EN sincronizado — 2026-07-24 16:37:24 -06:00

- `02.02_sets_and_partitions` y `02.03_probability_foundations` coinciden con
  ES en frames y listings (14/14 + 4/4; 16/16 + 3/3).
- Se eliminaron los ejercicios heredados y se corrigieron declaraciones de
  clase duplicadas o ausentes. Los cuatro mazos compilaron dos veces sin errores,
  referencias indefinidas, etiquetas duplicadas ni `Overfull \\hbox`.
- La matriz registra 33 filas completas de cuatro vías; el siguiente grupo se
  seleccionará entre los mazos EN parciales restantes.

### Segundo grupo de mazos EN sincronizado — 2026-07-24 16:45:10 -06:00

- Condicional, Bayes y muestreo coinciden con ES en frames y listings
  (16/16 + 4/4; 14/14 + 3/3; 14/14 + 3/3).
- Se retiraron los ejercicios heredados y se verificaron seis dobles
  compilaciones; no hay errores, referencias indefinidas, etiquetas duplicadas
  ni `Overfull \\hbox`.
- La matriz registra 36 filas completas de cuatro vías; quedan 36 filas
  parciales para grupos posteriores.

### Primer grupo del capítulo 3 sincronizado — 2026-07-24 16:59:09 -06:00

- Las filas 11, 12 y 16 quedaron en paridad ES/EN: PMF y soporte (14 frames),
  Bernoulli/binomial (14 frames) y Poisson (17 frames), con tres listings por
  par.
- Se retiraron únicamente ejercicios heredados y un comentario residual de
  ejercicio; no se modificaron las notas, los archivos `(p)` ni Python.
- Los seis mazos pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas, etiquetas duplicadas ni `Overfull \\hbox`; los
  únicos avisos `vbox` pertenecen a portadas EN. La matriz registra 39 filas
  completas de cuatro vías y 33 parciales.

### Segundo grupo del capítulo 3 sincronizado — 2026-07-24 17:13:35 -06:00

- Las filas 13--15 y 17 quedaron en paridad ES/EN: multinomial (14 frames),
  geométrica/binomial negativa (14), hipergeométrica (16) y distribuciones
  discretas para ciencia de datos (15), con tres listings por par.
- Se retiraron ocho frames de ejercicios heredados en cada mazo EN y se añadieron
  los desarrollos faltantes frente a ES. No se modificaron notas, Python ni
  archivos `(p)`.
- Los ocho mazos pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas, etiquetas duplicadas ni `Overfull \\hbox`; los avisos
  `vbox` restantes son de portadas EN. La matriz registra 43 filas completas
  de cuatro vías y 29 parciales.

### Capítulo 1 sincronizado — 2026-07-24 17:24:01 -06:00

- Las filas 1--3 quedaron en paridad ES/EN: introducción (10 frames),
  tendencia central (13) y dispersión (14), con 1, 2 y 2 listings por par.
- Se retiraron seis frames de ejercicios heredados por mazo EN, se añadieron
  declaraciones `documentclass` ausentes y se compactaron frames con avisos
  verticales. No se modificaron notas, Python ni archivos `(p)`.
- Los seis mazos pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas, etiquetas duplicadas ni `Overfull \\hbox`; los únicos
  avisos `vbox` restantes son de portadas EN. La matriz registra 46 filas
  completas de cuatro vías y 26 parciales.

### Capítulo 4 sincronizado — 2026-07-24 17:34:27 -06:00

- Las filas 18--22 quedaron en paridad ES/EN: PDF y soporte, esperanza y
  varianza, uniforme, normal y gamma/beta/Weibull, cada una con 15 frames y 3
  listings por par.
- Se retiraron ocho frames de ejercicios heredados por mazo EN y se añadieron
  los desarrollos teóricos faltantes frente a ES. No se modificaron notas,
  Python ni archivos `(p)`.
- Los diez mazos pasaron dos compilaciones con código 0, sin errores,
  referencias indefinidas, etiquetas duplicadas ni `Overfull \\hbox`; los únicos
  avisos `vbox` restantes son de portadas EN. La matriz registra 51 filas
  completas de cuatro vías y 21 parciales.

### Pendientes vigentes al 2026-07-23 14:47:30 -06:00

- No quedan pendientes técnicos de este cierre: captions ANOVA, orden Normal/Exponencial y compatibilidad `scipy.stats.kstest` están verificados.

### Reconciliación notas ES–mazos ES al 2026-07-23 17:32:50 -06:00

- La fuente de verdad para el inventario es la nota de lectura ES: hay 72
  `\section`/`\section*` activas y la matriz `docs/matriz-notas-presentaciones-es.md`
  registra exactamente una correspondencia por sección.
- La Unidad 1 usa la ampliación pedagógica 1.1–1.6. El analítico MA1001B sigue
  conservando sus cuatro subtemas oficiales; la ampliación no es una nueva
  transcripción curricular.
- `02.00_introduccion_probabilidad` es la introducción sin numerar y
  `02.01`–`02.06` son los seis temas de trabajo, incluidos Fundamentos,
  Técnicas de conteo y Bayes como secciones propias.
- Un mazo ES no incorpora problemas de las secciones `(p)`: se excluyen los
  bloques `Ejercicio en Clase`, `Problema X.Y.Z`, etiquetas `prob:` y rutas
  `(p)`. El contenido de clase usa ejemplos y soluciones ya resueltos en teoría.

### Cierre de la reconciliación física al 2026-07-24 11:35:16 -06:00

- La auditoría de la matriz confirmó 72 filas, 72 rutas físicas y cero
  duplicados.
- Se archivaron 8 mazos legado y se eliminaron referencias a ejercicios o
  problemas de los mazos vivos.
- Los 72 mazos ES compilaron dos veces sin errores ni desbordamientos en
  páginas de contenido. No se alteraron `presentaciones/en/` ni
  `presentaciones/code/`.
- Las referencias a `3-3-2-2` y a diez problemas en el registro histórico de
  este archivo son solo antecedentes fechados, no requisitos activos.

## Piloto cerrado: 02.03 Técnicas de conteo — 2026-07-24 14:20:02 -06:00

- `presentaciones/es/02_teoria_probabilidad/02.03_tecnicas_de_conteo.tex` y
  `presentaciones/en/02_probability_theory/02.03_counting_techniques.tex`
  tienen la misma estructura de **22 frames**.
- Los cuatro ejemplos usados provienen de la teoría (`exmp:conteo.1`–
  `exmp:conteo.4`); no se incorporan problemas `(p)`, etiquetas `prob:` ni
  ejercicios sin resolver.
- No se añadió un script Python: el puente computacional usa aritmética exacta
  y tablas calculadas dentro del mazo, por lo que `\lstinputlisting` permanece
  en cero en ambos idiomas.
- La doble compilación de ambos mazos terminó con código 0, cero referencias
  indefinidas, cero etiquetas duplicadas y cero `Overfull \\hbox`/`\\vbox`.
- La matriz pasa de 5 a 6 filas completas de cuatro vías; quedan 66 filas
  parciales. El inventario físico pasa a 48 mazos ES desarrollados y 55 mazos
  EN. El siguiente bloque queda pendiente: capítulo 5, sin iniciarlo en este
  corte.

## 3. Registro histórico del desarrollo hasta el 2026-07-23 11:03:37 -06:00

Las secciones siguientes conservan decisiones, conteos y protocolos de etapas anteriores. Sus referencias a la convención histórica de 10 problemas `3-3-2-2`, a estados intermedios y a archivos retirados son históricas y no constituyen instrucciones para trabajo nuevo.

### Unidad 1 / Capítulo 02: Teoría de la Probabilidad (`100% COMPLETADA`)
- $\checkmark$ **02.01 Introducción a la Probabilidad:** Mazos ES/EN de 20 diapositivas (`0 overfulls` reportados en el registro de compilación anterior al 2026-07-23), sin script computacional dedicado.
- $\checkmark$ **02.02 Conjuntos y Particiones:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.02_sets_partitions.py`.
- $\checkmark$ **02.03 Fundamentos y Axiomas:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.03_probability_axioms.py`.
- $\checkmark$ **02.04 Probabilidad Condicional:** Mazos ES/EN de 20 diapositivas (`0 overfulls`), script `02.04_conditional_probability.py`.
- $\checkmark$ **02.05 Teorema de Bayes:** 100% completado (Remediación modular total bajo el Estándar de Oro).
  - *Cuaderno de Problemas:* 10 problemas en `latex/teorema_de_bayes(p).tex` organizados bajo la convención histórica 3-3-2-2 (Problemas 2.5.1 al 2.5.10).
  - *Laboratorio Python:* `presentaciones/code/02_teoria_probabilidad/02.05_bayes_theorem.py` (simulación de test médico diagnóstico y VPP empírico vs. teórico, evaluación exacta de clasificador Naive Bayes anti-spam, y actualización bayesiana secuencial a lo largo de observaciones iterativas).
  - *Mazos Beamer:* 22 diapositivas pedagógicas simétricas en `presentaciones/es/02_teoria_probabilidad/02.05_teorema_bayes.tex` y `en/02_probability_theory/02.05_bayes_theorem.tex` (revelado progresivo `\pause`, puente computacional Python en 4 diapositivas sin truncar, 4 problemas en clase desarrollados en Enunciado $\to$ Resolución para cada nivel de la taxonomía, cero marcado informal y compilación certificada con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **02.06 Muestreo Aleatorio y TLC:** 100% completado (Remediación modular total bajo el Estándar de Oro).
  - *Cuaderno de Problemas:* 10 problemas en `latex/muestreo_aleatorio(p).tex` organizados bajo la convención histórica 3-3-2-2.
  - *Laboratorio Python:* `presentaciones/code/02_teoria_probabilidad/02.06_random_sampling.py` (simulación MAS con vs sin reemplazo, verificación empírica de FPC, evolución del error en LGN con cota de Chebyshev, y estandarización CLT en población exponencial $N=50,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas simétricas en `presentaciones/es/02_teoria_probabilidad/02.06_muestreo_aleatorio.tex` y `en/02_probability_theory/02.06_random_sampling.tex` (revelado progresivo `\pause`, puente computacional Python de 4 diapositivas, 4 problemas en clase desarrollados en Enunciado $\to$ Resolución, cero marcado informal y compilación certificada con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).

### Unidad 2 / Capítulo 03: Variables Aleatorias Discretas (`Avance actual: 10 de 10 secciones completadas --- 100% FINALIZADO`)
- $\checkmark$ **03.01 PMF y Soporte:** 100% completado (Remediación modular total).
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `latex/variables_aleatorias_discretas(p).tex` (Problemas 3.1.1 al 3.1.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.01_pmf_and_support.py` (normalización polinomial, probabilidad condicional en soporte discreto, simulación Monte Carlo de suma de dados y transformación no lineal $|X-1|$ con sumas por preimágenes).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.01_pmf_y_soporte.tex` y `en/03_discrete_random_variables/03.01_pmf_and_support.tex` (revelado progresivo `\pause`, puente numérico Python en 4 diapositivas, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución para cada nivel de la taxonomía, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.02 CDF Discreta:** 100% completado (Remediación modular total).
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `latex/variables_aleatorias_discretas(p).tex` (Problemas 3.2.1 al 3.2.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.02_discrete_cdf.py` (construcción de CDF, operador de diferencia $\Delta F$ para recuperar PMF, probabilidades de intervalos y simulación empírica ECDF con $N=100,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.02_cdf_discreta.tex` (revelado progresivo `\pause`, puente numérico Python en 4 diapositivas, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución para cada nivel de la taxonomía, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.03 Esperanza Matemática, Varianza y Momentos:** 100% completado (Remediación modular total).
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `latex/variables_aleatorias_discretas(p).tex` (Problemas 3.3.1 al 3.3.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.03_expectation_and_variance.py` (cálculo de momentos exactos, LOTUS, estandarización Z y simulación Monte Carlo de LLN con $N=100,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.03_esperanza_y_varianza.tex` (revelado progresivo `\pause`, puente numérico Python en 4 diapositivas, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución para cada nivel de la taxonomía, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.04 Distribuciones de Bernoulli y Binomial:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `los cuadernos de sección vigentes` (Problemas 3.4.1 al 3.4.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.py` (validación vectorizada en numpy/scipy y simulación Monte Carlo $N=100,000$).
  - *Mazos Beamer:* 22 diapositivas pedagógicas y modulares en `presentaciones/es/03_variables_aleatorias_discretas/03.04_bernoulli_binomial.tex` (revelado progresivo `\pause`, puente numérico Python tras teoría, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.05 Distribuciones Geométrica y Binomial Negativa:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `los cuadernos de sección vigentes` (Problemas 3.5.1 al 3.5.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.py` (validación combinatoria con SciPy y Monte Carlo $N=250,000$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.05_geometric_negative_binomial.tex` y `presentaciones/en/03_discrete_random_variables/03.05_geometric_negative_binomial.tex` (revelado progresivo `\pause`, 4 ejercicios interactivos en clase divididos en Enunciado/Resolución, cero marcado informal y compilado con **0 `Overfull \vbox` y 0 `Overfull \hbox`**).
- $\checkmark$ **03.06 Distribución Hipergeométrica:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `los cuadernos de sección vigentes` (Problemas 3.6.1 al 3.6.10).
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.06_hypergeometric.py` (validación PMF, FPCF con Monte Carlo $N=250,000$ y prueba exacta de Fisher).
  - *Mazos Beamer:* mazos ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.06_hipergeometrica.tex` y `presentaciones/en/03_discrete_random_variables/03.06_hypergeometric.tex`, compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`**.
  - *Libro Maestro:* Compilado limpiamente (`[Modelación Estadística].tex`).
- $\checkmark$ **03.07 Distribución de Poisson y Procesos de Llegada:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `los cuadernos de sección vigentes` (Problemas 3.7.1 al 3.7.10): cálculo directo de PMF, equidispersión, ley de eventos raros, aditividad, deducción analítica de momentos y propiedad condicional binomial en suma de Poisson.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.07_poisson_distribution.py` (validación de PMF y equidispersión, ley de eventos raros Binomial $\to$ Poisson con TVD, aditividad y distribución condicional binomial verificada por simulación Monte Carlo con $N=250,000$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.07_poisson_distribution.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.07_poisson_distribution.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 552 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **03.08 Distribución Multinomial y Ensayos Politómicos:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `los cuadernos de sección vigentes` (Problemas 3.8.1 al 3.8.10): coeficientes multinomiales, probabilidades conjuntas, marginales binomiales, simulación de ensayos politómicos, covarianzas negativas, deducción de momentos factoriales, distribuciones condicionales y aplicación a tablas de contingencia.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.08_multinomial_distribution.py` (validación de PMF multinomial y normalización, simulación Monte Carlo de covarianzas con $N=250,000$ verificando $\cov(X_i, X_j) = -n p_i p_j$, distribución condicional multinomial en sub-vector verificada con filtro de 43{,}324 muestras de 500,000 simulaciones).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.08_multinomial_distribution.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.08_multinomial_distribution.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 560 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **03.09 Distribución Normal y Aproximación Continua:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `los cuadernos de sección vigentes` (Problemas 3.9.1 al 3.9.10): PDF Normal y estandarización $Z$, cálculo de probabilidades con la regla 68-95-99.7, aproximación Binomial-Normal con corrección de Yates, Poisson-Normal con $\lambda \ge 30$, deducción del Teorema de De Moivre-Laplace vía MGF, MGF de la Normal, TLC aplicado a sumas de Poisson y Exponential.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.09_normal_approximation.py` (verificación de PDF Normal con integración numérica $\int f = 1$, estandarización $Z$ y regla empírica, aproximación Binomial-Normal con y sin Yates mostrando reducción de error de $0.0112$ a $0.0021$, Poisson-Normal con error $< 0.001$, TLC para suma de 50 exponenciales verificado por Monte Carlo con $N=250{,}000$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.09_normal_approximation.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.09_normal_approximation.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 568 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **03.10 Distribuciones Discretas en Ciencia de Datos:** 100% completado (**CIERRE DEL CAPÍTULO 03**).
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `los cuadernos de sección vigentes` (Problemas 3.10.1 al 3.10.10): MLE de Poisson, detección de sobredispersión por cociente $D = s^{2}/\bar{x}$, intervalos de Wald/exacto/bootstrap, ajuste de Binomial Negativa por momentos, comparación de modelos vía AIC/BIC, test de razón de verosimilitud de Wilks, modelo jerárquico Poisson-Gamma, inferencia en confiabilidad exponencial.
  - *Laboratorio Python:* `presentaciones/code/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.py` (ajuste MLE de Poisson y Binomial Negativa con $\Delta$AIC $= 16.21$ a favor de NegBin, test de Wilks con $\Lambda = 45.34$ y $p < 10^{-6}$ para $n = 200$ de NegBin, intervalos de Wald/exacto/bootstrap para $\lambda$ Poisson con 12 meses de reclamaciones, bootstrap de parámetros de Binomial Negativa con $B = 10{,}000$ muestras).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/03_variables_aleatorias_discretas/03.10_discrete_distributions_data_science.tex` (24 frames) y `presentaciones/en/03_discrete_random_variables/03.10_discrete_distributions_data_science.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 576 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.02 Función de Distribución Acumulada Continua y Cuantiles:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `latex/variables_aleatorias_continuas(p).tex` (Problemas 4.2.1 al 4.2.10): CDF exponencial, cuantiles, método de inversión, prueba de Kolmogorov-Smirnov, log-normal, propiedades axiomáticas de $F$.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.02_continuous_cdf.py` (validación de propiedades de CDF; cuantiles por inversión numérica; método de inversión verificado con KS test $p > 0.4$; test KS aplicado a $n = 50$ muestras Uniform).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.02_continuous_cdf.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.02_continuous_cdf.tex` (20 frames), compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 590 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.03 Esperanza Matemática, Varianza y Teorema LOTUS Continuo:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en `latex/esperanza_matematica(p).tex` (Problemas 4.3.1 al 4.3.10): esperanza y varianza de PDF triangular, momentos de Exponential, asimetría y curtosis, LOTUS, linealidad, ley total de varianza, propagación de incertidumbre.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.03_expectation_and_variance.py` (verificación de momentos para Triangular, Uniform, Exponential, Normal; LOTUS para $\E[\sqrt{X}] = 0.8$ y $\E[\log X] = -0.5$; asimetría $\gamma_{1} = 2$ y curtosis $\gamma_{2} = 6$ de Exponential; Monte Carlo con $N = 250{,}000$ confirma valores teóricos; ley total de varianza validada en modelo jerárquico).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.03_expectation_and_variance.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.03_expectation_and_variance.tex` (20 frames), compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 596 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.04 Distribución Uniforme Continua $U(a, b)$:** 100% completado.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en los cuadernos de variables continuas vigentes (Problemas 4.4.1 al 4.4.10): PDF y CDF de $U(2, 8)$, momentos, propiedad de no-falta-de-memoria, cuantiles, simulación Monte Carlo, método de inversión, máxima entropía, orden estadísticas, MLE de midrange, y prueba de Kolmogorov-Smirnov.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.04_uniform_distribution.py` (validación de $\int f = 1$; comparación de CDF manual vs SciPy con tolerancia $0$; cuantiles por inversión numérica; Monte Carlo con $N = 100{,}000$ verifica $\E[X] \approx 0.5$ y $\Var(X) \approx 0.0833$; máxima entropía verificada: Uniform(0,1) tiene $h = 0 > -0.125 = h(\text{Beta}(2,2))$; prueba KS distingue correctamente muestras Uniform de Exponential).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.04_uniform_distribution.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.04_uniform_distribution.tex` (20 frames), compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 602 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.05 Distribución Normal / Gaussiana y Puntaje $Z$:** 100% completado.
  - *Cuaderno de Problemas:* cobertura vigente de los seis niveles Bloom para el espejo ES/EN: PDF y CDF Normal, estandarización al puntaje $Z$, regla 68-95-99.7, prueba $Z$ de una muestra, deducción de MGF Normal, suma de normales independientes, Teorema del Límite Central y aproximación Binomial-Normal con corrección de Yates.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.05_normal_distribution.py` (validación de $\int f = 1$ con tolerancia $< 10^{-7}$; estandarización $Z$ verificada con tolerancia $< 10^{-16}$ para 6 puntos; regla 68-95-99.7 confirmada; cuantiles $z_{0.025} = -1.96$, $z_{0.975} = 1.96$; prueba $Z$ con $Z = 1.5$, $p = 0.134$; TLC verificado: suma de 30 uniformes $\sim N(15, 2.5)$ con KS $p = 0.71$; aproximación Binomial-Normal con error $0.001$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.05_normal_distribution.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.05_normal_distribution.tex` (20 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, ejemplos resueltos y **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 614 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.06 Distribución Exponencial y Procesos sin Memoria:** 100% completado.
  - *Cuaderno de Problemas:* cobertura vigente de los seis niveles Bloom para el espejo ES/EN: PDF y CDF exponencial, momentos, conexión con proceso de Poisson, propiedad de falta de memoria, cuantiles, MLE $\hat{\lambda} = 1/\bar{X}$, distribución Erlang, sistemas de confiabilidad en serie y sistema de colas M/M/1.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.06_exponential_distribution.py` (verificación de $\int f = 1$; propiedad de falta de memoria con tolerancia $< 10^{-15}$; MLE con $n = 50$ muestras produce $\hat{\lambda} = 2.36 \pm 0.37$ con CI bootstrap al 95\% $[1.82, 3.27]$; Erlang$(5, 1)$ verificada con KS test $p = 0.46$; sistema de $n = 10$ componentes en serie con MTTF = 100 h; sistema M/M/1 con $\rho = 0.833$, $L = 5$ y $W = 1$).
  - *Mazos Beamer:* mazos pedagógicos y modulares ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.06_exponential_distribution.tex` (24 frames) y `presentaciones/en/04_continuous_random_variables/04.06_exponential_distribution.tex` (20 frames), como tratamiento pedagógico de la subsección Exponencial incluida dentro de Gamma en el libro, con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido.
  - *Libro Maestro:* Recompilado limpiamente a 608 páginas (`[Modelación Estadística].tex`).
- $\checkmark$ **04.07 Distribuciones Gamma, Beta y Weibull:** 100% completado (**CIERRE DEL CAPÍTULO 04**).
  - *Teoría del Libro Maestro:* Se auditó la subsección Gamma existente en el archivo histórico de teoría de variables continuas y se agregaron las subsecciones nuevas `Distribución beta` y `Distribución Weibull` (con sus espejos en el archivo histórico EN de teoría de variables continuas), ya que solo la teoría Gamma preexistía en el libro maestro.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en los cuadernos de variables continuas vigentes (Problemas 4.7.1 al 4.7.10): PDF y normalización Gamma, casos particulares Exponencial y Chi-cuadrada, momentos vía MGF, PDF y momentos Beta, actualización bayesiana conjugada y propiedad de simetría, confiabilidad y tasa de falla Weibull, comparación de lotes Weibull, conexión Gamma-Chi-cuadrada, y proceso de reemplazo Gamma/Erlang vs. Weibull.
  - *Laboratorio Python:* `presentaciones/code/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.py` (validación de $\int f = 1$ para Gamma, Beta y Weibull vía `scipy.integrate.quad`; propiedad aditiva de Erlang con $P(T>1.5)=0.1736$; casos particulares Exponencial y Chi-cuadrada verificados exactos contra SciPy; momentos Beta$(3,5)$ exactos; propiedad de simetría Beta verificada numéricamente; actualización bayesiana Beta$(2,2) \to$ Beta$(16,8)$; comparación de funciones de riesgo Weibull para $\beta=1$ vs. $\beta=2$).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/04_variables_aleatorias_continuas/04.07_gamma_beta_weibull.tex` (23 frames) y `presentaciones/en/04_continuous_random_variables/04.07_gamma_beta_weibull.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 622 páginas (`[Modelación Estadística].tex`).

### Corrección final de correspondencia del capítulo 04 — 2026-07-24 15:58:15 -06:00

La auditoría física encontró que la fila 23, **Función generadora de momentos**,
conservaba un esqueleto ES de cuatro frames y no tenía contraparte EN porque el
mazo EN `04.06_exponential_distribution` ya ocupaba ese número. Se corrigió sin
modificar las notas ni añadir Python:

- `presentaciones/es/04_variables_aleatorias_continuas/04.06_moment_generating_function.tex`
  ahora tiene 22 frames.
- Se creó `presentaciones/en/04_continuous_random_variables/04.08_moment_generating_function.tex`
  con 22 frames; `04.08` evita la colisión numérica con Exponencial.
- Ambos mazos se compilaron dos veces con código 0, sin errores, referencias
  indefinidas, etiquetas duplicadas ni desbordamientos en contenido.
- La matriz queda con 72 mazos ES desarrollados, 80 mazos EN físicos, 72 rutas
  EN candidatas únicas y 31 filas completas de cuatro vías; los ocho mazos EN
  restantes son históricos o no tienen contraparte ES activa.

Se repitió la doble compilación a las `2026-07-24 15:58:15 -06:00` tras retirar
referencias textuales ambiguas a `(p)` en las diapositivas; el resultado siguió
siendo código 0 y sin desbordamientos en contenido.

No se creó commit ni se hizo `git push`.

### Reconciliación 1:1 del capítulo 05 — 2026-07-24 14:51:34 -06:00

Se cerró el bloque gradual de las filas 24--26 y 32--33 de la matriz. La fuente
de verdad fue la nota ES; las notas EN se normalizaron en tipo de sección y los
mazos de problemas quedaron fuera.

- Se desarrollaron cinco mazos ES y se crearon cinco contrapartes EN:
  `05.00_inferential_statistics_introduction`,
  `05.01_variable_transformations`,
  `05.02_distributions_of_random_variable_functions`,
  `05.08_fundamental_statistical_concepts` y
  `05.09_z_and_t_statistics`.
- Cada par tiene 22 frames, cero `\\lstinputlisting` y cero referencias a
  `Ejercicio en Clase`, `Problema`, `prob:` o `(p)`. No se añadió script Python.
- Los diez mazos se compilaron dos veces con código 0; todos los logs reportan
  cero errores, referencias indefinidas, etiquetas duplicadas y
  `Overfull \\hbox`/`\\vbox`. Los maestros ES y EN también compilaron dos veces
  sin errores ni referencias indefinidas.
- La matriz queda en 58 filas con notas EN estructuralmente coincidentes, 53
  mazos ES desarrollados, 60 mazos EN físicos y 11 filas completas de cuatro
  vías. El siguiente bloque (capítulo 6) permanece sin iniciar.

La sección histórica siguiente conserva los mazos de laboratorio 05.01--05.05;
no debe confundirse con las filas activas 24--26 y 32--33 de la matriz.

### Unidad 4 / Capítulo 05: Distribuciones de Muestreo (`Avance histórico: 5 de 5 secciones completadas`)
- $\checkmark$ **05.01 Muestreo Aleatorio Simple, Media y Varianza Muestral Insesgada:** 100% completado (**APERTURA DEL CAPÍTULO 05**).
  - *Teoría del Libro Maestro:* Se auditó el archivo histórico de teoría de distribuciones de muestreo (ES) y su espejo el archivo histórico EN de teoría de distribuciones de muestreo (EN) — la subsección "Distribuciones muestrales de medias" ya cubría $E(\bar X)=\mu$ y $\Var(\bar X)=\sigma^2/n$, pero no la insesgadez de la varianza muestral. Se agregó la subsección nueva "Estadísticos y Varianza Muestral Insesgada" con la definición formal de estadístico, la corrección de Bessel y su demostración completa.
  - *Cuaderno de Problemas:* Se creó el conjunto de cuadernos de distribuciones de muestreo vigentes con 10 problemas bajo la convención histórica 3-3-2-2 (Problemas 5.1.1 al 5.1.10): media/varianza muestral, distinción estadístico vs. parámetro, derivación de $\Var(\bar X)=\sigma^2/n$, comparación de estimadores sesgado/insesgado, demostración formal de $E(S^2)=\sigma^2$, consistencia de $\bar X$, fórmula abreviada de $S^2$, y corrección por población finita (FPC). El material histórico se conectó al libro maestro durante esa etapa.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.01_sample_statistics.py` (verificación Monte Carlo de $E(S^2)=\sigma^2$ vs. estimador sesgado con $N=200{,}000$ muestras; distribución muestral de $\bar X$ verificada para $n=25,100,400$; corrección por población finita verificada empíricamente por muestreo sin reemplazo, FPC teórica $\approx 31.50$ vs. empírica $\approx 31.61$).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.01_sample_statistics.tex` (18 frames) y `presentaciones/en/05_sampling_distributions/05.01_sample_statistics.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 628 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (448 páginas) sin errores.
  - *Correcciones adicionales aplicadas durante esa etapa histórica (fuera del alcance directo de 05.01, pero bloqueaban una compilación limpia del libro maestro):* se definieron los comandos `\E` y `\Prob` (faltantes) en `latex/_pe_comandos.tex`, eliminando cientos de errores "Undefined control sequence" en problemas de capítulos previos; se corrigió un `\begin{align*}`/`\end{itemize}` mal balanceado en `los cuadernos de sección vigentes`; se reemplazaron caracteres Unicode sin soporte (ideogramas chinos accidentales y ✓ literal) por `\checkmark` en `los cuadernos de sección vigentes` y `latex/variables_aleatorias_continuas(p).tex`. El libro maestro compila ahora con **0 errores de LaTeX** (`! ...`) de punta a punta.
- $\checkmark$ **05.02 Teorema del Límite Central Asintótico:** 100% completado.
  - *Teoría del Libro Maestro:* Nueva subsección "Teorema del Límite Central: Convergencia Asintótica" agregada al archivo histórico de teoría de distribuciones de muestreo (ES) y a su espejo histórico EN — convergencia en distribución formal, demostración completa vía FGM (siguiendo el mismo método usado como ejercicio en la 04.05), y el teorema de Berry-Esseen para la tasa de convergencia $O(1/\sqrt n)$. El TLC introductorio de `muestreo_aleatorio.tex` (usado en 02.06) se dejó sin cambios, ya que este tratamiento es deliberadamente más riguroso y complementario.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en los cuadernos de distribuciones de muestreo vigentes (Problemas 5.2.1 al 5.2.10): aplicación directa del TLC, identificación de $Z_n$, heurística $n\ge30$ vs. Berry-Esseen, TLC para sumas (reclamaciones de seguros), cota de Berry-Esseen numérica, TLC para proporciones muestrales, demostración FGM para la Exponencial, derivación de $n$ mínimo a partir de Berry-Esseen, aproximación Binomial-Normal con corrección de Yates, y TLC combinado con la FPC de la Sección 05.01.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.02_central_limit_theorem.py` (convergencia verificada vía prueba de Kolmogorov-Smirnov desde una población Exponencial fuertemente asimétrica para $n=5,30,100$; tasa de Berry-Esseen verificada empíricamente con razones observadas $\approx 0.53$ y $\approx 0.55$ contra la razón teórica $0.5$; aplicaciones a sumas de reclamaciones de seguros y proporciones muestrales, con verificación cruzada Monte Carlo).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.02_central_limit_theorem.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.02_central_limit_theorem.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 632 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (450 páginas) sin errores.
- $\checkmark$ **05.03 Distribución Chi-Cuadrada y Varianza Muestral:** 100% completado.
  - *Teoría del Libro Maestro:* La subsección "Distribución $\chi^2$" en el archivo histórico de teoría de distribuciones de muestreo (ES) y su espejo EN ya cubría definición, propiedades y la observación de que $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$, pero sin PDF explícita ni demostración. Se agregó la densidad formal, el **Teorema de Fisher** completo (independencia de $\bar X$ y $S^2$, más el resultado chi-cuadrada) con bosquejo de demostración vía transformación ortogonal (Teorema de Cochran), y un ejemplo resuelto.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en los cuadernos de distribuciones de muestreo vigentes (Problemas 5.3.1 al 5.3.10): propiedades básicas, definición vía suma de normales al cuadrado, aplicación directa del estadístico $(n-1)S^2/\sigma^2$, reproductividad, MGF vía la conexión Gamma (Sección 04.07), prueba de hipótesis para $\sigma^2$, derivación algebraica de $E(\chi^2_\nu)=\nu$ y $\Var(\chi^2_\nu)=2\nu$, demostración de reproductividad vía MGF, y la descomposición $T=Z/\sqrt{\chi^2_{n-1}/(n-1)}$ que anticipa la distribución $t$ de Student (05.04).
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.03_chi_squared_distribution.py` (propiedades y conexión Gamma verificadas exactas; reproductividad verificada por KS test $p=0.908$; Teorema de Fisher verificado con correlación$(\bar X, S^2)\approx 0.004$ y KS test $p=0.517$ contra $\chi^2_9$; cobertura empírica del intervalo de confianza para $\sigma^2$ de $94.87\%$ vs. $95\%$ nominal).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.03_chi_squared_distribution.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.03_chi_squared_distribution.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 636 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (450 páginas) sin errores.
- $\checkmark$ **05.04 Distribución $t$ de Student y Muestras Pequeñas:** 100% completado.
  - *Teoría del Libro Maestro:* La subsección "Distribución $t$ de Student" en el archivo histórico de teoría de distribuciones de muestreo (ES) y su espejo EN ya cubría definición, PDF, propiedades y la observación del estadístico $t$, pero le faltaba la aplicación práctica central: el intervalo de confianza para $\mu$ con $\sigma$ desconocida. Se agregó el teorema del intervalo de confianza, una observación sobre por qué el ajuste importa más en muestras pequeñas, y un ejemplo resuelto comparando el intervalo $t$ contra el (incorrecto) intervalo $z$.
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en los cuadernos de distribuciones de muestreo vigentes (Problemas 5.4.1 al 5.4.10): propiedades de la $t$, construcción de intervalos de confianza, comparación de cuantiles $t$ vs. $z$, prueba $t$ de una muestra, derivación analítica de $\Var(T)=\nu/(\nu-2)$, convergencia a la Normal vía Slutsky, muestras pareadas, y determinación iterativa de tamaño de muestra.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.04_student_t_distribution.py` (varianza y convergencia de cuantiles verificadas exactas; comparación de intervalos $t$ vs. $z$ mostrando una diferencia del $17.7\%$ para $n=9$; prueba $t$ de una muestra; cobertura empírica del IC del $95.09\%$ vs. $95\%$ nominal).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.04_student_t_distribution.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.04_student_t_distribution.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 640 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (452 páginas) sin errores.
- $\checkmark$ **05.05 Distribución $F$ de Fisher-Snedecor:** 100% completado (**CIERRE DEL CAPÍTULO 05**).
  - *Teoría del Libro Maestro:* La subsección "Distribución $F$ de Snedecor" en el archivo histórico de teoría de distribuciones de muestreo (ES) y su espejo EN ya era muy completa (definición, PDF, propiedades, prueba de igualdad de varianzas, y un ANOVA completamente resuelto). Se agregó el **intervalo de confianza para $\sigma_1^2/\sigma_2^2$** y la **identidad $T^2\sim F_{1,\nu}$**, que conecta formalmente las tres distribuciones del capítulo ($\chi^2$, $t$, $F$).
  - *Cuaderno de Problemas:* 10 problemas bajo la convención histórica 3-3-2-2 en los cuadernos de distribuciones de muestreo vigentes (Problemas 5.5.1 al 5.5.10): propiedades básicas, propiedad recíproca, prueba $F$ de varianzas, ANOVA a partir de estadísticos resumidos, intervalo de confianza para el cociente de varianzas, demostración de $T^2\sim F_{1,\nu}$, derivación de $E(F)=d_2/(d_2-2)$, un ANOVA completo con datos crudos, y un problema de decisión que conecta la prueba $F$ con la elección entre prueba $t$ agrupada o de Welch.
  - *Laboratorio Python:* `presentaciones/code/05_distribuciones_muestreo/05.05_fisher_f_distribution.py` (propiedades, recíproco y la identidad $T^2\sim F_{1,\nu}$ verificados vía KS test; prueba $F$ e IC para $\sigma_1^2/\sigma_2^2$ con cobertura empírica de $94.97\%$; ANOVA completo verificado exacto contra `scipy.stats.f_oneway`).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/05_distribuciones_muestreo/05.05_fisher_f_distribution.tex` (17 frames) y `presentaciones/en/05_sampling_distributions/05.05_fisher_f_distribution.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 644 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (452 páginas) sin errores.

### Reconciliación 1:1 del capítulo 06 — 2026-07-24 15:07:32 -06:00

Se cerró el bloque de las filas 35, 37, 38 y 40 de la matriz, tomando las
secciones ES como fuente de verdad.

- Se desarrollaron cuatro mazos ES y cuatro contrapartes EN:
  `06.02_confidence_intervals`, `06.04_standard_errors`,
  `06.05_confidence_intervals_proportions` y
  `06.07_sample_size_estimation`.
- Cada par tiene 22 frames, cero `\\lstinputlisting` y cero referencias a
  problemas, `(p)` o ejercicios sin resolver. No se añadió Python.
- La fila 38 dejó de apuntar al mazo EN compartido de varianzas y ahora tiene
  una ruta propia de proporciones.
- Los ocho mazos se compilaron dos veces con código 0; sus logs reportan cero
  errores, referencias indefinidas, etiquetas duplicadas y `Overfull`.
- La matriz queda en 57 mazos ES desarrollados, 64 mazos EN físicos y 15 filas
  completas de cuatro vías. El siguiente bloque (capítulo 7) permanece sin
  iniciar.

La sección histórica siguiente conserva los laboratorios 06.01--06.05 y no
debe confundirse con las filas activas cerradas en este corte.

### Unidad 5 / Capítulo 06: Estimación y su Relación con Ciencia de Datos (`Avance histórico: 5 de 5 secciones completadas`)
- $\checkmark$ **06.01 Estimación Puntual, Insesgadez, Eficiencia y Consistencia:** 100% completado (**APERTURA DEL CAPÍTULO 06**).
  - *Teoría del Libro Maestro:* `latex/estimacion_puntual.tex` (ES) y `latex/en_estimacion_puntual.tex` (EN) ya contenían un desarrollo extenso y avanzado de MLE y Método de Momentos, pero el texto introductorio hacía referencia a una "sección anterior" que definía los criterios de calidad de un estimador — contenido que en realidad nunca se había escrito. Se agregó la subsección faltante "Criterios de Calidad de un Estimador Puntual": definición formal de estimador, sesgo, ECM con demostración de la descomposición sesgo-varianza, eficiencia relativa, la Cota Inferior de Cramér-Rao, y consistencia (con la vía práctica vía Chebyshev).
  - *Cuaderno de Problemas:* 10 problemas nuevos bajo la convención histórica 3-3-2-2 (Problemas 6.1.1 al 6.1.10) agregados a `latex/estimacion_puntual(p).tex` (que ya contenía 10 problemas avanzados preexistentes sobre MLE/MoM/Cramér-Rao/Rao-Blackwell, dejados intactos): insesgadez de combinaciones lineales, cálculo numérico de sesgo y ECM, eficiencia relativa, insesgadez asintótica, consistencia vía Chebyshev, derivación de la CRLB para la media normal, y el estimador de encogimiento (\emph{shrinkage}) óptimo que minimiza el ECM.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.01_point_estimation_quality.py` (descomposición sesgo-varianza-ECM y eficiencia relativa $\bar X$ vs. $T_1$ ($\text{Ef}\approx 16.07$, teórico $n=16$); estimador de encogimiento óptimo $c^*\approx 0.643$ con reducción de ECM del $35.7\%$, verificado por búsqueda en malla; consistencia de la proporción muestral verificada vía cota de Chebyshev vs. Monte Carlo).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.01_point_estimation_quality.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.01_point_estimation_quality.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 650 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (454 páginas) sin errores.
- $\checkmark$ **06.02 Método de Momentos (MoM):** 100% completado.
  - *Teoría del Libro Maestro:* La subsección "Método de Momentos (MoM)" en `latex/estimacion_puntual.tex` (ES) y su espejo EN ya tenía definición, teorema del procedimiento general, y un ejemplo resuelto (Gamma). Se agregó un segundo ejemplo ("el caso delicado" $U(-\theta,\theta)$, donde el primer momento no identifica al parámetro) y una observación de propiedades/limitaciones del MoM (consistencia vía LGN, menor eficiencia que MLE, posibilidad de estimaciones inadmisibles).
  - *Cuaderno de Problemas:* 10 problemas nuevos bajo la convención histórica 3-3-2-2 (Problemas 6.2.1 al 6.2.10) agregados a `latex/estimacion_puntual(p).tex`: MoM para Poisson, Geométrica, Uniforme de dos parámetros, Binomial, Beta, consistencia vía LGN, MoM sin forma cerrada para Weibull, y comparación MoM vs. MLE para la Gamma.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.02_method_of_moments.py` (estimadores cerrados de la Gamma verificados exactos; el caso delicado $U(-\theta,\theta)$ verificado; eficiencia relativa MLE/MoM $\approx 1.14$ confirmando que el MLE es más eficiente, vía comparación Monte Carlo contra `scipy.stats.gamma.fit`).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.02_method_of_moments.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.02_method_of_moments.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 654 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (454 páginas) sin errores.
- $\checkmark$ **06.03 Estimación por Máxima Verosimilitud (MLE) y Score:** 100% completado.
  - *Teoría del Libro Maestro:* La subsección MLE en `latex/estimacion_puntual.tex` (ES) y su espejo EN ya tenía definición, ecuación de score (mencionada informalmente), dos ejemplos (Bernoulli, Normal) y propiedades asintóticas listadas sin demostración. Se agregó la subsubsección formal "La Función de Score y Normalidad Asintótica": definición de la función de score, sus propiedades (media cero con demostración, identidad de la información), y el Teorema de Normalidad Asintótica del MLE, conectado explícitamente con la Cota de Cramér-Rao de la Sección 06.01.
  - *Cuaderno de Problemas:* 10 problemas nuevos bajo la convención histórica 3-3-2-2 (Problemas 6.3.1 al 6.3.10) agregados a `latex/estimacion_puntual(p).tex`: score y su media cero para la Exponencial, Información de Fisher, normalidad asintótica aplicada a la Poisson, MLE de la Geométrica vía score, demostración general de la identidad de la información, score vectorial para la Normal, MLE de la distribución Rayleigh, y el método delta para $\hat\sigma_{MLE}=\sqrt{\hat\sigma^2_{MLE}}$.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.py` (propiedades del score verificadas para la Exponencial; normalidad asintótica del MLE de Poisson verificada vía Monte Carlo con IC aproximado $[3.133, 3.867]$; MLE de Rayleigh y método delta verificados con varianzas empíricas que coinciden con las teóricas).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.03_maximum_likelihood_estimation.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.03_maximum_likelihood_estimation.tex` (19 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 658 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (456 páginas) sin errores.
- $\checkmark$ **06.04 Intervalos de Confianza para Medias Poblacionales ($Z$ y $t$):** 100% completado.
  - *Teoría del Libro Maestro:* `latex/intervalos_de_confianza.tex` (ES) y su espejo EN eran de estilo histórico/conceptual (pruebas de hipótesis, valores-$p$, colas) sin fórmula explícita de IC para $\mu$; el archivo `el archivo histórico de teoría de intervalos de confianza` ya contenía teoría rigurosa avanzada (diferencia de medias, proporciones, varianzas, tamaño de muestra) pero asumía que el caso de una sola muestra ya había sido cubierto. Se agregó la subsección faltante "Construcción del Intervalo de Confianza para una Media Poblacional": los teoremas formales del IC con $Z$ (σ conocida) y con $t$ (σ desconocida), la estructura común "estimador ± margen de error", y un ejemplo resuelto comparando ambos casos.
  - *Cuaderno de Problemas:* Se auditó `latex/intervalos_de_confianza(p).tex` y se encontró que **ya contenía un cuaderno completo bajo la convención histórica 3-3-2-2** (10 problemas con etiquetas descriptivas `prob-ic-*`) cubriendo exactamente el tema de 06.04: IC básico con $Z$, decisión $Z$ vs. $t$, tamaño de muestra, varianza agrupada, aproximación de Welch, y una demostración epistemológica rigurosa de la interpretación frecuentista. No se creó un cuaderno nuevo para evitar duplicar contenido ya completo y de alta calidad.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.04_confidence_intervals_means.py` (comparación IC $Z$ vs. $t$ verificada exacta; IC de diferencia de medias con varianza agrupada verificado idéntico a la solución existente; cobertura frecuentista verificada vía Monte Carlo con $100{,}000$ repeticiones, $94.96\%$ vs. $95\%$ nominal).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.04_confidence_intervals_means.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.04_confidence_intervals_means.tex` (19 frames), citando los problemas existentes `prob-ic-1`, `prob-ic-6`, `prob-ic-analit-pooled` y `prob-ic-desaf-epistemologia`, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 660 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (456 páginas) sin errores.
- $\checkmark$ **06.05 Intervalos de Confianza para Varianzas y Proporciones:** 100% completado (**CIERRE DEL CAPÍTULO 06**).
  - *Teoría del Libro Maestro:* `el archivo histórico de teoría de intervalos de confianza` (ES) y su espejo EN ya contenían teoremas rigurosos y completos para IC de varianza ($\chi^2$), razón de varianzas ($F$), proporción (Wald) y diferencia de proporciones, además de fórmulas de tamaño de muestra. Se agregó el **Intervalo de Wilson (Score)** explícito, que la observación existente solo mencionaba por nombre sin dar su fórmula, junto con una explicación de por qué mantiene mejor cobertura real que Wald.
  - *Cuaderno de Problemas:* Se auditó los cuadernos de intervalos de confianza vigentes y se confirmó que **ya contenía un cuaderno bajo la convención histórica 3-3-2-2 completo y de nivel avanzado** (10 problemas) cubriendo IC para varianza, razón de varianzas, diferencia de proporciones A/B, tamaño de muestra, y dos problemas desafiantes de gran calidad (transformación de Fisher para correlación, método delta para cocientes de medias). No se creó un cuaderno nuevo para evitar duplicar contenido ya excelente.
  - *Laboratorio Python:* `presentaciones/code/06_estimacion_estadistica/06.05_confidence_intervals_variances.py` (IC $\chi^2$ para varianza verificado exacto; comparación Wald vs. Wilson mostrando que Wilson nunca cruza el $0$; IC $F$ para razón de varianzas y prueba A/B verificados idénticos a las soluciones existentes; IC de Fisher para correlación exacto; **estudio de cobertura Monte Carlo revelando que Wald solo cubre 87.65\% cuando el nominal es 95\%, mientras Wilson cubre 95.64\%** --- confirmación numérica contundente de por qué Wilson es preferible).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/06_estimacion_estadistica/06.05_confidence_intervals_variances.tex` (17 frames) y `presentaciones/en/06_estimation_data_science/06.05_confidence_intervals_variances.tex` (20 frames), citando los problemas existentes `prob:ic_varianza`, `prob:dif_proporciones_ab`, `prob:ic_razon_varianzas` y `prob:ic-desaf-fisher`, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente a 660 páginas (`[Modelación Estadística].tex`); también se recompiló `[Statistical Modeling].tex` (458 páginas) sin errores.

### Reconciliación 1:1 del capítulo 07 — 2026-07-24 15:24:57 -06:00

Se cerró el bloque de las filas 42--45, 47--48 y 51--52 de la matriz, usando
las notas ES como fuente canónica.

- Se desarrollaron ocho mazos ES y se crearon ocho contrapartes EN:
  `07.02_ci_hypothesis_tests`, `07.03_p_values_decisions`,
  `07.04_one_mean_test`, `07.05_hypothesis_testing_guide`,
  `07.07_proportion_tests`, `07.08_variance_tests`,
  `07.11_homogeneity_tests` y `07.12_multiple_proportions`.
- Cada par tiene 22 frames, cero `\\lstinputlisting` y cero referencias a
  problemas sin resolver, `(p)` o `prob:`. No se añadió Python.
- `latex/en_guia_prueba_hipotesis.tex` quedó alineado con la fuente ES usando
  `\\section*` y `\\subsection*`.
- Los 16 mazos se compilaron dos veces con código 0. Los únicos avisos
  `Overfull \\vbox` pertenecen a la portada exenta; las páginas de contenido
  no presentan desbordamientos, errores, referencias indefinidas ni etiquetas
  duplicadas.
- La matriz queda en 65 mazos ES desarrollados, 72 mazos EN físicos y 23 filas
  completas de cuatro vías. El siguiente bloque es el capítulo 8.

No se creó commit ni se hizo `git push`; el capítulo 8 no se inicia en este
corte.

### Unidad 6 / Capítulo 07: Docimasia (Pruebas de Hipótesis) (catálogo histórico)
- $\checkmark$ **07.01 Fundamentos: $H_0$ vs. $H_1$, Errores Tipo I y II, y Potencia:** 100% completado (**APERTURA DEL CAPÍTULO 07**).
  - *Teoría del Libro Maestro:* `latex/pruebas_de_hipotesis.tex` (ES) y su espejo EN ya contenían un desarrollo completo (notación formal, tipos de prueba, errores Tipo I/II, nivel de significación, valor-$p$, regla de decisión, ejemplo íntegro), pero carecían de una fórmula formal para relacionar potencia con tamaño de muestra. Se agregó la subsección faltante "Potencia y Tamaño de Muestra": el teorema del tamaño de muestra $n=((Z_\alpha+Z_\beta)\sigma/(\mu_a-\mu_0))^2$ para una prueba $Z$ de una cola, con una observación sobre el *trade-off* triangular entre $\alpha$, $\beta$ y $n$.
  - *Cuaderno de Problemas:* **No existía un archivo `(p).tex` para esta sección** (a diferencia de `chi_cuadrada(p).tex` y `cuadernos de pruebas de hipótesis vigentes`, que sí existían). Se creó desde cero `latex/pruebas_de_hipotesis(p).tex` y su espejo `latex/en_pruebas_de_hipotesis(p).tex` con 10 problemas nuevos bajo la convención histórica 3-3-2-2 (Problemas 7.1.1 al 7.1.10): formulación de $H_0/H_a$, interpretación de errores Tipo I/II en contexto médico, prueba $Z$ completa, cálculo de $\beta$ y potencia, tamaño de muestra para potencia objetivo, deducción de la función de potencia general, tasa de error familiar (FWER) y corrección de Bonferroni, el Lema de Neyman-Pearson (optimalidad UMP del test $Z$), y la deducción rigurosa de la fórmula de tamaño de muestra desde las definiciones puras de $\alpha$ y $\beta$. Se conectó (`\input`) al libro maestro ES y EN justo después de `pruebas_de_hipotesis`.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.py` (tasa de Error Tipo I verificada vía Monte Carlo con 200,000 réplicas, $0.0503$ vs. $\alpha=0.05$ nominal; potencia analítica y empírica coincidentes para $\mu_a=108$; tamaño de muestra $n=31$ verificado empíricamente alcanzando potencia $0.9073$ vs. objetivo $0.90$, mientras $n=30$ se queda corto).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.01_hypothesis_testing_basics.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.01_hypothesis_testing_basics.tex` (17 frames), citando los problemas nuevos 7.1.1, 7.1.5, 7.1.7 y 7.1.9, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente (668 páginas ES); también se recompiló `[Statistical Modeling].tex` sin errores. Nota: se encontró un bloqueo transitorio de archivo (SumatraPDF con el PDF abierto) durante la primera compilación posterior a los cambios de la Sección 07.03; se resolvió reintentando la compilación.
- $\checkmark$ **07.02 Pruebas $Z$ y $t$ para Medias de Una y Dos Muestras:** 100% completado.
  - *Teoría del Libro Maestro:* `el archivo histórico de teoría de pruebas de hipótesis` (ES) y su espejo EN ya contenían teoremas rigurosos completos para los cuatro casos de comparación de dos medias (varianzas conocidas, varianza agrupada, Welch, pareadas), además de pruebas de proporciones, varianzas y homogeneidad. No se requirió teoría nueva.
  - *Cuaderno de Problemas:* Se auditó los cuadernos de pruebas de hipótesis vigentes y se confirmó que **ya contenía un cuaderno bajo la convención histórica 3-3-2-2 completo y de nivel avanzado** (10 problemas con etiquetas descriptivas `prob:doc_*`) cubriendo dos medias, proporciones, varianzas, homogeneidad y Marascuilo. No se creó un cuaderno nuevo para evitar duplicar contenido ya completo.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.02_z_t_tests_means.py` (prueba $t$ de una muestra verificada contra `scipy.stats.ttest_1samp`; comparación directa de varianza agrupada vs. Welch bajo homoscedasticidad y heteroscedasticidad, verificada contra `scipy.stats.ttest_ind`; prueba $t$ pareada verificada contra `scipy.stats.ttest_rel`).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.02_z_t_tests_means.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.02_z_t_tests_means.tex` (17 frames), citando los problemas existentes `prob:doc_dos_medias_iguales`, `prob:doc_welch_hetero`, `prob:doc_errores_potencia_muestra` y `prob:doc_desaf_lrt_wilks`, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* No requirió recompilación (no se modificó el libro maestro en esta sección); verificado indirectamente en la recompilación final del capítulo.
- $\checkmark$ **07.03 Pruebas de Bondad de Ajuste $\chi^2$:** 100% completado.
  - *Teoría del Libro Maestro:* `latex/chi_cuadrada.tex` (ES) y su espejo EN ya contenían la introducción, el estadístico, la distribución $\chi^2$ y un ejemplo de bondad de ajuste (dado), pero carecían de un teorema formal para la prueba de bondad de ajuste y la Regla de Cochran. Se agregó la subsección "Prueba formal de bondad de ajuste": el teorema con $\nu=k-1-m$ grados de libertad (donde $m$ es el número de parámetros estimados de la muestra), y una observación formalizando la Regla de Cochran (ningún $E_i<1$; máximo 20\% de celdas con $E_i<5$) y el procedimiento de fusión de celdas.
  - *Cuaderno de Problemas:* Se auditó `latex/chi_cuadrada(p).tex` y se confirmó que **ya contenía un cuaderno bajo la convención histórica 3-3-2-2 completo** (10 problemas, mezclando bondad de ajuste e independencia) con etiquetas `prob:3.9.*` y `prob:chi-*`. No se creó un cuaderno nuevo; se seleccionaron los 4 problemas de sabor "bondad de ajuste" para esta sección (3.9.1, 3.9.2, chi-analit-poisson, chi-desaf-teorema-pearson), dejando los de sabor "independencia/homogeneidad" para la Sección 07.04.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.py` (bondad de ajuste uniforme verificada contra `scipy.stats.chisquare`; ajuste Poisson con $\hat\lambda$ estimado y grados de libertad corregidos ($\nu=k-1-m$) verificado contra `scipy.stats.chisquare(ddof=1)`; violación de la Regla de Cochran detectada y corregida mediante fusión de celdas, con el estadístico recalculado).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.03_goodness_of_fit_tests.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.03_goodness_of_fit_tests.tex` (17 frames), citando los problemas existentes 3.9.1, 3.9.2, chi-analit-poisson y chi-desaf-teorema-pearson, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente tras agregar el teorema formal y la Regla de Cochran; también se recompiló `[Statistical Modeling].tex` sin errores.
- $\checkmark$ **07.04 Tablas de Contingencia y Pruebas de Independencia:** 100% completado (**CIERRE DEL CAPÍTULO 07**).
  - *Teoría del Libro Maestro:* `latex/chi_cuadrada.tex` (independencia) y `el archivo histórico de teoría de pruebas de hipótesis` (homogeneidad, Marascuilo) ya contenían teoría rigurosa y completa para esta sección (diferencia conceptual independencia vs. homogeneidad, estadístico común, procedimiento post-hoc de Marascuilo). No se requirió teoría nueva.
  - *Cuaderno de Problemas:* Se reutilizaron los problemas de sabor "independencia/homogeneidad" ya existentes en `latex/chi_cuadrada(p).tex` (3.9.3, 3.9.5, chi-analit-homogeneidad-z, chi-desaf-contingencia-2x2) y los cuadernos de pruebas de hipótesis vigentes (`prob:homogeneidad_contingencia`), citándolos directamente sin duplicar contenido.
  - *Laboratorio Python:* `presentaciones/code/07_pruebas_hipotesis/07.04_contingency_tables.py` (prueba de independencia en tabla $4\times3$ verificada contra `scipy.stats.chi2_contingency`; prueba de homogeneidad en 3 cohortes independientes con la misma fórmula pero diseño muestral distinto; **identidad exacta $Z^2=\chi^2$ verificada numéricamente a precisión de máquina** ($|\chi^2-Z^2|<10^{-10}$) en una tabla $2\times2$ de ensayo clínico).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/07_pruebas_hipotesis/07.04_contingency_tables.tex` (17 frames) y `presentaciones/en/07_hypothesis_testing/07.04_contingency_tables.tex` (17 frames), citando los problemas existentes 3.9.3, 3.9.5 y las secciones analítica/desafiante de contingencia $2\times2$, con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente (`[Modelación Estadística].tex` y `[Statistical Modeling].tex`), confirmando **0 errores y 0 referencias indefinidas** tras el cierre completo del Capítulo 07.

### Reconciliación 1:1 del capítulo 08 — 2026-07-24 15:41:01 -06:00

Se cerró el bloque de las filas 53, 55--56 y 58--59 de la matriz, tomando las
notas ES como fuente canónica.

- Se desarrollaron cinco mazos ES y se crearon cinco contrapartes EN:
  `08.01_experimental_strategies`, `08.03_fixed_effects`,
  `08.04_post_hoc_comparisons`, `08.06_randomized_blocks_latin_squares` y
  `08.07_factorial_designs`.
- Cada par tiene 22 frames, cero `\\lstinputlisting` y cero referencias a
  problemas sin resolver, `(p)` o `prob:`. No se añadió Python.
- `latex/en_efectos_modelo_fijo.tex` se alineó con la fuente ES en las marcas
  `section*`/`subsection*` y etiquetas `eq:esperanza_cmtr`,
  `tab:anova_un_factor` y `eq:tukey_hsd`. También se añadió
  `eq:modelo_dbca` a `latex/en_dbca_cuadrados_latinos.tex`.
- Los diez mazos se compilaron dos veces con código 0. Los únicos avisos
  `Overfull \\vbox` pertenecen a las portadas exentas; las páginas de contenido
  no presentan desbordamientos, errores, referencias indefinidas ni etiquetas
  duplicadas.
- La matriz queda en 70 mazos ES desarrollados, 77 mazos EN físicos y 28 filas
  completas de cuatro vías. El siguiente bloque es el capítulo 9.

No se creó commit ni se hizo `git push`; el capítulo 9 no se inicia en este
corte.

### Unidad 7 / Capítulo 08: Elementos de Diseño de Experimentos (ANOVA) (catálogo histórico)
- $\checkmark$ **Corrección previa:** se detectó y corrigió una corrupción de codificación en `latex/diseno_experimentos_anova.tex` --- 33 instancias del macro `\textbf{` habían perdido el carácter `\` y quedado como un carácter tabulador literal seguido de `extbf{` (probablemente por una sustitución automática defectuosa en una etapa histórica anterior al 2026-07-23), lo cual no producía errores de compilación pero renderizaba texto literal "extbf{...}" en lugar de negritas en el PDF. Se corrigió programáticamente a nivel de bytes y se recompiló el libro maestro dos veces, confirmando **0 errores y 0 referencias indefinidas**.
- $\checkmark$ **08.01 Análisis de Varianza de un Factor (One-Way ANOVA) y Prueba $F$:** 100% completado (**APERTURA DEL CAPÍTULO 08**).
  - *Teoría del Libro Maestro:* `latex/diseno_experimentos_anova.tex` (ES) y su espejo EN ya contenían un desarrollo íntegro y riguroso: fundamentos del DoE (los Tres Principios de Fisher), el modelo lineal paramétrico del ANOVA de un factor, el teorema de partición de sumas de cuadrados ($\text{SCT}=\text{SCTR}+\text{SCE}$), el estadístico $F$, los tres procedimientos post-hoc (LSD de Fisher, HSD de Tukey/Tukey-Kramer, Corrección de Bonferroni) y el Diseño en Bloques Completos al Azar (DBCA). No se requirió teoría nueva más allá de la corrección de codificación.
  - *Cuaderno de Problemas:* Se auditó los cuadernos de diseño experimental vigentes y se confirmó que **ya contenía un cuaderno bajo la convención histórica 3-3-2-2 completo** (10 problemas con etiquetas descriptivas, auto-numerados como Problemas 8.6.1 a 8.6.10 al compilar) cubriendo ANOVA de un factor, Tukey HSD, DBCA, LSD/Bonferroni, ANOVA desbalanceado con $R^2$, verificación de supuestos, potencia/tamaño de muestra, el Teorema de Cochran y la eficiencia relativa del DBCA. Se citaron los Problemas 8.6.3, 8.6.5, 8.6.8 y 8.6.9 (uno por nivel) sin duplicar contenido.
  - *Laboratorio Python:* `presentaciones/code/08_diseno_experimentos/08.01_one_way_anova.py` (descomposición SCT=SCTR+SCE para 4 configuraciones de servidor verificada contra `scipy.stats.f_oneway`; HSD de Tukey vía `scipy.stats.studentized_range`; Diseño en Bloques Completos al Azar con verificación de la identidad SCT=SCTR+SCB+SCE y cálculo de la Eficiencia Relativa del bloqueo, $\text{ER}\approx70.18$).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/08_diseno_experimentos/08.01_one_way_anova.tex` (17 frames) y `presentaciones/en/08_experimental_design/08.01_one_way_anova.tex` (17 frames), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, 4 ejercicios interactivos en clase (Niveles 1-4) con Enunciado/Resolución, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente (ES y EN) tras la corrección de codificación, confirmando **0 errores y 0 referencias indefinidas**.
- $\checkmark$ **08.02 Supuestos del ANOVA, Prueba de Levene/Bartlett y Diagnóstico:** 100% completado (**CIERRE DEL CAPÍTULO 08**).
  - *Teoría del Libro Maestro:* `latex/diseno_experimentos_anova.tex` (sección "Verificación de supuestos en ANOVA y aplicaciones en Ciencia de Datos") y su espejo EN ya contenían teoría completa sobre homoscedasticidad (Bartlett, Levene/Brown-Forsythe), normalidad de residuos (Q-Q Plot, Shapiro-Wilk, Kolmogorov-Smirnov), independencia, y las alternativas metodológicas (ANOVA de Welch, transformaciones Box-Cox, Kruskal-Wallis). No se requirió teoría nueva.
  - *Cuaderno de Problemas:* Se auditó los cuadernos de diseño experimental vigentes y se detectó que **solo 1 de los 10 problemas existentes** (Problema 8.6.7, Nivel Analítico) abordaba específicamente la verificación de supuestos --- insuficiente para cubrir los 4 niveles de dificultad requeridos por esta sección. Se agregaron **3 problemas nuevos** (Problemas 8.6.11 a 8.6.13, apéndice "Complemento --- Verificación de Supuestos") en ES y EN: cálculo del estadístico de Bartlett (Fundamental), la Prueba de Levene aplicada como ANOVA sobre desviaciones absolutas (Operativo), y la demostración formal de que Levene es algebraicamente idéntico al ANOVA de un factor aplicado a $Z_{ij}=|Y_{ij}-\bar Y_{i.}|$ (Desafiante). Se verificó que la numeración automática no alteró los problemas 8.6.1-8.6.10 ya citados en la Sección 08.01.
  - *Laboratorio Python:* `presentaciones/code/08_diseno_experimentos/08.02_anova_assumptions.py` (Prueba de Bartlett y Prueba de Levene centrada en la media verificadas contra `scipy.stats.bartlett` y `scipy.stats.levene(center='mean')`, con la implementación manual de Levene como ANOVA de un factor sobre $|Y_{ij}-\bar Y_{i.}|$ reproduciendo el estadístico de scipy exactamente, $W=2.9880$; Prueba de Shapiro-Wilk sobre residuos de un ANOVA de 3 grupos; comparación de ANOVA paramétrico vs. Kruskal-Wallis sobre datos exponenciales asimétricos).
  - *Mazos Beamer:* mazos pedagógicos ES/EN en `presentaciones/es/08_diseno_experimentos/08.02_anova_assumptions.tex` (17 frames) y `presentaciones/en/08_experimental_design/08.02_anova_assumptions.tex` (17 frames), citando los Problemas 8.6.11, 8.6.12, 8.6.7 y 8.6.13 (uno por nivel), con revelado progresivo `\pause`, puente numérico Python en 3 bloques, cero marcado informal y compilados con **0 `Overfull \vbox` y 0 `Overfull \hbox`** en contenido (portada exenta).
  - *Libro Maestro:* Recompilado limpiamente (`[Modelación Estadística].tex` y `[Statistical Modeling].tex`), confirmando **0 errores y 0 referencias indefinidas** tras el cierre completo del Capítulo 08.

### Reconciliación 1:1 del capítulo 09 — 2026-07-24 15:49:29 -06:00

Se cerró el bloque de las filas 62 y 70 de la matriz, usando las notas ES como
fuente canónica.

- Se desarrollaron dos mazos ES y se crearon dos contrapartes EN:
  `09.02_regresiones_lineales_section` y `09.11_model_summary`.
- Cada par tiene 22 frames, cero `\\lstinputlisting` y cero referencias a
  problemas sin resolver, `(p)` o `prob:`. No se añadió Python.
- Las notas ES/EN ya tenían secciones y etiquetas estructuralmente coincidentes;
  no fue necesario modificar teoría.
- Los cuatro mazos se compilaron dos veces con código 0. Los únicos avisos
  `Overfull \\vbox` pertenecen a las portadas exentas; las páginas de contenido
  no presentan desbordamientos, errores, referencias indefinidas ni etiquetas
  duplicadas.
- La matriz queda en 72 mazos ES desarrollados, 79 mazos EN físicos y 30 filas
  completas de cuatro vías. Este bloque cierra la etapa gradual de desarrollo de
  mazos prevista en el plan.

No se creó commit ni se hizo `git push`.

### Tema complementario / Capítulo 09: Regresiones Lineales y Múltiples (catálogo histórico)

**Nota de corrección estructural (2026-07-16):** una versión anterior de este capítulo agrupó 7 archivos de teoría distintos en una sola "Sección 09.01" (17 frames), violando la regla estructural del proyecto de que cada archivo/sección de las notas debe tener su propio mazo Beamer 1:1. Se corrigió dividiendo esa sección en 6 mazos independientes (09.01-09.06) y renumerando las 2 secciones que ya eran 1:1 correctas: la antigua **09.02 (regresión múltiple) → 09.07**, y la antigua **09.03 (diagnóstico de regresión) → 09.09**. Los huérfanos `introduccion_regresiones_lineales.tex` (superado por `regresiones_lineales.tex`, mismo patrón que el precedente del Capítulo 05) y `resumen_modelo.tex` (28 líneas de puro resumen ya cubierto por 09.07/09.09) no reciben mazo propio, igual que sus análogos en capítulos anteriores.

Directorio base Python: `presentaciones/code/09_regresiones/`. Todas las 12 secciones fueron recompiladas dos veces (ES+EN) confirmando **0 errores, 0 referencias indefinidas y 0 `Overfull \vbox`/`\hbox`** en contenido (portada exenta); el libro maestro (`[Modelación Estadística].tex` y `[Statistical Modeling].tex`) fue recompilado dos veces al cierre del capítulo con el mismo resultado limpio.

- $\checkmark$ **09.01 Correlación como Premisa de la Regresión** (**APERTURA DEL CAPÍTULO 09**). Teoría: `latex/correlacion.tex`. Mazo conceptual/motivacional (coeficiente de Pearson, rango, correlación $\neq$ causalidad) sin ejercicios numéricos propios --- cita hacia adelante a la Sección 09.02. Laboratorio: `09.01_correlation.py`. Mazos: `es/09_regresiones/09.01_correlation.tex` / `en/09_regressions/09.01_correlation.tex` (15 frames c/u).
- $\checkmark$ **09.02 Introducción a la Regresión Lineal.** Teoría: `latex/regresiones_lineales.tex` (huérfano respaldado: `introduccion_regresiones_lineales.tex`). Mazo conceptual (modelo estocástico vs. determinístico, cinco supuestos clásicos) sin ejercicios numéricos propios --- cita hacia adelante a la Sección 09.03. Laboratorio: `09.02_introduction_to_regression.py`. Mazos: `09.02_introduction_to_regression.tex` (15 frames c/u).
- $\checkmark$ **09.03 Matemáticas de la Regresión: Derivación MCO y $R^2$.** Teoría: `latex/matematicas_regresiones.tex`. Cuaderno: se citan los Problemas 9.8.7 (Analítico, $R^2=r^2$), 9.8.9 y 9.8.10 (Desafiante, deducción de ecuaciones normales e insesgo) de `latex/regresiones_lineales(p).tex`. Laboratorio: `09.03_mathematics_of_regression.py`. Mazos: `09.03_mathematics_of_regression.tex` (19 frames c/u).
- $\checkmark$ **09.04 Regresión Lineal sobre Datos Simulados.** Teoría: `latex/simulacion_regresion.tex`. Mazo íntegramente demostrativo: el laboratorio Python (parámetros poblacionales verdaderos conocidos, comparación recta ajustada vs. recta oráculo) constituye el ejercicio resuelto completo; sin cita formal de problemas del cuaderno. Laboratorio: `09.04_regression_on_simulated_data.py`. Mazos: `09.04_regression_on_simulated_data.tex` (13 frames c/u).
- $\checkmark$ **09.05 Coeficientes Óptimos, Pruebas $t$/$F$ y RSE.** Teoría: `latex/valores_optimos.tex`. Cuaderno: se citan los Problemas 9.8.4 y 9.8.6 (Operativo: prueba $t$ de la pendiente e IC) de `latex/regresiones_lineales(p).tex`. Laboratorio: `09.05_optimal_coefficients_and_tests.py`. Mazos: `09.05_optimal_coefficients_and_tests.tex` (16 frames c/u).
- $\checkmark$ **09.06 Implementación en Python con `statsmodels`.** Teoría: `latex/implementacion_regresion.tex`. Mazo demostrativo (comparación directa "motor manual" vs. `model.summary()`); sin cita formal de problemas. Laboratorio: `09.06_statsmodels_style_summary.py`. Mazos: `09.06_implementation_with_statsmodels.tex` (13 frames c/u).
- $\checkmark$ **09.07 Regresión Múltiple, Ecuación Normal y Regularización Ridge/Lasso** (**renumerado desde la antigua 09.02**). Teoría: `latex/regresion_multiple.tex` (incluye la Ecuación Normal matricial y Ridge/Lasso agregados en la etapa de corrección documentada antes del 2026-07-23). Cuaderno: se citan los Problemas 9.10.1, 9.10.4, 9.10.7 y 9.10.9 de `latex/regresion_multiple(p).tex`. Laboratorio: `09.07_multiple_linear_regression.py`. Mazos: `09.07_multiple_linear_regression.tex` (21 frames c/u), con Hoja de Ruta y cierre reescritos para la numeración final (el siguiente tema real es 09.08).
- $\checkmark$ **09.08 Validación de Modelos y $k$-fold Cross-Validation.** Teoría: `latex/validacion_modelo.tex` (ya completa, sin cambios). Mazo demostrativo (detección de sobreajuste con 15 predictores de ruido puro, $k$-fold desde cero, comparación de modelos vía CV); sin cita formal de problemas --- `latex/validacion_modelo(p).tex` ya existía completo y conectado al libro maestro, disponible para referencia directa del alumno. Laboratorio: `09.08_model_validation.py`. Mazos: `09.08_model_validation.tex` (13 frames c/u).
- $\checkmark$ **09.09 Diagnóstico de Residuos y Multicolinealidad (VIF)** (**renumerado desde la antigua 09.03**). Teoría: `latex/supuestos_regresion.tex`. Cuaderno: `latex/supuestos_regresion(p).tex` (creado en la etapa de corrección documentada antes del 2026-07-23, 10 problemas nuevos bajo la convención histórica 3-3-2-2 auto-numerados 9.14.1-9.14.10); se citan los Problemas 9.14.1, 9.14.5, 9.14.7 y 9.14.9. Laboratorio: `09.09_regression_diagnostics.py`. Mazos: `09.09_regression_diagnostics.tex` (21 frames c/u), con Hoja de Ruta y cierre reescritos (el siguiente tema real es 09.10).
- $\checkmark$ **09.10 Regresión con `scikit-learn`.** Teoría: `latex/regresion_scikit.tex`. Cuaderno nuevo: `latex/regresion_scikit(p).tex` (10 problemas bajo la convención histórica 3-3-2-2, auto-numerados 9.17.1-9.17.10); se citan los Problemas 9.17.2, 9.17.4, 9.17.7 y 9.17.9. Laboratorio: `09.10_scikit_learn_regression.py` --- **única excepción documentada en todo el proyecto a la regla numpy/scipy**: usa `sklearn` real (`LinearRegression`, `train_test_split`, `RFE`) porque el tema de la sección es la propia librería. Mazos: `09.10_scikit_learn_regression.tex` (20 frames c/u).
- $\checkmark$ **09.11 Variables Categóricas y Variables Muda.** Teoría: `latex/otros_problemas.tex` (mitad categórica; división conceptual del archivo). Cuaderno nuevo: `latex/otros_problemas_categoricas(p).tex` (10 problemas bajo la convención histórica 3-3-2-2, auto-numerados 9.19.1-9.19.10); se citan los Problemas 9.19.1, 9.19.5, 9.19.7 y 9.19.10. Laboratorio: `09.11_categorical_dummy_variables.py`. Mazos: `09.11_categorical_dummy_variables.tex` (20 frames c/u).
- $\checkmark$ **09.12 Transformaciones No Lineales y Regresión Polinomial** (**CIERRE DEL CAPÍTULO 09**). Teoría: `latex/otros_problemas.tex` (mitad no lineal). Cuaderno nuevo: `latex/otros_problemas_transformaciones(p).tex` (10 problemas bajo la convención histórica 3-3-2-2, auto-numerados 9.20.1-9.20.10); se citan los Problemas 9.20.1, 9.20.4, 9.20.7 y 9.20.9. Laboratorio: `09.12_nonlinear_polynomial_regression.py` (regresión polinomial como caso de regresión múltiple vía $Z=X^2$, comparación lineal vs. cuadrática con Prueba $F$ Parcial, y multicolinealidad polinomial vía VIF). Mazos: `09.12_nonlinear_polynomial_regression.tex` (19 frames c/u), con diapositiva final de cierre de capítulo sintetizando las 12 secciones.

---

## 4. Plan histórico de Armonización Estructural y Curricular (Notas y Presentaciones ES/EN)


Para resolver definitivamente la discrepancia de numeración reportada y asegurar la paridad bilingüe de todo el ecosistema (*tufte-book* en ES/EN + Beamer ES/EN + Python), se establece la siguiente hoja de ruta en 3 fases de ejecución estricta:

### Fase 1: Reordenamiento y Formalización en las Notas Maestras (`latex/`)
1. **Versión en Español (`el archivo histórico de teoría de distribuciones discretas`):**
   Reordenar los bloques teóricos dentro del archivo para que la progresión de secciones sea estrictamente consecutiva y coincida con el orden pedagógico de las distribuciones discretas:
   - **Sección 3.1:** Funciones de masa de probabilidad discretas (PMF y soporte) (`variables_aleatorias_discretas.tex`)
   - **Sección 3.2:** Función de distribución acumulada para variables aleatorias discretas (CDF) (`variables_aleatorias_discretas.tex`)
   - **Sección 3.3:** Esperanza matemática y varianza en variables aleatorias discretas (`variables_aleatorias_discretas.tex`)
   - **Sección 3.4:** Distribución Binomial y Bernoulli (`archivo histórico de teoría de distribuciones discretas`)
   - **Sección 3.5:** Distribuciones Geométrica y Binomial Negativa (`archivo histórico de teoría de distribuciones discretas` --- *Traslado inmediato después de Binomial*)
   - **Sección 3.6:** Distribución Hipergeométrica (`archivo histórico de teoría de distribuciones discretas` --- *Traslado tras Geométrica*)
   - **Sección 3.7:** Distribución de Poisson (`archivo histórico de teoría de distribuciones discretas`)
   - **Sección 3.8:** Distribución Multinomial (`archivo histórico de teoría de distribuciones discretas`)
   - **Sección 3.9:** Distribución Normal y aproximación continua (`archivo histórico de teoría de distribuciones discretas`)
   - **Sección 3.10:** Distribuciones discretas en ciencia de datos (`archivo histórico de teoría de distribuciones discretas`)
2. **Versión en Inglés (`latex/en_variables_aleatorias_discretas.tex` y `el archivo histórico EN de teoría de distribuciones discretas`):**
   Aplicar la misma jerarquía y reordenamiento en las notas en inglés (`[Statistical Modeling].tex`):
   - Elevar `Discrete Probability Functions` a **Section 3.1** y `Distribution Functions` a **Section 3.2**.
   - Redactar e integrar **Section 3.3:** `Mathematical Expectation and Variance of Discrete Random Variables`.
   - Reordenar `el archivo histórico EN de teoría de distribuciones discretas` en **Sections 3.4 a 3.10** en simetría 1:1 exacta con la versión en español.
3. **Certificación de Compilación del Libro:** Compilar dos veces tanto `[Modelación Estadística].tex` como `[Statistical Modeling].tex` para validar las tablas de contenido (`.toc`) y las referencias cruzadas.

### Fase 2: Renombramiento y Alinear Títulos en Mazos Beamer (`presentaciones/`)
1. Auditores y ajuste de subtítulos (`\subtitle{Sección 03.XX --- ...}`) en los mazos existentes `03.01` a `03.06` en las carpetas `presentaciones/es/03_variables_aleatorias_discretas/` y `presentaciones/en/03_discrete_random_variables/`.
2. Verificar que los identificadores de archivo (`03.01` a `03.06`) mapeen en simetría total 1:1 con las Secciones 3.1 a 3.6 formalizadas en la Fase 1.

### Fase 3: Desarrollo Curricular de las Secciones Faltantes (03.07 a 03.10)
Con el nuevo ordenamiento consolidado, el desarrollo de temas restantes del Capítulo 3 abarcará los siguientes 4 módulos, cada uno ejecutado bajo la estructura de oro (**10 Problemas convención histórica 3-3-2-2 en `(p).tex` ES/EN $\to$ Script Python en inglés $\to$ 22 Slides Beamer ES/EN con 0 Overfulls**):
- **Sección 03.07:** Distribución de Poisson y Procesos de Llegada (`03.07_poisson_distribution.py`, mazos ES/EN de 22 diapositivas).
- **Sección 03.08:** Distribución Multinomial y Ensayos Politómicos (`03.08_multinomial_distribution.py`, mazos ES/EN de 22 diapositivas).
- **Sección 03.09:** Distribución Normal y Aproximación Continua de Variables Discretas (`03.09_normal_approximation.py`, mazos ES/EN de 22 diapositivas).
- **Sección 03.10:** Distribuciones Discretas en Ciencia de Datos y Casos Prácticos (`03.10_discrete_distributions_data_science.py`, mazos ES/EN de 22 diapositivas).

---

## 5. Protocolo histórico de Arranque para la Sección 04.07 --- COMPLETADO

**Estado: ejecutada y cerrada.** La Sección 04.07 (Distribuciones Gamma, Beta y Weibull) fue completada siguiendo el protocolo de 6 pasos descrito abajo, cerrando el Capítulo 04 al 100%. Esta guía se conserva como referencia histórica del protocolo aplicado; la siguiente intervención fechada debe iniciar la **Sección 05.01** (ver Sección 5 de este documento, Unidad 4 / Capítulo 05).

<details>
<summary>Protocolo de 6 pasos ejecutado para la 04.07 (referencia histórica)</summary>

**Secciones 04.01 a 04.06 del Capítulo 04 completadas.** Cuando un nuevo agente inicie en esta u otra computadora con el fin de continuar el proyecto, deberá ejecutar de inmediato la **Sección 04.07: Distribuciones Gamma, Beta y Weibull**, siguiendo este protocolo exacto de 6 pasos:

### Paso 1: Auditoría de Teoría y Creación/Integración de `(p).tex`
1. Consultar el archivo histórico de teoría de variables continuas (donde se ubica la teoría de las distribuciones Gamma, Beta y Weibull).
2. Verificar si los cuadernos de variables continuas vigentes cubren los problemas de la 04.07. Si no existen, agregar los 10 problemas bajo la convención histórica `3-3-2-2` usando los entornos institucionales (`\begin{problema}`, `\begin{sugerencia}`, `\begin{solucion}`):
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

## 6. Mapeo curricular histórico — Capítulos 03 al 09

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
- **Sección 04.05:** Distribución Normal / Gaussiana ($N(\mu, \sigma^2)$) y Puntaje $Z$ (`04.05_normal_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.
- **Sección 04.06:** Distribución Exponencial y Procesos Continuos Sin Memoria (`04.06_exponential_distribution.py`). **100% COMPLETADO** — ver descripción detallada arriba.
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

### Unidad 7 / Capítulo 08: Elementos de Diseño de Experimentos (ANOVA) (`Avance actual: 2 de 2 secciones completadas --- 100% FINALIZADO`)
Directorio base Python: `presentaciones/code/08_diseno_experimentos/`
- **Sección 08.01:** Análisis de Varianza de un Factor (ANOVA 1-Way) y Prueba $F$ (`08.01_one_way_anova.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 08.02:** Supuestos del ANOVA, Prueba de Levene/Bartlett y Diagnóstico (`08.02_anova_assumptions.py`). **100% COMPLETADO** --- ver descripción detallada arriba.

---

### Tema Complementario / Capítulo 09: Regresiones Lineales y Múltiples (`Avance actual: 12 de 12 secciones completadas --- 100% FINALIZADO`)
Directorio base Python: `presentaciones/code/09_regresiones/`
- **Sección 09.01:** Correlación como Premisa de la Regresión (`09.01_correlation.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.02:** Introducción a la Regresión Lineal (`09.02_introduction_to_regression.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.03:** Matemáticas de la Regresión: Derivación MCO y $R^2$ (`09.03_mathematics_of_regression.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.04:** Regresión Lineal sobre Datos Simulados (`09.04_regression_on_simulated_data.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.05:** Coeficientes Óptimos, Pruebas $t$/$F$ y RSE (`09.05_optimal_coefficients_and_tests.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.06:** Implementación en Python con `statsmodels` (`09.06_statsmodels_style_summary.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.07:** Regresión Lineal Múltiple, Ecuación Normal y Regularización Ridge/Lasso (`09.07_multiple_linear_regression.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.08:** Validación de Modelos y $k$-fold Cross-Validation (`09.08_model_validation.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.09:** Diagnóstico de Residuos, Multicolinealidad (VIF) y Supuestos Clásicos (`09.09_regression_diagnostics.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.10:** Regresión con `scikit-learn` (`09.10_scikit_learn_regression.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.11:** Variables Categóricas y Variables Muda (`09.11_categorical_dummy_variables.py`). **100% COMPLETADO** --- ver descripción detallada arriba.
- **Sección 09.12:** Transformaciones No Lineales y Regresión Polinomial (`09.12_nonlinear_polynomial_regression.py`). **100% COMPLETADO** --- ver descripción detallada arriba (**CIERRE DEL CAPÍTULO 09**).

---

## 7. Referencia de Comandos Rápida para Agentes AI

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
