import Mathlib.Tactic

/-!
# Función generadora de momentos — problemas

Formaliza `latex/funcion_generadora_momentos(p).tex`. `prob:5a5f63a`
(Recordar), `prob:f26d9b0` (Comprender) y `prob:5098ae4` (Evaluar) son
puramente conceptuales, sin cálculo numérico, no formalizados.
`prob:cf5e60c` (Analizar) reutiliza `FuncionGeneradoraMomentos.prob_cf5e60c_general`
de la teoría, no se repite. `prob:2c4cd93` (Aplicar, FGM de Poisson vía
serie) necesitaría la misma maquinaria `tsum`/`NormedSpace.expSeries_div_hasSum_exp`
de `distribucion_poisson` — Tier C/D, no reproducida en este pase (el
resultado en sí, $M_X(t)=e^{\lambda(e^t-1)}$, es estándar y no se
cuestiona). `prob:a48cc99` (Crear, FGM de $U(0,1)$) ya está cubierto por
`FuncionGeneradoraMomentos.prob_a48cc99_mgf` de la teoría — el valor
$E[X]=1/2$ es una instancia trivial de la fórmula general de la media
uniforme ya probada en `DistribucionUniformeContinua.media_uniforme`; no
hay ningún teorema nuevo que formalizar en este archivo de problemas.
-/

namespace FuncionGeneradoraMomentosProblemas

end FuncionGeneradoraMomentosProblemas
