import requests
import pandas as pd
import json

url = "http://www.inmuebles.clarin.com/Regiones/FindProvincias?contentType=json&idPais=1"

headers = {"User-Agent":"Mozilla/5.0"}
respuesta_res = requests.get(url, headers=headers).text

# Creo archivo
archivo = 'json/provincias/provincias.json'
fichero = open(archivo, 'wt')
fichero.write(respuesta_res)
fichero.close()

