import requests
import pandas as pd
import json
import pathlib

# Lista de Provincias
url_provincias = "http://www.inmuebles.clarin.com/Regiones/FindProvincias?contentType=json&idPais=1"
headers = {"User-Agent":"Mozilla/5.0"}
provincias_res = requests.get(url_provincias, headers=headers).text
df = pd.read_json(url_provincias)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
id_list = df['Id'].tolist()
provincia_list = df['Nombre'].tolist()

for prov in range(len(id_list)):
    # Lista de Partidos de la Provincia prov
    url_partidos = "http://www.inmuebles.clarin.com/Regiones/FindPartidos?contentType=json&IdProvincia=" + str(id_list[prov])
    headers = {"User-Agent":"Mozilla/5.0"}
    partidos_res = requests.get(url_partidos, headers=headers).text
    df_partidos = pd.read_json(url_partidos)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    id_list_partidos = df_partidos['Id'].tolist()
    partidos_list = df_partidos['Nombre'].tolist()

    for part in range(len(id_list_partidos)):
        # Hago una peticion por cada partido para extraer las localidades

        url_localidades = "http://www.inmuebles.clarin.com/Regiones/FindLocalidades?contentType=json&IdPartido=" + str(id_list_partidos[part])

        headers = {"User-Agent":"Mozilla/5.0"}
        respuesta_res = requests.get(url_localidades, headers=headers).text

        # Creo carpeta
        pathlib.Path('json/localidades/' + provincia_list[prov].replace(' ', '-').lower()).mkdir(parents=True, exist_ok=True) 

        # Creo un archivo por cada localidad
        archivo = 'json/localidades/' + provincia_list[prov].replace(' ', '-').lower()  + '/' + partidos_list[part].replace(' ', '-').lower() + '.json'
        fichero = open(archivo, 'wt')
        fichero.write(respuesta_res)
        fichero.close()