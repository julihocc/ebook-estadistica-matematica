import Mathlib.Tactic

/-!
# Distribuciones de tipo gamma — problemas

Formaliza `latex/distribuciones_tipo_gamma(p).tex`. `prob:f00c4b6`
(Recordar) y `prob:de365e8` (Comprender) son puramente conceptuales, sin
cálculo numérico, no formalizados. `prob:6b498ea` (Analizar) parte 1 es
sustitución directa de parámetros en una fórmula ya dada
($M_X(t)=(1-\beta t)^{-\alpha}$ con $\alpha=\nu/2,\beta=2$), trivial por
definición, no formalizado aparte; parte 2 (suma de $\chi^2$) depende del
teorema Tier D de suma de gammas de la teoría, no se repite.
-/

namespace DistribucionesTipoGammaProblemas

/-- `prob:491786c` (Aplicar) — $X\sim\mathrm{Beta}(6,4)$: $\mathbb
E(X)=0.6$, $\mathrm{Var}(X)=24/1100\approx0.0218$. -/
theorem prob_491786c :
    (6 : ℝ) / (6 + 4) = 0.6 ∧ |(24 : ℝ) / 1100 - 0.0218| < 1e-4 := by
  constructor <;> norm_num

/-- `prob:0f44096` (Evaluar) — Weibull($\beta=1,\eta=10$) vs.
Weibull($\beta=2,\eta=10$): $h_A(t)=0.1$ constante; $h_B(5)=0.1$ (empatan),
$h_B(15)=0.3>h_A$. -/
theorem prob_0f44096 :
    (1 : ℝ) / 10 = 0.1 ∧ (2 / 10 : ℝ) * (5 / 10) = 0.1 ∧ (2 / 10 : ℝ) * (15 / 10) = 0.3 := by
  norm_num

/-- `prob:31a003b` (Crear) — $X\sim\mathrm{Exp}(\lambda=4)$: $\mathbb
E[X]=1/4=0.25$ horas $=15$ minutos. -/
theorem prob_31a003b : (1 : ℝ) / 4 = 0.25 ∧ (0.25 : ℝ) * 60 = 15 := by norm_num

end DistribucionesTipoGammaProblemas
