# AGENTS.md

## What this is

A Spanish-language LaTeX ebook (_Modelación Estadística_) using `tufte-book`, with an English mirror. CC BY 4.0.
No CI, no tests, no build system. Build artifacts (`.aux`, `.pdf`, `.toc`, `.synctex.gz`) are committed; `.log` files are `.gitignore`d and should not be re-added.

## Build

```bash
cd latex
pdflatex "[Modelación Estadística].tex"   # run twice for TOC / cross-refs
```

## Structure

```
latex/[Modelación Estadística].tex   ← ES master file; \inputs every chapter section
latex/[Statistical Modeling].tex     ← EN master file (mirror, currently catching up)
latex/_*.tex                         ← shared preamble infrastructure (9 files)
latex/<topic>.tex                    ← theory content (definitions, theorems, examples)
latex/en_<topic>.tex                 ← English mirror for theory content
latex/<topic>(p).tex                 ← exercise/problem companion for the same topic
latex/en_<topic>(p).tex              ← English mirror for problem companions
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
- **All ES prose is in Spanish** (babel: `spanish,mexico`). EN files under `latex/en_*.tex` are the parallel English content; the theory file set now mirrors ES, while EN problem companions remain pending migration. Read `docs/proximos-pasos-2026-07-22.md` before editing them.
- **Code listings**: Use `\begin{lstlisting}[language=Python]` (styled in `_color-listings.tex`) or `\lstinputlisting[language=python]{../code/...}`.
- **Custom environments** (defined in `_entornos.tex`): `teorema`, `lema`, `proposicion`, `corolario`, `problema`, `ejemplo`, `definicion`, `axioma`, `propiedad`, `observacion`, `sugerencia`, `solucion` (TecRojo), `algoritmo` (TecAzulOscuro) — colores institucionales del Tec de Monterrey definidos en `_paquetes.tex`. Additional from `_md_entornos.tex`: `conj`, `ax`, `tdv`, `claim`, `case`.
- **Custom commands**: See `_comandos.tex`, `_md_comandos.tex`, `_pe_comandos.tex`. Notable: `\Var`, `\cov`, `\comb`, `\s` (sigma), `\corr` (rho), `\card`, `\particion`.
- **Archived stubs/orphans**: retired `pe-*.tex` files and the old empty stub files live under `archive/latex/`, not in the live master.
- **Python scripts** in `code/` are standalone, stdlib or numpy-only. No venv, no `requirements.txt`.
- **Problem-file convention (ES)**: every live Spanish `latex/*(p).tex` file uses exactly 6 problems ordered by Bloom's taxonomy (Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear), documented as invisible LaTeX comments, with hashed `\label{prob:<7-hex>}` tags. The old 10-problem 3-3-2-2 tier convention is historical and must not be used for new ES problem files.
- **Syllabus coverage**: the official program (`docs/MA1001B - Analítico.pdf`) defines 7 units, which map 1:1 onto chapters 2–8 of the master file. Chapter 1 (Estadística Descriptiva) and chapter 9 (Regresiones Lineales y Múltiples) are supplementary content beyond the official syllabus — there is no "Unit 8" to fill.
- **Historical problem-numbering diagnostic**: `docs/diagnostico-cuadernos-problemas-2026-07-20.md` records the pre-migration state where numeric labels landed in the wrong compiled sections. Its findings no longer apply to live ES `(p).tex` files after the 2026-07-20 and 2026-07-22 migrations, but the EN problem mirror remains pending (visible tier headings, mixed legacy labels, and missing exact counterparts).

## Beamer Presentations & Python Labs (`presentaciones/`)

When working on Beamer slide decks or Python computational labs, **you MUST immediately consult `presentaciones/README.md`, `presentaciones/ROADMAP.md`, and `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md` before taking any action**. The last of these is the most detailed and most current — it is not cross-linked from the other two — and defines the mandatory 5-block, ~22-slide deck structure, including the 2026-07-18 change of Block IV away from citing unsolved `(p).tex` problems toward reusing already-solved `\ejemplo`/`\solucion` pairs from the theory section. `ROADMAP.md` still describes the older "3-3-2-2" problem taxonomy as current in places; prefer the `CHANGELOG.md` 2026-07-18 entry where they conflict.
Key rules enforced in `presentaciones/README.md`:
1. **Single Source of Truth in English for Code**: Python scripts reside in `presentaciones/code/<unit>/<ID>_<name_in_english>.py` (`numpy`/`scipy` only, strict English comments/variables). Do NOT create Spanish `.py` scripts. Both Spanish (`presentaciones/es/`) and English (`presentaciones/en/`) Beamer decks import lines from the exact same English `.py` script via `\lstinputlisting`.
2. **Zero Overfull Warning Policy**: Slide decks must compile (`pdflatex`) with **ZERO `Overfull \vbox` and ZERO `Overfull \hbox`** warnings across all content slides (pages 2+). Use compact sizing (`\small`, `\footnotesize`, `\scriptsize`), tight vertical spacing (`\vspace{-0.1cm}` to `-0.2cm`), and two-column layouts `\begin{columns}[T]`. Title page uses `\begin{frame}[plain]`.
3. **Institutional Identity**: Author `Juliho Castillo Colmenares` (`julihocc@tec.mx`), `Tecnológico de Monterrey`. Uses institutional palette `#EC2661` (TecRojo) and `#1A2E51` (TecAzul).
4. **Reproducible 6-Step Checklist**: Every new section must follow the exact 6-step checklist detailed in `presentaciones/README.md` (theory audit $\to$ problem sync under the current convention $\to$ Python lab in English $\to$ ES/EN Beamer decks $\to$ double `pdflatex` compilation zero-warning verification $\to$ changelog/catalog update). Do not `git commit` or `git push` unless explicitly asked.

