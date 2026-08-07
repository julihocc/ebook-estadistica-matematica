import Mathlib.Tactic

/-!
# Distribución muestral F — problemas

Formaliza `latex/distribucion_muestral_f(p).tex`. `prob:20ee012`
(Recordar) es conceptual. `prob:2e8078c` (Comprender) reutiliza
`DistribucionMuestralF.reciprocidad_F`, no se repite. `prob:23d903e`
(Analizar, $T^2\sim F_{1,\nu}$) es una identidad definicional dado que
$Z^2\sim\chi^2_1$ por la propia definición de $\chi^2_1$ — no aporta
cálculo adicional que verificar.
-/

namespace DistribucionMuestralFProblemas

/-- `prob:b47df2a` (Aplicar) — $S_1^2=45,S_2^2=20$: $F=45/20=2.25<3.62$
(no se rechaza $H_0$). -/
theorem prob_b47df2a : (45 : ℝ) / 20 = 2.25 ∧ (2.25 : ℝ) < 3.62 := by norm_num

/-- `prob:e04a795` (Evaluar) — $S_1^2=50,S_2^2=48$: $F=50/48\approx1.042<3.36$
(no se rechaza $H_0$). -/
theorem prob_e04a795 : |(50 : ℝ) / 48 - 1.042| < 1e-3 ∧ (50 : ℝ) / 48 < 3.36 := by norm_num

/-- `prob:6277cc2` (Crear) — $S_1^2=4.2,S_2^2=1.5$: $F=4.2/1.5=2.8<4.82$
(no se rechaza $H_0$). -/
theorem prob_6277cc2 : (4.2 : ℝ) / 1.5 = 2.8 ∧ (2.8 : ℝ) < 4.82 := by norm_num

end DistribucionMuestralFProblemas
