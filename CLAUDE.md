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
latex/pe-NN <title>.tex              ← standalone parallel chapters (NOT included by master, orphaned)
latex/images/, em/, pe/              ← near-duplicate image directories (~80 files each)
code/<topic>/<example>/              ← standalone Python scripts for the book (\lstinputlisting targets)
soluciones/                          ← solution write-ups (mostly empty)
docs/                                ← syllabus reference + planning docs (see below)
presentaciones/                      ← Beamer decks (es/, en/) + Python labs (code/), see its own README.md
archive/                             ← retired content, not part of the live build
```

## Key conventions (LaTeX book, `latex/`)

- **Master file**: all `\input{}` calls live in the master `.tex`. Chapter files are flat (no nested `\input{}`).
- **`_` prefix files** are infrastructure loaded by the master preamble. Do not `\input{}` them from chapter files.
- **Duplicate preamble files exist**: `_comandos_md.tex` = `_md_comandos.tex`, `_comandos_pe.tex` ≈ `_pe_comandos.tex`, `_comandos_trig.tex` = `_trig_comandos.tex`. Only the `_md_*` / `_pe_*` / `_trig_*` naming is loaded by the master — the `_comandos_*` variants are stale duplicates.
- **Image paths in chapters**: referenced as `./images/...` or `./pe/...`; `images/` and `em/` dirs are near-identical.
- **`pe-*.tex` files are orphaned**: they use different environment names (`defn`/`thm`/`rem`/`axiom` instead of `definicion`/`teorema`/`observacion`/`axioma`) and are not included by the master.
- **All ES prose is in Spanish** (babel: `spanish,mexico`); EN files under `latex/en_*.tex` are the parallel English content and should be kept structurally in sync with their ES counterpart (same `\section`/`\subsection` shape) — see `docs/revision-notas-2026-07-13.md` for the kind of ES/EN divergence bugs that have occurred (missing sections, mismatched problem numbering) and how they were diagnosed.
- **Code listings**: `\begin{lstlisting}[language=Python]` (styled in `_color-listings.tex`) or `\lstinputlisting[language=python]{../code/...}`.
- **Custom environments** (`_entornos.tex`): `teorema`, `lema`, `proposicion`, `corolario`, `problema`, `ejemplo`, `definicion`, `axioma`, `propiedad`, `observacion`, `sugerencia`, `solucion` (TecRojo), `algoritmo` (TecAzulOscuro) — colores institucionales del Tec de Monterrey (`_paquetes.tex`). Additional from `_md_entornos.tex`: `conj`, `ax`, `tdv`, `claim`, `case`.
- **Custom commands**: see `_comandos.tex`, `_md_comandos.tex`, `_pe_comandos.tex`. Notable: `\Var`, `\cov`, `\comb`, `\s` (sigma), `\corr` (rho), `\card`, `\particion`.
- **Empty stub files**: `estadistica-descriptiva.tex`, `regresiones-lineales.tex`, `conceptos-estadisticos.tex` are empty — do not add content to these unless they are actually `\input{}`'d by the master (currently they are not).
- **LaTeX section-numbering gotcha**: a `\label` on a subsection block does not dictate the compiled section number — the printed number depends purely on how many real (non-starred) `\section`/`\subsection` commands precede it via the master's `\input` order. Don't assume a label like `\label{prob:4.1.1}` will compile to "4.1.1"; verify against the compiled `.aux`/PDF. `\subsection*` (starred) does not advance the counter.
- **Problem numbering convention is currently in flux** — see "Active restructuring" below before touching any `(p).tex` file or its problem taxonomy.

## Active restructuring (read before editing chapters 2-8 or problem files)

Two planning documents in `docs/` describe **decided but not-yet-executed** structural work. Check these before assuming the current `\section` layout, chapter-to-syllabus mapping, or problem-count convention is final:

- `docs/MA1001B-plan-de-estudios.md` — official syllabus (7 units, numbered subtopics 1.1–7.6) that chapters 2–8 of the master book are meant to map to 1:1. Chapter 1 (Estadística Descriptiva) and chapter 9 (Regresiones) are supplementary, outside the official syllabus.
- `docs/plan-renumeracion-temario-MA1001B.md` — detailed, file-by-file plan to renumber/reorganize `latex/*.tex` chapters 2–8 (ES only; `en_*`, `presentaciones/`, and `(p).tex` files are explicitly out of scope for this particular plan) so each chapter has exactly one numbered `\section` per syllabus subtopic. Execution order: chapters 6 → 3 → 4 → 5 → 2 → 8 → 7. If asked to work on chapter restructuring, follow this plan's per-chapter table rather than improvising a new mapping.
- `docs/revision-notas-2026-07-13.md` and `CHANGELOG.md` — history of ES/EN divergence fixes and the still-unresolved problem-numbering offset bug; read before trusting that ES and EN chapter structures currently match.
- `CHANGELOG.md` (2026-07-18 entry) records a **decided-but-unexecuted** change to the problem-file/slide conventions: moving from "one `(p).tex` per chapter" to "one `(p).tex` per section", from a fixed 10-problem 3-3-2-2 taxonomy to a flexible 3-6 problems per section, and from visible difficulty banners to LaTeX comments. Check this entry before creating or restructuring any `(p).tex` file — the "3-3-2-2" rule below is the convention being phased out, not necessarily the one to apply to new work.

## Beamer Presentations & Python Labs (`presentaciones/`)

**Before touching anything under `presentaciones/`, read `presentaciones/README.md` and `presentaciones/ROADMAP.md` first** — they are the authoritative operational manual for this subtree (written explicitly for AI agents) and take precedence over general repo conventions. Highlights:

1. **Single source of truth in English for code**: Python labs live only in `presentaciones/code/<unit>/<ID>_<name_in_english>.py`, strictly English comments/variables/output, `numpy`/`scipy` only (no `matplotlib`, no GUI deps). Never create per-language `.py` duplicates — both the ES and EN Beamer decks `\lstinputlisting` the exact same script.
2. **Zero Overfull Warning Policy**: compiled decks must have zero `Overfull \vbox`/`\hbox` on content slides (page 2+). Achieve via `\small`/`\footnotesize`/`\scriptsize`, tight `\vspace{-0.1cm}` to `-0.2cm`, `\begin{columns}[T]`, and splitting long code across multiple slides.
3. **Institutional identity**: every deck header uses the shared preamble (`_preambulo_beamer.tex` / `_en_preambulo_beamer.tex`), author `Juliho Castillo Colmenares` (`julihocc@tec.mx`), `Tecnológico de Monterrey`, palette TecRojo `#EC2661` / TecAzul `#1A2E51`.
4. **6-step checklist** for adding/updating a section (full detail in `presentaciones/README.md` §3): theory audit in `latex/<seccion>.tex` → problem file sync → English Python lab → ES/EN Beamer decks (same script import) → double `pdflatex` compile with zero-warning verification on both → update `CHANGELOG.md` + the catalog table in `presentaciones/README.md`/`ROADMAP.md`. Do not `git commit`/`git push` as part of this checklist — leave changes staged for the author to review.
5. Chapters 2–9 have per-chapter catalog tables in `presentaciones/README.md` (§4 onward) tracking completion status per section — consult these before assuming a section still needs work.

## Non-obvious conventions worth knowing

- `AGENTS.md` at the repo root duplicates most of the LaTeX-book conventions above; keep both in sync if one changes, or prefer consolidating into one file if asked.
- The book's problem-tier "3-3-2-2" standard (Nivel Fundamental/Operativo/Analítico/Desafiante) is being deprecated in favor of a flexible 3-6-problem convention — see "Active restructuring" above.
