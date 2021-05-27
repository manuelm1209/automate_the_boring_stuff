#! python3
from pathlib import Path
import os

print('\n--- current working directory ---')
print(Path.cwd())

print('\n--- Cambiar cwd ---')
os.chdir('/Users')
print(Path.cwd())

print('\n--- Home Directory ---')
print(Path.home())

print('\n--- Crear carpetas en Home mac (CODIGO COMENTADO) ---')
# .mkdir() solo puede crear un directoria a la vez.
# os.makedirs('/Users/mac/carpeta1/carpeta2')
print('Se han creado 2 carpetas en Home mac: /Users/mac/carpeta1/carpeta2')
print('QUITAR # PARA EJECUTAR CODIGO')

print('\n--- Relative path from home directory ---')
print(Path.home() / Path('my/relative/path'))
