# AGENTS.md

## What this is

A Spanish-language LaTeX ebook (_Modelación Estadística_) using `tufte-book`. CC BY 4.0.
No CI, no tests, no build system. Build artifacts (`.aux`, `.pdf`, `.toc`, `.synctex.gz`) are committed; `.log` files are `.gitignore`d and should not be re-added.

## Build

```bash
cd latex
pdflatex "[Modelación Estadística].tex"   # run twice for TOC / cross-refs
```

## Structure

```
latex/[Modelación Estadística].tex   ← master file; \inputs every chapter section
latex/_*.tex                         ← shared preamble infrastructure (9 files)
latex/<topic>.tex                    ← theory content (definitions, theorems, examples)
latex/<topic>(p).tex                 ← exercise/problem companion for the same topic
latex/pe-NN <title>.tex             ← standalone parallel chapters (NOT included by master)
latex/images/, em/, pe/             ← near-duplicate image directories (~80 files each)
latex/particiones/, licencia/        ← specialized image dirs
code/<topic>/<example>/              ← standalone Python scripts (\lstinputlisting targets)
soluciones/                          ← solution write-ups (mostly empty)
```

## Key conventions

- **Master file**: All `\input{}` calls are in the master. Chapter files are flat (no nested `\input{}`).
- **`_` prefix files** are infrastructure loaded by the master preamble. Do not `\input{}` them from chapter files.
- **Duplicate preamble files exist**: `_comandos_md.tex` = `_md_comandos.tex`, `_comandos_pe.tex` ≈ `_pe_comandos.tex`, `_comandos_trig.tex` = `_trig_comandos.tex`. Only the `_md_*` / `_pe_*` / `_trig_*` naming is loaded by the master — the `_comandos_*` variants are stale duplicates.
- **Image paths in chapters**: Referenced as `./images/...` or `./pe/...`. The `images/` and `em/` dirs are near-identical.
- **`pe-*.tex` files are orphaned**: They use different environment names (`defn`/`thm`/`rem`/`axiom` instead of `definicion`/`teorema`/`observacion`/`axioma`) and are NOT included by the master.
- **All prose is in Spanish** (babel: `spanish,mexico`).
- **Code listings**: Use `\begin{lstlisting}[language=Python]` (styled in `_color-listings.tex`) or `\lstinputlisting[language=python]{../code/...}`.
- **Custom environments** (defined in `_entornos.tex`): `teorema`, `lema`, `proposicion`, `corolario`, `problema`, `ejemplo`, `definicion`, `axioma`, `propiedad`, `observacion`, `sugerencia`, `solucion` (TecRojo), `algoritmo` (TecAzulOscuro) — colores institucionales del Tec de Monterrey definidos en `_paquetes.tex`. Additional from `_md_entornos.tex`: `conj`, `ax`, `tdv`, `claim`, `case`.
- **Custom commands**: See `_comandos.tex`, `_md_comandos.tex`, `_pe_comandos.tex`. Notable: `\Var`, `\cov`, `\comb`, `\s` (sigma), `\corr` (rho), `\card`, `\particion`.
- **Empty stub files**: `estadistica-descriptiva.tex`, `regresiones-lineales.tex`, `conceptos-estadisticos.tex` are empty — do not add content to these unless they are `\input{}`'d by the master (they are not).
- **Python scripts** in `code/` are standalone, stdlib or numpy-only. No venv, no `requirements.txt`.
- **Problem-tier standard ("3-3-2-2")**: every `(p).tex` file organizes its "Enunciados de los problemas" into four `\subsubsection*` tiers, in order: Nivel Fundamental (3 problems), Nivel Operativo (3), Nivel Analítico (2), Nivel Desafiante (2). Apply this same structure to any new topic's problem file.
- **Syllabus coverage**: the official program (`docs/MA1001B - Analítico.pdf`) defines 7 units, which map 1:1 onto chapters 2–8 of the master file. Chapter 1 (Estadística Descriptiva) and chapter 9 (Regresiones Lineales y Múltiples) are supplementary content beyond the official syllabus — there is no "Unit 8" to fill.
- **Problem numbering is actively broken, not just planned work**: `docs/diagnostico-cuadernos-problemas-2026-07-20.md` is a read-only audit confirming 81% of numeric `\label{prob:X.Y.Z}` across the 19 `(p).tex` files (chapters 2–8) compile to a different section than their name suggests, plus a live duplicate-label collision (`prob:3.9.1`–`.5` in `distribuciones_especiales(p).tex` vs `chi_cuadrada(p).tex`) that makes solution hints in the compiled PDF point to the wrong problem. Check it before assuming a `(p).tex` file's problems live where its labels claim. The "3-3-2-2" rule above is being phased out (see `CHANGELOG.md`, 2026-07-18 entry) in favor of 3-6 problems per section — don't apply it to new problem files without checking that entry first.

## Beamer Presentations & Python Labs (`presentaciones/`)

When working on Beamer slide decks or Python computational labs, **you MUST immediately consult `presentaciones/README.md`, `presentaciones/ROADMAP.md`, and `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md` before taking any action**. The last of these is the most detailed and most current — it is not cross-linked from the other two — and defines the mandatory 5-block, ~22-slide deck structure, including the 2026-07-18 change of Block IV away from citing unsolved `(p).tex` problems toward reusing already-solved `\ejemplo`/`\solucion` pairs from the theory section. `ROADMAP.md` still describes the older "3-3-2-2" problem taxonomy as current in places; prefer the `CHANGELOG.md` 2026-07-18 entry where they conflict.
Key rules enforced in `presentaciones/README.md`:
1. **Single Source of Truth in English for Code**: Python scripts reside in `presentaciones/code/<unit>/<ID>_<name_in_english>.py` (`numpy`/`scipy` only, strict English comments/variables). Do NOT create Spanish `.py` scripts. Both Spanish (`presentaciones/es/`) and English (`presentaciones/en/`) Beamer decks import lines from the exact same English `.py` script via `\lstinputlisting`.
2. **Zero Overfull Warning Policy**: Slide decks must compile (`pdflatex`) with **ZERO `Overfull \vbox` and ZERO `Overfull \hbox`** warnings across all content slides (pages 2+). Use compact sizing (`\small`, `\footnotesize`, `\scriptsize`), tight vertical spacing (`\vspace{-0.1cm}` to `-0.2cm`), and two-column layouts `\begin{columns}[T]`. Title page uses `\begin{frame}[plain]`.
3. **Institutional Identity**: Author `Juliho Castillo Colmenares` (`julihocc@tec.mx`), `Tecnológico de Monterrey`. Uses institutional palette `#EC2661` (TecRojo) and `#1A2E51` (TecAzul).
4. **Reproducible 6-Step Checklist**: Every new section must follow the exact 6-step checklist detailed in `presentaciones/README.md` (theory audit $\to$ problem notebook 3-3-2-2 $\to$ Python lab in English $\to$ ES/EN Beamer decks $\to$ double `pdflatex` compilation zero-warning verification $\to$ commit & log update).

