import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import LeanVerificacion.DistribucionGeometricaBinomialNegativa

/-!
# Distribución geométrica y binomial negativa — problemas

Formaliza `latex/distribucion_geometrica_binomial_negativa(p).tex`.
`prob:287fdc5` (Recordar) es puro recordatorio de la PMF, ya cubierta en la
teoría — no se repite. `prob:a4a72f3` (Analizar) pide derivar la función
generadora de momentos de la geométrica y de la binomial negativa —
**Tier D, no formalizado**: además de otra serie geométrica infinita
(esta vez en la variable compleja/real $e^t$, con la condición de
convergencia adicional $t<-\ln q$), requeriría construir la noción de FGM
como objeto formal, que el proyecto no tiene.

**Observación de convención (no es un error matemático):** `prob:6ccfa13`
usa $X$ = número de *ensayos* hasta el $r$-ésimo éxito (soporte
$\{r,r+1,\dots\}$, $f_X(k)=\binom{k-1}{r-1}p^rq^{k-r}$), mientras que
`eq:2.10.10` de la teoría usa $X$ = número de *fracasos* antes del
$r$-ésimo éxito (soporte $\{0,1,2,\dots\}$,
$f_X(k)=\binom{k+r-1}{r-1}p^rq^k$). Son las dos parametrizaciones estándar
de la binomial negativa (difieren por el desplazamiento $X_\text{ensayos}=
X_\text{fracasos}+r$), cada una internamente consistente en el problema
donde se usa, pero el libro nunca señala explícitamente el cambio de
convención entre la sección de teoría y este problema. Documentado aquí
para que no se confunda con una divergencia real en una revisión futura.
-/

namespace DistribucionGeometricaBinomialNegativaProblemas

/-- `prob:0ebda90` (Comprender) — aplicación numérica de la pérdida de
memoria con $m=5$, $n=3$: $P(X>8\mid X>5)=P(X>3)$, instancia directa de
`perdida_memoria` (no una nueva verificación independiente). -/
theorem prob_0ebda90 (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) :
    (∑' k : ℕ, (1 - p) ^ (k + 8) * p) / (∑' k : ℕ, (1 - p) ^ (k + 5) * p) =
      ∑' k : ℕ, (1 - p) ^ (k + 3) * p :=
  DistribucionGeometricaBinomialNegativa.perdida_memoria p hp0 hp1 5 3

/-- `prob:6ccfa13` (Aplicar) — auditoría con $r=3$, $p=0.10$ (convención de
"ensayos", ver observación arriba): $P(X=20)=\binom{19}{2}(0.10)^3(0.90)^{17}
\approx0.0285$. -/
theorem prob_6ccfa13 :
    let coef : ℝ := Nat.choose 19 2
    coef = 171 ∧ |coef * (0.10 : ℝ) ^ 3 * (0.90 : ℝ) ^ 17 - 0.0285| < 1e-4 := by
  norm_num [Nat.choose]

/-- `prob:ca5c4c8` (Evaluar) — índice de dispersión $s^2/\bar x=13.44/3.2=4.2$
(sobredispersión respecto a Poisson); estimadores por método de momentos
$\hat p=\bar x/s^2\approx0.2381$, $\hat r=\bar x\hat p/(1-\hat p)\approx1$. -/
theorem prob_ca5c4c8 :
    let xbar : ℝ := 3.2
    let s2 : ℝ := 13.44
    let phat := xbar / s2
    let rhat := xbar * phat / (1 - phat)
    s2 / xbar = 4.2 ∧ |phat - 0.2381| < 1e-4 ∧ |rhat - 1| < 1e-2 := by
  norm_num

/-- `prob:4c2c37d` (Crear) — equipo de ventas con $r=4$, $p=0.15$ (convención
de "ensayos"): $\mathbb E[X]=r/p=4/0.15\approx26.67$;
$\mathrm{Var}(X)=r(1-p)/p^2=4(0.85)/(0.15)^2\approx151.11$;
$\sigma_X\approx12.29$. La aritmética se verifica confiando en las fórmulas
dadas (no se re-derivan aquí las fórmulas generales de la binomial negativa
en convención de "ensayos" — Tier D, ver cabecera del archivo de teoría). -/
theorem prob_4c2c37d :
    |(4 : ℝ) / 0.15 - 26.67| < 1e-2 ∧
      |(4 : ℝ) * (1 - 0.15) / 0.15 ^ 2 - 151.11| < 1e-2 ∧
      |Real.sqrt ((4 : ℝ) * (1 - 0.15) / 0.15 ^ 2) - 12.29| < 1e-2 := by
  have hlo : (12.28 : ℝ) < Real.sqrt ((4 : ℝ) * (1 - 0.15) / 0.15 ^ 2) := by
    rw [Real.lt_sqrt (by norm_num)]; norm_num
  have hhi : Real.sqrt ((4 : ℝ) * (1 - 0.15) / 0.15 ^ 2) < 12.30 := by
    rw [Real.sqrt_lt' (by norm_num)]; norm_num
  refine ⟨by norm_num, by norm_num, abs_lt.mpr ⟨by linarith, by linarith⟩⟩

end DistribucionGeometricaBinomialNegativaProblemas
