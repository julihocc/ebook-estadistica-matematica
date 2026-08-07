import Mathlib.Tactic

/-!
# Distribuciones muestrales de medias — teoría

Formaliza `latex/distribuciones_muestrales_medias.tex`. **`eq:3.2.7`/`eq:3.2.8`/`eq:3.2.9`
($E(\bar X)=\mu$, $\Var(\bar X)=\sigma^2/n$, $\mathrm{DE}(\bar X)=\sigma/\sqrt n$) y
`eq:5.1.2` (insesgadez de $S^2$, $E(S^2)=\sigma^2$) son duplicados exactos de
teoremas ya probados en el capítulo piloto**: `VariablesAleatorias.esperanza_media_muestral`,
`varianza_media_muestral`, `esperanza_varianza_muestral` (no importado en
este worktree por el problema de longitud de ruta de Windows, ver nota en
`EsperanzaMatematica.lean`, pero las demostraciones ya existen y están
probadas — no se reproducen aquí). El Teorema del Límite Central
(`eq:5.2.1`) y el teorema de Berry-Esseen (`eq:5.2.2`) son Tier D
(resultados asintóticos profundos, ya identificados como tales en el
plan original de este proyecto de verificación). Se formalizan los dos
ejemplos numéricos.
-/

namespace DistribucionesMuestralesMedias

/-- `exmp:sample-mean-and-unbiased-variance` — muestra $\{12,15,11,18,14\}$:
$\bar X=70/5=14$, $S^2=30/4=7.5$. -/
theorem exmp_media_varianza_muestral :
    ((12 : ℝ) + 15 + 11 + 18 + 14) / 5 = 14 ∧
      ((12 - 14 : ℝ) ^ 2 + (15 - 14) ^ 2 + (11 - 14) ^ 2 + (18 - 14) ^ 2 + (14 - 14) ^ 2) / 4 = 7.5 := by
  constructor <;> norm_num

/-- `exmp:5.2.1` — $\mathrm{Exp}$ tiempo de servicio, $\mu=4,\sigma=4,n=64$:
$\mathrm{DE}(\bar X)=4/\sqrt{64}=0.5$, $Z=(4.5-4)/0.5=1$ exacto (el valor
$\Phi(1)\approx0.8413$ ya se confirmó en `distribucion_normal`, Tier C,
no se repite). -/
theorem exmp_5_2_1 : (4 : ℝ) / Real.sqrt 64 = 0.5 ∧ ((4.5 : ℝ) - 4) / 0.5 = 1 := by
  have h64 : Real.sqrt (64 : ℝ) = 8 := by
    rw [show (64 : ℝ) = 8 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
  rw [h64]
  norm_num

end DistribucionesMuestralesMedias
