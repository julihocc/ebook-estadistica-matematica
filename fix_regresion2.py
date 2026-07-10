"""Procesar regresion_multiple.tex: convertir []\\texttt{} + lstlisting a lstinputlisting"""
import re
import os

BS = chr(92)
LB = chr(123)
RB = chr(125)

tex_file = 'latex/regresion_multiple.tex'
code_dir = 'code/regresion'

with open(tex_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Construir el patron usando concatenacion
# \[\]{texto}
part1 = BS + '[' + BS + ']' + BS + LB  # \[\]{

# \texttt{advertisingModel2.py}
part2 = 'advertisingModel2' + BS + '.py' + RB  # advertisingModel2\.py}

# \s*
part3 = BS + 's*'

# \\begin{lstlisting}
part4 = BS + BS + 'begin' + BS + LB + 'lstlisting' + RB

# (.*?)
part5 = '(.*?)'

# \\end{lstlisting}
part6 = BS + BS + 'end' + BS + LB + 'lstlisting' + RB

full_pat = part1 + part2 + part3 + part4 + part5 + part6
print('Patron: ' + repr(full_pat))

m = re.search(full_pat, content, re.DOTALL)
if m:
    py_content = m.group(1)
    lines = py_content.split('\n')
    non_empty = [l for l in lines if l.strip()]
    if non_empty:
        min_indent = min(len(l) - len(l.lstrip()) for l in non_empty)
        cleaned = [l[min_indent:] if len(l) >= min_indent else l for l in lines]
    else:
        cleaned = lines
    py_text = '\n'.join(cleaned).strip() + '\n'
    py_path = code_dir + '/advertisingModel2.py'
    os.makedirs(code_dir, exist_ok=True)
    with open(py_path, 'w', encoding='utf-8') as f:
        f.write(py_text)
    print('creado: ' + py_path)

    old_block = m.group(0)
    new_block = BS + 'lstinputlisting[language=Python]' + LB + '../' + code_dir + '/advertisingModel2.py' + RB
    content = content.replace(old_block, new_block)
    with open(tex_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print('bloque reemplazado')
else:
    print('no se encontro')
