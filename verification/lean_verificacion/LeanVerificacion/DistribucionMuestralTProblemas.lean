import Mathlib.Tactic

/-!
# Distribución muestral t — problemas

Formaliza `latex/distribucion_muestral_t(p).tex`. `prob:3de3320`
(Recordar) y `prob:03aebae` (Comprender) son conceptuales.
-/

namespace DistribucionMuestralTProblemas

/-- `prob:e378132` (Aplicar) — muestra $\{23,25,21,27,24\}$: $\bar
X=120/5=24$, suma de desviaciones al cuadrado $=20$, $S^2=20/4=5$,
$\mathrm{SE}=S/\sqrt5=1$ exacto, margen $=2.776\cdot1=2.776$, IC
$=[21.224,26.776]$. -/
theorem prob_e378132 :
    ((23 : ℝ) + 25 + 21 + 27 + 24) / 5 = 24 ∧
      ((23 - 24 : ℝ) ^ 2 + (25 - 24) ^ 2 + (21 - 24) ^ 2 + (27 - 24) ^ 2 + (24 - 24) ^ 2) = 20 ∧
      (20 : ℝ) / 4 = 5 ∧ Real.sqrt 5 / Real.sqrt 5 = 1 ∧
      (24 : ℝ) + 2.776 * 1 = 26.776 ∧ (24 : ℝ) - 2.776 * 1 = 21.224 := by
  refine ⟨by norm_num, by norm_num, by norm_num, ?_, by norm_num, by norm_num⟩
  exact div_self (by positivity)

/-- `prob:7943b46` (Analizar) — dado $E(Z^2)=1$ y $E(1/\chi^2_\nu)=1/(\nu-2)$
(datos del problema), $\Var(T)=\nu\cdot E(Z^2)\cdot E(1/\chi^2_\nu)=\nu/(\nu-2)$,
general para $\nu>2$. -/
theorem prob_7943b46 (nu : ℝ) (hnu : nu ≠ 2) : nu * 1 * (1 / (nu - 2)) = nu / (nu - 2) := by
  field_simp

/-- `prob:bbda1fa` (Evaluar) — error relativo entre $t_{19,0.025}\approx2.093$
y $z_{0.025}=1.96$: $(2.093-1.96)/1.96\approx6.8\%$. -/
theorem prob_bbda1fa : |((2.093 : ℝ) - 1.96) / 1.96 - 0.068| < 1e-3 := by norm_num

/-- **`prob:c34507c` (Crear) — hallazgo confirmado.** La solución afirma
que la suma de desviaciones al cuadrado de $\{8.2,7.9,8.5,8.1,7.8,8.3\}$
(alrededor de $\bar X=48.8/6=122/15$) es "aproximadamente $0.3033$", pero
el valor exacto es $1/3\approx0.3333$ — un error de aproximadamente $0.03$
que se propaga a $S^2$ ($1/15\approx0.0667$, no $\approx0.0607$), $S$
($\approx0.2582$, no $\approx0.246$), el error estándar
($\approx0.1054$, no $\approx0.1004$), el margen ($\approx0.271$, no
$\approx0.258$) y el intervalo de confianza final ($\approx[7.862,8.404]$,
no $[7.875,8.391]$). Presente idéntico en EN (`en_distribucion_muestral_t(p).tex`,
mismo $S\approx0.246$/IC $[7.875,8.391]$) — confirma fuente compartida. -/
theorem prob_c34507c_hallazgo :
    ((8.2 : ℝ) - 122 / 15) ^ 2 + (7.9 - 122 / 15) ^ 2 + (8.5 - 122 / 15) ^ 2 +
        (8.1 - 122 / 15) ^ 2 + (7.8 - 122 / 15) ^ 2 + (8.3 - 122 / 15) ^ 2 = 1 / 3 ∧
      ¬ |((8.2 : ℝ) - 122 / 15) ^ 2 + (7.9 - 122 / 15) ^ 2 + (8.5 - 122 / 15) ^ 2 +
          (8.1 - 122 / 15) ^ 2 + (7.8 - 122 / 15) ^ 2 + (8.3 - 122 / 15) ^ 2 - 0.3033| < 1e-3 := by
  constructor
  · norm_num
  · norm_num

end DistribucionMuestralTProblemas
