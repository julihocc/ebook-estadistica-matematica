import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# Calibración del método

Antes de confiar el harness a capítulos no auditados, se codifican aquí dos
errores matemáticos ya encontrados y corregidos manualmente (documentados en
`docs/revision-notas-2026-07-13.md`), tal como aparecían en el texto ANTES de
su corrección (ver commits `674c1e7` y `4fc0342`), para confirmar que el
método efectivamente los detecta como matemáticamente falsos.

Cada lema de calibración prueba que la afirmación pre-corrección es **distinta**
del valor que el libro pre-corrección afirmaba obtener — es decir, el texto
pre-fix era internamente inconsistente (mostraba una fórmula y afirmaba un
resultado que esa fórmula no produce). Esto es justo lo que un auditor humano
(o Lean) debe detectar.
-/

namespace Calibracion

/-- `chi_cuadrada.tex:48` antes de `674c1e7` — el texto mostraba
`g = ((553-500)^2 + (447-500)^5) / 500` (exponente `5` en vez de `2`) y
afirmaba `g ≈ 11.236`. La fórmula tal como estaba escrita da un valor muy
distinto (el término `(447-500)^5 = (-53)^5` es enorme y negativo, no `2809`),
así que la afirmación `≈ 11.236` es falsa para la fórmula escrita. -/
theorem chi_cuadrada_pre_fix_no_es_11_236 :
    ((553 - 500 : ℝ) ^ 2 + (447 - 500 : ℝ) ^ 5) / 500 ≠ 11.236 := by
  norm_num

/-- La fórmula corregida (`674c1e7`, exponente `2` en ambos términos) sí produce
el valor que el libro afirma, `11.236`, exactamente. -/
theorem chi_cuadrada_corregida_es_11_236 :
    ((553 - 500 : ℝ) ^ 2 + (447 - 500 : ℝ) ^ 2) / 500 = 11.236 := by
  norm_num

/-- `esperanza_matematica.tex:103-107` antes de `4fc0342` — el bloque residual
afirmaba
`μ = $20(1/6) + $40(1/6) + $60(1/6) = ($20+$40+$60+3×$0)/6 = $15`.
La segunda igualdad es un error aritmético puro: `(20+40+60+3×0)/6 = 20`, no
`15` (y de hecho el ejemplo correcto, ya presente en el texto en la líneas
92-96, obtiene `$20`). -/
theorem esperanza_pre_fix_no_es_15 :
    ((20 : ℝ) + 40 + 60 + 3 * 0) / 6 ≠ 15 := by
  norm_num

/-- El valor correcto de esa misma suma es `$20`, que coincide con el resultado
que el libro reporta en su ejemplo (línea 96: "el jugador gana \$20 por juego"). -/
theorem esperanza_correcta_es_20 :
    ((20 : ℝ) + 40 + 60 + 3 * 0) / 6 = 20 := by
  norm_num

end Calibracion
