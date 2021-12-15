from dataclasses import dataclass
from AtributosAnexo import AtributosAnexo
from Identificador import Identificador
from MetadatoAnexo import MetadatoAnexo
from Promulgacion import Promulgacion
from AtributosNorma import AtributosNorma
from TipoNumero import TipoNumero
from Metadato import Metadato
from Titulo import Titulo
from Anexo import Anexo
from Norma import Norma
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import json


def soupConsultarLey(idLey: str) -> BeautifulSoup:
    try:
        url = 'http://www.leychile.cl/Consulta/obtxml?opt=7&idLey=' + str(idLey)
        xml_data = requests.get(url).content  # Conseguir el contenido en xml
        print(f"Solicitud exitosa para ley: {str(idLey)}")
        return BeautifulSoup(xml_data, "xml")  # objeto que contiene la sopita
    except:
        return None

@dataclass
class NormaBuilder:
    idLey: str
    norma: Norma
    def __init__(self, idLey=None) -> None:
        self.setIdLey(idLey)
        self.norma = self.crearNormaConLey(idLey)

    def setIdLey(self, idLey: str):
        if idLey is None:
            self.idLey = "Ley Vacia"
        else:
            self.idLey = idLey

    def getIdLey(self):
        return self.idLey

    def setIdentificador(self, xml_parser: BeautifulSoup) -> Identificador:
        dictIdentificador = getDictIdentificador(xml_parser)
        jsonIdentificador = getJson(dictIdentificador)  # Importante 1/4
        return Identificador(jsonIdentificador['TipoNumero'], jsonIdentificador['Organismos'], jsonIdentificador['FechaPublicacion'], jsonIdentificador['FechaPromulgacion'])

    def setMetadato(self, xml_parser: BeautifulSoup) -> Metadato:
        dictMetadato = getDictMetadato(xml_parser)
        jsonMetadato = getJson(dictMetadato)    
        return Metadato(jsonMetadato['Titulo'], jsonMetadato['Materias'], jsonMetadato['IdentificacionFuente'], jsonMetadato['NumeroFuente'])

    def setAnexo(self, xml_parser: BeautifulSoup) -> Anexo:
        try:
            dictAnexo = getDictAnexos(xml_parser)
            jsonAnexo = getJson(dictAnexo)
            return Anexo(jsonAnexo['FechaVersion'], jsonAnexo['MetadatoAnexo'] )
        except:
            return Anexo()

    def setPromulgacion(self, xml_parser: BeautifulSoup) ->Promulgacion:
        try:
            dictPromulgacion = getDictPromulgacion(xml_parser)
            jsonPromulgacion = getJson(dictPromulgacion)
            return Promulgacion(jsonPromulgacion['Texto'], jsonPromulgacion['FechaVersion'], jsonPromulgacion['Derogado'])
        except:
            return {}

    def setAtributos(self, xml_parser: BeautifulSoup) -> AtributosNorma:
        dictAtributos = getDictAtributos(xml_parser)
        jsonAtributos = getJson(dictAtributos)
        return AtributosNorma(jsonAtributos['SchemaVersion'], jsonAtributos['NormaId'], jsonAtributos['FechaVersion'], jsonAtributos['Derogado'], jsonAtributos['EsTratado'])

    def crearNormaConLey(self, idLey: str) -> Norma:
        idLey = 4808
        xml_parser = soupConsultarLey(idLey)
        identificador = self.setIdentificador(xml_parser) # Identificado
        metadato = self.setMetadato(xml_parser) # Metadato
        anexo = self.setAnexo(xml_parser)  # Anexo
        promulgacion = self.setPromulgacion(xml_parser)  # Promulgacion 
        atributos = self.setAtributos(xml_parser)  # Atributos
        print("---------------------Identificador--------------------------")

        print("   ------------------TipoNumero--------------------------   ")
        print(f"Norma tipo: {identificador.tipoNumero['Tipo']} \nNúmero: {identificador.tipoNumero['Numero']}")
        print("   ------------------------------------------------------   ")
        print(f"Organismos: \n{identificador.organismos}")
        print(f"Fecha publicacion: \n{identificador.fechaPublicacion}")
        print(f"Fecha promulgacion: \n{identificador.fechaPromulgacion}")
        print("------------------------------------------------------------")
        print(metadato.tituloNorma)
        print("------------------------------------------------------------")
        print(f"Anexo: \n{anexo.metadatoAnexo.tituloAnexo}")
        print("------------------------------------------------------------")
        print("Promulgacion: ")
        print(atributos)
        return Norma(identificador, metadato)

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


def getDictPromulgacion(xml_parser: BeautifulSoup) -> dict:
    promulgacion_parser = xml_parser.Promulgacion
    texto = xml_parser.Promulgacion.Texto.contents[0]
    fechaVersion = xml_parser.Promulgacion['fechaVersion']
    derogado = xml_parser.Promulgacion['derogado']
    promulgacion = {
        'Texto' : texto,
        'FechaVersion' : fechaVersion,
        'Derogado' : derogado
    }
    return promulgacion

def getDictAtributos(xml_parser: BeautifulSoup) -> dict:
    schemaVersion = xml_parser.Norma['SchemaVersion']
    normaId = xml_parser.Norma['normaId']
    fechaVersion = xml_parser.Norma['fechaVersion']
    derogado = xml_parser.Norma['derogado']
    esTratado = xml_parser.Norma['esTratado']
    atributos = {
        'SchemaVersion' : schemaVersion,
        'NormaId' : normaId,
        'FechaVersion' : fechaVersion,
        'Derogado' : derogado,
        'EsTratado' : esTratado
    }
    return atributos

# Actual Code
norma = NormaBuilder("20000")