# Plan Maestro de Reestructuración Pedagógica — Capítulos 04 al 09 (Notas y Presentaciones en ES/EN)

## 1. Goal Description
El objetivo es auditar integralmente la jerarquía actual de los **Capítulos 04 al 09** en las notas maestras en español (`latex/*.tex`) e inglés (`latex/en_*.tex`), identificando qué subsecciones (`\subsection`) conviene **elevar al rango de Sección principal (`\section`)** (por exceso de condensación teórica) y qué secciones fragmentadas conviene **consolidar en módulos pedagógicos coherentes** (por exceso de dispersión). 

Este rediseño garantiza que cada sección del libro sea **compacta, manejable, digerible** y se traduzca de forma exacta y simétrica (1:1) en una presentación Beamer de 20 a 22 diapositivas y un laboratorio reproducible de Python en inglés.

---

## 2. User Review Required

> [!IMPORTANT]
> **Aprobación de Arquitectura Modular:**
> La siguiente tabla muestra el diagnóstico de problemas actuales en el índice (`.toc`) y la solución propuesta para cada capítulo del libro maestro (`[Modelación Estadística].tex` y `[Statistical Modeling].tex`). Al aprobar este plan, las notas en español e inglés adoptarán esta estructura formal para alinear todas las presentaciones futuras.

> [!TIP]
> **Beneficio Pedagógico:**
> Con este plan, ningún tema durará más de 1 sesión de clase o 1 mazo Beamer (`22 slides`), eliminando secciones "monstruo" de más de 30 páginas y secciones "fragmento" de 2 páginas.

---

## 3. Propuesta Curricular Detallada por Capítulo

### Capítulo 04: Variables Aleatorias Continuas
#### Diagnóstico Actual
Actualmente la Sección `4.3` (*Distribuciones continuas avanzadas*) aglomera en un solo bloque la Distribución Uniforme, Normal, Gamma, Exponencial, Chi-cuadrada y las Funciones Generadoras de Momentos (FGM). Es pedagógicamente inabarcable en una sola presentación.

#### Reestructuración Propuesta (Elevación de Subsecciones $\to$ 7 Secciones Modularizadas)
| Nueva Sección | Título Propuesto (Español / Inglés) | Subsección Elevada / Origen en `latex/` |
| :--- | :--- | :--- |
| **Sección 4.1** | Función de Densidad de Probabilidad (PDF) y Soporte Continuo | `4.1 Variables aleatorias continuas` (Conceptos base) |
| **Sección 4.2** | Función de Distribución Acumulada (CDF) Continua y Cuantiles | `\subsection{Distribución conjunta y condicional / CDF}` |
| **Sección 4.3** | Esperanza Matemática, Varianza y Teorema LOTUS Continuo | `4.2 Esperanza matemática y momentos` |
| **Sección 4.4** | Distribución Uniforme Continua ($U(a,b)$) | Elevar `\subsection{Distribución uniforme continua}` en `4.3` |
| **Sección 4.5** | Distribución Exponencial y Procesos Continuos Sin Memoria | Elevar `\subsubsection{Caso particular: exponencial}` en `4.3` |
| **Sección 4.6** | Distribución Normal / Gaussiana ($N(\mu, \sigma^2)$) y Puntaje $Z$ | Elevar `\subsection{Distribución normal}` en `4.3` |
| **Sección 4.7** | Distribuciones Gamma, Beta, Weibull y FGM | Elevar `\subsection{Distribuciones gamma}` y `\subsection{FGM}` |

---

### Capítulo 05: Distribuciones de Muestreo
#### Diagnóstico Actual
La Sección `5.2` (*Distribuciones de muestreo*) está severamente saturada: mezcla teoremas de transformación lineal, distribuciones Chi-cuadrada ($\chi^2$), $t$ de Student, $F$ de Snedecor y aplicaciones en Ciencia de Datos (A/B testing, Bootstrap y Machine Learning).

#### Reestructuración Propuesta (Elevación de Subsecciones $\to$ 5 Secciones Modularizadas)
| Nueva Sección | Título Propuesto (Español / Inglés) | Subsección Elevada / Origen en `latex/` |
| :--- | :--- | :--- |
| **Sección 5.1** | Muestreo Aleatorio Simple y Transformación de Variables | `5.1 Introducción` + `\subsection{Transformación de variables}` |
| **Sección 5.2** | Teorema del Límite Central (TLC) y Ley de Grandes Números | Elevar `5.3 Conceptos TLC y LGN` al 2º lugar pedagógico |
| **Sección 5.3** | Distribución Chi-Cuadrada ($\chi^2(k)$) y Varianza Muestral | Elevar `\subsection{Distribución chi-cuadrada}` en `5.2` |
| **Sección 5.4** | Distribución $t$ de Student ($t(\nu)$) y Muestras Pequeñas | Elevar `\subsection{Distribución t de Student}` / `5.4` |
| **Sección 5.5** | Distribución $F$ de Snedecor y Aplicaciones en Ciencia de Datos | Elevar `\subsection{Distribución F}` + `A/B testing & Bootstrap` |

---

### Capítulo 06: Estimación y su Relación con Ciencia de Datos
#### Diagnóstico Actual
La Sección `6.1` combina Máxima Verosimilitud (MLE) y Método de Momentos (MoM) en una misma sesión. A su vez, la `6.3` mezcla intervalos de confianza de medias, proporciones, varianzas y cálculo de tamaño muestral.

#### Reestructuración Propuesta (Elevación y Desglose $\to$ 5 Secciones Modularizadas)
| Nueva Sección | Título Propuesto (Español / Inglés) | Subsección Elevada / Origen en `latex/` |
| :--- | :--- | :--- |
| **Sección 6.1** | Estimación Puntual, Insesgadez, Eficiencia y Consistencia | `6.1 Introducción a las propiedades de los estimadores` |
| **Sección 6.2** | Método de Momentos (MoM) | Elevar `\subsection{Método de Momentos (MoM)}` en `6.1` |
| **Sección 6.3** | Estimación por Máxima Verosimilitud (MLE) y Score | Elevar `\subsection{Método de Máxima Verosimilitud}` en `6.1` |
| **Sección 6.4** | Intervalos de Confianza para Medias ($Z$ y $t$) y Tamaño Muestral | Separar de `6.3`: enfoque en Medias de 1 y 2 poblaciones |
| **Sección 6.5** | Intervalos de Confianza para Varianzas ($\chi^2$) y Proporciones ($p$) | Separar de `6.3`: enfoque en Proporciones y Varianzas |

---

### Capítulo 07: Docimasia (Pruebas de Hipótesis)
#### Diagnóstico Actual
La Sección `7.4` agrupa en una sola unidad pruebas tan diversas como comparación de dos medias con varianzas desiguales, pruebas de proporciones, pruebas de razón de varianzas ($F$), y pruebas de homogeneidad vs. independencia en tablas de contingencia.

#### Reestructuración Propuesta (Elevación y Desglose $\to$ 4 Secciones Modularizadas)
| Nueva Sección | Título Propuesto (Español / Inglés) | Subsección Elevada / Origen en `latex/` |
| :--- | :--- | :--- |
| **Sección 7.1** | Fundamentos de Docimasia: $H_0$ vs $H_1$, Errores y Valor-$p$ | Consolidación de `7.1` y la guía paso a paso `7.2` |
| **Sección 7.2** | Pruebas $Z$ y $t$ para Medias y Proporciones (1 y 2 Muestras) | Elevar `Pruebas sobre dos medias y proporciones` de `7.4` |
| **Sección 7.3** | Pruebas de Bondad de Ajuste $\chi^2$ y Pruebas de Varianzas ($F$) | Consolidar `7.3 Prueba chi-cuadrada` con `Pruebas de varianzas` |
| **Sección 7.4** | Tablas de Contingencia, Pruebas de Independencia y Homogeneidad | Elevar `Pruebas de homogeneidad vs independencia` de `7.4` |

---

### Capítulo 08: Elementos de Diseño de Experimentos (ANOVA)
#### Diagnóstico Actual
La estructura actual (`8.1` a `8.6`) tiene secciones de 1 página (como `8.1` y `8.4`). Para hacer los temas robustos y equilibrados, se propone compactar el capítulo en **2 Secciones maestras completas**, o bien mantener 4 secciones formales equilibradas.

#### Reestructuración Propuesta ($\to$ 2 Secciones Maestras Equilibradas)
| Nueva Sección | Título Propuesto (Español / Inglés) | Subsección Elevada / Origen en `latex/` |
| :--- | :--- | :--- |
| **Sección 8.1** | Análisis de Varianza de un Factor (One-Way ANOVA) y Fundamentos DoE | Consolidación de `8.1 Fundamentos DoE` y `8.2 One-Way ANOVA` |
| **Sección 8.2** | Pruebas Post-Hoc, Bloques Completos al Azar (DBCA) y Diagnóstico | Consolidar `8.3 Post-hoc`, `8.4 DBCA` y `8.5 Diagnóstico de supuestos` |

---

### Capítulo 09: Regresiones Lineales y Múltiples
#### Diagnóstico Actual
El Capítulo 9 sufre de hiper-fragmentación: tiene **16 secciones (`9.1` a `9.16`)**, donde varias son únicamente páginas introductorias o listados de código sueltos, diluyendo el hilo conductor inferencial.

#### Reestructuración Propuesta (Consolidación de 16 Secciones $\to$ 4 Secciones Maestras)
| Nueva Sección | Título Propuesto (Español / Inglés) | Subsección Elevada / Origen en `latex/` |
| :--- | :--- | :--- |
| **Sección 9.1** | Correlación y Regresión Lineal Simple (OLS, Mínimos Cuadrados y $R^2$) | Consolidar las actuales `9.1 a 9.8` (Teoría, demostraciones y OLS 1-var) |
| **Sección 9.2** | Regresión Lineal Múltiple, Multicolinealidad (VIF) y Selección | Consolidar `9.9` y `9.10` (Ecuación normal, Ridge/Lasso y VIF) |
| **Sección 9.3** | Diagnóstico de Residuos, Supuestos Clásicos y Transformaciones | Consolidar `9.13` y `9.16` (Durbin-Watson, Breusch-Pagan, Q-Q, variables categóricas) |
| **Sección 9.4** | Validación de Modelos y Machine Learning con `scikit-learn` | Consolidar `9.11`, `9.12`, `9.14` y `9.15` ($k$-fold CV y Train/Test Split) |

---

## 4. Proposed Changes (Archivos Afectados en `latex/`)

Cuando se apruebe el inicio de ejecución para un capítulo en particular (o de manera progresiva conforme avancemos en la escritura de presentaciones), las modificaciones en LaTeX se aplicarán simétricamente en ambos idiomas:

### Archivos de Variables Aleatorias Continuas (`Capítulo 04`)
- `[MODIFY]` `variables_aleatorias_continuas.tex` / `en_variables_aleatorias_continuas.tex`
- `[MODIFY]` `distribuciones_continuas.tex` / `en_distribuciones_continuas.tex`

### Archivos de Distribuciones de Muestreo (`Capítulo 05`)
- `[MODIFY]` `introduccion_inferencia.tex` / `en_introduccion_inferencia.tex`
- `[MODIFY]` `distribuciones_muestreo.tex` / `en_distribuciones_muestreo.tex`

### Archivos de Estimación (`Capítulo 06`)
- `[MODIFY]` `estimacion_puntual.tex` / `en_estimacion_puntual.tex`
- `[MODIFY]` `estimacion_intervalos.tex` / `en_estimacion_intervalos.tex`

### Archivos de Pruebas de Hipótesis (`Capítulo 07`)
- `[MODIFY]` `pruebas_hipotesis.tex` / `en_pruebas_hipotesis.tex`
- `[MODIFY]` `pruebas_z_t.tex` / `en_pruebas_z_t.tex`

### Archivos de Diseño de Experimentos (`Capítulo 08`) y Regresión (`Capítulo 09`)
- `[MODIFY]` `anova.tex` / `en_anova.tex`
- `[MODIFY]` `regresion_lineal.tex` / `en_regresion_lineal.tex`
- `[MODIFY]` `regresion_multiple.tex` / `en_regresion_multiple.tex`

---

## 5. Verification Plan
1. **Doble Compilación Sin Ruptura de Enlaces:**
   Verificar que `pdflatex` compile sin errores tanto `[Modelación Estadística].tex` como `[Statistical Modeling].tex`.
2. **Inspección del TOC:**
   Confirmar que el índice autogenerado refleje exactamente las nuevas secciones compactas y que desaparezcan las agrupaciones gigantescas y las secciones de una sola carilla.
