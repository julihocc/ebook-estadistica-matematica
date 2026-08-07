import Mathlib.Tactic

/-!
# Distribuciones muestrales de medias — problemas

Formaliza `latex/distribuciones_muestrales_medias(p).tex`. `prob:22013b6`
(Recordar) y `prob:f4e7b8b` (Comprender) son conceptuales, sin cálculo.
`prob:716e9bb` (Analizar, demostración de $E(S^2)=\sigma^2$) es el mismo
teorema que `DistribucionesMuestralesMedias` (teoría) — ya cubierto por
`VariablesAleatorias.esperanza_varianza_muestral` del capítulo piloto, no
se repite. `prob:0555e27` (Evaluar) es conceptual.
-/

namespace DistribucionesMuestralesMediasProblemas

/-- `prob:6815de7` (Aplicar) — $n=100,\mu=800,\sigma=300$: $E(T)=80000$,
$\Var(T)=9{,}000{,}000$, $\mathrm{DE}(T)=3000$, $Z=(85000-80000)/3000=5/3$
exacto (el valor $\Phi(5/3)\approx0.9522$ es Tier C, ver
`verification/scipy/distribuciones_muestrales_medias/numeric_checks.py`). -/
theorem prob_6815de7 :
    (100 : ℝ) * 800 = 80000 ∧ (100 : ℝ) * 300 ^ 2 = 9000000 ∧
      Real.sqrt (9000000 : ℝ) = 3000 ∧ ((85000 : ℝ) - 80000) / 3000 = 5 / 3 := by
  refine ⟨by norm_num, by norm_num, ?_, by norm_num⟩
  rw [show (9000000 : ℝ) = 3000 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]

/-- `prob:2e2f544` (Crear) — $\sigma=1.2,n=64$: $\mathrm{DE}(\bar X)=0.15$,
$Z=(4.3-4)/0.15=2$ exacto ($\Phi(2)\approx0.9772$ es Tier C, mismo script). -/
theorem prob_2e2f544 : (1.2 : ℝ) / Real.sqrt 64 = 0.15 ∧ ((4.3 : ℝ) - 4) / 0.15 = 2 := by
  have h64 : Real.sqrt (64 : ℝ) = 8 := by
    rw [show (64 : ℝ) = 8 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  rw [h64]
  norm_num

end DistribucionesMuestralesMediasProblemas
