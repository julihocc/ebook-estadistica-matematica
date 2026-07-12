"""Limpia sintaxis rota residual en archivos .tex"""
import re
import os

files = [
    'latex/regresion_multiple.tex',
    'latex/otros_problemas.tex',
    'latex/regresion_scikit.tex',
]

for tex_file in files:
    if not os.path.exists(tex_file):
        continue
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    changes = 0

    # 1. []{nombre.py} (con posible espacio al final) en su propia linea -> eliminar
    # Solo si NO es seguido por lstlisting que necesitemos
    # Conservador: eliminar solo los [] (vacio) y []{texto} en su propia linea
    for m in re.finditer(r'^\[\]\{[^\}]*\}\s*\n', content, re.MULTILINE):
        full = m.group(0)
        content = content.replace(full, '', 1)
        changes += 1

    # 2. [] (sin nada) en su propia linea -> eliminar
    for m in re.finditer(r'^\[\]\s*\n', content, re.MULTILINE):
        full = m.group(0)
        content = content.replace(full, '', 1)
        changes += 1

    if content != original:
        with open(tex_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print('updated: ' + tex_file + ' (' + str(changes) + ' changes)')
    else:
        print('no changes: ' + tex_file)
