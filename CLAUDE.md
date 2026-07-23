# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Spanish-language LaTeX ebook (*Modelación Estadística*, `tufte-book` class) with an English mirror, plus a companion set of Beamer slide decks and Python labs under `presentaciones/`. CC BY 4.0. No CI, no test suite, no package manager. Build artifacts (`.aux`, `.pdf`, `.toc`, `.synctex.gz`) are committed; `.log` files are `.gitignore`d and should not be re-added.

## Build commands

Master book (Spanish):
```bash
cd latex
pdflatex "[Modelación Estadística].tex"   # run twice for TOC / cross-refs
```

English mirror lives alongside as `latex/[Statistical Modeling].tex` (same pattern).

Beamer decks (each section is its own standalone `.tex`, compiled from its own directory):
```bash
cd presentaciones/es/<unidad>/ && pdflatex -interaction=nonstopmode <archivo>.tex && pdflatex -interaction=nonstopmode <archivo>.tex
cd presentaciones/en/<unidad>/ && pdflatex -interaction=nonstopmode <archivo>.tex && pdflatex -interaction=nonstopmode <archivo>.tex
```
After compiling, grep the `.log` for `Overfull \vbox`/`Overfull \hbox` — content slides (page 2+) must have zero of these (see Beamer rules below).

Python labs are standalone scripts, stdlib/numpy/scipy only, no venv:
```bash
python presentaciones/code/<unidad>/<archivo>.py
```

## Repository structure

```
latex/[Modelación Estadística].tex   ← ES master file; \inputs every chapter section
latex/[Statistical Modeling].tex     ← EN master file (mirror, kept structurally parallel)
latex/_*.tex                         ← shared preamble infrastructure
latex/<topic>.tex                    ← ES theory content; latex/en_<topic>.tex is its EN mirror
latex/<topic>(p).tex                 ← ES exercise/problem companion; latex/en_<topic>(p).tex is its EN mirror
latex/images/, em/, pe/              ← near-duplicate image directories (~80 files each)
code/<topic>/<example>/              ← standalone Python scripts for the book (\lstinputlisting targets)
soluciones/                          ← solution write-ups (mostly empty)
docs/                                ← syllabus reference + planning docs (see below)
presentaciones/                      ← Beamer decks (es/, en/) + Python labs (code/), see its own README.md
archive/latex/                       ← retired content, not part of the live build: pe-NN <title>.tex
                                        (orphaned parallel chapters) and 3 empty stub files, moved out of
                                        latex/ in commit 136315b
```

## Key conventions (LaTeX book, `latex/`)

- **Master file**: all `\input{}` calls live in the master `.tex`. Chapter files are flat (no nested `\input{}`).
- **`_` prefix files** are infrastructure loaded by the master preamble. Do not `\input{}` them from chapter files.
- **Duplicate preamble files exist**: `_comandos_md.tex` = `_md_comandos.tex`, `_comandos_pe.tex` ≈ `_pe_comandos.tex`, `_comandos_trig.tex` = `_trig_comandos.tex`. Only the `_md_*` / `_pe_*` / `_trig_*` naming is loaded by the master — the `_comandos_*` variants are stale duplicates.
- **Image paths in chapters**: referenced as `./images/...` or `./pe/...`; `images/` and `em/` dirs are near-identical.
- **All ES prose is in Spanish** (babel: `spanish,mexico`); EN files under `latex/en_*.tex` are the parallel English content. The EN theory and problem files now mirror the live ES file set; each problem pair uses six Bloom-ordered problems and shared hash labels. Historical EN bundles remain under `archive/latex/en-pre-syllabus-2026-07-22/`.
- **Code listings**: `\begin{lstlisting}[language=Python]` (styled in `_color-listings.tex`) or `\lstinputlisting[language=python]{../code/...}`.
- **Custom environments** (`_entornos.tex`): `teorema`, `lema`, `proposicion`, `corolario`, `problema`, `ejemplo`, `definicion`, `axioma`, `propiedad`, `observacion`, `sugerencia`, `solucion` (TecRojo), `algoritmo` (TecAzulOscuro) — colores institucionales del Tec de Monterrey (`_paquetes.tex`). Additional from `_md_entornos.tex`: `conj`, `ax`, `tdv`, `claim`, `case`.
- **Custom commands**: see `_comandos.tex`, `_md_comandos.tex`, `_pe_comandos.tex`. Notable: `\Var`, `\cov`, `\comb`, `\s` (sigma), `\corr` (rho), `\card`, `\particion`.
- **LaTeX section-numbering gotcha**: a `\label` on a subsection block does not dictate the compiled section number — the printed number depends purely on how many real (non-starred) `\section`/`\subsection` commands precede it via the master's `\input` order. Don't assume a label like `\label{prob:4.1.1}` will compile to "4.1.1"; verify against the compiled `.aux`/PDF. `\subsection*` (starred) does not advance the counter. A few theory files still have no `\section` of their own (`fundamentos_de_probabilidad.tex`, `teorema_de_bayes.tex` — orphan `\subsection`; `estadisticos_z_t.tex` — `\section*`), so content there inherits the previous section's printed number; known and left as-is.
- **Problem-file convention (ES) is now settled and fully applied**: every `latex/*(p).tex` file (excluding `en_*`) uses exactly 6 problems ordered by Bloom's taxonomy level (Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear, documented as an invisible `% <Nivel>` LaTeX comment) and hashed `\label{prob:<7-hex>}` tags (no numeric `prob:X.Y.Z` labels remain anywhere in `latex/*(p).tex`). This replaced the old 10-problem 3-3-2-2 tier convention (visible `Nivel Fundamental/Operativo/Analítico/Desafiante` banners, numeric labels) across two migration sessions — see `CHANGELOG.md` entries dated 2026-07-20 ("continuación 2") and 2026-07-22. `docs/diagnostico-cuadernos-problemas-2026-07-20.md` documents the pre-migration state (81% of numeric labels landing in the wrong section) as a historical snapshot only — its findings no longer apply to any current file.

## Chapter structure (chapters 2–8 renumbered to the MA1001B syllabus)

`docs/MA1001B-plan-de-estudios.md` is the official syllabus (7 units, numbered subtopics 1.1–7.6) that chapters 2–8 of the master book map to 1:1. Chapter 1 (Estadística Descriptiva) and chapter 9 (Regresiones) are supplementary, outside the official syllabus.

`docs/plan-renumeracion-temario-MA1001B.md` — the file-by-file plan that renumbered/reorganized `latex/*.tex` chapters 2–8 (ES only) to this mapping — **has already been executed** (its own header records "Estado: Ejecutado el 2026-07-20"; verified 2026-07-22 against the master's actual `\input` order). Treat its per-chapter table as a historical record of what was done, not a to-do list. `docs/revision-notas-2026-07-13.md` and `CHANGELOG.md` document the history of ES/EN divergence fixes that preceded and followed this renumbering.

## English mirror gap (read before editing `latex/en_*.tex`)

The ES-only chapter renumbering above (2026-07-20) and both `(p).tex` convention migrations (2026-07-20, 2026-07-22) were initially scoped to Spanish only. Checkpoints 4A--4K completed the English mirror on 2026-07-23: the live tree now contains 60 ES problem files and 60 one-to-one EN counterparts, all with six Bloom-ordered problems and shared hash labels. Superseded EN bundles were preserved under `archive/latex/en-pre-syllabus-2026-07-22/` and removed from the live master. The detailed migration record remains in `docs/proximos-pasos-2026-07-22.md`.

## Beamer Presentations & Python Labs (`presentaciones/`)

**Before touching anything under `presentaciones/`, read `presentaciones/README.md`, `presentaciones/ROADMAP.md`, and `presentaciones/ESPECIFICACIONES_Y_REQUERIMIENTOS.md` first** — they are the authoritative operational manual for this subtree (written explicitly for AI agents) and take precedence over general repo conventions. `ESPECIFICACIONES_Y_REQUERIMIENTOS.md` is the most detailed and most current of the three (it is not cross-linked from the other two): it defines the mandatory 5-block, ~22-slide deck structure (identity/roadmap → theory → 4-slide Python lab bridge → worked-example reinforcement → synthesis/transition) and documents the 2026-07-18 shift away from citing unsolved `(p).tex` problems in Block IV toward reusing already-solved `\ejemplo`/`\solucion` pairs from the theory section. `ROADMAP.md` still describes the older 10-problem "3-3-2-2" taxonomy as the live standard in places — defer to the CHANGELOG 2026-07-18 entry (flexible 3-6 problems per section) over ROADMAP.md where they conflict. Other highlights:

1. **Single source of truth in English for code**: Python labs live only in `presentaciones/code/<unit>/<ID>_<name_in_english>.py`, strictly English comments/variables/output, `numpy`/`scipy` only (no `matplotlib`, no GUI deps). Never create per-language `.py` duplicates — both the ES and EN Beamer decks `\lstinputlisting` the exact same script.
2. **Zero Overfull Warning Policy**: compiled decks must have zero `Overfull \vbox`/`\hbox` on content slides (page 2+). Achieve via `\small`/`\footnotesize`/`\scriptsize`, tight `\vspace{-0.1cm}` to `-0.2cm`, `\begin{columns}[T]`, and splitting long code across multiple slides.
3. **Institutional identity**: every deck header uses the shared preamble (`_preambulo_beamer.tex` / `_en_preambulo_beamer.tex`), author `Juliho Castillo Colmenares` (`julihocc@tec.mx`), `Tecnológico de Monterrey`, palette TecRojo `#EC2661` / TecAzul `#1A2E51`.
4. **6-step checklist** for adding/updating a section (full detail in `presentaciones/README.md` §3): theory audit in `latex/<seccion>.tex` → problem file sync → English Python lab → ES/EN Beamer decks (same script import) → double `pdflatex` compile with zero-warning verification on both → update `CHANGELOG.md` + the catalog table in `presentaciones/README.md`/`ROADMAP.md`. Do not `git commit`/`git push` as part of this checklist — leave changes staged for the author to review.
5. Chapters 2–9 have per-chapter catalog tables in `presentaciones/README.md` (§4 onward) tracking completion status per section — consult these before assuming a section still needs work.

## Non-obvious conventions worth knowing

- `AGENTS.md` at the repo root duplicates most of the LaTeX-book conventions above; keep both in sync if one changes, or prefer consolidating into one file if asked.
- The book's old problem-tier "3-3-2-2" standard (Nivel Fundamental/Operativo/Analítico/Desafiante) is historical for the live book. Current ES and EN `(p).tex` files use exactly 6 Bloom-ordered problems with shared hash labels.
