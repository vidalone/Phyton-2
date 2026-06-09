import os
from pathlib import Path

fichero_path = Path(Path.home(), 'directori_ficheros')

if not fichero_path.exists():
    os.makedirs(fichero_path)

fichero_path: Path = fichero_path.joinpath('miquijote001.txt')

with fichero_path.open('w') as fichero:
    entrada: list[str] = """ HOLA MUNDO"""

with open('miquijote001.txt', 'a') as fichero:
    fichero.write(entrada)