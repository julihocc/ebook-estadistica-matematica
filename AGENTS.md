# AGENTS.md

## What this is

A Spanish-language LaTeX ebook (_Modelación Estadística_) using `tufte-book`. CC BY 4.0.
No CI, no tests, no build system, no `.gitignore`. Build artifacts (`.aux`, `.log`, `.pdf`, `.toc`, `.synctex.gz`) are committed.

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
- **Custom environments** (defined in `_entornos.tex`): `teorema`, `lema`, `proposicion`, `corolario`, `problema`, `ejemplo`, `definicion`, `axioma`, `propiedad`, `observacion`, `sugerencia`, `solucion` (maroon), `algoritmo` (RedViolet). Additional from `_md_entornos.tex`: `conj`, `ax`, `tdv`, `claim`, `case`.
- **Custom commands**: See `_comandos.tex`, `_md_comandos.tex`, `_pe_comandos.tex`. Notable: `\Var`, `\cov`, `\comb`, `\s` (sigma), `\corr` (rho), `\card`, `\particion`.
- **Empty stub files**: `estadistica-descriptiva.tex`, `regresiones-lineales.tex`, `conceptos-estadisticos.tex` are empty — do not add content to these unless they are `\input{}`'d by the master (they are not).
- **Python scripts** in `code/` are standalone, stdlib or numpy-only. No venv, no `requirements.txt`.
