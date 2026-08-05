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

## Estado del build (acumulado)

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3005/3005 jobs, sin `sorry`, sin errores ni advertencias de linter propias del proyecto** (solo las de estilo genéricas de Mathlib que no aplican aquí). 47 teoremas en total: 4 en `Calibracion.lean`, 11 en `FundamentosProbabilidad.lean`, 9 en `FundamentosProbabilidadProblemas.lean`, 8 en `TecnicasDeConteo.lean`, 5 en `TecnicasDeConteoProblemas.lean`, 4 en `ProbabilidadCondicional.lean`, 6 en `ProbabilidadCondicionalProblemas.lean`.

Nota técnica acumulada: (1) nunca usar `import Mathlib` completo en Windows — falla por longitud de ruta en ~12 archivos no relacionados y compila ~8600 archivos innecesarios; importar solo los módulos específicos necesarios. (2) la notación postfix `!` de `Nat.factorial` causa errores de parseo poco claros combinada con `*`/`/`; usar `Nat.factorial n` explícito. (3) para afirmaciones "≈" del libro, probar una cota de tolerancia explícita (`|x - valor_libro| < ε`) en vez de intentar igualdad exacta.

## Próximos pasos

**Nota de cobertura — capítulos aún no procesados que preceden al piloto en el orden real de `\input` del libro:** `introduccion_estadistica_descriptiva`, `medidas_tendencia_central`, `medidas_dispersion` (1 `propiedad` detectada), `introduccion_probabilidad`, `conjuntos` — y sus 5 pares `(p)` — se saltaron deliberadamente porque el piloto se eligió por ser el capítulo más rico en axiomas, no por ser el primero del libro. Quedan pendientes de una pasada posterior; hasta entonces esta bitácora no representa cobertura completa de principio a fin, solo de los capítulos listados arriba.

Continuar capítulo por capítulo en el orden de `\input` del libro (archivo de teoría, luego su par `(p)`), agregando una entrada a esta misma bitácora por capítulo, sin volver a preguntar en cada nuevo lote — próximo: `teorema_de_bayes` (0 teoremas formales detectados en el escaneo inicial por `grep`, pero el conteo de entornos no es señal suficiente — el archivo se leerá completo porque probablemente contiene el Teorema de Bayes real que `probabilidad_condicional.tex` dejó comentado, posiblemente como `definicion` o `align` sin entorno formal) y su par `(p)`. Después, retomar los 5 capítulos saltados arriba. Los errores confirmados se reportan aquí pero **no se corrigen** en este pase — la corrección de `.tex` es un paso posterior que requiere aprobación explícita por hallazgo.
