# ******************************************************
# *     Lectura de archvios desde directorio           *
# ******************************************************

import os
from pathlib import Path

fichero_path = Path('002', '002_Ejercicio1.py')

with fichero_path.open('r') as file:
    print(file.read())