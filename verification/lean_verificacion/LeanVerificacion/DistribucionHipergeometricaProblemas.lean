import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import LeanVerificacion.DistribucionHipergeometrica

/-!
# Distribución hipergeométrica — problemas

Formaliza `latex/distribucion_hipergeometrica(p).tex`. `prob:748a77d`
(Recordar) es puro recordatorio de la PMF, ya cubierta en la teoría — no se
repite. `prob:64e9a8d` partes 1–2 son pasos de derivación en prosa/símbolos
sin un número concreto que verificar de forma aislada; la parte 3 (combinar
las piezas algebraicas en la fórmula cerrada de $\mathrm{Var}(X)$) es
exactamente `varianza_hipergeometrica_algebra` de la teoría — no se repite
aquí.
-/

namespace DistribucionHipergeometricaProblemas

/-- `prob:5e6e8bf` (Comprender) — los dos casos límite del Factor de
Corrección por Población Finita $(N-n)/(N-1)$: en $n=1$ vale $1$
(sin corrección); en $n=N$ vale $0$ (censo completo, sin incertidumbre
muestral). -/
theorem prob_5e6e8bf (N : ℕ) (hN2 : 2 ≤ N) :
    ((N : ℝ) - 1) / ((N : ℝ) - 1) = 1 ∧ ((N : ℝ) - N) / ((N : ℝ) - 1) = 0 := by
  have hN1 : (N : ℝ) - 1 ≠ 0 := by
    have : (2 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN2
    linarith
  constructor
  · field_simp
  · rw [sub_self, zero_div]

/-- `prob:1651c98` (Aplicar) — lote $N=30,K=6,n=5$: $P(X=0)=\binom60
\binom{24}5/\binom{30}5=42504/142506\approx0.2983$;
$P(X\le1)\approx0.7457$. -/
theorem prob_1651c98 :
    let den : ℝ := Nat.choose 30 5
    let P0 : ℝ := (Nat.choose 6 0 : ℝ) * (Nat.choose 24 5 : ℝ) / den
    let P1 : ℝ := (Nat.choose 6 1 : ℝ) * (Nat.choose 24 4 : ℝ) / den
    den = 142506 ∧ |P0 - 0.2983| < 1e-4 ∧ |P0 + P1 - 0.7457| < 1e-4 := by
  norm_num [Nat.choose]

/-- `prob:7cf587b` (Evaluar), parte tratable en Lean — $N=2000,K=100,n=20$:
la regla $n/N<0.05$ se cumple ($n/N=0.01$); $P(Y=2)\approx0.188677$ para la
aproximación $\mathrm{Bin}(20,0.05)$ ($p=K/N$ exacto, $=1/20$) SÍ coincide
con el libro. -/
theorem prob_7cf587b :
    let nN : ℝ := 20 / 2000
    let PY2 : ℝ := (Nat.choose 20 2 : ℝ) * (1 / 20 : ℝ) ^ 2 * (19 / 20 : ℝ) ^ 18
    nN = 0.01 ∧ nN < 0.05 ∧ |PY2 - 0.188677| < 1e-6 := by
  norm_num [Nat.choose]

/-! `prob:7cf587b`, $P(X=2)$ hipergeométrico exacto — **Tier C, no en
Lean**: $\binom{2000}{20}$/$\binom{1900}{18}$ agotan el tiempo de cómputo de
`norm_num [Nat.choose]` (timeout determinista de `maxHeartbeats` incluso
subiendo `maxRecDepth` a 8000) — no es infactible en principio, solo
demasiado lento para este entorno. Verificado en su lugar con
`verification/scipy/distribucion_hipergeometrica/prob_7cf587b.py`
(aritmética racional exacta con `fractions.Fraction`, no de punto flotante).
**Hallazgo: el libro afirma $P(X=2)\approx0.189725$, pero el valor correcto
es $\approx0.189525$** — los dígitos "5" y "7" están intercambiados
(`0.189`**5**`25` vs `0.189`**7**`25`), consistente con un error de
transcripción. El error absoluto real entre hipergeométrica y binomial
(`|PX2-PY2|≈0.000848`) sigue siendo pequeño, así que la conclusión
cualitativa del problema (la aproximación binomial es apropiada) no cambia,
solo la cifra intermedia. -/

/-- `prob:969b25a` (Crear) — biblioteca $N=200,K=25,n=15$: $\mathbb E[X]=
15(25/200)=1.875$ ✓. **Hallazgo menor: el libro afirma $\mathrm{Var}(X)=
1.640625(185/199)\approx1.5254$, pero el valor correcto es
$\approx1.5252$** (verificado con `Fraction` exacta: $19425/12736=
1.5252041\ldots$) — de nuevo, aparente transcripción de dígitos ("52" vs
"54"), consistente con el otro hallazgo numérico menor de este mismo
archivo (`prob:7cf587b`). El factor intermedio $1.640625$ que el libro sí
muestra es correcto; el error está solo en el redondeo final. -/
theorem prob_969b25a :
    let EX : ℝ := 15 * (25 / 200 : ℝ)
    let VarX : ℝ := 15 * (25 / 200 : ℝ) * (1 - 25 / 200) * ((200 - 15) / (200 - 1) : ℝ)
    EX = 1.875 ∧ ¬ |VarX - 1.5254| < 1e-4 ∧ |VarX - 1.5252| < 1e-4 := by
  refine ⟨by norm_num, ?_, by norm_num⟩
  rw [not_lt]
  norm_num

end DistribucionHipergeometricaProblemas
