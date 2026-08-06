import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import LeanVerificacion.FundamentosProbabilidad
import LeanVerificacion.ProbabilidadCondicional
import LeanVerificacion.TeoremaDeBayes

/-!
# Teorema de Bayes — problemas

Formaliza los problemas de `latex/teorema_de_bayes(p).tex`. `prob:a7e87e4`
(Analizar) pide demostrar el Teorema de Bayes para una partición finita
general — es exactamente `TeoremaDeBayes.bayes_particion`, ya formalizado en
la teoría; no se repite la demostración aquí.
-/

namespace TeoremaDeBayesProblemas

/-- `prob:054ed26` (Recordar) — dado balanceado de 6 caras: $P(A)=3/6=0.5$
(sin información), y $P(A\mid I)=2/3\approx0.6667$ (dado impar). Convención:
`Fin 6` indexa las caras $1$–$6$ como $0$–$5$. $A=\{1,2,3\}$ es `{0,1,2}`,
$I=\{1,3,5\}$ (impares) es `{0,2,4}`, y $A\cap I=\{1,3\}$ es `{0,2}` — las
cardinalidades se cuentan con `decide`, no se escriben a mano, para que un
conteo incorrecto del libro pudiera detectarse. -/
theorem prob_054ed26 :
    let A : Finset (Fin 6) := {0, 1, 2}
    let I : Finset (Fin 6) := {0, 2, 4}
    (A.card : ℚ) / 6 = 0.5 ∧ ((A ∩ I).card : ℚ) / 6 / ((I.card : ℚ) / 6) = 2 / 3 := by
  intro A I
  have hA : A.card = 3 := by decide
  have hI : I.card = 3 := by decide
  have hAI : (A ∩ I).card = 2 := by decide
  rw [hA, hI, hAI]
  norm_num

/-- `prob:bde7784` (Comprender) — $P(Z) = (0.10)(0.60)+(0.15)(0.40) = 0.12$, y
$P(M\mid Z) = 0.06/0.12 = 0.50$. El numerador de Bayes se liga con `let` y se
reutiliza como en el resto del capítulo. -/
theorem prob_bde7784 :
    let pM : ℝ := 0.60
    let pH : ℝ := 0.40
    let pZgM : ℝ := 0.10
    let pZgH : ℝ := 0.15
    let pZ := pZgM * pM + pZgH * pH
    let num := pZgM * pM
    pZ = 0.12 ∧ num / pZ = 0.50 := by
  norm_num

/-- `prob:e14faa0` (Aplicar) — $P(A)=0.72$; $P(E\mid A)=0.875$; $P(A')=0.28$;
$P(E'\mid A')=0.75$. Cada cantidad derivada se liga con `let` y se reutiliza
en el paso siguiente. -/
theorem prob_e14faa0 :
    let pE : ℝ := 0.70
    let pEc : ℝ := 1 - pE
    let pAgE : ℝ := 0.90
    let pAgEc : ℝ := 0.30
    let pA := pAgE * pE + pAgEc * pEc
    let pAc := 1 - pA
    let pAcgE : ℝ := 1 - pAgE
    let pAcgEc : ℝ := 1 - pAgEc
    let numE := pAgE * pE
    let numEc := pAcgEc * pEc
    pEc = 0.30 ∧ pA = 0.72 ∧ numE / pA = 0.875 ∧ pAc = 0.28 ∧
      pAcgE = 0.10 ∧ pAcgEc = 0.70 ∧ numEc / pAc = 0.75 := by
  norm_num

/-- `prob:a7e87e4` (Analizar) — el Teorema de Bayes para una partición finita
general es `TeoremaDeBayes.bayes_particion`. -/
theorem prob_a7e87e4 {Ω : Type*} {P : Set Ω → ℝ} (h : FundamentosProbabilidad.Axiomas P)
    {ι : Type*} (s : Finset ι) (E : ι → Set Ω)
    (hpd : ∀ i ∈ s, ∀ i' ∈ s, i ≠ i' → Disjoint (E i) (E i'))
    (hcover : (⋃ i ∈ s, E i) = Set.univ) (B : Set Ω) {j : ι} (hj : j ∈ s) :
    ProbabilidadCondicional.condicional P B (E j) =
      P (E j) * ProbabilidadCondicional.condicional P (E j) B /
        ∑ i ∈ s, P (E i) * ProbabilidadCondicional.condicional P (E i) B :=
  TeoremaDeBayes.bayes_particion h s E hpd hcover B hj

/-- `prob:898898e` (Evaluar) — la Falacia del Fiscal, forma de momios: razón
de verosimilitud $\text{LR}=1/10^{-6}=10^6$, momios a priori $=1/5{,}000{,}000$,
momios a posteriori $=10^6\times(1/5{,}000{,}000)=1/5=0.20$, y
$P(I\mid E) = 0.20/1.20 = 1/6\approx0.1667$. Los momios a posteriori se ligan
con `let` y se reutilizan al convertir a probabilidad. -/
theorem prob_898898e :
    let priorOdds : ℝ := 1 / 5000000
    let lr : ℝ := 1 / 1e-6
    let postOdds := lr * priorOdds
    let pIgivenE := postOdds / (1 + postOdds)
    postOdds = 0.20 ∧ pIgivenE = 1 / 6 := by
  norm_num

/-- `prob:3bf9f42` (Crear) — clasificación de riesgo crediticio: $P(D) =
(0.02)(0.50)+(0.08)(0.35)+(0.25)(0.15) = 0.0755$, y el vector de posteriores
$P(\text{Exc}\mid D)\approx0.1325$, $P(\text{Reg}\mid D)\approx0.3709$,
$P(\text{Def}\mid D)\approx0.4967$ (tolerancia $10^{-4}$ cada uno). $P(D)$ se
liga con `let` y se reutiliza como denominador común de las 3 fórmulas de
Bayes. -/
theorem prob_3bf9f42 :
    let pExc : ℝ := 0.50
    let pReg : ℝ := 0.35
    let pDef : ℝ := 0.15
    let pDgExc : ℝ := 0.02
    let pDgReg : ℝ := 0.08
    let pDgDef : ℝ := 0.25
    let pD := pDgExc * pExc + pDgReg * pReg + pDgDef * pDef
    pD = 0.0755 ∧
      |(pDgExc * pExc) / pD - 0.1325| < 1e-4 ∧
      |(pDgReg * pReg) / pD - 0.3709| < 1e-4 ∧
      |(pDgDef * pDef) / pD - 0.4967| < 1e-4 := by
  refine ⟨by norm_num, ?_, ?_, ?_⟩ <;> (rw [abs_lt]; constructor <;> norm_num)

end TeoremaDeBayesProblemas
