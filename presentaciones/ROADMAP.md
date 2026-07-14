# Hoja de Ruta y Trabajo Pendiente (Presentaciones Beamer & Labs Python)

Este documento detalla el estado global del proyecto en la rama `crear-presentaciones`, la planeación curricular de las siguientes unidades del sílabo oficial (**MA1001B** --- *Modelación Estadística*) y las instrucciones exactas para que el siguiente agente inicie el trabajo de forma ágil y coordinada.

---

## 1. Estado Global del Proyecto

- **Capítulo 01: Estadística Descriptiva (Contenido Suplementario)** $\to$ *Pendiente de presentaciones* (Nota: el libro no incluye `estadistica-descriptiva.tex` en la master actual; es contenido de soporte).
- **Capítulo 02: Teoría de la Probabilidad (Unidad 1 del Sílabo Oficial)** $\to$ $\checkmark$ **100% COMPLETADO Y VERIFICADO**
  - Secciones `02.01` a `02.06`: Presentaciones en español e inglés listas, compiladas con cero advertencias de desbordamiento, y laboratorios computacionales en Python puros (`numpy`/`scipy`) en `presentaciones/code/02_teoria_probabilidad/`.
- **Capítulo 03: Variables Aleatorias Discretas y Distribuciones de Probabilidad (Unidad 2)** $\to$ **EN DESARROLLO (Secciones 03.01 y 03.02 Completadas)**
  - $\checkmark$ **Sección 03.01: Funciones de Probabilidad Discretas (PMF y Soporte)** $\to$ *Completada (20 diapositivas ES/EN, 0 warnings, lab `03.01_pmf_and_support.py`)*
  - $\checkmark$ **Sección 03.02: Función de Distribución Acumulada (CDF Discreta)** $\to$ *Completada (20 diapositivas ES/EN, 0 warnings, lab `03.02_discrete_cdf.py`, 10 problemas 3-3-2-2)*
  - **$\leftarrow$ PRÓXIMO OBJETIVO INMEDIATO: Sección 03.03: Esperanza Matemática y Varianza Operacional**
- **Capítulo 04: Variables Aleatorias Continuas y sus Distribuciones (Unidad 3)** $\to$ *Pendiente*
- **Capítulo 05: Distribuciones Muestrales y Teoremas Límites (Unidad 4)** $\to$ *Pendiente*
- **Capítulo 06: Estimación Puntual e Intervalos de Confianza (Unidad 5)** $\to$ *Pendiente*
- **Capítulo 07: Pruebas de Hipótesis (Unidad 6)** $\to$ *Pendiente*
- **Capítulo 08: Análisis de Varianza (ANOVA) y Pruebas Chi-Cuadrada (Unidad 7)** $\to$ *Pendiente*
- **Capítulo 09: Regresiones Lineales y Múltiples (Contenido Suplementario)** $\to$ *Pendiente*

---

## 2. Planificación Curricular --- Próxima Unidad: Capítulo 03 (Unidad 2 del Sílabo)

El **Capítulo 03: Variables Aleatorias Discretas** formaliza el paso del álgebra de eventos (`\Omega`) a funciones numerables con masa probabilística y momentos algebraicos.

### Inventario de Secciones a Desarrollar (Capítulo 03)
A partir de la estructura del libro maestro y el sílabo, se desarrollarán las siguientes 9 secciones (cada una con: cuaderno de problemas 3-3-2-2 en `latex/`, script de Python en `presentaciones/code/03_variables_aleatorias_discretas/` y dos mazos Beamer en `presentaciones/es/03_variables_aleatorias_discretas/` y `presentaciones/en/03_discrete_random_variables/`):

1. $\checkmark$ **Sección 03.01: Conceptos Básicos y Función de Masa de Probabilidad (PMF)** *(100% COMPLETADA)*
   - *Foco teórico:* Definición medible de V.A. discreta, condiciones de normalización $\sum p_X(x) = 1$.
   - *Lab Python (`03.01_pmf_and_support.py`):* Verificación empírica de PMFs custom y muestreo por transformación inversa.
2. $\checkmark$ **Sección 03.02: Función de Distribución Acumulada (CDF) Discreta** *(100% COMPLETADA)*
   - *Foco teórico:* Propiedades escalonadas por la derecha (cadlag), saltos de probabilidad y cuantiles discretos.
   - *Lab Python (`03.02_discrete_cdf.py`):* Construcción numérico-vectorial de mesetas CDF, inversión $\Delta F(x)$ e intervalos.
3. $\checkmark$ **Sección 03.03: Esperanza Matemática, Varianza y Momentos** *(100% COMPLETADA)*
   - *Foco teórico:* Linealidad de la esperanza, teorema de la ley del estadístico inconsciente (LOTUS) en discretas, identidad computacional $\text{Var}(X) = E(X^2) - [E(X)]^2$, estandarización $Z$-score y Teorema del Centro de Gravedad.
   - *Lab Python (`03.03_expectation_and_variance.py`):* Cálculo de momentos brutos y centrales (`numpy`), verificación LOTUS, invariantes en estandarización $Z$ y simulación Monte Carlo de la LLN.
4. $\rightarrow$ **Sección 03.04: Distribuciones de Bernoulli y Binomial** *(FOCO ACTUAL)*
   - *Foco teórico:* Ensayos independientes, coeficientes binomiales, $\text{Bin}(n,p)$ como suma de Bernoullis.
   - *Lab Python (`03.04_bernoulli_binomial.py`):* Simulación de inspección de piezas o control de calidad ($n$ ensayos, tasa de fallo $p$).
5. **Sección 03.05: Distribuciones Geométrica y Binomial Negativa**
   - *Foco teórico:* Tiempo de espera hasta el 1er éxito (y hasta el $r$-ésimo éxito), propiedad de pérdida de memoria de la Geométrica.
   - *Lab Python (`03.05_geometric_negative_binomial.py`):* Simulación computacional de colas y fallas en servidores hasta caídas sucesivas.
6. **Sección 03.06: Distribución Hipergeométrica**
   - *Foco teórico:* Muestreo sin reemplazo de tamaño $n$ en población $N$ con $K$ éxitos, convergencia a Binomial si $N \to \infty$.
   - *Lab Python (`03.06_hypergeometric.py`):* Simulación de lotes industriales con piezas defectuosas sin reemplazo.
7. **Sección 03.07: Distribución de Poisson y Procesos de Poisson**
   - *Foco teórico:* Ley de eventos raros ($\lambda = np$), intervalos de tiempo continuo conteo en intervalo $[0, t]$.
   - *Lab Python (`03.07_poisson_distribution.py`):* Aproximación Binomial-Poisson y simulación de llegadas de paquetes en redes o llamadas en call-centers.
8. **Sección 03.08: Momentos y Funciones Generadoras de Momentos (MGF)**
   - *Foco teórico:* $M_X(t) = E(e^{tX})$, obtención de derivadas en el origen para calcular momentos, unicidad e independencia por producto de MGFs.
   - *Lab Python (`03.08_moment_generating_functions.py`):* Evaluaciones numéricas de MGF para verificar derivadas parciales numéricamente (`scipy.misc.derivative` o diferencias finitas en `numpy`).
9. **Sección 03.09: Desigualdades Probabilísticas en V.A. Discretas**
   - *Foco teórico:* Cota de Markov para variables no negativas ($P(X \ge a) \le E(X)/a$), Cota de Chebyshev reformulada para dispersión de variables discretas.
   - *Lab Python (`03.09_probability_inequalities.py`):* Verificación empírica masiva de que los porcentajes empíricos de cola extrema respetan estrictamente los topes teóricos de Markov y Chebyshev.

---

## 3. Instrucciones de Arranque para la Próxima Sesión (Para el Subagente)

Cuando inicies una nueva sesión con el objetivo de continuar el desarrollo:

1. **Revisa la documentación maestro:** Lee cuidadosamente `presentaciones/README.md` (Las 4 Reglas de Oro y el checklist de 6 pasos).
2. **Crea o verifica la estructura de carpetas:**
   ```bash
   mkdir -p presentaciones/code/03_variables_aleatorias_discretas
   mkdir -p presentaciones/es/03_variables_aleatorias_discretas
   mkdir -p presentaciones/en/03_discrete_random_variables
   ```
3. **Comienza con la Sección 03.04 (`03.04_bernoulli_binomial`):**
   - Consulta el archivo `latex/variables_aleatorias_discretas.tex` y el companion `variables_aleatorias_discretas(p).tex` para formalizar y resolver problemas bajo la taxonomía 3-3-2-2.
   - Aplica el flujo integral y no termines la sección hasta comprobar en la terminal con `pdflatex` que las presentaciones PDF en español e inglés tienen exactamente 0 `Overfull \vbox` y 0 `Overfull \hbox` en todas sus diapositivas de contenido.
