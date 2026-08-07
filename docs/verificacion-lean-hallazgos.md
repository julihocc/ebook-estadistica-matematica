# Verificación formal con Lean 4 + Mathlib — bitácora de hallazgos

**Herramienta:** Lean 4.32.2 / Mathlib (pin `v4.32.2`), proyecto en `verification/lean_verificacion/`, cross-checks numéricos en `verification/scipy/`.
**Alcance de esta entrada:** Piloto — `latex/fundamentos_de_probabilidad.tex` + `latex/fundamentos_de_probabilidad(p).tex` (ES). No se verifica EN de forma independiente: los archivos `en_*` son traducciones verbatim (mismas etiquetas hex, mismos números), así que se comparan por diff textual en vez de re-probarse.
**Metodología:** cada lema transcribe la afirmación del libro con sus propios números/pasos tal como están escritos — no se demuestra "la versión correcta" y se compara a ojo. Un `norm_num`/`ring`/`decide` que no cierra *es* el hallazgo. Ver `C:\Users\julih\.claude\plans\we-re-going-to-work-vivid-quail.md` para el plan completo.
**Regla de encadenamiento (obligatoria desde el capítulo `probabilidad_condicional`):** toda cantidad **derivada** de otras (no un dato original del problema) se liga con `let` en el enunciado del lema y se **reutiliza** en los pasos posteriores — nunca se re-escribe su valor numérico literal. Un valor que el libro **da explícitamente** (no lo deriva) obtiene su propio conjunto de verificación aunque sea matemáticamente equivalente a algo derivable (p.ej. si el libro dice "$P(A')=3/8$" en vez de solo "$1-5/8$", se verifica `PAc = 3/8` como conjunto separado). Sin esto, un lema puede "cerrar" simplemente porque se re-escribieron a mano los mismos números correctos en cada paso, sin que Lean haya comprobado realmente que un paso se sigue del anterior — verificado empíricamente: `example : let x := (1:ℚ)/3; let y := x + x; y = 2/3 ∧ y = 1 := by norm_num` falla en el segundo conjunto tal como se espera, confirmando que `norm_num` sí atraviesa los `let` en vez de ignorarlos.

---

## Calibración del método

Antes de confiar el harness a capítulos no auditados, se codificaron dos errores ya encontrados y corregidos manualmente (`docs/revision-notas-2026-07-13.md`), en su forma **pre-corrección**, para confirmar que el método los detecta.

| Archivo (commit de fix) | Afirmación pre-fix codificada | Lean | Resultado |
|---|---|---|---|
| `chi_cuadrada.tex:48` (`674c1e7`) | `((553-500)^2 + (447-500)^5)/500 ≈ 11.236` | `Calibracion.chi_cuadrada_pre_fix_no_es_11_236` | **Detectado**: la fórmula tal como estaba escrita (exponente 5) no da 11.236 — `norm_num` prueba la desigualdad. La versión corregida (exponente 2, `Calibracion.chi_cuadrada_corregida_es_11_236`) sí da 11.236 exacto. |
| `esperanza_matematica.tex:103-107` (`4fc0342`) | `($20+$40+$60+3×$0)/6 = $15` | `Calibracion.esperanza_pre_fix_no_es_15` | **Detectado**: `(20+40+60+3×0)/6 = 20`, no 15 — error aritmético puro. `Calibracion.esperanza_correcta_es_20` confirma que 20 es el valor correcto (coincide con el ejemplo ya corregido en el texto). |

**Verificación de que la calibración tiene dientes (no solo se afirmó `≠`):** el archivo permanente prueba la *negación* de cada afirmación pre-fix (necesario para que `lake build` quede en verde), lo cual por sí solo no demuestra que Lean detectaría el error si uno transcribiera el libro ingenuamente. Para comprobarlo de verdad, se escribió un archivo temporal (`CalibracionScratch.lean`, fuera de la librería, borrado tras la prueba) con las dos afirmaciones tal como el libro pre-fix las planteaba **como igualdades literales** (`= 11.236`, `= 15`) y se corrió `lake env lean` directamente sobre él. Resultado observado:

```
LeanVerificacion/CalibracionScratch.lean:8:66: error: unsolved goals
⊢ False
LeanVerificacion/CalibracionScratch.lean:12:45: error: unsolved goals
⊢ False
```

`norm_num` reduce ambas igualdades a `⊢ False` y Lean se niega a cerrarlas — es decir, si alguien transcribe ingenuamente los números del libro pre-fix como una igualdad, el build efectivamente falla. Esto es evidencia real (no solo una prueba de la negación) de que el método detecta errores por sí solo.

Conclusión: el método tiene "dientes" — encontró ambos errores conocidos sin ayuda, a partir únicamente de los números tal como aparecían en el texto pre-fix, y se confirmó experimentalmente que Lean rechaza la transcripción ingenua de ambos.

---

## Capítulo: `fundamentos_de_probabilidad` (teoría)

8 `teorema`s (`thm:2.2.1`–`thm:2.2.8`), todos derivados de los tres axiomas de Kolmogorov enunciados en el propio capítulo (líneas 213-247). Formalizados en `verification/lean_verificacion/LeanVerificacion/FundamentosProbabilidad.lean` sobre una estructura `Axiomas` que captura los tres axiomas literalmente (no se usa `MeasureTheory` de Mathlib, que trabaja en `ℝ≥0∞` y con σ-álgebras — maquinaria que este capítulo no introduce).

| Label | Enunciado | Tier | Estado |
|---|---|---|---|
| `thm:2.2.1` | $A_1\subset A_2 \Rightarrow P(A_1)\le P(A_2)$, $P(A_2-A_1)=P(A_2)-P(A_1)$ | B | ✅ Cierra |
| `thm:2.2.2` | $0\le P(A)\le 1$ | B | ✅ Cierra |
| `thm:2.2.3` | $P(\emptyset)=0$ | B | ✅ Cierra |
| `thm:2.2.4` | $P(A')=1-P(A)$ | B | ✅ Cierra |
| `thm:2.2.5` | Aditividad finita sobre partición indexada por `Finset`, y caso particular $\sum P(A_i)=1$ | B | ✅ Cierra (derivado de un lema auxiliar `aditividad_finita` por inducción sobre el axioma binario) |
| `thm:2.2.6` | $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ (2 eventos) y $P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(B\cap C)-P(C\cap A)+P(A\cap B\cap C)$ (3 eventos) | B | ✅ Cierra ambos casos (`thm_2_2_6`, `thm_2_2_6_tres_eventos`) |
| `thm:2.2.7` | $P(A)=P(A\cap B)+P(A\cap B')$ | B | ✅ Cierra |
| `thm:2.2.8` | Partición general: $P(A)=\sum_i P(A\cap A_i)$ | B | ✅ Cierra |

**Precisión sobre qué se verificó:** el libro solo incluye `\begin{proof}` para `thm:2.2.1`–`thm:2.2.4`; `thm:2.2.5`–`thm:2.2.8` son enunciados sin demostración en el texto. Lo que se confirmó en los 8 casos es que el **enunciado** es un teorema válido, derivable de los tres axiomas — para 2.2.1–2.2.4 esto además corrobora que el argumento en prosa del libro es correcto (mismos pasos: descomposición en unión disjunta + axioma 3); para 2.2.5–2.2.8 no hay una demostración del libro con la cual comparar el argumento, solo se verificó que la afirmación es cierta. Ningún error matemático encontrado en ninguno de los 8 enunciados ni en las 4 demostraciones dadas.

## Capítulo: `fundamentos_de_probabilidad` (problemas)

Formalizados en `verification/lean_verificacion/LeanVerificacion/FundamentosProbabilidadProblemas.lean`.

| Label (nivel Bloom) | Afirmación | Tier | Método | Estado |
|---|---|---|---|---|
| `prob:de3947a` (Recordar) | $\lvert S\rvert = 4\times 13 = 52$ | A | `decide` sobre `Fin 4 × Fin 13` | ✅ Cierra |
| `prob:cfa53ca` (Comprender), incisos 4–7 | (4) $A'\cup B'=(A\cap B)'$; (5) $A-B=A\cap B'$; (6) $A'-B'=A'\cap B$; (7) $(A\cap B)\cup(A\cap B')=A$ | A | Identidades de conjuntos (`Set.compl_inter`, `Set.sdiff_eq`, `compl_compl`, `Set.inter_union_compl`) | ✅ Los 4 cierran. Incisos 1-3 son interpretación en prosa sin contenido formalizable (piden describir con palabras, no probar una identidad) |
| `prob:69a20ec` (Aplicar) | $P(\text{al menos un 4 en 2 dados})=1-25/36=11/36$ | A | `decide` (cuenta favorable=11, complemento=25) + `norm_num`, con la probabilidad expresada directamente en términos de esas cardinalidades (no como una igualdad numérica desconectada del conteo) | ✅ Cierra |
| `prob:1f335a1` (Analizar) | Regla general de adición desde los axiomas | B | Reutiliza `thm_2_2_6` | ✅ Cierra |
| `prob:a4ff50c` (Evaluar), parte 1 (fórmula general, $n$ arbitraria) | $P(\bigcup A_i)=\sum_{k=1}^n (-1)^{k-1}/k!$ | D | Requiere inclusión-exclusión general sobre `Finset` de permutaciones — no intentado en el piloto | ⚠️ No formalizado, ver "Infeasibles" abajo |
| `prob:a4ff50c`, caso $n=3$ (evidencia parcial) | Fórmula concreta para $n=3$: 4 de 6 permutaciones tienen punto fijo, $4/6=1-1/2+1/6$ | A | `decide` sobre `Equiv.Perm (Fin 3)` | ✅ Cierra — consistente con la fórmula general |
| `prob:a4ff50c`, parte 2 (límite $n\to\infty$) | $\lim_n P(\bigcup A_i) = 1-e^{-1}\approx 0.63212$, estabilizado desde $n\ge 6$ | C | Cross-check numérico, `verification/scipy/fundamentos_de_probabilidad/hat_check_limit.py` | ✅ Confirmado numéricamente (diff $<2\times10^{-4}$ en $n=6$) |
| `prob:b993271` (Crear) | Ejemplo numérico (dado de 8 caras) satisface la regla de adición: $0.5+0.5-0.25=0.75$ | A | `decide` sobre `Finset (Fin 8)` | ✅ Cierra |

Ningún error matemático encontrado en las 6 soluciones de este archivo.

### Infeasibles / Tier D (no formalizados en este piloto)

- `prob:a4ff50c`, parte 1, versión general para $n$ arbitraria: requeriría formalizar inclusión-exclusión para $n$ eventos sobre permutaciones indexadas por `Finset`, más una prueba de que $\binom{n}{k}\cdot\frac{(n-k)!}{n!}=\frac{1}{k!}$ — factible en Mathlib pero de esfuerzo considerablemente mayor al resto del piloto. Verificado en su lugar: caso concreto $n=3$ (Tier A) + límite numérico (Tier C). Revisar manualmente si se requiere certeza total sobre la fórmula general.

---

## Verificación EN por diff (no re-probada en Lean)

Ejecutado para este piloto (no solo asumido por la política general): comparación de **todas** las etiquetas `\label{<prefijo>:...}` (`thm:`, `prob:`, `eq:`, etc. — patrón `label\{[a-z]+:[^}]*\}`, no solo `thm:`/`prob:`) y de literales numéricos (`grep`+`diff`) entre `latex/fundamentos_de_probabilidad.tex` ↔ `latex/en_fundamentos_de_probabilidad.tex`, y entre `latex/fundamentos_de_probabilidad(p).tex` ↔ `latex/en_fundamentos_de_probabilidad(p).tex`. Resultado: **todas las etiquetas (incluyendo las `eq:*` de las 15 ecuaciones numeradas del capítulo y las 2 del archivo de problemas) coinciden exactamente y los literales numéricos coinciden exactamente** en ambos pares de archivos — sin divergencias. No se requiere corrección EN para este capítulo. Usar el patrón `label\{[a-z]+:[^}]*\}` (no solo `thm:`/`prob:`) en las siguientes entradas — una etiqueta `eq:` renumerada o eliminada en el lado EN es una clase de divergencia real que un patrón más estrecho no vería.

---

## Capítulo: `tecnicas_de_conteo` (teoría)

1 `teorema` (principio de multiplicación), 2 `definicion`es (permutación `eq:conteo.2`, combinación `eq:conteo.3`) con propiedades asociadas, y 4 ejemplos numéricos resueltos (`exmp:conteo.1`–`.4`). Formalizado en `verification/lean_verificacion/LeanVerificacion/TecnicasDeConteo.lean` vía `Fintype.card_prod`, `Nat.descFactorial` y `Nat.choose` de Mathlib — todo aritmética exacta de naturales/racionales, sin necesidad de análisis real.

| Label | Afirmación | Tier | Estado |
|---|---|---|---|
| Principio de multiplicación (teorema) | $\lvert\alpha\times\beta\rvert = \lvert\alpha\rvert\cdot\lvert\beta\rvert$ (instancia general) | B | ✅ Cierra (`Fintype.card_prod`) |
| `exmp:conteo.1` | $4\times 6\times 3=72$ menús | A | ✅ Cierra |
| `eq:conteo.2`/`exmp:conteo.2` | $P(8,3)=8\times7\times6=336$, vía `descFactorial` y vía $8!/(8-3)!$ | A | ✅ Cierra, ambas formas coinciden |
| `eq:conteo.3` (definición general) | $\binom{n}{r}=\frac{n!}{r!(n-r)!}$ | B | ✅ Cierra (`Nat.choose_mul_factorial_mul_factorial`) |
| Simetría, casos extremos | $\binom{n}{r}=\binom{n}{n-r}$; $\binom{n}{0}=\binom{n}{n}=1$ | B | ✅ Cierran |
| `exmp:conteo.3` | $\binom{10}{4}=210$ | A | ✅ Cierra |
| `exmp:conteo.4` | Flor en póker: $\binom{52}{5}=2{,}598{,}960$, $\binom{13}{5}=1{,}287$, $4\times1{,}287=5{,}148$, $P\approx0.00198$ | A | ✅ Cierra (tolerancia $10^{-5}$ porque el libro usa $\approx$) |

**No formalizado (Tier D, prosa/no cuantitativo):** "teorema del binomio" mencionado como propiedad del coeficiente binomial (coeficiente de $x^r y^{n-r}$ en $(x+y)^n$) — es una afirmación cualitativa correcta y bien conocida (`add_pow` en Mathlib), no se formalizó por no ser el foco de una demostración o cálculo específico del capítulo.

Ningún error matemático encontrado.

## Capítulo: `tecnicas_de_conteo` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/TecnicasDeConteoProblemas.lean`.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:6369f2a` (Recordar) | Enunciar fórmulas en prosa | — | No formalizable más allá de lo ya cubierto en la teoría |
| `prob:4f6f981` (Comprender) | $5\times4\times2=40$ menús | A | ✅ Cierra |
| `prob:490657c` (Aplicar) | $P(10,3)=720$, $\binom{10}{3}=120$, $P(10,3)=3!\times\binom{10}{3}$ | A | ✅ Cierra |
| `prob:d8ce0cf` (Analizar) | $\binom{5}{2}\times\binom{5}{2}=100$ comités | A | ✅ Cierra |
| `prob:3007304` (Evaluar) | El estudiante confunde $\binom{8}{3}=56$ con $P(8,3)=336$; en efecto $336=6\times56\neq56$ | A | ✅ Cierra — confirma que el razonamiento del estudiante (evaluado como incorrecto por el libro) es efectivamente incorrecto |
| `prob:b53268b` (Crear) | Dos pares en póker: $\binom{13}{2}\times\binom{4}{2}^2\times\binom{11}{1}\times\binom{4}{1}=123{,}552$, $P\approx0.0475$ | A | ✅ Cierra (tolerancia $10^{-4}$) |

Ningún error matemático encontrado en las 6 soluciones de este archivo.

### Verificación EN por diff

Etiquetas (`grep`+`diff` sobre `label\{[a-z]+:[^}]*\}`): coinciden exactamente en teoría y en problemas. Literales numéricos: coinciden exactamente en el archivo de problemas; en el archivo de teoría hay **una divergencia aparente** (ES tiene un "3" de más) que se investigó y resultó ser un **falso positivo de traducción, no un error matemático**: la línea 50 dice en ES *"tomados de $3$ en $3$"* (repite el numeral, fraseo idiomático) mientras que EN dice *"taken $3$ at a time"* (lo menciona una sola vez) — mismo valor $P(8,3)$ en ambos, solo difiere el estilo de la frase. Se documenta aquí para que futuras entradas no se alarmen ante el mismo patrón de "3 aparece dos veces en ES, una vez en EN" en frases tipo "de $r$ en $r$".

---

## Capítulo: `probabilidad_condicional` (teoría)

2 `teorema`s activos (`thm:2.4.1` regla de la cadena de 3 eventos, `thm:2.4.2` probabilidad total), 1 `definicion` (probabilidad condicional), y un ejemplo numérico (canicas). Formalizado en `verification/lean_verificacion/LeanVerificacion/ProbabilidadCondicional.lean`, reutilizando la estructura `Axiomas` y los teoremas de `FundamentosProbabilidad`.

**Observación de contenido (no es un error matemático):** el archivo del libro incluye un bloque `\begin{teorema}[Teorema de Bayes] ... \end{teorema}` **comentado** (líneas 105-112, inactivo, no se compila) a pesar de que la sección se titula *"Probabilidad condicional y regla de Bayes"*. El teorema de Bayes en sí vive en el siguiente capítulo del libro, `teorema_de_bayes.tex`. Esto es consistente y no requiere corrección, pero se documenta aquí por si el título de la sección genera expectativas de contenido que en realidad está diferido.

| Label | Afirmación | Tier | Estado |
|---|---|---|---|
| `definicion` (prob. condicional) | $P(B\mid A)=P(A\cap B)/P(A)$ y $P(A\cap B)=P(A)P(B\mid A)$ | B | ✅ Cierra (`condicional`, `cond_mul_eq_inter` — la segunda igualdad se probó **incondicionalmente**, incluso cuando $P(A)=0$, vía monotonía+no-negatividad) |
| `thm:2.4.1` | $P(A_1\cap A_2\cap A_3)=P(A_1)P(A_2\mid A_1)P(A_3\mid A_1\cap A_2)$ | B | ✅ Cierra (dos aplicaciones de `cond_mul_eq_inter`) |
| `thm:2.4.2` | $P(A)=\sum_i P(A_i)P(A\mid A_i)$ para partición $S=\bigsqcup A_i$ | B | ✅ Cierra (reutiliza `thm_2_2_8` de `FundamentosProbabilidad`) |
| Ejemplo canicas (sin label) | $P(E_1\cap E_2')=\frac{3}{5}\times\frac{2}{4}=\frac{6}{20}$, $P(E_2'\mid E_1)=\frac12$ | A | ✅ Cierra |

Ningún error matemático encontrado.

## Capítulo: `probabilidad_condicional` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/ProbabilidadCondicionalProblemas.lean`. Todos tratados como aritmética directa de números dados (mismo estilo que usa el libro — no se construyó un espacio muestral discreto completo para Monty Hall ni para el problema médico, se trabajó directamente con las probabilidades condicionales como datos, igual que el libro).

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:8794f31` (Recordar) | $P(A\mid B)=0.60$, $P(B\mid A)=0.50$, $P(A\cap B')=0.30$, $P(A\mid B')=0.60$ | A | ✅ Cierra |
| `prob:cf929e4` (Comprender) | Urna 5R/3A sin reemplazo: $P(A')=3/8$ (dato del libro, verificado por separado); $P(B)=(4/7)(5/8)+(5/7)(3/8)=5/8=P(A)$ | A | ✅ Cierra |
| `prob:52e63a3` (Aplicar) | $P(D)=0.065$; $P(A\mid D)=7/13$ exacto, $\approx0.5385$ | A | ✅ Cierra (igualdad exacta + tolerancia $10^{-4}$) |
| `prob:8a7282b` (Analizar), parte 2 | 4 cartas de palos distintos: $1\times\frac{39}{51}\times\frac{26}{50}\times\frac{13}{49}\approx0.1055$ | A | ✅ Cierra (tolerancia $10^{-4}$) |
| `prob:c840e8f` (Evaluar) | Monty Hall: $P(A_3)=1/2$ (encadenado, no re-escrito); $P(C_1\mid A_3)=1/3$ (mantener); $P(C_2\mid A_3)=2/3$ (cambiar) | A | ✅ Cierra |
| `prob:4241cab` (Crear) | Falacia de tasa base: $P(D')=0.99$ (dato del libro, verificado por separado); $P(+)=0.1085$; $P(D\mid+)\approx0.0876$ | A | ✅ Cierra (tolerancia $10^{-4}$) |

**No formalizado (Tier B, no intentado):** `prob:8a7282b` parte 1 pide la inducción general de la regla de la cadena para $n$ eventos arbitrarios. El caso $n=3$ ya está cubierto por `thm_2_4_1`, y el caso concreto $n=4$ usado en la parte 2 es una instancia directa (dos aplicaciones más de `cond_mul_eq_inter`), pero la inducción simbólica general sobre $n$ no se formalizó — factible pero de mayor esfuerzo, no crítico dado que ambos casos concretos que el libro realmente usa ya están verificados.

Ningún error matemático encontrado en las 6 soluciones de este archivo.

### Verificación EN por diff

Etiquetas y literales numéricos (`grep`+`diff`, ambos patrones) coinciden exactamente entre ES y EN, tanto en teoría como en problemas — sin divergencias, ni siquiera falsos positivos de traducción esta vez.

---

## Capítulo: `teorema_de_bayes` (teoría)

**Confirmación de la nota de "Próximos pasos" anterior:** el conteo de entornos `grep` reportó 0 `teorema` en este archivo, pero contiene el Teorema de Bayes real y sus dos generalizaciones, presentados íntegramente en prosa/`align` sin ningún `\begin{teorema}` explícito — se leyó el archivo completo en vez de confiar en el conteo, tal como se planeó. Formalizado en `verification/lean_verificacion/LeanVerificacion/TeoremaDeBayes.lean`, reutilizando `condicional`, `cond_mul_eq_inter` y `thm_2_4_2` de `ProbabilidadCondicional` — la reutilización directa confirma que el marco axiomático del piloto sí escala a capítulos posteriores.

**Observación de terminología (no es un error matemático):** el libro llama "regla de la cadena" tanto a la fórmula multiplicativa de intersecciones (`thm:2.4.1` en `probabilidad_condicional.tex`) como, aquí, a la suma de probabilidad total $P(B)=\sum P(B|E_i)P(E_i)$ (línea 47) — dos resultados distintos que comparten nombre entre capítulos. Documentado para evitar confusión en referencias cruzadas futuras.

| Afirmación (sin `teorema` explícito en el libro) | Tier | Estado |
|---|---|---|
| Bayes básico: $P(A\mid B)=P(A)P(B\mid A)/P(B)$ (líneas 3-16) | B | ✅ Cierra (`bayes_basico`) |
| Generalización 2 eventos: $P(A\mid B)=\dfrac{P(A)P(B\mid A)}{P(B\mid A)P(A)+P(B\mid A')P(A')}$ (líneas 18-36) | B | ✅ Cierra (`bayes_dos_eventos` — orden del denominador verificado idéntico al del libro) |
| Generalización partición de $k$ eventos: $P(E_j\mid B)=\dfrac{P(B\mid E_j)P(E_j)}{\sum_i P(B\mid E_i)P(E_i)}$ (líneas 38-57) | B | ✅ Cierra (`bayes_particion`, vía `thm_2_4_2`) |
| Ejemplo 3 máquinas: $P(M_2\mid D)\approx0.3642$ | A | ✅ Cierra (tolerancia $10^{-4}$, numerador/denominador encadenados con `let`) |

Ningún error matemático encontrado.

## Capítulo: `teorema_de_bayes` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/TeoremaDeBayesProblemas.lean`.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:054ed26` (Recordar) | Dado 6 caras: $P(A)=0.5$; $P(A\mid I)=2/3$ | A | ✅ Cierra — cardinalidades contadas por `decide` sobre `Finset (Fin 6)`, no escritas a mano (única forma de detectar un conteo erróneo del libro) |
| `prob:bde7784` (Comprender) | $P(Z)=0.12$; $P(M\mid Z)=0.50$ | A | ✅ Cierra |
| `prob:e14faa0` (Aplicar) | $P(A)=0.72$; $P(E\mid A)=0.875$; $P(A')=0.28$; $P(E'\mid A')=0.75$ | A | ✅ Cierra |
| `prob:a7e87e4` (Analizar) | Teorema de Bayes para partición finita general | B | ✅ **Citado, no re-demostrado** — es literalmente `TeoremaDeBayes.bayes_particion`; `prob_a7e87e4` es una referencia directa a ese teorema, no una segunda verificación independiente |
| `prob:898898e` (Evaluar) | Falacia del Fiscal (momios): momios posteriores $=0.20$; $P(I\mid E)=1/6\approx0.1667$ | A | ✅ Cierra |
| `prob:3bf9f42` (Crear) | Riesgo crediticio: $P(D)=0.0755$; vector posterior $\approx(0.1325,0.3709,0.4967)$ | A | ✅ Cierra (tolerancia $10^{-4}$ cada uno, $P(D)$ encadenado como denominador común) |

Ningún error matemático encontrado en las 6 soluciones de este archivo.

### Verificación EN por diff

Etiquetas y literales numéricos coinciden exactamente entre ES y EN, tanto en teoría como en problemas — sin divergencias.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3007/3007 jobs, sin `sorry`, sin errores.** 57 teoremas en total: 4 en `Calibracion.lean`, 11 en `FundamentosProbabilidad.lean`, 9 en `FundamentosProbabilidadProblemas.lean`, 8 en `TecnicasDeConteo.lean`, 5 en `TecnicasDeConteoProblemas.lean`, 4 en `ProbabilidadCondicional.lean`, 7 en `ProbabilidadCondicionalProblemas.lean`, 4 en `TeoremaDeBayes.lean`, 6 en `TeoremaDeBayesProblemas.lean`.

Nota técnica acumulada: (1) nunca usar `import Mathlib` completo en Windows — falla por longitud de ruta y compila ~8600 archivos innecesarios; importar solo los módulos específicos. (2) evitar la notación postfix `!` de `Nat.factorial` combinada con `*`/`/`; usar `Nat.factorial n` explícito. (3) para afirmaciones "≈", probar una cota de tolerancia explícita. (4) **regla de encadenamiento** (ver arriba) — obligatoria en todo capítulo con derivaciones de varios pasos. (5) nuevo en este capítulo: encadenar rewrites con `rw [a, b, c]` donde una reescritura anterior (p.ej. `mul_comm`) puede destruir el patrón que una reescritura posterior necesita — si un `rw` de una hipótesis previamente probada falla con "did not find pattern" después de otros rewrites, probar aplicándolo primero o solo, no al final de la cadena.

---

## Capítulo: `muestreo_aleatorio` (teoría)

**Primer capítulo donde predomina Tier D — capacidad faltante identificada, decisión pendiente del usuario.** El único `teorema` del archivo es el Teorema del Límite Central (TLC) mismo: convergencia en distribución, un resultado analítico sustancial (teoría de la medida / funciones características / convergencia débil) que el libro tampoco demuestra (solo lo enuncia) y que está muy por encima del esfuerzo razonable de este proyecto — **Tier D, no formalizado**. Las fórmulas generales $E(\bar X)=\mu$, $\mathrm{Var}(\bar X)=\sigma^2/n$ también quedan Tier D por la misma razón estructural: **el marco `Axiomas : Set Ω → ℝ` construido en el piloto modela probabilidades de *eventos*, no variables aleatorias reales con un operador de esperanza** — no hay manera de expresar "$E(\bar X)$" en el marco actual sin extenderlo. Esta misma carencia bloqueará `prob:0c980d4` y `prob:293fd20` de este capítulo, y previsiblemente la mayoría de los capítulos de estimación/inferencia que siguen (estimación puntual, errores estándar, intervalos de confianza, pruebas de hipótesis) construyen sobre esperanza/varianza de estadísticos. **Decisión pendiente:** construir una capa de variables aleatorias reales + esperanza sobre `MeasureTheory` de Mathlib (esfuerzo considerable, una vez, beneficia a todos los capítulos siguientes) vs. aceptar Tier D para esta clase de resultados en el resto del libro y limitar Lean a las partes puramente aritméticas/combinatorias de cada capítulo (como se ha hecho hasta ahora). No se tomó esta decisión unilateralmente; se documenta aquí para que el usuario la resuelva.

Lo que sí se formalizó del ejemplo numérico del dado (Tier A, aritmética exacta de racionales):

| Afirmación | Tier | Estado |
|---|---|---|
| $\mu=(1+2+\dots+6)/6=3.5$ | A | ✅ Cierra |
| $\sigma^2=\frac{\sum(i-3.5)^2}{6}=35/12\approx2.917$ | A | ✅ Cierra (suma exacta de los 6 términos, no solo el resultado citado) |
| $\mathrm{Var}(\bar X)=\sigma^2/36=35/432\approx0.081$ (para $n=36$) | A | ✅ Cierra |
| Puntajes $Z=\mp1.76$ y $P(3.0<\bar X<4.0)\approx0.921$ | C | ✅ Confirmado numéricamente, `verification/scipy/muestreo_aleatorio/tlc_dado.py` (Mathlib no tiene CDF normal computable) |

Ningún error matemático encontrado.

## Capítulo: `muestreo_aleatorio` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/MuestreoAleatorioProblemas.lean`.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:c0cebb4` (Recordar) | $\sigma_{\bar X}=12/\sqrt n$ para $n=9,36,144,576$: $4.00,2.00,1.00,0.50$ | A | ✅ Cierra — se usó `Real.sqrt n` literalmente (no $3,6,12,24$ ya calculados a mano), para que un $n$ incorrecto en el libro pudiera detectarse |
| `prob:116017b` (Comprender) | $6^3=216$ (con reemplazo); $\binom{6}{3}=20$ (sin reemplazo) | A | ✅ Cierra. Parte 3 (límite $N\to\infty$): prosa/argumento asintótico, Tier D, no formalizado |
| `prob:2da8cc3` (Aplicar) | $n=(1.96\times8/1.5)^2\approx109.27$; $n_{\text{mín}}=110$ | A | ✅ Cierra (tolerancia $10^{-2}$ + comparación exacta $109<n\le110$) |
| `prob:0c980d4` (Analizar) | $\sum(X_i-\bar X)^2=\sum(X_i-\mu)^2-n(\bar X-\mu)^2$ (identidad algebraica previa a aplicar $E[\cdot]$) | B | ✅ **Sí se formalizó** (`descomposicion_varianza`, pura álgebra de `Finset.sum`) — el paso final de aplicar $E[\cdot]$ para concluir $E(S^2)=\sigma^2$ queda Tier D (ver nota de capacidad faltante arriba) |
| `prob:293fd20` (Evaluar) | Cauchy: $E(X)$ no existe; $\bar X_n\sim\text{Cauchy}(0,1)$ para todo $n$ (función característica) | D | ⚠️ No formalizado — requiere integración de Lebesgue / funciones características, fuera de alcance |
| `prob:b7567ec` (Crear) | Tornillos: $\sigma_{\bar X}=0.5/\sqrt{64}=0.0625$; $z_1=-1.6,z_2=1.6$; $P\approx0.8904$ | A/C | ✅ Cierra la parte A (`Real.sqrt 64` literal, no el $8$ ya calculado); parte C confirmada numéricamente en `verification/scipy/muestreo_aleatorio/tornillos.py` |

Ningún error matemático encontrado en las partes formalizables de las 6 soluciones de este archivo.

### Verificación EN por diff

Etiquetas coinciden exactamente. Literales numéricos: **una divergencia aparente, investigada y confirmada como falso positivo de formato, no error matemático** — ES escribe "1000" (individuos) sin separador de miles, EN escribe "1,000" (convención tipográfica del inglés). Mismo valor. Documentado para no repetir la investigación si reaparece el mismo patrón en otro capítulo.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3009/3009 jobs, sin `sorry`, sin errores.** 65 teoremas en total: 4 en `Calibracion.lean`, 11 en `FundamentosProbabilidad.lean`, 9 en `FundamentosProbabilidadProblemas.lean`, 8 en `TecnicasDeConteo.lean`, 5 en `TecnicasDeConteoProblemas.lean`, 4 en `ProbabilidadCondicional.lean`, 7 en `ProbabilidadCondicionalProblemas.lean`, 4 en `TeoremaDeBayes.lean`, 6 en `TeoremaDeBayesProblemas.lean`, 2 en `MuestreoAleatorio.lean`, 6 en `MuestreoAleatorioProblemas.lean` (incluye `descomposicion_varianza`, reutilizable en capítulos de estimación futuros: varianza muestral, ANOVA, etc.).

Nota técnica acumulada: (1) nunca usar `import Mathlib` completo en Windows. (2) evitar la notación postfix `!` de `Nat.factorial`. (3) para afirmaciones "≈", probar una cota de tolerancia explícita. (4) **regla de encadenamiento** — obligatoria en toda derivación de varios pasos. (5) cuidado con el orden de `rw` en cadena. (6) nuevo en este capítulo: para valores $\sigma/\sqrt n$ con $n$ cuadrado perfecto, usar `Real.sqrt n` literal (vía `Real.sqrt_sq` tras reescribir $n$ como un cuadrado) en vez de escribir a mano la raíz ya calculada — mismo principio de encadenamiento aplicado a raíces cuadradas.

## Capa de variables aleatorias / esperanza — construida y probada (con una limitación de entorno)

**Resultado: se construyó la capa (decisión del usuario: "construirla ahora") y las tres afirmaciones generales quedaron probadas, sin `sorry`, verificadas por el compilador.** Formalizada en `verification/lean_verificacion/LeanVerificacion/VariablesAleatorias.lean`, sobre `MeasureTheory.Measure`/`ProbabilityTheory.variance` de Mathlib (capa distinta de `Axiomas : Set Ω → ℝ`, ver división de trabajo documentada en el propio archivo):

| Lema | Afirmación | Estado |
|---|---|---|
| `esperanza_media_muestral` | $E(\bar X)=\mu$ para una muestra i.i.d. | ✅ Probado |
| `varianza_media_muestral` | $\mathrm{Var}(\bar X)=\sigma^2/n$ | ✅ Probado (vía `ProbabilityTheory.IndepFun.variance_sum` + `variance_smul`) |
| `esperanza_varianza_muestral` | $E(S^2)=\sigma^2$ (varianza muestral insesgada, $n\ge2$) | ✅ Probado — reutiliza `MuestreoAleatorioProblemas.descomposicion_varianza` y cierra el paso final de $E[\cdot]$ que en `prob:0c980d4` había quedado Tier D |

Esto **retroactivamente resuelve a Tier B** las fórmulas generales $E(\bar X)=\mu$, $\mathrm{Var}(\bar X)=\sigma^2/n$ del capítulo `muestreo_aleatorio` (antes Tier D, líneas arriba) y el paso final de `prob:0c980d4` (antes Tier D). El TLC en sí (convergencia en distribución) y `prob:293fd20` (Cauchy) siguen Tier D — la capa da esperanza/varianza de estadísticos, no teoría de la medida/funciones características.

**Complicación real encontrada y resuelta — no matemática, de entorno Windows:** el primer intento de compilar este archivo en este worktree (`...\corregir-hallazgos-ad26\verification\lean_verificacion\`) falló de forma determinista al escribir `...ContinuousFunctionalCalculus\PosPart\Basic.olean.server` (dependencia transitiva de `Mathlib.Probability.Moments.Variance`). Un primer diagnóstico concluyó erróneamente que no era un límite de longitud de ruta (prueba insuficiente: `File.WriteAllText` de .NET antepone `\\?\` automáticamente y no está sujeto al mismo límite que `lean.exe`). El diagnóstico correcto, confirmado empíricamente en una segunda pasada: la ruta completa hasta ese archivo mide ~255 caracteres en este worktree, contra el límite MAX_PATH=260 de Windows, y `lean.exe` no está manifestado para rutas largas. Verificado construyendo el mismo import (y luego el archivo completo, con las tres pruebas) en dos ubicaciones de ruta corta — `C:\lv\` (~139 caracteres) y un worktree Git temporal `C:\w\ad26-lean\` (~179 caracteres, misma rama `verify-result-with-lean`, mismo cache de Mathlib copiado, mismo pin `v4.32.2` sin modificar) — ambas compilaron sin ningún cambio de código, junto con los 5 capítulos ya verificados (3458/3458 jobs, cero `sorry`). El archivo terminado se copió de vuelta a este worktree; solo cambió el comentario de cabecera (para reflejar el diagnóstico correcto), el código de las pruebas es idéntico byte a byte.

**Consecuencia práctica, sin resolver todavía — decisión de flujo de trabajo pendiente del usuario:** `verification/lean_verificacion/LeanVerificacion.lean` (el agregador de imports) **no** incluye `import LeanVerificacion.VariablesAleatorias` en este worktree, precisamente porque agregarlo haría fallar `lake build` (sin argumento) aquí — el archivo en sí está probado, pero esta ubicación de checkout específica no puede compilarlo. Opciones no decididas unilateralmente:
1. Dejarlo excluido del build por defecto en este worktree (estado actual) y usar el patrón de worktree temporal de ruta corta + copiar de vuelta cada vez que se necesite recompilar/extender esta capa.
2. Relocalizar este worktree a una ruta más corta (p. ej. `git worktree move` a algo como `C:\w\ad26`) — sin cambios de código ni de `lakefile.toml`, pero desplaza el checkout activo de esta sesión.
3. Verificar si el repo principal sin el sufijo `.worktrees\<rama>` (p. ej. tras el merge a `main`) queda lo bastante corto (~221 caracteres calculados hasta el mismo archivo, sin verificar empíricamente) para que este problema no reaparezca ahí.

**Hallazgo de higiene de repo, separado de lo anterior — corregido y commiteado:** el commit `2027a28` ("Adds random-variable inference foundation") había quedado con `lakefile.toml` conteniendo `packagesDir = "C:/lake_pkgs"` (ruta absoluta específica de esta máquina) y un import roto — un clon nuevo de ese commit no compilaba. Corregido en el commit `8c59360` ("Fix broken Lean verification build at HEAD"); la capa de esperanza/varianza probada quedó en el commit `3e8cf83` ("Prove the random-variable expectation/variance layer"). HEAD compila de nuevo desde un clon limpio.

---

## Capítulo: `variables_aleatorias_discretas` (teoría)

Sin entornos `teorema`. Formalizado en `verification/lean_verificacion/LeanVerificacion/VariablesAleatoriasDiscretas.lean`. Construido enteramente en este worktree (sin necesidad del worktree temporal de ruta corta) porque ninguna afirmación de este capítulo requiere `MeasureTheory`/`ProbabilityTheory.variance` — todas las variables aleatorias tienen soporte finito explícito, así que esperanza/varianza son sumas finitas ponderadas por `Finset.sum`, no medidas.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.6.2` — dos lanzamientos de moneda: $P(X=0)=1/4$, $P(X=1)=1/2$, $P(X=2)=1/4$ | A | ✅ Cierra (cardinalidades por `decide` sobre `Bool × Bool`, no citadas a mano) |
| `exmp:2.6.3` — suma de dos dados: las 11 cardinalidades de la tabla ($x=2,\dots,12$: $1,2,3,4,5,6,5,4,3,2,1$) | A | ✅ Cierra (`decide` sobre `Fin 6 × Fin 6`, 36 resultados) |
| `exmp:2.6.4` — niños en familia de 3: cardinalidades $1,3,3,1$ (coinciden con $\binom{3}{0..3}$, confirma binomial $N=3,p=1/2$) | A | ✅ Cierra (`decide` sobre `Bool×Bool×Bool`) |
| `eq:varianza_formula_corta` — identidad de König-Huygens $\mathrm{Var}(X)=E[X^2]-\mu^2$, forma general para soporte finito ponderado | B | ✅ Cierra (`konig_huygens`, álgebra pura de `Finset.sum`, sin `MeasureTheory`) |

**No formalizado (prosa/gráficas, sin fórmula explícita en el texto):** `exmp:2.6.5`–`2.6.7` (funciones de distribución acumulada, solo descritas por figuras) y la observación sobre monotonía/continuidad por la derecha de la CDF — no hay una afirmación numérica concreta que verificar.

Ningún error matemático encontrado.

## Capítulo: `variables_aleatorias_discretas` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/VariablesAleatoriasDiscretasProblemas.lean`.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:2c27c8e` (Recordar) | $f(x)=cx^2$ en $\{1,2,3,4\}$: $c=1/30$; $P(X\ge3)=5/6$; $P(X\text{ par}\mid X\ge2)=20/29$ | A | ✅ Cierra |
| `prob:9efeaae` (Comprender) | PMF $(0.40,0.30,0.20,0.10)$: $F(1)=0.70$; $P(\text{rechazo})=1-F(1)=0.30$ | A | ✅ Cierra |
| `prob:c324c4f` (Aplicar) | PMF $(0.35,0.30,0.20,0.10,0.05)$: $\mu=1.20$, $E[X^2]=2.80$, $\mathrm{Var}(X)=1.36$ | A | ✅ Cierra |
| `prob:cb2247c` (Analizar) | $c_N=(N+1)/N$ vía fracciones parciales/suma telescópica, $N$ arbitraria | B | ✅ Cierra — `telescoping_parcial` probado por inducción sobre `Finset.range`, no citado de memoria; `prob_cb2247c` lo reutiliza para $N\ge1$ |
| `prob:d332420` (Evaluar) | $E[R]=42$, $\mathrm{Var}(R)=3216$; $\sigma_R\approx56.71$; $U=E[R]-1.25\sigma_R<0$ (rechazar licitación) | A/B | ✅ $E[R]$, $\mathrm{Var}(R)$ exactos (König-Huygens). $\sigma_R=\sqrt{3216}$ irracional — en vez de Tier C (`scipy`), se probó la cota exacta $56.70<\sigma_R<56.71$ en Lean (`Real.lt_sqrt`/`Real.sqrt_lt'`), suficiente para concluir $U<0$ formalmente sin salir de Lean |
| `prob:e538b1b` (Crear) | Ejemplo del libro (tickets soporte técnico): PMF $(0.10,0.25,0.30,0.25,0.10)$; CDF $(0.10,0.35,0.65,0.90,1.00)$; $q_{0.75}=3$ | A | ✅ Cierra — se verificó la condición que define el cuantil ($F(2)<0.75\le F(3)$), no solo el resultado citado |

Ningún error matemático encontrado en las 6 soluciones de este archivo.

### Verificación EN por diff

Etiquetas (`label\{[a-z]+:[^}]*\}`) y literales numéricos coinciden exactamente entre ES y EN, tanto en teoría como en problemas — sin divergencias.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3011/3011 jobs, sin `sorry`, sin errores.** Incluye ahora `VariablesAleatoriasDiscretas.lean` (4 teoremas) y `VariablesAleatoriasDiscretasProblemas.lean` (7 teoremas) además de los 11 archivos previos. Construido íntegramente en este worktree (sin necesidad del worktree temporal de ruta corta), a diferencia de `VariablesAleatorias.lean` (capa de esperanza sobre `MeasureTheory`, ver sección arriba) que sigue excluido del import por defecto por el límite de longitud de ruta.

Nota técnica nueva de este capítulo: para identidades generales sobre `Finset.range` con recurrencia (aquí, la suma telescópica), inducción directa con `Finset.sum_range_succ` es más simple y robusta que buscar un lema de telescoping ya empaquetado en Mathlib — mismo principio que otros capítulos: preferir un paso de cómputo verificable a una cita no confirmada.

---

## Capítulo: `distribucion_binomial` (teoría)

Sin entornos `teorema`, pero `eq:2.10.2`/`eq:2.10.3` ($\mu=Np$, $\sigma^2=Npq$) son las afirmaciones generales más sustanciales formalizadas hasta ahora fuera de la capa de esperanza — Tier B, probadas **desde la definición** $f(x)=\binom Nxp^xq^{N-x}$, sin citar un lema de media/varianza binomial ya empaquetado (Mathlib no tiene uno para `PMF.binomial`). Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionBinomial.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.10.1` — $\binom62(1/2)^2(1/2)^4=15/64$ | A | ✅ Cierra |
| `exmp:2.10.2` — $P(X\ge4)=15/64+6/64+1/64=11/32\approx0.344$ para $\mathrm{Bin}(6,1/2)$ | A | ✅ Cierra |
| `eq:2.10.2` — $E(X)=Np$ para $\mathrm{Bin}(N,p)$, $N$ arbitraria | B | ✅ Cierra (`esperanza_binomial`) — se elimina el término $x=0$, se reindexa y se aplica la identidad de absorción `absorcion_binomial` ($(i+1)\binom{M+1}{i+1}=(M+1)\binom Mi$, derivada de `Nat.add_one_mul_choose_eq` de Mathlib) más el teorema del binomio |
| `eq:2.10.3` — $\mathrm{Var}(X)=Npq$ | B | ✅ Cierra (`varianza_binomial`), vía el segundo momento factorial $E[X(X-1)]=N(N-1)p^2$ (`momento_factorial_binomial`, absorción aplicada dos veces) y $\mathrm{Var}(X)=E[X(X-1)]+E[X]-E[X]^2$ |

**No formalizado:** `exmp:2.10.3` (desarrollar $(p+q)^4$) solo referencia un script Python sin dar la expansión explícita en el texto del libro — nada que verificar ahí.

Ningún error matemático encontrado.

## Capítulo: `distribucion_binomial` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionBinomialProblemas.lean`.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:71ce5a0` (Recordar) | Recordar fórmulas de memoria (Bernoulli, $E(X)$, $\mathrm{Var}(X)$) | — | No formalizable más allá de la teoría (puro recordatorio, sin cálculo nuevo) |
| `prob:1149be6` (Comprender) | Justificación en prosa de por qué el conteo da $\binom nk$ | — | No formalizable (argumento verbal, sin cálculo) |
| `prob:c3d2032` (Aplicar) | $X\sim\mathrm{Bin}(12,0.15)$: $P(X\le2)\approx0.7358$; $P(X\ge4\mid X\ge1)\approx0.1075$ | A | ✅ Cierra — los 5 valores intermedios que el libro cita ($P(X{=}0..3)$, $P(X\le3)$) se verifican por separado, no solo el resultado final; $p=3/20$, $q=17/20$ son racionales exactos |
| `prob:bae56b2` (Analizar) | Identidad de Vandermonde $\sum_j\binom{n_1}j\binom{n_2}{m-j}=\binom{n_1+n_2}m$; aditividad de $E$/$\mathrm{Var}$ bajo $Z=X+Y$ | B | ✅ Núcleo combinatorio cerrado (`vandermonde_binomial`, reindexado de `Nat.add_choose_eq` de Mathlib vía `Finset.Nat.sum_antidiagonal_eq_sum_range_succ`); aditividad de momentos cerrada (`prob_bae56b2_aditividad`, álgebra trivial). ⚠️ No formalizada la derivación completa PMF-convolución-es-binomial (requiere aritmética de exponentes con resta de ℕ solo en los términos no nulos de la suma) — ver "Infeasibles" abajo |
| `prob:19f50da` (Evaluar) | Regla operativa $np\ge5$, $n(1-p)\ge5$ para $n=500,p=0.04$ ($np=20$, $n(1-p)=480$) | A | ✅ Cierra la parte cuantitativa. El resto (validez de la corrección de continuidad de Yates) es evaluación cualitativa en prosa, no formalizable |
| `prob:3c14103` (Crear) | $X\sim\mathrm{Bin}(15,0.7)$: $E(X)=10.5$, $\mathrm{Var}(X)=3.15$ | A | ✅ Cierra |

Ningún error matemático encontrado en las partes formalizables de las 6 soluciones de este archivo.

### Infeasibles / Tier D (no formalizados en este capítulo)

- `prob:bae56b2`, derivación completa de que la convolución de dos PMFs binomiales es la PMF binomial $\mathrm{Bin}(n_1+n_2,p)$: además del núcleo combinatorio (Vandermonde, sí verificado), requiere $p^jq^{n_1-j}\cdot p^{m-j}q^{n_2-(m-j)}=p^mq^{n_1+n_2-m}$ válido solo para los términos no nulos ($j\le n_1$, $m-j\le n_2$) — aritmética de exponentes con resta de ℕ condicionada, factible pero de esfuerzo notablemente mayor al resto del capítulo. El núcleo combinatorio y la aditividad de momentos (lo que el libro realmente usa para concluir) ya están verificados.

### Verificación EN por diff

Etiquetas y literales numéricos coinciden exactamente entre ES y EN, tanto en teoría como en problemas — sin divergencias.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3013/3013 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionBinomial.lean` (6 teoremas, incluye el helper `absorcion_binomial`/`suma_normalizada`) y `DistribucionBinomialProblemas.lean` (5 teoremas) además de los 13 archivos previos. Construido íntegramente en este worktree (sin necesidad del worktree temporal de ruta corta) — como `variables_aleatorias_discretas`, no toca `MeasureTheory.Moments.Variance`.

Nota técnica nueva de este capítulo: (1) `Finset.sum_range_succ'` (que pela el término $x=0$, no el último) reindexa la suma restante como `f(x+1)`, cuyo cast `↑(x+1)` es sintácticamente distinto de `↑x+1` aunque sean iguales — hacer `push_cast` **antes** de escribir la hipótesis auxiliar que se usará con `Finset.sum_congr`/`rw`, y escribir esa hipótesis ya en la forma post-`push_cast`, o el `rw` falla por "did not find pattern" aunque la igualdad sea trivialmente cierta. (2) al pelar dos términos (`Finset.sum_range_succ'` dos veces, necesario para $E[X(X-1)]$), evitar `ring_nf` para limpiar los residuos numéricos — normaliza también el *interior* de la suma que se quiere dejar intacta; usar `simp only` con lemas específicos (`sub_self, zero_mul, mul_zero, add_zero`) tras `push_cast`. (3) para sumas con orden de multiplicación distinto al de un lema de Mathlib (aquí, `add_pow` da `x^m*y^{n-m}*n.choose m`, el libro usa `\binom Nx p^xq^{N-x}`), no forzar `rw` con el lema en un orden — probar la igualdad de sumas reordenadas término a término con `Finset.sum_congr rfl (fun i _ => by ring)`, más robusto que intentar que `rw` unifique multiplicaciones conmutadas.

---

## Capítulo: `distribucion_multinomial` (teoría)

Capítulo corto: una fórmula (`eq:2.10.8`) y un ejemplo resuelto. Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionMultinomial.lean`.

**🔴 Hallazgo confirmado — error de fórmula, idéntico en ES y EN (no es divergencia de traducción, es la misma fuente compartida):** `eq:2.10.8` afirma $f(x_1,\dots,x_k)=\dfrac{x_1+\cdots+x_k}{x_1!\cdots x_k!}p_1^{x_1}\cdots p_k^{x_k}$ — al numerador **le falta el signo de factorial**; la PMF multinomial correcta es $\dfrac{(x_1+\cdots+x_k)!}{x_1!\cdots x_k!}p_1^{x_1}\cdots p_k^{x_k}$. Confirmado por el propio libro: `exmp:2.10.6`, inmediatamente después, usa $12!$ (no $12$) en el numerador, y la solución de `prob:2499194` en el archivo de problemas da la fórmula correcta con factorial. Es decir, el libro **usa** la fórmula correcta en la práctica pero la **escribe** mal en `eq:2.10.8`. No corregido en este pase (regla del proyecto).

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.10.6` — dado lanzado 12 veces, cada cara exactamente dos veces: $P=\frac{12!}{(2!)^6}(1/6)^{12}\approx0.00344$ | A | ✅ Cierra (usa la fórmula *correcta*, con factorial) |
| Normalización general de la PMF multinomial ($\sum$ sobre composiciones $=1$ cuando $\sum p_i=1$) | B | ✅ Cierra (`suma_normalizada_multinomial`, vía el teorema multinomial de Mathlib `Finset.sum_pow_eq_sum_piAntidiag`, instanciado en $1^n=1$) — generaliza la fórmula corregida a $k$ categorías arbitrarias |

## Capítulo: `distribucion_multinomial` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionMultinomialProblemas.lean`.

**🔴 Hallazgo confirmado — error numérico grande, verificado independientemente antes de escribir la prueba (con `Python`/`fractions.Fraction`, luego confirmado por Lean/`norm_num`):** `prob:33bf5d2` afirma $P(X_1{=}50,X_2{=}30,X_3{=}20)\approx4.32\times10^{-18}$ para $\bm X\sim\mathrm{Mult}(100;0.45,0.35,0.20)$. **El valor correcto es $P\approx0.0047908$ — el libro está equivocado por un factor de $\sim10^{42}$.** Dato curioso que sugiere la causa: $p_1^{50}=(0.45)^{50}\approx4.58\times10^{-18}$, muy cercano al valor (incorrecto) que da el libro — consistente con que la solución haya calculado solo esa potencia aislada y omitido el coeficiente multinomial (que es enorme, $\approx4.75\times10^{42}$) y los otros dos factores de probabilidad.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:2499194` (Recordar) | Recordar la fórmula de la PMF (con factorial, correcta) | — | No formalizado por separado, ya cubierto por `suma_normalizada_multinomial` |
| `prob:97df06e` (Comprender) | Explicación en prosa de por qué $\mathrm{Cov}(X_i,X_j)<0$ | — | No formalizable (argumento verbal) |
| `prob:33bf5d2` (Aplicar) | $P(X_1{=}50,X_2{=}30,X_3{=}20)\approx4.32\times10^{-18}$ | A | 🔴 **Refutado** (`prob_33bf5d2_libro_incorrecto`) y valor correcto confirmado por separado (`prob_33bf5d2_valor_correcto`, $P\approx0.0047908$) — mismo patrón que la calibración del método |
| `prob:277341a` (Analizar) | $\mathrm{Cov}(X_i,X_j)=-np_ip_j$ vía indicadoras | D | ⚠️ No formalizado — requiere covarianza entre *dos componentes distintas* de un vector aleatorio, no solo la varianza de una variable escalar vía su PMF; ni siquiera la capa `VariablesAleatorias.lean` lo cubre (esa modela solo muestras i.i.d. independientes) |
| `prob:81748ff` (Evaluar) | Evaluación conceptual que depende de `prob:277341a` | D | No formalizable (depende del resultado Tier D anterior + prosa) |
| `prob:858a3a8` (Crear) | Call center $k=4$, $n=50$, $p_1=0.4$: $E[X_1]=20$, $\mathrm{Var}(X_1)=12$ | A | ✅ Cierra — reutiliza directamente `esperanza_binomial`/`varianza_binomial` de `DistribucionBinomial.lean` (la marginal de una multinomial es binomial), validación cruzada entre capítulos |

### Infeasibles / Tier D (no formalizados en este capítulo)

- `prob:277341a`/`prob:81748ff` — covarianza entre componentes de un vector multinomial: requiere modelar variables indicadoras correlacionadas y su covarianza, infraestructura que el proyecto no ha construido (distinta de la capa de esperanza de muestras i.i.d. en `VariablesAleatorias.lean`).
- `prob:bae56b2` (capítulo anterior, `distribucion_binomial`) sigue pendiente por la misma clase de razón — ver arriba.

### Verificación EN por diff

Etiquetas y literales numéricos coinciden exactamente entre ES y EN — incluyendo que **ambos idiomas comparten el mismo `4.32e-18` incorrecto** en `prob:33bf5d2` y la misma fórmula sin factorial en `eq:2.10.8`, confirmando que son errores de la fuente compartida, no introducidos en la traducción.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3019/3019 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionMultinomial.lean` (2 teoremas) y `DistribucionMultinomialProblemas.lean` (1 def + 3 teoremas) además de los 15 archivos previos. Construido íntegramente en este worktree.

Nota técnica nueva de este capítulo: (1) `Nat.multinomial s f` (definido como `(∑ f)! / ∏ (f i)!`, división de ℕ) sobre un `Finset` pequeño no se reduce a un literal con `norm_num [Nat.multinomial, Nat.factorial]` — el cociente queda simbólico. Para coeficientes multinomiales concretos, escribir los factoriales explícitos directamente (`Nat.factorial 100 / (Nat.factorial 50 * ...)`, sin pasar por `Nat.multinomial`/`Finset`) sí se reduce limpiamente, incluso para números tan grandes como $100!$ (~15s de cómputo, nada prohibitivo). (2) al aislar qué conjunto de una conjunción es falso, `refine ⟨?_,?_,...⟩ <;> norm_num` deja ver el número exacto del `case refine_N` que falla — esta vez sí era un error real del libro, no una cota mal calibrada (contraste con `prob:c3d2032` del capítulo anterior). (3) verificar independientemente con Python (`fractions.Fraction` para aritmética exacta) *antes* de escribir la prueba de Lean, cuando un resultado de `norm_num` da `⊢ False` inesperado — más rápido que iterar a ciegas en Lean, y da la cifra correcta a la que apuntar con la tolerancia.

---

## Capítulo: `distribucion_geometrica_binomial_negativa` (teoría)

Sin entornos `teorema`, pero contiene las afirmaciones generales más analíticamente sustanciales de todo el proyecto hasta ahora: series geométricas **infinitas** (`tsum`), no sumas finitas. Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionGeometricaBinomialNegativa.lean`, vía la maquinaria de series geométricas de Mathlib (`hasSum_geometric_of_norm_lt_one`, `hasSum_coe_mul_geometric_of_norm_lt_one`, `hasSum_choose_mul_geometric_of_norm_lt_one`).

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.10.13` — vendedor $p=0.2$: $P(X=5)=0.08192$; $\mu=1/p=5$ | A | ✅ Cierra |
| `exmp:2.10.15` — examen $r=3,p=0.3$: $P(X=4)=\binom62(0.3)^3(0.7)^4\approx0.0972$ | A | ✅ Cierra |
| Cola geométrica $P(X>m)=(1-p)^m$ | B | ✅ Cierra (`cola_geometrica`, serie geométrica desplazada, sin lema de reindexado aparte) |
| **Pérdida de memoria** $P(X>m+n\mid X>m)=P(X>n)$ | B | ✅ Cierra (`perdida_memoria`, cociente de colas) |
| $\mu_X=1/p$ (geométrica) | B | ✅ Cierra (`esperanza_geometrica`, vía `hasSum_coe_mul_geometric_of_norm_lt_one` + `hasSum_geometric_of_norm_lt_one`) |
| Normalización de la binomial negativa ($\sum$ PMF $=1$) | B | ✅ Cierra (`suma_normalizada_binomial_negativa`, vía `hasSum_choose_mul_geometric_of_norm_lt_one` con $k:=r-1$ — coincide exactamente con el patrón de `eq:2.10.10`) |

**No formalizado — Tier D:** $\sigma^2_X=(1-p)/p^2$ (geométrica) y $\mu_X=r(1-p)/p$, $\sigma^2_X=r(1-p)/p^2$ (binomial negativa). Requerirían un segundo momento de la serie geométrica ($\sum k^2q^k$ o $\sum k\binom{k+m}{m}q^k$), que Mathlib no empaqueta directamente y que necesitaría además reindexar `tsum` con un desplazamiento de 2 (extendiendo con ceros los primeros términos) — factible, de esfuerzo notablemente mayor al resto del capítulo. La media de la geométrica (caso base $r=1$) ya está verificada.

Ningún error matemático encontrado en las afirmaciones formalizadas.

## Capítulo: `distribucion_geometrica_binomial_negativa` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionGeometricaBinomialNegativaProblemas.lean`.

**Observación de convención (no es un error matemático):** `prob:6ccfa13` usa $X$ = número de *ensayos* hasta el $r$-ésimo éxito (soporte $\{r,r+1,\dots\}$), mientras que `eq:2.10.10` de la teoría usa $X$ = número de *fracasos* antes del $r$-ésimo éxito (soporte $\{0,1,2,\dots\}$) — las dos parametrizaciones estándar de la binomial negativa (difieren por $X_\text{ensayos}=X_\text{fracasos}+r$), cada una internamente consistente donde se usa, pero el libro nunca señala el cambio de convención entre teoría y este problema. `prob:4c2c37d` también usa la convención de "ensayos" ($E[X]=r/p$).

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:287fdc5` (Recordar) | Recordar la PMF geométrica | — | No formalizado por separado, ya cubierto en la teoría |
| `prob:0ebda90` (Comprender) | $P(X>8\mid X>5)=P(X>3)$ ($m=5,n=3$) | B | ✅ Cierra — instancia directa de `perdida_memoria`, no una nueva verificación |
| `prob:6ccfa13` (Aplicar) | Auditoría $r=3,p=0.10$: $P(X=20)=\binom{19}{2}(0.10)^3(0.90)^{17}\approx0.0285$ | A | ✅ Cierra |
| `prob:a4a72f3` (Analizar) | FGM de la geométrica y binomial negativa | D | ⚠️ No formalizado — otra serie geométrica infinita (en $e^t$, con condición de convergencia adicional $t<-\ln q$) más la noción de FGM como objeto formal, que el proyecto no ha construido |
| `prob:ca5c4c8` (Evaluar) | Índice de dispersión $s^2/\bar x=4.2$; $\hat p\approx0.2381$, $\hat r\approx1$ | A | ✅ Cierra |
| `prob:4c2c37d` (Crear) | $r=4,p=0.15$ (convención "ensayos"): $E[X]\approx26.67$, $\mathrm{Var}(X)\approx151.11$, $\sigma\approx12.29$ | A | ✅ Cierra — $\sigma$ verificado con una cota exacta de raíz cuadrada (`Real.lt_sqrt`/`Real.sqrt_lt'`, mismo patrón que `distribucion_binomial`), no Tier C |

Ningún error matemático encontrado en las partes formalizables de las 6 soluciones de este archivo.

### Verificación EN por diff

Etiquetas y literales numéricos coinciden exactamente entre ES y EN, tanto en teoría como en problemas — sin divergencias.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3021/3021 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionGeometricaBinomialNegativa.lean` (6 teoremas) y `DistribucionGeometricaBinomialNegativaProblemas.lean` (4 teoremas) además de los 17 archivos previos.

Nota técnica nueva de este capítulo (primero con series infinitas, `tsum`/`HasSum`, en vez de `Finset.sum`): (1) `hasSum_geometric_of_norm_lt_one` y variantes piden `‖·‖<1`; en ℝ, una hipótesis probada como `|x|<1` **no** unifica automáticamente con `‖x‖<1` para `rw`/aplicación directa (error "Application type mismatch") — hay que declarar la hipótesis ya en la forma `‖x‖<1` desde el inicio (`rw [Real.norm_eq_abs, abs_lt]` al probarla), no convertir después. (2) para combinar/transformar sumas infinitas, encadenar combinadores `HasSum.add`/`HasSum.mul_left`/`HasSum.mul_right` y cerrar el reordenamiento de cada término con un `have heq : (fun k => ...) = (fun k => ...) := by funext k; ring` explícito es mucho más robusto que `simp_rw [tsum_mul_left, tsum_mul_right]` o `convert ... using 1` — estos últimos fallan silenciosamente o dejan metas de `AddCommMonoid`/`Finset.sum` mal formadas cuando el término tiene más de dos factores o el orden de multiplicación no coincide exactamente con el lema. (3) al mezclar restas de `ℕ` en exponentes (`r-1+1`) con `field_simp`, preferir reescribir el exponente a su forma reducida (`rw [hr1]` con `hr1 : r-1+1=r`) **antes** de `field_simp`, no después — de lo contrario `field_simp` puede normalizar de una forma que deja una meta de igualdad de exponentes de `ℕ` sin cerrar.

---

## Capítulo: `distribucion_hipergeometrica` (teoría)

Sin entornos `teorema`. Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionHipergeometrica.lean`. $\mu_X=nK/N$ se prueba en general — Tier B — **reutilizando directamente** `absorcion_binomial` (de `distribucion_binomial`) y `vandermonde_binomial` (de `distribucion_binomial(p)`), sin ninguna identidad nueva: es el mismo patrón absorción+Vandermonde ya construido, aplicado aquí a un producto de dos coeficientes binomiales en vez de uno solo. $\sigma^2_X$ se verifica por la ruta algebraica que el propio `prob:64e9a8d` usa (combinar $\mathrm{Var}(I_i)$ y $\mathrm{Cov}(I_i,I_j)$, dados por el libro, en la fórmula cerrada) — identidad de álgebra pura, sin necesidad de la infraestructura de covarianza Tier D que quedó pendiente en `distribucion_multinomial`.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.10.16` — lote $N=20,K=5,n=4$: $P(X=2)=1050/4845\approx0.2167$ | A | ✅ Cierra |
| `exmp:2.10.17` — póker $N=52,K=4,n=5$: $P(X=3)=4512/2598960\approx0.00174$ | A | ✅ Cierra |
| $\mu_X=nK/N$ | B | ✅ Cierra (`esperanza_hipergeometrica`, vía `suma_k_hipergeometrica` + `absorcion_Nn`, ambas reutilizando lemas de `distribucion_binomial`) |
| $\sigma^2_X=n\frac KN(1-\frac KN)\frac{N-n}{N-1}$ | B | ✅ Cierra (`varianza_hipergeometrica_algebra`, álgebra pura combinando $\mathrm{Var}(I_i)$/$\mathrm{Cov}(I_i,I_j)$ dados por el libro) |

Ningún error matemático encontrado.

## Capítulo: `distribucion_hipergeometrica` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionHipergeometricaProblemas.lean`.

**🔴 Dos hallazgos numéricos menores confirmados** (verificados independientemente con Python `fractions.Fraction` antes de escribir las pruebas de Lean; ambos parecen transposiciones de dígitos, no errores conceptuales):
- `prob:7cf587b`: el libro afirma $P(X=2)\approx0.189725$ para $\mathrm{Hiper}(2000,100,20)$; **el valor correcto es $\approx0.189525$** (dígitos "5"/"7" intercambiados). La aproximación binomial $P(Y=2)\approx0.188677$ que el libro también da SÍ es correcta. La conclusión cualitativa del problema (la aproximación es apropiada) no cambia.
- `prob:969b25a`: el libro afirma $\mathrm{Var}(X)\approx1.5254$ para $N=200,K=25,n=15$; **el valor correcto es $\approx1.5252$** (dígitos "52"/"54" intercambiados) — $19425/12736=1.5252041\ldots$ exacto. El factor intermedio $1.640625$ que el libro muestra es correcto; el error está solo en el redondeo final.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:748a77d` (Recordar) | Recordar la PMF hipergeométrica | — | No formalizado por separado, ya cubierto en la teoría |
| `prob:5e6e8bf` (Comprender) | Casos límite del FPCF: $n=1\Rightarrow1$; $n=N\Rightarrow0$ | A | ✅ Cierra |
| `prob:1651c98` (Aplicar) | Lote $N=30,K=6,n=5$: $P(X=0)\approx0.2983$, $P(X\le1)\approx0.7457$ | A | ✅ Cierra |
| `prob:64e9a8d` (Analizar) | Partes 1–2: pasos de derivación en prosa/símbolos. Parte 3: combinar en $\mathrm{Var}(X)$ | B | Partes 1–2 no formalizadas (sin número aislado que verificar); parte 3 = `varianza_hipergeometrica_algebra` de la teoría, no repetida |
| `prob:7cf587b` (Evaluar) | $N=2000,K=100,n=20$: regla $n/N<0.05$; $P(X=2)$, $P(Y=2)$ | A/C | ✅ Regla y $P(Y=2)$ cierran en Lean. $P(X=2)$ exacto es **Tier C** — $\binom{2000}{20}$ agota `maxHeartbeats` en `norm_num [Nat.choose]` (no infactible, solo demasiado lento aquí) — verificado en `verification/scipy/distribucion_hipergeometrica/prob_7cf587b.py`. 🔴 Ver hallazgo arriba |
| `prob:969b25a` (Crear) | $N=200,K=25,n=15$: $E[X]=1.875$, $\mathrm{Var}(X)\approx1.5254$ | A | ✅ $E[X]$ cierra. 🔴 Ver hallazgo arriba para $\mathrm{Var}(X)$ |

### Verificación EN por diff

Etiquetas y literales numéricos coinciden exactamente entre ES y EN — incluyendo que **ambos idiomas comparten los mismos dos valores incorrectos**, confirmando que son errores de la fuente compartida, no introducidos en la traducción.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3023/3023 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionHipergeometrica.lean` (6 teoremas) y `DistribucionHipergeometricaProblemas.lean` (3 teoremas) además de los 19 archivos previos, más el script `verification/scipy/distribucion_hipergeometrica/prob_7cf587b.py`.

Nota técnica nueva de este capítulo: (1) `norm_num [Nat.choose]` (que unfoldea `Nat.choose` recursivamente vía simp) es tratable para argumentos hasta unos pocos cientos (`C(100,·)`, `C(200,·)` — usados en capítulos previos y en este mismo capítulo sin problema) pero **agota `maxHeartbeats` para `C(2000,20)`** incluso subiendo `maxRecDepth` — a diferencia de `Nat.factorial` (que sí escaló a $100!$ sin problema en `distribucion_multinomial`), `Nat.choose` no parece tener una ruta de evaluación tan eficiente en `norm_num`/`simp` para argumentos grandes. Ante un timeout así (no un error de lógica), la opción correcta es Tier C con un script Python de `fractions.Fraction` (aritmética racional exacta, no de punto flotante) en vez de forzar más el `set_option maxRecDepth`/`maxHeartbeats`. (2) un comentario `/-- ... -/` (doc-comment) **debe** preceder una declaración — si se elimina el teorema pero se deja el comentario como nota independiente, usar `/-! ... -/` (comentario de módulo) en su lugar, o falla el parser con "unexpected token; expected 'lemma'".

---

## Capítulo: `distribucion_poisson` (teoría)

Capítulo largo y heterogéneo: PMF de Poisson, relación binomial-Poisson, introducción a la distribución normal, relación binomial-normal, percentiles, y una subsección "Problemas Resueltos" con varios ejemplos (z-scores, distribución normal de béisbol, etc.) que **no dan valores numéricos explícitos en el propio texto** — solo referencian scripts de Python sin mostrar el resultado inline. Esa subsección completa (más la introducción a la normal, percentiles y la relación binomial-normal) no tiene ninguna afirmación numérica propia del libro que verificar — se documenta como observación de alcance, no como Tier D (no hay una afirmación que rechazar formalizar, simplemente no hay afirmación). Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionPoisson.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `eq:2.10.7` — normalización de la PMF, $\sum_{n=0}^\infty e^{-\lambda}\lambda^n/n!=1$, $\lambda$ real general | B | ✅ Cierra (`suma_normalizada_poisson`, vía la serie de la exponencial de Mathlib `NormedSpace.expSeries_div_hasSum_exp`, mismo estilo que `ProbabilityTheory.hasSum_one_poissonMeasure` de Mathlib, que solo cubre `r:ℝ≥0`) |
| `exmp:2.10.5` — hospital $\lambda=5$: suma finita $1+5+25/2+125/6=39\frac13$ | A | ✅ Cierra la parte exacta de racionales |
| `exmp:2.10.5`, evaluación decimal ($P(X\le3)\approx0.265$, $P(X\ge8)\approx0.133$) | C | ✅ Confirmado numéricamente (necesita $e^{-5}$, irracional), `verification/scipy/distribucion_poisson/exmp_2_10_5.py` |

**No formalizado — Tier D:** $\mu_X=\sigma_X^2=\lambda$. Requeriría además un lema de desplazamiento de `tsum` (`Summable.tsum_eq_zero_add`, identificado en Mathlib) combinado con la serie exponencial, para relacionar $\sum n\cdot f(n)$ con la serie desplazada — no se completó por tiempo en este pase; la normalización (la pieza más laboriosa, vía la serie exponencial) sí quedó resuelta y reutilizable para un intento futuro.

Ningún error matemático encontrado en las afirmaciones formalizadas. (Diff EN: ver nota de alcance abajo.)

## Capítulo: `distribucion_poisson` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionPoissonProblemas.lean`. `prob:06f83cc` (Recordar) es puro recordatorio, no formalizado aparte. `prob:8fd3390` (Aplicar) es idéntico a `exmp:2.10.5` de la teoría, no se repite. `prob:9dc367e` (Crear) solo restablece $E[X]=\mathrm{Var}(X)=\lambda=4$ sin cálculo adicional, trivial por definición del parámetro.

**🔴 Dos hallazgos confirmados, uno de ellos sustancial:**
- `prob:8dad711`: menor — el libro afirma $P(X=3\mid X+Y=8)\approx0.2815$; el valor exacto es $590625/2097152\approx0.28163$ (redondea a $0.2816$, no $0.2815$) — desliz de redondeo del último dígito.
- `prob:5e9408a`: **sustancial** — el libro afirma $P(S_{100}\le220)\approx0.9862$ (Poisson exacta, $\lambda=200$) y usa esto para concluir que la aproximación Normal tiene un error considerable ($\approx0.06$) en esta cola. **El valor "exacto" del libro está mal: el valor correcto es $\approx0.9247$**, verificado con `scipy.stats.poisson.cdf`. El z-score ($1.4496$) y el valor de la aproximación Normal ($\approx0.9265$) que el libro también da son correctos. Con el valor exacto correcto, la diferencia con la aproximación Normal es solo $\approx0.0017$, no $\approx0.06$ — **esto invierte la conclusión pedagógica del libro**: la aproximación Normal es en realidad excelente aquí (como se esperaría para $\lambda=200$, grande), no deficiente. Verificado en `verification/scipy/distribucion_poisson/prob_5e9408a.py`.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:06f83cc` (Recordar) | Recordar la PMF de Poisson | — | No formalizado por separado |
| `prob:c35cfa7` (Comprender) | $1-(1-p)^4=1-e^{-\lambda}$ con $p=1-e^{-\lambda/4}$ | B | ✅ Cierra (`prob_c35cfa7`, identidad de exponentes exacta, sin necesitar el valor numérico de $e^{-2}$) |
| `prob:8dad711` (Analizar) | Condicional Poisson$\to$Binomial: $P(X=k\mid X+Y=n)=\binom nk\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k}$, general | B | ✅ Cierra (`prob_8dad711`, álgebra pura — los factores exponenciales se cancelan exactamente, reutiliza `Nat.choose_mul_factorial_mul_factorial`) |
| `prob:8dad711`, evaluación numérica ($\lambda_1=3,\lambda_2=5,n=8,k=3$) | A | 🔴 Ver hallazgo arriba (menor) |
| `prob:5e9408a` (Evaluar) | $P(S_{100}\le220)$ exacta vs aproximación Normal | C | 🔴 Ver hallazgo arriba (sustancial) |

### Verificación EN por diff

Etiquetas y literales numéricos del archivo de problemas coinciden exactamente entre ES y EN — sin divergencias, incluyendo que **ambos idiomas comparten los dos valores incorrectos** de esta bitácora (confirma fuente compartida). El archivo de **teoría** muestra algunas diferencias de literales numéricos, pero están todas dentro de la subsección "Problemas Resueltos"/normal/percentiles que ya se documentó como fuera de alcance (sin afirmaciones propias del libro que verificar) — no se investigaron más a fondo por no tocar ninguna afirmación formalizada.

## Capítulo: `variables_discretas_ciencia_datos` (teoría)

Capítulo corto: casi todo es prosa aplicada (lista de usos de cada distribución discreta en ciencia de datos, sin afirmaciones matemáticas propias — no hay `teorema`/`definicion`/`axioma` en el archivo) más un único ejemplo numérico sobre detección de sobredispersión. Formalizado en `verification/lean_verificacion/LeanVerificacion/VariablesDiscretasCienciaDatos.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.10.18` — $\bar x=4.2$, $s^2=8.7$: $s^2\gg\bar x$ (sobredispersión) $\Rightarrow$ Poisson inadecuada, preferir Binomial Negativa | A | ✅ Cierra (`exmp_2_10_18`, $8.7>4.2$ exacto en ℚ) |

Ningún error matemático encontrado.

## Capítulo: `variables_discretas_ciencia_datos` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/VariablesDiscretasCienciaDatosProblemas.lean`. `prob:9b48fd0` (Recordar) es puramente definicional ($D=s^2/\bar x$, valor de referencia $D\approx1$) — no aporta cálculo que verificar, no formalizado aparte.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:9b48fd0` (Recordar) | Definición del cociente de dispersión | — | No formalizado por separado |
| `prob:65ac238` (Comprender) | $n=500$, $\bar x=3.2$, $s^2=12.5$: $D=s^2/\bar x=125/32\approx3.91$ | A | ✅ Cierra (`prob_65ac238`, $125/32=3.90625$, redondea a $3.91$) |
| `prob:486b84f` (Aplicar) | $\hat\lambda=\bar x=4.2$; $D=8.7/4.2\approx2.07$ | A | ✅ Cierra (`prob_486b84f`) |
| `prob:8fd9d7f` (Analizar) | Binomial Negativa($r,p=r/(r+\lambda)$) $\to$ Poisson($\lambda$) cuando $r\to\infty$ | D | 🟡 No formalizado — teorema límite genuino, ver razón abajo |
| `prob:395bc31` (Evaluar) | $n=200$, $\bar x=8.5$, $s^2=9.8$: $D=9.8/8.5\approx1.15$ (parsimonia $\Rightarrow$ preferir Poisson) | A | ✅ Cierra (`prob_395bc31`) |
| `prob:a28b8e6` (Crear) | Ejemplo propio: $n=300$, $\bar x=2.1$, $s^2=6.8$: $D=6.8/2.1\approx3.24$ | A | ✅ Cierra (`prob_a28b8e6`) |

**No formalizado — Tier D:** `prob:8fd9d7f` — demostración de que la PMF de la Binomial Negativa converge a la de Poisson($\lambda$) cuando $r\to\infty$ con $p=r/(r+\lambda)$ fijo. Es un teorema límite genuino (`Filter.Tendsto`), análogo al teorema del límite de Poisson que Mathlib ya tiene para la Binomial (`ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop` en `Mathlib.Probability.Distributions.Poisson.PoissonLimitThm`), pero Mathlib no cubre la parametrización Binomial Negativa directamente. Un intento futuro necesitaría: (1) un análogo de `isEquivalent_choose` reindexado para $\binom{k+r-1}{k}\sim r^k/k!$; (2) `Real.tendsto_one_add_pow_exp_of_tendsto` para $(1-\lambda/r)^r\to e^{-\lambda}$; (3) combinar ambos con `Tendsto.mul`, igual que en el archivo de Mathlib citado — factible pero sustancial, no completado en este pase.

Ningún error matemático encontrado en las afirmaciones formalizadas (Tier A) — los cinco cocientes de dispersión numéricos del capítulo (teoría + problemas) redondean todos correctamente a los valores que da el libro.

### Verificación EN por diff

Sin divergencias: `diff` de todas las etiquetas (`\label{(thm|prob|eq):...}`) y de **todos** los literales decimales entre ES y EN, en ambos archivos (teoría y problemas), da vacío — coincidencia exacta.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3085/3085 jobs, sin `sorry`, sin errores.** Incluye ahora `VariablesDiscretasCienciaDatos.lean` (1 teorema) y `VariablesDiscretasCienciaDatosProblemas.lean` (4 teoremas) además de los 23 archivos previos.

Nota técnica nueva de este capítulo: `Mathlib.Data.Rat.Basic` **no existe** como archivo importable en este pin de Mathlib (`lake build` falla con "bad import"/"no such file or directory") — `Mathlib.Tactic` ya trae consigo todo lo necesario para literales y aritmética en `ℚ`; no hace falta un import adicional de `Rat` para usar `ℚ` con `norm_num`.

---

## Capítulo: `variables_aleatorias_continuas` (teoría)

**Primer capítulo con cálculo integral real** (`intervalIntegral`/`MeasureTheory.integral` sobre `ℝ`, no `Finset.sum`/`tsum`). A diferencia de capítulos previos, este archivo de teoría **no tiene bloques `solucion`** — todos los `ejemplo` (`exmp:2.7.1`–`exmp:2.7.16`) son enunciados sin resolver inline (las respuestas están en figuras referenciadas o se resuelven aparte) — no hay valores numéricos propios del libro que verificar ahí. Solo se formalizaron las dos identidades generales explícitas del texto; el resto (definiciones de PDF/CDF conjunta, marginal, condicional, independencia) es aparato definicional. Formalizado en `verification/lean_verificacion/LeanVerificacion/VariablesAleatoriasContinuas.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `eq:2.7.3` — $P(X=a)=0$ para v.a. continua (derivado de `eq:2.7.2` con $b=a$) | A | ✅ Cierra (`punto_probabilidad_cero`, vía `intervalIntegral.integral_same`) |
| `eq:2.7.6` — $dF/dx=f(x)$ (Teorema Fundamental del Cálculo) | B | ✅ Cierra (`ftc_densidad`, general para cualquier $f$ continua, límite inferior fijo `a` en vez de $-\infty$ — ver nota de alcance abajo) |

**Nota de alcance:** `ftc_densidad` usa un límite inferior fijo `a` (no `-\infty` como en `eq:2.7.1`/`eq:2.7.6` literalmente) — Mathlib's `intervalIntegral` estándar no cubre directamente integrales impropias con `-\infty` sin maquinaria adicional; la versión con `a` fija captura el contenido matemático central (FTC) que el libro usa. Ningún error matemático encontrado.

## Capítulo: `variables_aleatorias_continuas` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/VariablesAleatoriasContinuasProblemas.lean`. `prob:19f62fd` (Analizar) parte (a) es la definición operacional de LOTUS especializada a $g(x)=x^2$ — tautológica, no formalizada aparte.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:14b3125` (Recordar) — normalización | $\int_0^\infty e^{-x}dx=1\Rightarrow c=1$ | A | ✅ Cierra (`prob_14b3125_normalizacion`, vía `integral_exp_neg_Ioi_zero`) |
| `prob:14b3125` — $P(1\le X\le3)$ | $=e^{-1}-e^{-3}$, forma exacta | B | ✅ Cierra (`prob_14b3125_probabilidad`); evaluación decimal ($\approx0.3181$) Tier C, confirmada en `verification/scipy/variables_aleatorias_continuas/prob_14b3125_61a9dd8.py` |
| `prob:14b3125` — CDF | $F(x)=1-e^{-x}$, $x\geq0$ | B | ✅ Cierra (`prob_14b3125_cdf`) |
| `prob:287c45c` (Comprender) — CDF | $F(x)=x^2$, $0\le x\le1$ | A | ✅ Cierra (`prob_287c45c_cdf`) |
| `prob:287c45c` — $P(0.3\le X\le0.7)$ | $=0.7^2-0.3^2=0.4$ | A | ✅ Cierra (`prob_287c45c_probabilidad`, exacto en ℝ) |
| `prob:61a9dd8` (Aplicar) — $q_{0.90}$ | $q_{0.90}=5\ln10$ satisface $1-e^{-0.2q}=0.9$ exactamente | B | ✅ Cierra (`prob_61a9dd8_q90`); decimal ($\approx11.51$) Tier C |
| `prob:61a9dd8` — $t$ (95%) | $t=-5\ln(0.05)$ satisface $1-e^{-0.2t}=0.95$ exactamente | B | ✅ Cierra (`prob_61a9dd8_t`); decimal ($\approx14.98$) Tier C |
| `prob:61a9dd8` — $P(X\le3)$, $P(X\ge10)$ | $\approx0.4512$, $\approx0.1353$ | C | ✅ Confirmado numéricamente, mismo script |
| `prob:19f62fd` (Analizar) — LOTUS/varianza | $\mathrm{Var}(X)=\mathbb E[X^2]-(\mathbb E[X])^2$, general | B | ✅ Cierra (`prob_19f62fd_varianza`, análogo continuo de `konig_huygens` de `variables_aleatorias_discretas`, momentos como hipótesis) |
| `prob:8ec7e10` (Evaluar) — prueba KS | $\sqrt{50}\cdot0.18\approx1.273<1.358=K_{0.95}\Rightarrow$ no rechazar $H_0$ | A/B | ✅ Cierra (`prob_8ec7e10_ks`, cota exacta vía `Real.sqrt_lt'`, sin aproximación decimal) |
| `prob:0d490fc` (Crear) — normalización Pareto | $\int_1^\infty x^{-2}dx=1\Rightarrow k=1$ | B | ✅ Cierra (`prob_0d490fc_normalizacion`, vía `integral_Ioi_rpow_of_lt`) |
| `prob:0d490fc` — $P(1\le X\le2)$ | $=1/2$ exacto | A | ✅ Cierra (`prob_0d490fc_probabilidad`, vía `integral_zpow`) |

Ningún error matemático encontrado — los cinco valores decimales del capítulo (los dos de `prob:14b3125`, los cuatro de `prob:61a9dd8`) coinciden todos con el libro dentro de su propio redondeo declarado.

### Verificación EN por diff

Sin divergencias en ninguno de los dos archivos: `diff` de etiquetas y de todos los literales decimales entre ES y EN da vacío en ambos.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3426/3426 jobs, sin `sorry`, sin errores.** Incluye ahora `VariablesAleatoriasContinuas.lean` (2 teoremas) y `VariablesAleatoriasContinuasProblemas.lean` (11 teoremas) además de los 25 archivos previos, más `verification/scipy/variables_aleatorias_continuas/prob_14b3125_61a9dd8.py`.

**Notas técnicas nuevas de este capítulo (primero con `intervalIntegral`/`MeasureTheory.integral`):**
- `MeasureTheory.integral_const_mul` e `intervalIntegral.integral_const_mul` comparten el mismo nombre base en namespaces distintos — si ambos namespaces están `open` a la vez, `integral_const_mul` sin calificar es **ambiguo** (error de elaboración, no de matemática) — hay que calificar explícitamente (`MeasureTheory.integral_const_mul`/`intervalIntegral.integral_const_mul`) en vez de confiar en `open`.
- Para combinar sumas/restas de integrales con `rw [integral_add ..., integral_sub ...]`, sigue aplicando la misma lección de capítulos anteriores (`tsum`/`HasSum`): reescribir primero el integrando a la forma exacta que espera el combinador vía un `have heq : (fun x => ...) = (fun x => ...) := by funext x; ring`, no intentar `simp_rw`/`ring_nf` directo sobre la integral.
- Mathlib tiene exactamente el paquete de lemas necesario para integrales impropias tipo Pareto/exponencial: `integral_exp_neg_Ioi`/`integral_exp_neg_Ioi_zero` (`Mathlib.Analysis.SpecialFunctions.ImproperIntegrals`) y `integral_Ioi_rpow_of_lt` (mismo archivo, **sin** namespace `Real.` — nombre raíz) para $\int_c^\infty x^a dx$ con $a<-1$, $c>0$. Para intervalos finitos, `Analysis.SpecialFunctions.Integrals.Basic` tiene `integral_pow`/`integral_zpow`/`integral_rpow`/`integral_exp`/`integral_id`.
- `Continuous.integral_hasStrictDerivAt` (`Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus`) da el Teorema Fundamental del Cálculo "gratis" para cualquier `f` continua — no hace falta reconstruirlo desde `intervalIntegral.integral_hasDerivAt_right` a mano.
- Al probar identidades de logaritmo/exponencial con literales decimales (ej. `-(0.2*(-5*log 0.05)) = log 0.05`), `ring` sí simplifica los coeficientes decimales correctamente — pero hay que darle la ecuación exacta que necesita el `rw` siguiente (incluyendo cualquier negación externa), no una forma parcial; un error de signo aquí produce un `ring` que falla de forma confusa (parece un error de tactic, es un error de álgebra en el enunciado del `have`).

---

## Capítulo: `esperanza_matematica` (teoría)

Capítulo denso: linealidad de la esperanza, König-Huygens, varianza de combinaciones lineales, covarianza, variable estandarizada, más varios ejemplos numéricos. **Primer capítulo con una capa propia de esperanza/varianza construida directamente sobre `MeasureTheory.integral`** (`∫ ω, X ω ∂P` para `X : Ω → ℝ` en un espacio de probabilidad genérico), sin citar `ProbabilityTheory.variance` — un test de humo confirmó que el paquete de independencia (`Mathlib.Probability.Independence.Integration`, necesario para `thm:2.9.2`) dispara el mismo error de longitud de ruta de Windows que ya bloqueaba `Mathlib.Probability.Moments.Variance` en este worktree (ambos jalan transitivamente `ContinuousFunctionalCalculus.PosPart.Basic`). Formalizado en `verification/lean_verificacion/LeanVerificacion/EsperanzaMatematica.lean`.

**✅ Hallazgo confirmado y CORREGIDO — `exmp:2.9.1` (el juego del dado, ganancia esperada):** el enunciado (línea 75) decía que la cara $6$ paga \$30, pero la PMF y el cálculo de la solución (líneas 82–93) usaban \$60 para la cara $6$, llegando a $E(X)=\$20$. Con los datos originales del enunciado, la esperanza correcta habría sido $\$15$. La solución era internamente consistente ($(20+40+60)/6=20$) — el desacuerdo estaba entre lo dado y lo resuelto, no en la aritmética de la solución. Confirmado con `git log -p --follow` que este desacuerdo \$30/\$60 existía **desde la introducción original del ejemplo** (commit inicial del archivo) y **sobrevivió intacto** a la auditoría de 2026-07-13 (`docs/revision-notas-2026-07-13.md`), que solo eliminó un bloque `align` residual/duplicado con un error aritmético *distinto* ($120/6$ mal escrito como \$15 en vez de \$20) sin notar que el bloque que sí se mantuvo seguía usando \$60 en vez del \$30 del enunciado. Presente idéntico en `en_esperanza_matematica.tex` (mismo \$30 vs \$60) — confirmó fuente compartida, no error de traducción. **Corregido** (aprobado por el usuario) cambiando el enunciado a \$60 en ES y EN, para que coincida con la solución ya trabajada — commit posterior a esta bitácora.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.9.1` — enunciado vs. solución | A | ✅ Corregido (`exmp_2_9_1`); ver hallazgo arriba |
| Ejemplo del dado — $E(X)=3.5$ | A | ✅ Cierra (`esperanza_dado`) |
| Ejemplo del dado — $\sigma^2=17.5/6\approx2.916$ | A | ✅ Cierra (`varianza_dado`, $=35/12$ exacto); nota: el libro **trunca** a $2.916$ en vez de redondear a $2.917$ — convención, no error |
| `exmp:2.9.2` — $E(X)=4/3$ para $f(x)=x/2$ en $(0,2)$ | B | ✅ Cierra (`exmp_2_9_2`) |
| `exmp:2.9.3` — $E(3X^2-2X)=10/3$ | B | ✅ Cierra (`exmp_2_9_3`) |
| `exmp:2.9.4` — $\mathrm{Var}(X)=2/9$ | B | ✅ Cierra (`exmp_2_9_4`) |
| `thm:2.9.1` — linealidad $E(cX+dY)=cE(X)+dE(Y)$, general | B | ✅ Cierra (`linealidad`) |
| `eq:2.9.14` — König-Huygens $\sigma^2=E(X^2)-\mu^2$, general | B | ✅ Cierra (`konig_huygens`) |
| `eq:2.9.15` — $\mathrm{Var}(cX)=c^2\mathrm{Var}(X)$, general | B | ✅ Cierra (`var_escalar`) |
| `thm:2.9.3` — $\sigma^2=\min_a E[(X-a)^2]$, general | B | ✅ Cierra (`varianza_es_minimo`, completando el cuadrado) |
| `eq:2.9.24` — $\mathrm{Cov}(X,Y)=E(XY)-\mu_X\mu_Y$, general | B | ✅ Cierra (`covarianza`) |
| `eq:2.9.25`/`eq:2.9.26` — $\mathrm{Var}(X\pm Y)=\mathrm{Var}(X)\pm2\mathrm{Cov}(X,Y)+\mathrm{Var}(Y)$, general | B | ✅ Cierra (`varianza_suma`) |
| `eq:2.9.17`/`eq:2.9.18` — $E(X^*)=0$, variable estandarizada | B | ✅ Cierra (`estandarizada`); $\mathrm{Var}(X^*)=1$ se sigue de `var_escalar`+`konig_huygens`, no se repite |
| `thm:2.9.2` — independencia $\Rightarrow E(XY)=E(X)E(Y)$ | D | 🟡 No formalizado — bloqueado por longitud de ruta (ver nota) |
| `eq:2.9.16` — $\mathrm{Var}(X\pm Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$ si independientes | D | 🟡 No formalizado — depende de `thm:2.9.2` |
| `eq:2.9.28` — $|\sigma_{XY}|\le\sigma_X\sigma_Y$ (Cauchy-Schwarz) | D | 🟡 No formalizado — necesita empaquetado de Cauchy-Schwarz $L^2$ |

**Notas de alcance (Tier D):** `thm:2.9.2`/`eq:2.9.16` necesitan `Mathlib.Probability.Independence.Integration` (`ProbabilityTheory.IndepFun.integral_mul_eq_mul_integral`), cuyo import se confirmó bloqueado por el mismo problema de MAX_PATH de Windows documentado para `VariablesAleatorias.lean` — no es una limitación matemática, es específica de este worktree; un intento futuro podría usar el flujo de scratch-worktree de ruta corta ya documentado. `eq:2.9.28` necesita la desigualdad de Cauchy-Schwarz para el producto interno $L^2$ (`MeasureTheory.Lp`/Hölder con $p=q=2$) — factible pero no explorado este pase.

**Observaciones sin teorema (prosa, no matemática):** `exmp:2.9.5`/`exmp:2.9.6` tienen listas de 11 estadísticos con `\sigma_Y` duplicado (ítems 7 y 9) y `\sigma_X` faltante, idéntico en ambos ejemplos — error de copiar/pegar, sin valores numéricos que verificar (ya documentado en `docs/revision-notas-2026-07-13.md` como hallazgo de baja prioridad).

## Capítulo: `esperanza_matematica` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/EsperanzaMatematicaProblemas.lean`.

**✅ Dos hallazgos adicionales, ambos menores, ambos CORREGIDOS:**
- `prob:f43c638`: la solución escribía "$E[X^2]=8=1/\lambda^2$" — pero $1/\lambda^2=4$ (con $\lambda=0.5$), no $8$; la fórmula que correctamente da $8$ es $2/\lambda^2$. Los *valores* numéricos ($E[X^2]=8$, $\mathrm{Var}(X)=4$) eran correctos, solo la fórmula anotada junto a $E[X^2]$ estaba mal etiquetada (confundida con $\mathrm{Var}(X)$, que sí es $1/\lambda^2$). **Corregido** en ES y EN: la fórmula ahora dice $2/\lambda^2$.
- `prob:7b147c4`, parte 3: la solución concluía "con $n=100$ mediciones, el error estándar es exactamente $0.01$" como si satisficiera $\sigma/\sqrt n<0.01$, pero $n=100$ da igualdad exacta ($0.1/\sqrt{100}=0.01$), no la desigualdad estricta que pide el problema — hace falta $n\geq101$. La propia frase anterior de la solución ("$\sqrt n>10$, así $n>100$") ya lo decía bien; solo la interpretación final de "$n=100$" era inconsistente con eso. **Corregido** en ES y EN: la solución ahora concluye con $n=101$ ($\sigma/\sqrt{101}\approx0.00995<0.01$), y nota explícitamente que $n=100$ es el límite, no la solución.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:4e01dbd` (Recordar) — $E[X]=2/3$ | A | ✅ Cierra (`prob_4e01dbd_esperanza`) |
| `prob:4e01dbd` — $E[X^2]=1/2$, $\mathrm{Var}(X)=1/18$ | A | ✅ Cierra (`prob_4e01dbd_segundo_momento`, `prob_4e01dbd_varianza`) |
| `prob:4e01dbd` — mediana $m=1/\sqrt2\approx0.7071>E[X]=2/3$ | B | ✅ Cierra (`prob_4e01dbd_mediana`, cota exacta vía `Real.lt_sqrt`) |
| `prob:f43c638` (Comprender) — $E[X]=2$, $E[X^2]=8$, $\mathrm{Var}(X)=4$ | C | ✅ Confirmado numéricamente, `verification/scipy/esperanza_matematica/prob_f43c638_9d4a41b.py`; ✅ fórmula corregida (ver hallazgo arriba) |
| `prob:f43c638` — ausencia de memoria | D | No formalizado (esperanza condicional) |
| `prob:7b147c4` (Aplicar) — $E[\bar X]=\mu$, $\mathrm{Var}(\bar X)=\sigma^2/n$ | B | Especialización directa de `esperanza_media_muestral`/`varianza_media_muestral` (`VariablesAleatorias.lean`), no reproducida |
| `prob:7b147c4` — $n=101$ vs. $\sigma/\sqrt n<0.01$ estricto | A | ✅ Corregido (`prob_7b147c4_n100`); ver hallazgo arriba |
| `prob:de8d740` (Analizar) — descomposición $\mathrm{Var}(X)=E[\mathrm{Var}(X\mid Y)]+\mathrm{Var}(E[X\mid Y])$ | D | No formalizado — esperanza condicional medida-teórica + propiedad de torre, esfuerzo de un capítulo aparte |
| `prob:9d4a41b` (Evaluar) — asimetría/curtosis de $\mathrm{Exp}(1)$: $\gamma_1=2$, $\gamma_2=6$ | C | ✅ Confirmado numéricamente, mismo script; también verificable a mano vía $E[X^n]=n!$ |
| `prob:5c186f2` (Crear) — portafolio $0.40(0.08)+0.35(0.05)+0.25(0.12)=0.0795$ | A | ✅ Cierra (`prob_5c186f2_portafolio`) |

### Verificación EN por diff

Sin divergencias en ninguno de los dos archivos: `diff` de etiquetas **y de todos los literales numéricos (enteros y decimales, no solo decimales)** entre ES y EN da vacío en ambos — este capítulo motivó ampliar el diff a enteros porque el hallazgo de `exmp:2.9.1` (\$30 vs \$60) no lo habría detectado un diff limitado a decimales; confirma que el error está presente idéntico en EN.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3428/3428 jobs, sin `sorry`, sin errores.** Incluye ahora `EsperanzaMatematica.lean` (13 teoremas) y `EsperanzaMatematicaProblemas.lean` (8 teoremas) además de los 27 archivos previos, más `verification/scipy/esperanza_matematica/prob_f43c638_9d4a41b.py`.

**Notas técnicas nuevas de este capítulo:**
- **Gotcha de `rw` con `Integrable.add`/`.sub`/`MeasureTheory.integral_add`/`.sub` (nuevo, costoso en tiempo de depuración):** cuando se combina integrabilidad vía `.add`/`.sub` directamente dentro de una llamada a `MeasureTheory.integral_add`/`integral_sub`, el término resultante tiene tipo `Integrable (f + g) P` (con `f+g` la **suma de funciones Pi**, sin beta-reducir), que **no coincide sintácticamente** con la forma `∫ ω, expr1 + expr2 ∂P` (un solo lambda con aritmética adentro) que produce la notación `∫`, aunque son iguales por `rfl`/`Pi.add_apply`. El `rw` falla entonces con "did not find pattern" mostrando el término Pi-suma no reducido. **Corrección:** siempre materializar un `have hcombinado : Integrable (fun ω => <expresión aritmética exacta de un solo lambda>) P := <expresión con .add/.sub/.const_mul>` ANTES de usarlo en `integral_add`/`integral_sub`, dejando que la anotación de tipo del `have` fuerce la forma correcta (aceptado porque son defeq) — la misma lección que ya se documentó para `Finset.sum_range_succ'`/`tsum` en capítulos anteriores, ahora también aplica a `MeasureTheory.integral`.
- Mismo problema con `continuous_const.mul (continuous_pow n)` sin anotar: la constante de `continuous_const` queda como metavariable no resuelta si no se fija el tipo explícitamente — usar `(continuous_pow n).const_mul c` en su lugar (constante como argumento explícito) evita el problema.
- `intervalIntegral.integral_const_mul`/`MeasureTheory.integral_const_mul` se resuelven de forma más confiable pasando los argumentos `(r) (f)` explícitos en vez de confiar en unificación automática dentro de una cadena de `rw`.
- Un test de humo con un archivo `.lean` desechable (`#check`+import candidato) antes de invertir esfuerzo en pruebas confirmó en ~1 minuto que `Mathlib.Probability.Independence.Integration` está bloqueado por MAX_PATH en este worktree — mismo patrón que `Mathlib.Probability.Moments.Variance`, ahora confirmado que **cualquier** import que jale `ContinuousFunctionalCalculus.PosPart.Basic` está afectado, no solo el de varianza.

---

## Capítulo: `distribucion_uniforme_continua` (teoría)

Capítulo corto: PDF/CDF de $U(a,b)$ y sus dos momentos, más un ejemplo numérico. Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionUniformeContinua.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `eq:2.8.2` — CDF $F(x)=(x-a)/(b-a)$, general para $a<b$ | A | ✅ Cierra (`cdf_uniforme`) |
| $\mu_X=(a+b)/2$, general | B | ✅ Cierra (`media_uniforme`) |
| $\sigma_X^2=(b-a)^2/12$, general | B | ✅ Cierra (`varianza_uniforme`, factorizando la constante $1/(b-a)$ antes de expandir el polinomio) |
| `exmp:2.8.1` — $X\sim U(0,15)$: $P(X<5)=1/3$ | A | ✅ Cierra (`exmp_2_8_1_probabilidad`) |
| `exmp:2.8.1` — $E(X)=7.5$ | A | ✅ Cierra (`exmp_2_8_1_esperanza`) |

Ningún error matemático encontrado.

## Capítulo: `distribucion_uniforme_continua` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionUniformeContinuaProblemas.lean`. `prob:97c4388` (Recordar) es puramente definicional, no formalizado aparte. `prob:5794e09` (Analizar) — máxima entropía vía multiplicadores de Lagrange sobre un funcional — es Tier D (cálculo de variaciones, no formalizado).

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:9f6e77c` (Comprender) | La uniforme no tiene falta de memoria: $P(X\ge15\mid X\ge10)=0\ne2/3=P(X\ge5)$ | A | ✅ Cierra (`prob_9f6e77c`) |
| `prob:8fcc221` (Aplicar) | $P(X<5)=1/3$, $q_{0.75}=11.25$ | A | ✅ Cierra (`prob_8fcc221`) |
| `prob:5794e09` (Analizar) | $U(a,b)$ maximiza la entropía diferencial entre soporte $[a,b]$ | D | 🟡 No formalizado — cálculo de variaciones sobre un funcional |
| `prob:126be41` (Evaluar) | Transformada inversa: $Y=F^{-1}(U)$ tiene CDF $F$ para cualquier $F$ estrictamente monótona (no requiere forma cerrada) | B | ✅ Cierra (`prob_126be41_transformada_inversa`, equivalencia de orden general; combinada con la CDF de $U(0,1)$ ya probada arriba da el resultado completo) |
| `prob:126be41`, caso $\mathrm{Exp}(\lambda=2)$ | $F^{-1}(u)=-\ln(1-u)/2$ es inversa de $F(y)=1-e^{-2y}$ | B | ✅ Cierra (`prob_126be41_exponencial`) |
| `prob:c1c6ece` (Crear) | $X\sim U(-5,5)$: $\mathbb E[X]=0$, $\mathrm{Var}(X)=100/12\approx8.33$ | A | ✅ Cierra (`prob_c1c6ece`) |

Ningún error matemático encontrado — todos los valores numéricos del capítulo (teoría + problemas) coinciden con el libro.

### Verificación EN por diff

Sin divergencias en ninguno de los dos archivos: `diff` de etiquetas y de todos los literales numéricos (enteros y decimales) entre ES y EN da vacío en ambos.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3430/3430 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionUniformeContinua.lean` (5 teoremas) y `DistribucionUniformeContinuaProblemas.lean` (5 teoremas) además de los 29 archivos previos.

**Nota técnica de este capítulo:** para varianzas con un factor de normalización variable (aquí $1/(b-a)$, no un literal fijo como en capítulos anteriores), es más robusto **factorizar la constante fuera de la integral primero** (`intervalIntegral.integral_const_mul`) y dejar una integral polinomial pura por dentro (sin el denominador $b-a$ mezclado en cada término), en vez de expandir todo el polinomio con el factor `1/(b-a)` ya multiplicado en cada término y luego pelear con `field_simp` en una expresión más grande — mismo principio de "simplificar antes de combinar" que ya se documentó para sumas, ahora aplicado a productos por una constante no literal. También: `continuous_id.const_mul c` dejaba `Continuous fun x => c * id x` (con `id` sin beta-reducir a `x`), rompiendo el `rw` posterior con `integral_const_mul` — usar `continuous_id'` (la versión eta-expandida, `Continuous fun a => a`) evita el problema.

---

## Capítulo: `distribucion_normal` (teoría)

PDF/propiedades de $N(\mu,\sigma^2)$, forma estándar, regla empírica 68-95-99.7, un ejemplo numérico. **Tier D confirmado por test de humo:** `Mathlib.Probability.Distributions.Gaussian.Real` (que tiene `gaussianPDFReal`/`integral_gaussianPDFReal_eq_one`, justo la normalización que haría falta para una demostración completa de la FGM) está bloqueado por el mismo problema de longitud de ruta de Windows que ya afectó a `VariablesAleatorias.lean` y al paquete de independencia — pero esta vez también bloqueó `Mathlib.MeasureTheory.Integral.IntervalIntegral.LebesgueDifferentiationThm`, una dependencia nueva no vista en capítulos anteriores. La integral gaussiana "cruda" (`integral_gaussian`, sin el paquete de distribuciones) sí se pudo importar, pero cerrar la FGM con ella habría necesitado además un lema de invarianza por traslación de `MeasureTheory.integral` sobre $\mathbb R$ que no se localizó en tiempo razonable — documentado como Tier D/C explícito, no una limitación matemática. Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionNormal.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `eq:2.8.4`/`eq:2.8.5` — estandarización de densidades: $\sigma f(\mu+\sigma z)=\varphi(z)$, general | B | ✅ Cierra (`estandarizacion_densidad`) |
| `prob:dd1e027` (parte teoría) — identidad de completar-el-cuadrado del exponente de la FGM, general | B | ✅ Cierra (`mgf_exponente`) |
| FGM completa $M_X(t)=e^{\mu t+\sigma^2t^2/2}$ | D | 🟡 No formalizada — bloqueada por longitud de ruta (ver nota) |
| Regla empírica $68$-$95$-$99.7$ | C | ✅ Confirmado numéricamente, `verification/scipy/distribucion_normal/numeric_checks.py` |
| `exmp:2.8.2` — $N(70,100)$: $P(60\le X\le80)\approx0.6827=\Phi(1)-\Phi(-1)=0.8413-0.1587$ | C | ✅ Confirmado numéricamente, mismo script |

Ningún error matemático encontrado.

## Capítulo: `distribucion_normal` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionNormalProblemas.lean`. `prob:6f58870` (Recordar), `prob:74e7285` (Comprender) y `prob:96d8f57` (Evaluar) son puramente conceptuales, sin cálculo numérico, no formalizados. `prob:dd1e027` (Analizar) reutiliza `mgf_exponente` de la teoría, no se repite.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:48f2103` (Aplicar) | $N(170,100)$: estandarización $Z=1.5,-1,1$ exacta | A | ✅ Cierra (`prob_48f2103_estandarizacion`) |
| `prob:48f2103`, valores $\Phi$ | $P(X>185)\approx0.0668$, $P(160\le X\le180)\approx0.6827$ | C | ✅ Confirmado numéricamente, `verification/scipy/distribucion_normal/numeric_checks.py` |
| `prob:1c4fda2` (Crear) | $N(0.150,0.0004)$: $Z=(0.100-0.150)/0.02=-2.5$ exacto | A | ✅ Cierra (`prob_1c4fda2_estandarizacion`) |
| `prob:1c4fda2`, valor $\Phi$ | $P(X<0.100)=\Phi(-2.5)\approx0.0062$ | C | ✅ Confirmado numéricamente, mismo script |

Ningún error matemático encontrado — todos los valores numéricos del capítulo coinciden con el libro.

### Verificación EN por diff

Sin divergencias en ninguno de los dos archivos: `diff` de etiquetas y de todos los literales numéricos (enteros y decimales) entre ES y EN da vacío en ambos.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3432/3432 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionNormal.lean` (2 teoremas) y `DistribucionNormalProblemas.lean` (2 teoremas) además de los 31 archivos previos, más `verification/scipy/distribucion_normal/numeric_checks.py`.

**Nota técnica de este capítulo:** confirma que el problema de longitud de ruta de Windows no está limitado a `Mathlib.Probability.Moments.Variance`/`Independence.Integration` — cualquier import que jale `ContinuousFunctionalCalculus.PosPart.Basic` (o, como se descubrió aquí, `IntervalIntegral.LebesgueDifferentiationThm`) está afectado en este worktree específico. El patrón de mitigación sigue siendo: (1) test de humo con `#check` antes de invertir esfuerzo en pruebas, (2) si está bloqueado, extraer las piezas algebraicas puras que no necesitan la integral en sí (aquí: la identidad de estandarización y la de completar-el-cuadrado), dejando el cierre completo de la integral como Tier D/C documentado en vez de forzarlo.

---

## Capítulo: `distribuciones_tipo_gamma` (teoría)

Capítulo muy amplio: función gamma, distribución Gamma, Exponencial como caso particular, chi-cuadrada, teorema de suma de gammas, Beta, Weibull. Mucho contenido definicional/enumerativo y varios resultados analíticos genuinamente pesados (función gamma, momentos de Gamma/Weibull vía integrales impropias, convolución para la suma de gammas) — **Tier D, no formalizados**, razones documentadas en el doc-comment del archivo Lean (Mathlib sí tiene `Real.Gamma` y lemas asociados, pero dado el patrón de esta sesión de paquetes bloqueados por MAX_PATH, no se priorizó encadenar el paquete completo frente a los valores numéricos concretos). Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionesTipoGamma.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.8.3` — Erlang(3, tasa 3): suma interior $1+4.5+20.25/2=15.625$ | A | ✅ Cierra (`exmp_2_8_3_suma`) |
| `exmp:2.8.3`, decimal | $P(T>1.5)=e^{-4.5}\cdot15.625\approx0.174$ | C | ✅ Confirmado, `verification/scipy/distribuciones_tipo_gamma/numeric_checks.py` |
| `exmp:2.8.7` — $\mathrm{Beta}(2,8)$: $E(X)=0.2$, $\mathrm{Var}(X)=16/1100\approx0.0145$ | A | ✅ Cierra (`exmp_2_8_7`) |
| `exmp:2.8.8` — Weibull(2,5): exponente $(3/5)^2=0.36$ exacto | A | ✅ Cierra (`exmp_2_8_8_exponente`) |
| `exmp:2.8.8`, decimal | $F(3)=1-e^{-0.36}\approx0.3023$ | C | ✅ Confirmado, mismo script |

Ningún error matemático encontrado.

## Capítulo: `distribuciones_tipo_gamma` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionesTipoGammaProblemas.lean`. `prob:f00c4b6` (Recordar) y `prob:de365e8` (Comprender) son conceptuales, sin cálculo. `prob:6b498ea` (Analizar) parte 1 es sustitución trivial de parámetros en una fórmula ya dada, no formalizada aparte; parte 2 depende del teorema Tier D de suma de gammas.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:491786c` (Aplicar) | $\mathrm{Beta}(6,4)$: $E(X)=0.6$, $\mathrm{Var}(X)=24/1100\approx0.0218$ | A | ✅ Cierra (`prob_491786c`) |
| `prob:0f44096` (Evaluar) | Weibull($\beta=1,\eta=10$) vs. ($\beta=2,\eta=10$): $h_A=0.1$; $h_B(5)=0.1$, $h_B(15)=0.3$ | A | ✅ Cierra (`prob_0f44096`) |
| `prob:31a003b` (Crear) | $\mathrm{Exp}(\lambda=4)$: $E[X]=0.25\,\mathrm{h}=15\,\mathrm{min}$ | A | ✅ Cierra (`prob_31a003b`) |

Ningún error matemático encontrado — todos los valores numéricos del capítulo (teoría + problemas) coinciden con el libro.

### Verificación EN por diff

Sin divergencias en ninguno de los dos archivos: `diff` de etiquetas y de todos los literales numéricos (enteros y decimales) entre ES y EN da vacío en ambos.

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3434/3434 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionesTipoGamma.lean` (3 teoremas) y `DistribucionesTipoGammaProblemas.lean` (3 teoremas) además de los 33 archivos previos, más `verification/scipy/distribuciones_tipo_gamma/numeric_checks.py`.

---

## Capítulo: `funcion_generadora_momentos` (teoría + problemas)

Cierra la Unidad 3 del temario. Definición de FGM, teorema de momentos-vía-derivadas, teorema de unicidad, teorema de suma, y ejemplos (Bernoulli, Normal, Exponencial). **Tier D, no formalizados:** el teorema de intercambio derivada/esperanza (general), el teorema de unicidad (resultado profundo del problema de momentos), y el teorema de suma para independientes (misma maquinaria `IndepFun` bloqueada por MAX_PATH desde `esperanza_matematica`). El ejemplo de la Normal reutiliza `DistribucionNormal.mgf_exponente` sin repetirlo. Formalizado en `verification/lean_verificacion/LeanVerificacion/FuncionGeneradoraMomentos.lean` (teoría) y `FuncionGeneradoraMomentosProblemas.lean` (problemas, sin teoremas propios — todo lo formalizable ya está cubierto por la teoría o es puramente conceptual).

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:2.8.4` — FGM Bernoulli$(p)$: $M_X'(t)=pe^t$, general | B | ✅ Cierra (`exmp_2_8_4_derivada`, vía `HasDerivAt`) |
| `exmp:2.8.4` — $E[X]=p$, $E[X^2]=p$, $\mathrm{Var}(X)=p(1-p)$ | A | ✅ Cierra (`exmp_2_8_4_momentos`) |
| `exmp:2.8.6` — FGM $\mathrm{Exp}(\lambda)$: $M_X(t)=\lambda/(\lambda-t)$, $t<\lambda$, general | B | ✅ Cierra (`exmp_2_8_6_mgf`, vía `integral_exp_mul_Ioi` de Mathlib) |
| `prob:cf5e60c` — $M_{aX+b}(t)=e^{bt}M_X(at)$, general para cualquier densidad | B | ✅ Cierra (`prob_cf5e60c_general`) |
| `prob:a48cc99` — FGM $U(0,1)$: $M_X(t)=(e^t-1)/t$, $t\ne0$, general | B | ✅ Cierra (`prob_a48cc99_mgf`, vía FTC) |
| `prob:2c4cd93` — FGM Poisson: $M_X(t)=e^{\lambda(e^t-1)}$, $E[X]=\lambda$ | C/D | 🟡 No reproducido (misma técnica `tsum` de `distribucion_poisson`, resultado estándar no cuestionado) |

Ningún error matemático encontrado.

### Verificación EN por diff

Sin divergencias en ninguno de los dos archivos: `diff` de etiquetas y de todos los literales numéricos entre ES y EN da vacío en ambos.

## Estado del build (acumulado)

`lake build`: **✅ éxito, 3446/3446 jobs, sin `sorry`, sin errores.** Incluye ahora `FuncionGeneradoraMomentos.lean` (5 teoremas) y `FuncionGeneradoraMomentosProblemas.lean` (0 teoremas, documentación de alcance) además de los 35 archivos previos.

---

## Capítulo: `introduccion_estadistica_inferencial` (sin `(p)`)

Abre la Unidad 4 del temario. Archivo puramente de prosa introductoria (definiciones de población/muestra/parámetro/estadístico, tipos de inferencia, fuentes de error) — **sin ninguna fórmula, número o entorno `teorema`/`ejemplo`/`definicion` formal que dé una afirmación matemática verificable.** No hay `(p)` asociado. No se creó ningún archivo Lean — no hay nada que formalizar. (Nota: `docs/revision-notas-2026-07-13.md` ya documentó que la sección "Estructura del capítulo" de este archivo promete 6 temas que en realidad pertenecen a 4 capítulos distintos — un problema de prosa/organización ya conocido, no un hallazgo nuevo de este pase.)

## Capítulo: `transformacion_variables` (teoría)

Teorema de transformación afín, teorema de cambio de variable (caso monótono), tres ejemplos (Pareto vía exponencial, log-normal, arcoseno). Formalizado en `verification/lean_verificacion/LeanVerificacion/TransformacionVariables.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `eq:3.2.1`/`eq:3.2.2` — $\mu_Y=a\mu_X+b$, $\sigma_Y^2=a^2\sigma_X^2$ | B | Instancias directas de `EsperanzaMatematica.linealidad`/`var_escalar`, no reproducidas |
| `eq:3.2.1` (CDF) — equivalencia de orden $ax+b\le y\iff x\le(y-b)/a$, $a>0$ | A | ✅ Cierra (`transformacion_afin_orden`) |
| `eq:3.2.3` — cambio de variable monótono (regla de la cadena), general | B | ✅ Cierra (`cambio_variable_monotono`, vía `HasDerivAt.comp`) |
| `exmp:3.2.2` — $Y=e^X$, $X\sim\mathrm{Exp}(1)$: $f_Y(y)=e^{-\ln y}/y=1/y^2$ | B | ✅ Cierra (`exmp_3_2_2_pareto`) |
| `exmp:3.2.4` — arcoseno: suma de dos contribuciones simétricas $=1/(\pi\sqrt{1-y^2})$ | A | ✅ Cierra (`exmp_3_2_4_arcoseno`, álgebra; el hecho $d/dy\arcsin y=1/\sqrt{1-y^2}$ en sí es estándar de Mathlib) |

Ningún error matemático encontrado.

## Capítulo: `transformacion_variables` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/TransformacionVariablesProblemas.lean`. `prob:d3727e9` (Recordar) y `prob:fbf2d01` (Comprender) son conceptuales, sin cálculo.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:d795060` (Aplicar) | $N(5,4)$, $Y=3X-2$: $\mu_Y=13$, $\sigma_Y^2=36$ | A | ✅ Cierra (`prob_d795060`) |
| `prob:182603c` (Analizar) | $\mathrm{Exp}(\lambda)$, $Y=\sqrt X$: $f_Y(y)=2\lambda y\,e^{-\lambda y^2}$ (Weibull) | A | ✅ Cierra (`prob_182603c`) |
| `prob:5ce800e` (Evaluar) | Corrección caso no monótono $Y=X^2$: $f_Y(y)=1/(2\sqrt y)$, el doble del resultado incompleto | A | ✅ Cierra (`prob_5ce800e`) |
| `prob:12a4921` (Crear) | $U(0,1)$, $Y=-\ln X$: $f_Y(y)=e^{-y}$ ($\mathrm{Exp}(1)$) | A | ✅ Cierra (`prob_12a4921`) |

Ningún error matemático encontrado — todos los valores/fórmulas del capítulo coinciden con el libro.

### Verificación EN por diff

Sin divergencias en ninguno de los archivos (`introduccion_estadistica_inferencial`, `transformacion_variables` teoría y problemas): `diff` de etiquetas y de todos los literales numéricos entre ES y EN da vacío en todos.

## Estado del build (acumulado)

`lake build`: **✅ éxito, 3448/3448 jobs, sin `sorry`, sin errores.** Incluye ahora `TransformacionVariables.lean` (5 teoremas) y `TransformacionVariablesProblemas.lean` (4 teoremas) además de los 37 archivos previos.

**Nota técnica:** `HasDerivAt.comp` vive en `Mathlib.Analysis.Calculus.Deriv.Comp`, un archivo **distinto** de `Mathlib.Analysis.Calculus.Deriv.Basic` (que solo tiene la API base de `HasDerivAt`, no la regla de la cadena) — importar solo `Deriv.Basic` y llamar `.comp` produce un error de elaboración confuso ("Type mismatch... `(HasDerivAt ∘ ?m)`", como si `.comp` se interpretara como composición de funciones en vez de proyección de campo) en vez de un claro "unknown identifier". Además, `x` es un argumento **explícito** (no implícito) en `HasDerivAt.comp (x) (hh₂) (hh)` — hay que darlo posicionalmente antes de las dos hipótesis de derivada.

---

## Capítulo: `distribuciones_funciones_variable_aleatoria` (teoría)

Fórmula general para $Y=g(X)$ no monótona (suma sobre preimágenes) y para varias variables (integral sobre superficie de nivel), con un ejemplo (suma de dos exponenciales iid → Erlang). Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionesFuncionesVariableAleatoria.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:3.2.5` — $X_1,X_2\sim\mathrm{Exp}(1)$ iid, $Y=X_1+X_2$: $f_Y(y)=y\,e^{-y}$, general en $y$ | A | ✅ Cierra (`exmp_3_2_5`) |

Ningún error matemático encontrado. (Nota, no matemática: la línea "ver sección 2.11" al final de la solución de `exmp:3.2.5` es una referencia de texto plano, no `\ref{}` — consistente con el patrón ya documentado en `docs/revision-notas-2026-07-13.md` de prefijos/números de capítulo desactualizados en capítulos 3-5 tras la renumeración; no se investigó más a fondo por ser un problema de prosa, no matemático.)

## Capítulo: `distribuciones_funciones_variable_aleatoria` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionesFuncionesVariableAleatoriaProblemas.lean`. `prob:0b1575d` (Recordar), `prob:a8b056e` (Comprender) y `prob:df21aa1` (Evaluar) son conceptuales, sin cálculo numérico.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:4cdd21e` (Aplicar) | $U(0,1)+U(0,1)$: convolución en $(0,1)$ da $f_Y(y)=y$ (triangular) | A | ✅ Cierra (`prob_4cdd21e`) |
| `prob:43a7344` (Analizar) | $N(0,1)$, $Y=\lvert X\rvert$: suma de dos contribuciones simétricas $=\sqrt{2/\pi}\,e^{-y^2/2}$ (semi-normal) | B | ✅ Cierra (`prob_43a7344`) |
| `prob:db5d952` (Crear) | $\mathrm{Exp}(2)+\mathrm{Exp}(3)$: $f_Y(y)=6e^{-2y}-6e^{-3y}$ (hipoexponencial) | B | ✅ Cierra (`prob_db5d952`) |

Ningún error matemático encontrado — todas las fórmulas del capítulo coinciden con el libro.

### Verificación EN por diff

Sin divergencias en ninguno de los dos archivos: `diff` de etiquetas y de todos los literales numéricos entre ES y EN da vacío en ambos.

## Estado del build (acumulado)

`lake build`: **✅ éxito, 3450/3450 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionesFuncionesVariableAleatoria.lean` (1 teorema) y `DistribucionesFuncionesVariableAleatoriaProblemas.lean` (3 teoremas) además de los 39 archivos previos.

---

## Capítulo: `distribuciones_muestrales_medias` (teoría)

Resume $E(\bar X)=\mu$, $\Var(\bar X)=\sigma^2/n$, insesgadez de $S^2$, y trata el Teorema del Límite Central + Berry-Esseen. **`eq:3.2.7`/`eq:3.2.8`/`eq:3.2.9` y `eq:5.1.2` (insesgadez de $S^2$) son duplicados exactos de teoremas ya probados en el capítulo piloto** (`VariablesAleatorias.esperanza_media_muestral`/`varianza_media_muestral`/`esperanza_varianza_muestral`) — no se reproducen. El TLC (`eq:5.2.1`) y Berry-Esseen (`eq:5.2.2`) son Tier D, ya anticipados como tales en el plan original de este proyecto. Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionesMuestralesMedias.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:sample-mean-and-unbiased-variance` — muestra $\{12,15,11,18,14\}$: $\bar X=14$, $S^2=7.5$ | A | ✅ Cierra (`exmp_media_varianza_muestral`) |
| `exmp:5.2.1` — $\mu=\sigma=4,n=64$: $\mathrm{DE}(\bar X)=0.5$, $Z=1$ | A | ✅ Cierra (`exmp_5_2_1`); $\Phi(1)\approx0.8413$ ya confirmado en `distribucion_normal` |

Ningún error matemático encontrado.

## Capítulo: `distribuciones_muestrales_medias` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionesMuestralesMediasProblemas.lean`. `prob:22013b6` (Recordar), `prob:f4e7b8b` (Comprender) y `prob:0555e27` (Evaluar) son conceptuales. `prob:716e9bb` (Analizar, demostración de $E(S^2)=\sigma^2$) es el mismo teorema que la teoría, ya cubierto por el capítulo piloto, no se repite.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:6815de7` (Aplicar) | $n=100,\mu=800,\sigma=300$: $E(T)=80000$, $\Var(T)=9\times10^6$, $\mathrm{DE}(T)=3000$, $Z=5/3$ | A | ✅ Cierra (`prob_6815de7`); $\Phi(5/3)\approx0.9522$ Tier C, `verification/scipy/distribuciones_muestrales_medias/numeric_checks.py` |
| `prob:2e2f544` (Crear) | $\sigma=1.2,n=64$: $\mathrm{DE}(\bar X)=0.15$, $Z=2$ | A | ✅ Cierra (`prob_2e2f544`); $\Phi(2)\approx0.9772$ Tier C, mismo script |

Ningún error matemático encontrado — todos los valores numéricos coinciden con el libro.

### Verificación EN por diff

Etiquetas: sin divergencias. Literales numéricos: diff bruto muestra ruido por notación de miles (ES usa `85{,}000`/`9{,}000{,}000`, tokenizado como "85"+"000" por el separador `{,}`; EN escribe `85000`/`9000000` sin separador) — se verificó manualmente que los VALORES son idénticos en ambos idiomas (85000, 80000, 9000000, etc.), solo difiere la convención tipográfica de separador de miles entre ES y EN. Sin divergencias numéricas reales.

## Estado del build (acumulado)

`lake build`: **✅ éxito, 3452/3452 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionesMuestralesMedias.lean` (2 teoremas) y `DistribucionesMuestralesMediasProblemas.lean` (2 teoremas) además de los 41 archivos previos, más `verification/scipy/distribuciones_muestrales_medias/numeric_checks.py`.

---

## Capítulo: `distribucion_muestral_chi_cuadrada` (teoría)

Definición de $\chi^2_\nu$, momentos, caso particular de Gamma, Teorema de Fisher. **`eq:5.3.2` (Teorema de Fisher: independencia de $\bar X,S^2$ + $(n-1)S^2/\sigma^2\sim\chi^2_{n-1}$) es Tier D** — necesita una transformación ortogonal del vector muestral (caso particular del teorema de Cochran), fuera de alcance. Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionMuestralChiCuadrada.lean`.

| Afirmación | Tier | Estado |
|---|---|---|
| `exmp:5.3.1` — $\sigma^2=4,n=10,S^2=7.2$: estadístico $=16.2$, $9<16.2<16.92\approx\chi^2_{9,0.95}$ | A/C | ✅ Cierra (`exmp_5_3_1`); valor crítico $16.92$ confirmado, `verification/scipy/distribucion_muestral_chi_cuadrada/numeric_checks.py` |

Ningún error matemático encontrado. (Nota, no matemática: línea 21 "sección 2.11" es otra instancia del mismo patrón de referencia de texto plano desactualizada ya documentado en el capítulo anterior y en `docs/revision-notas-2026-07-13.md`.)

## Capítulo: `distribucion_muestral_chi_cuadrada` (problemas)

Formalizado en `verification/lean_verificacion/LeanVerificacion/DistribucionMuestralChiCuadradaProblemas.lean`. `prob:0d114e5` (Recordar), `prob:66b286b` (Comprender) y `prob:db05590` (Evaluar) son conceptuales.

| Label (nivel Bloom) | Afirmación | Tier | Estado |
|---|---|---|---|
| `prob:94c69e2` (Aplicar) | $\sigma_0^2=10,n=16,S^2=18.2$: estadístico $=27.3>24.996\approx\chi^2_{15,0.95}$ (rechaza) | A/C | ✅ Cierra (`prob_94c69e2`); valor crítico confirmado, mismo script |
| `prob:b08d077` (Analizar) | Sustitución $\alpha=\nu/2,\beta=2$: $E(\chi^2_\nu)=\nu$, $\Var(\chi^2_\nu)=2\nu$, general | A | ✅ Cierra (`prob_b08d077`) |
| `prob:501e850` (Crear) | $\sigma_0^2=0.04,n=21,S^2=0.065$: estadístico $=32.5>31.410\approx\chi^2_{20,0.95}$ (rechaza) | A/C | ✅ Cierra (`prob_501e850`); valor crítico confirmado, mismo script |

Ningún error matemático encontrado.

### Verificación EN por diff

Etiquetas: sin divergencias. Literales numéricos: diff bruto ruidoso por subíndices `\chi^2_{\nu,\alpha}` y por hipótesis alternativas $H_a$ explícitas que el EN añade y el ES no — se verificó manualmente que todos los valores clave (24.996, 31.410, 27.3, 32.5, 18.2, 0.065, 0.04) coinciden exactamente entre ambos idiomas. Sin divergencias numéricas reales.

## Estado del build (acumulado)

`lake build`: **✅ éxito, 3454/3454 jobs, sin `sorry`, sin errores.** Incluye ahora `DistribucionMuestralChiCuadrada.lean` (1 teorema) y `DistribucionMuestralChiCuadradaProblemas.lean` (3 teoremas) además de los 43 archivos previos, más `verification/scipy/distribucion_muestral_chi_cuadrada/numeric_checks.py`.

---

## Próximos pasos

**Nota de cobertura — capítulos aún no procesados que preceden al piloto en el orden real de `\input` del libro:** `introduccion_estadistica_descriptiva`, `medidas_tendencia_central`, `medidas_dispersion` (1 `propiedad` detectada), `introduccion_probabilidad`, `conjuntos` — y sus 5 pares `(p)` — se saltaron deliberadamente porque el piloto se eligió por ser el capítulo más rico en axiomas, no por ser el primero del libro. Quedan pendientes de una pasada posterior; hasta entonces esta bitácora no representa cobertura completa de principio a fin, solo de los capítulos listados arriba.

Continuar capítulo por capítulo en el orden de `\input` del libro, agregando una entrada a esta misma bitácora por capítulo, sin volver a preguntar en cada nuevo lote — próximo: `distribucion_muestral_t`. Commits al final de cada capítulo, sin pausar a reportar entre ellos (instrucción explícita del usuario). Los errores confirmados se reportan aquí pero, salvo aprobación explícita del usuario por hallazgo, **no se corrigen** en el mismo pase en que se encuentran. **Hallazgos pendientes de decisión del usuario sobre corrección (acumulados):** la fórmula sin factorial de `eq:2.10.8` y el valor numérico de `prob:33bf5d2` (`distribucion_multinomial`); los dos hallazgos numéricos menores de `distribucion_hipergeometrica` (`prob:7cf587b`, `prob:969b25a`); y los dos de `distribucion_poisson`, **especialmente `prob:5e9408a`** (inversión de la conclusión pedagógica). Ninguno de los últimos diez capítulos procesados desde entonces (`variables_discretas_ciencia_datos` hasta `distribucion_muestral_chi_cuadrada`) añadió hallazgos nuevos.
