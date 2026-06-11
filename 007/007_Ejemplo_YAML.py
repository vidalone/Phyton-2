import yaml

# Convertir un diccionario a yaml
usuarios = [{'nombre': 'Juan García', 'ocupacion': 'programador'},
            {'nombre': 'María Dominguez', 'ocupacion': 'tester'}]

print(yaml.dump(usuarios, allow_unicode=True))

# Escribir a un fichero
with open('usuarios.yaml', 'wt', encoding='utf-8') as f:
    yaml.dump(usuarios, f, allow_unicode=True)

# Leer ficheros yaml
with open('usuarios.yaml', encoding='utf-8') as f:
    datos = yaml.load(f, Loader=yaml.FullLoader)
    print(datos)