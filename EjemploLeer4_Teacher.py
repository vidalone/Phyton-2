import os
from pathlib import Path 

fichero_path = Path(Path.home(), 'directorio_ficheros')

if not fichero_path.exists():
    os.makedirs(fichero_path)

fichero_path = fichero_path.joinpath('miquijote001.txt') 

with fichero_path.open('w') as fichero:
    entrada = [""" En un lugar de la Mancha, de cuyo nombre no quiero
    acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en
    astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de
    algo más vaca que carnero, ...
    """]
    fichero.writelines(entrada)