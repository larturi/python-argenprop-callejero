import requests
import pandas as pd
import json
import pathlib
import sys
sys.path.insert(0, '/modulos/')
from modulos import ficheros

# Creo archivo de salida
fichero = ficheros.Fichero('localidades.csv')

# Lista de Provincias
url_provincias = "http://www.inmuebles.clarin.com/Regiones/FindProvincias?contentType=json&idPais=1"
headers = {"User-Agent":"Mozilla/5.0"}
provincias_res = requests.get(url_provincias, headers=headers).text
df = pd.read_json(url_provincias)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
id_list_prov = df['Id'].tolist()
provincia_list = df['Nombre'].tolist()

# Lista de Partidos de la Provincia prov
for prov in range(len(id_list_prov)):
    url_partidos = "http://www.inmuebles.clarin.com/Regiones/FindPartidos?contentType=json&IdProvincia=" + str(id_list_prov[prov])
    headers = {"User-Agent":"Mozilla/5.0"}
    partidos_res = requests.get(url_partidos, headers=headers).text
    df_partidos = pd.read_json(url_partidos)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    id_list_partidos = df_partidos['Id'].tolist()
    partidos_list = df_partidos['Nombre'].tolist()

    # Hago una peticion por cada partido para extraer las localidades
    for part in range(len(id_list_partidos)):
        url_localidades = "http://www.inmuebles.clarin.com/Regiones/FindLocalidades?contentType=json&IdPartido=" + str(id_list_partidos[part])

        headers = {"User-Agent":"Mozilla/5.0"}
        respuesta_res = requests.get(url_localidades, headers=headers).text
        df_localidades = pd.read_json(url_localidades)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        id_list_localidades = df_localidades['Id'].tolist()
        localidades_list = df_localidades['Nombre'].tolist()

        # Por cada localidad hago un insert en el csv
        for loc in range(len(id_list_localidades)):
            fichero.append(
                str(id_list_prov[prov]) + ';' + 
                provincia_list[prov]  + ';' +  
                str(id_list_partidos[part]) + ';' + 
                partidos_list[part] + ';' +
                str(id_list_localidades[loc]) + ';' + 
                localidades_list[loc] + ';' +  
                '\n')

            print(str(id_list_prov[prov]) + ';' + 
                provincia_list[prov]  + ';' +  
                str(id_list_partidos[part]) + ';' + 
                partidos_list[part] + ';' +
                str(id_list_localidades[loc]) + ';' + 
                localidades_list[loc] + ';')    


       