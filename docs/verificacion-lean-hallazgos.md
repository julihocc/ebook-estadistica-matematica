# Verificación formal con Lean 4 + Mathlib — bitácora de hallazgos

**Herramienta:** Lean 4.32.2 / Mathlib (pin `v4.32.2`), proyecto en `verification/lean_verificacion/`, cross-checks numéricos en `verification/scipy/`.
**Alcance de esta entrada:** Piloto — `latex/fundamentos_de_probabilidad.tex` + `latex/fundamentos_de_probabilidad(p).tex` (ES). No se verifica EN de forma independiente: los archivos `en_*` son traducciones verbatim (mismas etiquetas hex, mismos números), así que se comparan por diff textual en vez de re-probarse.
**Metodología:** cada lema transcribe la afirmación del libro con sus propios números/pasos tal como están escritos — no se demuestra "la versión correcta" y se compara a ojo. Un `norm_num`/`ring`/`decide` que no cierra *es* el hallazgo. Ver `C:\Users\julih\.claude\plans\we-re-going-to-work-vivid-quail.md` para el plan completo.

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

## Estado del build

`lake build` en `verification/lean_verificacion/` (Lean 4.32.2, Mathlib pin `v4.32.2`): **✅ éxito, 3001/3001 jobs, sin `sorry`, sin errores.** Solo advertencias de estilo (linter de Mathlib sobre encabezados de copyright / `import Mathlib.Tactic` amplio — no aplican a un proyecto downstream y se dejan como están). 24 teoremas en total: 4 en `Calibracion.lean`, 11 en `FundamentosProbabilidad.lean`, 9 en `FundamentosProbabilidadProblemas.lean`.

Nota técnica para las siguientes entradas: el primer intento con `import Mathlib` (todo el paquete) falló en Windows por una limitación de longitud de ruta del sistema de archivos al construir ~12 archivos de Mathlib no relacionados (CategoryTheory/AlgebraicTopology, rutas de compilación muy largas). Solución: importar solo los módulos de Mathlib realmente necesarios (`Mathlib.Tactic`, `Mathlib.Data.Set.Lattice`, `Mathlib.Data.Real.Basic`, etc.) en vez de `import Mathlib`. Esto también reduce el tiempo de build de forma drástica (no compila los ~8600 archivos de Mathlib, solo los ~3000 de los que depende transitivamente lo que se importa). Usar este patrón de aquí en adelante.

## Próximos pasos

Sujeto a tu aprobación: continuar capítulo por capítulo en el orden de `\input` del libro (archivo de teoría, luego su par `(p)`), agregando una entrada a esta misma bitácora por capítulo, sin volver a preguntar en cada nuevo lote. Los errores confirmados se reportan aquí pero **no se corrigen** en este pase — la corrección de `.tex` es un paso posterior que requiere tu aprobación explícita por hallazgo.
