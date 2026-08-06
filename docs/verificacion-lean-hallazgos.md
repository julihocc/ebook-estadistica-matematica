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

## Próximos pasos

**Nota de cobertura — capítulos aún no procesados que preceden al piloto en el orden real de `\input` del libro:** `introduccion_estadistica_descriptiva`, `medidas_tendencia_central`, `medidas_dispersion` (1 `propiedad` detectada), `introduccion_probabilidad`, `conjuntos` — y sus 5 pares `(p)` — se saltaron deliberadamente porque el piloto se eligió por ser el capítulo más rico en axiomas, no por ser el primero del libro. Quedan pendientes de una pasada posterior; hasta entonces esta bitácora no representa cobertura completa de principio a fin, solo de los capítulos listados arriba.

Continuar capítulo por capítulo en el orden de `\input` del libro (archivo de teoría, luego su par `(p)`), agregando una entrada a esta misma bitácora por capítulo, sin volver a preguntar en cada nuevo lote — próximo: `distribucion_geometrica_binomial_negativa`. Los errores confirmados se reportan aquí pero **no se corrigen** en este pase — la corrección de `.tex` es un paso posterior que requiere aprobación explícita por hallazgo. **Dos hallazgos nuevos de este capítulo pendientes de decisión del usuario sobre corrección:** la fórmula sin factorial de `eq:2.10.8`, y el valor numérico incorrecto de `prob:33bf5d2` ($4.32\times10^{-18}$ debería ser $\approx0.0047908$).
