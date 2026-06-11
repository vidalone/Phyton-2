# Ejemplo descargar y descomprimir un fichero con urllib.request
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

# Obtener el fichero con los datos de https://insights.stackoverflow.com/survey
# Pertenecen a la encuesta anual de desarrolladores año 2023
zip_url = 'https://cdn.stackoverflow.co/files/jo7n4k8s/production/49915bfd46d0902c3564fd9a06b509d08a20488c.zip/stack-overflow-developer-survey-2023.zip'

with urlopen(zip_url) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall('/home/usuario/')