import requests
import pandas as pd
import json

# Listo las provincias para recorrer cada una
url_provincias = "http://www.inmuebles.clarin.com/Regiones/FindProvincias?contentType=json&idPais=1"
headers = {"User-Agent":"Mozilla/5.0"}
provincias_res = requests.get(url_provincias, headers=headers).text
df = pd.read_json(url_provincias)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
id_list = df['Id'].tolist()
provincia_list = df['Nombre'].tolist()

# Url para iterar los partidos de cada provincia
url_partidos = "http://www.inmuebles.clarin.com/Regiones/FindPartidos?contentType=json&IdProvincia="

for i in range(len(id_list)):
    # Hago una peticion por cada provincia
    headers = {"User-Agent":"Mozilla/5.0"}
    respuesta_res = requests.get(url_partidos + str(id_list[i]), headers=headers).text

    # Creo un archivo por cada provincia
    archivo = 'json/partidos/partidos_' + provincia_list[i] + '.json'
    fichero = open(archivo, 'wt')
    fichero.write(respuesta_res)
    fichero.close()
