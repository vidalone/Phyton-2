import pandas as pd
import os
import shutil


fichero_csv = '36680.csv'
directorio = 'DatosGobOrg'
nuevo_fichero_tsv = 'escribir_tsv.tsv'

# *********************************************************************************
# 1 Convierte a .tsv 
leer_csv = pd.read_csv(fichero_csv, sep=';')
print(leer_csv.head(10))

with open(nuevo_fichero_tsv, 'w', encoding='utf-8', newline='') as write_tsv: 
    write_tsv.write(leer_csv.to_csv(sep='\t', index=False))

# *********************************************************************************
# 2 Creamos un nuevo directorio, comprobando que previamente existe, o no.
if not os.path.exists(directorio):
    os.makedirs(directorio)
    print('Creando el directorio"', directorio, "\".")
else:
    print('El directorio ya existe. Continuamos...')

# Copiamos archivo al nuevo directorio
shutil.copy(src=fichero_csv, dst=os.path.join(directorio, fichero_csv))

# *********************************************************************************
# 3 Escribimos un nuevo archivo con las 100 primeras lineas en TSV.
leer_csv = pd.read_csv(fichero_csv, sep='\t')

with open(nuevo_fichero_tsv, 'w', encoding='utf-8', newline='') as write_csv:
    # index=False no muestra el índice
    write_csv.write(leer_csv.head(100).to_csv(sep='\t', encoding='utf-8', index=False))

# Movemos archivo al nuevo directorio
print('\n\nMoviendo archivo a directorio;', nuevo_fichero_tsv, '->', directorio)
shutil.move(src=nuevo_fichero_tsv, dst=os.path.join(directorio, nuevo_fichero_tsv))

# *********************************************************************************
# 4 Convertir el fichero a formato .xlsx

print('\n\nConvirtiendo archivo a Excel\n')

leer_fichero = pd.read_csv(r'36680.csv', sep=';', encoding='utf-8')
leer_fichero.to_excel(r'esricbir_csv_36680.xlsx')


# Se crea el dataframe con pandas de un fichero Excel
df = pd.read_excel("esricbir_csv_36680.xlsx")
print(df)

# Selecciona la primera y la cuarta columna
print(df.iloc[:, [0, 3]])

# se exporta a excel
df.iloc[:, [0, 3]].to_excel('catalogo_cf_resumen.xlsx')


print('\n\nMoviendo archivos a directorio')
# Movemos archivo al nuevo directorio
shutil.move(src='esricbir_csv_36680.xlsx', dst=os.path.join(directorio, 'esricbir_csv_36680.xlsx'))

# Movemos archivo al nuevo directorio
shutil.move(src='catalogo_cf_resumen.xlsx', dst=os.path.join(directorio, 'catalogo_cf_resumen.xlsx'))