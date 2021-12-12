from Identificador import Identificador
from TipoNumero import TipoNumero
from Metadato import Metadato
from Ley import soupConsultarLey
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json


ley = 20000
xml_parser = soupConsultarLey(ley)

try:
    tipoLey = xml_parser.find('Tipo').contents[0]
except:
    tipoLey = "vacio"

try:
    numeroLey = xml_parser.find('Numero').contents[0]
except:
    tipoLey = "vacio"

tipoNumero = {
    'Tipo': tipoLey,
    'Numero': numeroLey
}

# TipoNumero
try:
    jsonTipoNumero = json.loads(json.dumps(tipoNumero, indent=4))  # Con dumps transforma a json y con loads retorna un json
    instanciaTipoNumero = TipoNumero(jsonTipoNumero['Tipo'], jsonTipoNumero['Numero'])  # objeto que contiene la instanciaTipoNumeros
except:
    instanciaTipoNumero = TipoNumero()


print("------------------------------------------------------------")
print(f"Norma tipo: {jsonTipoNumero['Tipo']} \nNúmero: {jsonTipoNumero['Numero']}")
print("------------------------------------------------------------")

# Identificador
organismos = []
identificador_parser = xml_parser.find('Identificador')
organismos_parser = identificador_parser.Organismos
for organismo_parser in organismos_parser:
    if organismo_parser != "\n":
        organismos.append(organismo_parser.contents[0])

fechaPublicacion_parser = identificador_parser['fechaPublicacion']
fechaPublicacion = datetime.strptime(fechaPublicacion_parser, '%Y-%m-%d')

fechaPromulgacion_parser = identificador_parser['fechaPromulgacion']
fechaPromulgacion = datetime.strptime(fechaPromulgacion_parser, '%Y-%m-%d')

instanciaIdentificador = Identificador(instanciaTipoNumero, organismos, fechaPublicacion, fechaPromulgacion)
print(instanciaIdentificador)


# Metadato

metadatos_parser = xml_parser.Metadatos
tituloNorma = metadatos_parser.TituloNorma.contents[0]
materias = []
listaMaterias = metadatos_parser.Materias
for materia in listaMaterias:
    if materia != "\n":
        materias.append(materia.contents[0])
identificacionFuente = xml_parser.find('IdentificacionFuente').contents[0]
numeroFuente = xml_parser.find('NumeroFuente').contents[0]

instanciaMetadato = Metadato(tituloNorma, materias, identificacionFuente, numeroFuente)

print(instanciaMetadato)