from Identificador import Identificador
from MetadatoAnexo import MetadatoAnexo
from TipoNumero import TipoNumero
from Metadato import Metadato
from Titulo import Titulo
from Anexo import Anexo
from Ley import soupConsultarLey
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json


def CrearTipoLey(xml_parser: BeautifulSoup) -> str:  # Retorna string para el Tipo de Ley
    try:
        return xml_parser.find('Tipo').contents[0]
    except:
        return "Ley"

def CrearNumeroLey(xml_parser: BeautifulSoup) -> int:  # Retorna un Integer para dato Numero
    try:
        return xml_parser.find('Numero').contents[0]
    except:
        return 0  # Por defecto cuando hay un problema

def getDictTipoNumero(xml_parser: BeautifulSoup) -> dict:  
    TipoNumero = {
        'Tipo': CrearTipoLey(xml_parser),  # Retorna un string para dato Tipo
        'Numero': CrearNumeroLey(xml_parser)  # Retorna un integer para dato Numero
    }
    return TipoNumero  

def getJson(dictionary: dict) -> json:  # Retorna un json con el diccionario enviado
    return json.loads(json.dumps(dictionary, indent=4, default=str))  # Con dumps transforma a json y con loads retorna un json

def CrearInstanciaTipoNumero(xml_parser: BeautifulSoup) -> TipoNumero:
    dictTipoNumero = getDictTipoNumero(xml_parser)
    jsonTipoNumero = getJson(dictTipoNumero)
    try:
        return TipoNumero(jsonTipoNumero['Tipo'], jsonTipoNumero['Numero'])  # objeto que contiene la instanciaTipoNumeros
    except:
        return TipoNumero()

def CrearOrganismos(identificador_parser: BeautifulSoup) -> list:
    organismos = []
    organismos_parser = identificador_parser.Organismos
    for organismo_parser in organismos_parser:
        if organismo_parser != "\n":
            organismos.append(organismo_parser.contents[0])
    return organismos

def CrearFechaPublicacion(identificador_parser: BeautifulSoup) -> datetime:
    fechaPublicacion_parser = identificador_parser['fechaPublicacion']
    return datetime.strptime(fechaPublicacion_parser, '%Y-%m-%d')

def CrearFechaPromulgacion(identificador_parser: BeautifulSoup) -> datetime:
    fechaPromulgacion_parser = identificador_parser['fechaPromulgacion']
    return datetime.strptime(fechaPromulgacion_parser, '%Y-%m-%d')

def getDictIdentificador(xml_parser: BeautifulSoup) -> dict:
    identificador_parser = xml_parser.find('Identificador')
    #TipoLey
    tipoNumero = getDictTipoNumero(xml_parser)  # Primeros datos para primer objeto (TipoNumero)
    organismos = CrearOrganismos(identificador_parser)
    fechaPublicacion = CrearFechaPublicacion(identificador_parser)
    fechaPromulgacion = CrearFechaPromulgacion(identificador_parser)

    identificador = {
        'TipoNumero' : tipoNumero,
        'Organismos' : organismos,
        'FechaPublicacion' : fechaPublicacion,
        'FechaPromulgacion': fechaPromulgacion}
    return identificador

def getDictMetadato(xml_parser: BeautifulSoup) -> dict:
    metadatos_parser = xml_parser.Metadatos
    tituloNorma = metadatos_parser.TituloNorma.contents[0]
    materias = []
    try:
        listaMaterias = metadatos_parser.Materias
        for materia in listaMaterias:
            if materia != "\n":
                materias.append(materia.contents[0])
    except:
        print("Materias no disponibles")

    identificacionFuente = xml_parser.find('IdentificacionFuente').contents[0]
    numeroFuente = xml_parser.find('NumeroFuente').contents[0]
    metadato = {
        'Titulo' : tituloNorma,
        'Materias' : materias,
        'IdentificacionFuente' : identificacionFuente,
        'NumeroFuente' : numeroFuente
    }
    return metadato

def getDictAnexos(xml_parser: BeautifulSoup) -> dict:
    anexos_parser = xml_parser.Anexos
    listaAnexos = anexos_parser.Anexo
    tituloAnexo = anexos_parser.Anexo.Titulo.contents[0]
    textoAnexo = anexos_parser.Anexo.Texto.contents[0]
    fechaVersionAnexo = anexos_parser.find("Anexo")['fechaVersion']
    fechaVersion = datetime.strptime(fechaVersionAnexo, '%Y-%m-%d')
    metadatoAnexo = MetadatoAnexo(tituloAnexo, textoAnexo)
    anexo = {
        'FechaVersion' : fechaVersion,
        'MetadatoAnexo' : {'Titulo' : tituloAnexo, 'Texto': textoAnexo}
    }
    return anexo

def imprimir() -> None:
    print("---------------------Identificador--------------------------")

    print("   ------------------TipoNumero--------------------------   ")
    print(f"Norma tipo: {jsonIdentificador['TipoNumero']['Tipo']} \nNúmero: {jsonIdentificador['TipoNumero']['Numero']}")
    print("   ------------------------------------------------------   ")
    print(f"Organismos: \n{instanciaIdentificador.organismos}")
    print(f"Fecha publicacion: \n{instanciaIdentificador.fechaPublicacion}")
    print(f"Fecha promulgacion: \n{instanciaIdentificador.fechaPromulgacion}")
    print("------------------------------------------------------------")
    # Metadato

    print(instanciaMetadato.tituloNorma)
    print("------------------------------------------------------------")
    

    #print(f"Anexo: \n{jsonAnexo['MetadatoAnexo']['Titulo']}")

    print("------------------------------------------------------------")



idLey = 4808
xml_parser = soupConsultarLey(idLey)

#Identificado
dictIdentificador = getDictIdentificador(xml_parser)
jsonIdentificador = getJson(dictIdentificador)  # Importante 1/4
instanciaIdentificador = Identificador(jsonIdentificador['TipoNumero'], jsonIdentificador['Organismos'], jsonIdentificador['FechaPublicacion'], jsonIdentificador['FechaPromulgacion'])
#Metadato

dictMetadato = getDictMetadato(xml_parser)
jsonMetadato = getJson(dictMetadato)    
instanciaMetadato = Metadato(jsonMetadato['Titulo'], jsonMetadato['Materias'], jsonMetadato['IdentificacionFuente'], jsonMetadato['NumeroFuente'])
'''
dictAnexo = getDictAnexos(xml_parser)
jsonAnexo = getJson(dictAnexo)
instanciaAnexo = Anexo(jsonAnexo['FechaVersion'], jsonAnexo['MetadatoAnexo'] )
'''
imprimir()
print(xml_parser.EstructurasFuncionales.EstructuraFuncional.find_all("Texto"))



