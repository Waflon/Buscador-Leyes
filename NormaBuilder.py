from TipoNumero import TipoNumero
from Anexo import *
from Titulo import *
from Norma import *
from bs4 import BeautifulSoup
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

    def setIdentificador(self, xml_parser: BeautifulSoup) -> Identificador:
        try:
            dictIdentificador = getDictIdentificador(xml_parser)
            jsonIdentificador = getJson(dictIdentificador)  # Importante 1/4
            return Identificador(jsonIdentificador['TipoNumero'], jsonIdentificador['Organismos'], jsonIdentificador['FechaPublicacion'], jsonIdentificador['FechaPromulgacion'])
        except:
            return Identificador()
            
    def setMetadatoNorma(self, xml_parser: BeautifulSoup) -> MetadatoNorma:
        try:
            dictMetadatoNorma = getDictMetadatoNorma(xml_parser)
            jsonMetadatoNorma = getJson(dictMetadatoNorma)    
            return MetadatoNorma(jsonMetadatoNorma['Titulo'], jsonMetadatoNorma['Materias'], jsonMetadatoNorma['IdentificacionFuente'], jsonMetadatoNorma['NumeroFuente'])
        except:
            return MetadatoNorma()

    def setEncabezado(self, xml_parser: BeautifulSoup) -> Encabezado:
        try:
            dictEncabezado = getDictEncabezado(xml_parser)
            jsonEncabezado = getJson(dictEncabezado)
            return Encabezado(jsonEncabezado['Texto'], jsonEncabezado['FechaVersion'], jsonEncabezado['Derogado'])
        except:
            return Encabezado()

    def setAnexo(self, xml_parser: BeautifulSoup) -> list:
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
            return Promulgacion()

    def setAtributos(self, xml_parser: BeautifulSoup) -> AtributosNorma:
        try:
            dictAtributos = getDictAtributosNorma(xml_parser)
            jsonAtributos = getJson(dictAtributos)
            return AtributosNorma(jsonAtributos['SchemaVersion'], jsonAtributos['NormaId'], jsonAtributos['FechaVersion'], jsonAtributos['Derogado'], jsonAtributos['EsTratado'])
        except:
            return AtributosNorma()
            
    def crearNormaConLey(self, idLey: str) -> Norma:
        xml_parser = soupConsultarLey(idLey)
        identificador = self.setIdentificador(xml_parser) # Identificado
        metadato = self.setMetadatoNorma(xml_parser) # Metadato
        listaAnexos = self.setListaAnexos(xml_parser)  # Anexo
        promulgacion = self.setPromulgacion(xml_parser)  # Promulgacion 
        atributos = self.setAtributos(xml_parser)  # Atributos
        encabezado = self.setEncabezado(xml_parser)
        return Norma(identificador, metadato, encabezado, promulgacion, [], [listaAnexos], "binarios", atributos)

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

def getJson(dictionary: dict) -> json:  # Retorna un json con el diccionario enviado
    return json.loads(json.dumps(dictionary, indent=4, default=str))  # Con dumps transforma a json y con loads retorna un json

def getTipoNumero(xml_parser: BeautifulSoup) -> TipoNumero:
    dictTipoNumero = getDictTipoNumero(xml_parser)
    jsonTipoNumero = getJson(dictTipoNumero)
    try:
        return TipoNumero(jsonTipoNumero['Tipo'], jsonTipoNumero['Numero'])  # objeto que contiene la instanciaTipoNumeros
    except:
        return TipoNumero()

def getOrganismos(identificador_parser: BeautifulSoup) -> list:
    organismos = []
    organismos_parser = identificador_parser.Organismos
    for organismo_parser in organismos_parser:
        if organismo_parser != "\n":
            organismos.append(organismo_parser.contents[0])
    return organismos

# Get Dictionaries
def getDictTipoNumero(xml_parser: BeautifulSoup) -> dict:  
    TipoNumero = {
        'Tipo': CrearTipoLey(xml_parser),  # Retorna un string para dato Tipo
        'Numero': CrearNumeroLey(xml_parser)  # Retorna un integer para dato Numero
    }
    return TipoNumero  

def getDictIdentificador(xml_parser: BeautifulSoup) -> dict:
    identificador_parser = xml_parser.find('Identificador')
    #TipoLey
    tipoNumero = getDictTipoNumero(xml_parser)  # Primeros datos para primer objeto (TipoNumero)
    organismos = getOrganismos(identificador_parser)
    fechaPublicacion = datetime.strptime(xml_parser.Identificador['fechaPublicacion'], '%Y-%m-%d')
    fechaPromulgacion = datetime.strptime(xml_parser.Identificador['fechaPromulgacion'], '%Y-%m-%d')

    identificador = {
        'TipoNumero' : tipoNumero,
        'Organismos' : organismos,
        'FechaPublicacion' : fechaPublicacion,
        'FechaPromulgacion': fechaPromulgacion}
    return identificador

def getDictMetadatoNorma(xml_parser: BeautifulSoup) -> dict:
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
    listaAnexos = []
    for anexo in anexos_parser:
        listaAnexos.append(anexo)
    metadatoAnexo = getDictMetadatoAnexo(anexos_parser)
    # listaAnexos = anexos_parser.Anexo
    fechaVersionAnexo = anexos_parser.find("Anexo")['fechaVersion']
    fechaVersion = datetime.strptime(fechaVersionAnexo, '%Y-%m-%d')
    anexo = {
        'FechaVersion' : fechaVersion,
        'MetadatoAnexo' : metadatoAnexo
    }
    return anexo

def getDictMetadatoAnexo(self, anexos_parser: BeautifulSoup) -> dict:
    tituloAnexo = anexos_parser.Anexo.Titulo.contents[0]
    textoAnexo = anexos_parser.Anexo.Texto.contents[0]
    metadatoAnexo ={
        'tituloAnexo' : tituloAnexo,
        'textoAnexo'  : textoAnexo
    }
    return metadatoAnexo

def getDictPromulgacion (xml_parser: BeautifulSoup) -> dict:
    texto = xml_parser.Promulgacion.Texto.contents[0]
    fechaVersion = datetime.strptime(xml_parser.Promulgacion['fechaVersion'], '%Y-%m-%d')
    derogado = xml_parser.Promulgacion['derogado']
    promulgacion = {
        'Texto' : texto,
        'FechaVersion' : fechaVersion,
        'Derogado' : derogado
    }
    return promulgacion

def getDictAtributosNorma(xml_parser: BeautifulSoup) -> dict:
    schemaVersion = xml_parser.Norma['SchemaVersion']
    normaId = xml_parser.Norma['normaId']
    fechaVersion = datetime.strptime(xml_parser.Norma['fechaVersion'], '%Y-%m-%d')
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

def getDictEncabezado(xml_parser: BeautifulSoup) -> dict:
    texto = xml_parser.Encabezado.Texto.contents[0]
    fechaVersion = datetime.strptime(xml_parser.Encabezado['fechaVersion'], '%Y-%m-%d')
    derogado = xml_parser.Encabezado['derogado']
    encabezado = {
        'Texto' : texto,
        'FechaVersion' : fechaVersion,
        'Derogado' : derogado
    }
    return encabezado

def getDictAtributosAnexo(xml_parser: BeautifulSoup) -> dict:
    idParte: str
    fechaVersion: datetime
    derogado: str
    transitorio: str