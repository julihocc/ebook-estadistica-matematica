import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Esperanza matemática — problemas

Formaliza `latex/esperanza_matematica(p).tex`. `prob:de8d740` (Analizar)
requiere esperanza condicional medida-teórica y la propiedad de torre —
Tier D, no formalizado (ver razón en su lugar). `prob:f43c638`
(Comprender) y `prob:9d4a41b` (Evaluar) necesitan momentos de la
exponencial vía integrales impropias con integración por partes — Tier C,
cross-check en `verification/scipy/esperanza_matematica/`.
-/

namespace EsperanzaMatematicaProblemas

open MeasureTheory intervalIntegral

/-- `prob:4e01dbd` (Recordar), parte 1 — $\E[X]=2/3$ para $f(x)=2x$ en
$[0,1]$. -/
theorem prob_4e01dbd_esperanza : (∫ x in (0 : ℝ)..1, x * (2 * x)) = 2 / 3 := by
  have heq : (fun x : ℝ => x * (2 * x)) = fun x => (2 : ℝ) * x ^ 2 := by funext x; ring
  rw [heq, intervalIntegral.integral_const_mul (2 : ℝ) (fun x : ℝ => x ^ 2), integral_pow]
  norm_num

/-- `prob:4e01dbd`, parte 2 — $\E[X^2]=1/2$, $\mathrm{Var}(X)=1/2-4/9=1/18$. -/
theorem prob_4e01dbd_segundo_momento : (∫ x in (0 : ℝ)..1, x ^ 2 * (2 * x)) = 1 / 2 := by
  have heq : (fun x : ℝ => x ^ 2 * (2 * x)) = fun x => (2 : ℝ) * x ^ 3 := by funext x; ring
  rw [heq, intervalIntegral.integral_const_mul (2 : ℝ) (fun x : ℝ => x ^ 3), integral_pow]
  norm_num

theorem prob_4e01dbd_varianza : (1 : ℝ) / 2 - (2 / 3 : ℝ) ^ 2 = 1 / 18 := by norm_num

/-- `prob:4e01dbd`, parte 3 — la mediana $m=1/\sqrt2$ satisface $m^2=1/2$,
y $\E[X]=2/3<m$ (asimetría hacia la izquierda desplaza la media bajo la
mediana). -/
theorem prob_4e01dbd_mediana :
    Real.sqrt (1 / 2) ^ 2 = (1 : ℝ) / 2 ∧ (2 : ℝ) / 3 < Real.sqrt (1 / 2) := by
  refine ⟨Real.sq_sqrt (by norm_num), ?_⟩
  rw [Real.lt_sqrt (by norm_num)]
  norm_num

/-- `prob:f43c638` (Comprender) — **hallazgo corregido.** Para
$X\sim\mathrm{Exp}(\lambda=0.5)$, la solución escribía "$\E[X^2]=8=1/\lambda^2$"
pero $1/\lambda^2=4$, no $8$; la fórmula correcta que da $8$ es
$2/\lambda^2$ (los *valores* numéricos $\E[X^2]=8$, $\mathrm{Var}(X)=4$ ya
eran correctos, solo la fórmula anotada estaba mal etiquetada). Corregido
en ES y EN. Los momentos en sí (Tier C, requieren integración por partes
de $\int x^n\cdot0.5e^{-0.5x}dx$) se verifican numéricamente en
`verification/scipy/esperanza_matematica/prob_f43c638_9d4a41b.py`. -/
theorem prob_f43c638_formula :
    (2 : ℝ) / 0.5 ^ 2 = 8 ∧ (8 : ℝ) - (1 / 0.5 : ℝ) ^ 2 = 4 := by
  norm_num

/-! `prob:7b147c4` (Aplicar), parte 1 — $\E[\bar X]=\mu$, $\mathrm{Var}(\bar
X)=\sigma^2/n$: especialización directa de `esperanza_media_muestral`/
`varianza_media_muestral` (`VariablesAleatorias.lean`, no importado en
este worktree por el problema de longitud de ruta de Windows — ver nota
en `EsperanzaMatematica.lean`); no se reproduce aquí, mismo resultado. -/

/-- `prob:7b147c4`, parte 3 — **hallazgo corregido.** La solución concluía
"con $n=100$ mediciones, el error estándar es exactamente $0.01$" como si
satisficiera $\sigma/\sqrt n<0.01$, pero $n=100$ da igualdad exacta
($0.1/\sqrt{100}=0.01$), no la desigualdad estricta pedida — se necesita
$n\geq101$. Corregido en ES y EN para concluir con $n=101$
($\sigma/\sqrt{101}\approx0.00995<0.01$) en vez de $n=100$. -/
theorem prob_7b147c4_n100 :
    ¬ ((0.1 : ℝ) / Real.sqrt 100 < 0.01) ∧ (0.1 : ℝ) / Real.sqrt 101 < 0.01 := by
  have h100 : Real.sqrt (100 : ℝ) = 10 := by
    rw [show (100 : ℝ) = 10 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  constructor
  · rw [h100]; norm_num
  · have h101 : (10 : ℝ) < Real.sqrt 101 := by
      rw [Real.lt_sqrt (by norm_num)]; norm_num
    have h101pos : (0 : ℝ) < Real.sqrt 101 := by linarith
    rw [div_lt_iff₀ h101pos]
    nlinarith

/-- `prob:5c186f2` (Crear) — linealidad aplicada a un portafolio:
$0.40(0.08)+0.35(0.05)+0.25(0.12)=0.0795$, exacto. -/
theorem prob_5c186f2_portafolio :
    (0.40 : ℝ) * 0.08 + 0.35 * 0.05 + 0.25 * 0.12 = 0.0795 := by norm_num

end EsperanzaMatematicaProblemas
