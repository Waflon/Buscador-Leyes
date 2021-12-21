from TipoNumero import TipoNumero
from Anexo import *
from Titulo import *
from Norma import *
from bs4 import BeautifulSoup
import requests
import json

def getJson(dictionary: dict) -> json:  # Retorna un json con el diccionario enviado
    return json.loads(json.dumps(dictionary, indent=4, default=str))  # Con dumps transforma a json y con loads retorna un json

'''------------------------SETTERS---------------------------------'''

def setIdentificador(xml_parser: BeautifulSoup) -> Identificador:
    try:
        dictIdentificador = getDictIdentificador(xml_parser)
        jsonIdentificador = getJson(dictIdentificador)  # Importante 1/4
        return Identificador(jsonIdentificador['TipoNumero'], jsonIdentificador['Organismos'], jsonIdentificador['FechaPublicacion'], jsonIdentificador['FechaPromulgacion'])
    except:
        return Identificador()
        
def setMetadatoNorma(xml_parser: BeautifulSoup) -> MetadatoNorma:
    try:
        dictMetadatoNorma = getDictMetadatoNorma(xml_parser)
        jsonMetadatoNorma = getJson(dictMetadatoNorma)    
        return MetadatoNorma(jsonMetadatoNorma['Titulo'], jsonMetadatoNorma['Materias'], jsonMetadatoNorma['IdentificacionFuente'], jsonMetadatoNorma['NumeroFuente'])
    except:
        return MetadatoNorma()

def setEncabezado(xml_parser: BeautifulSoup) -> Encabezado:
    try:
        dictEncabezado = getDictEncabezado(xml_parser)
        jsonEncabezado = getJson(dictEncabezado)
        return Encabezado(jsonEncabezado['Texto'], jsonEncabezado['FechaVersion'], jsonEncabezado['Derogado'])
    except:
        return Encabezado()

def setListaAnexos(xml_parser: BeautifulSoup) -> list:
    try:
        dictAnexo = getDictAnexos(xml_parser)
        jsonAnexo = getJson(dictAnexo)
        return [Anexo(jsonAnexo['Texto'], jsonAnexo['MetadatoAnexo'],jsonAnexo['IdParte'], jsonAnexo['FechaVersion'], jsonAnexo['Derogado'], jsonAnexo['Transitorio'] )]
    except:
        return [Anexo()]

def setPromulgacion(xml_parser: BeautifulSoup) ->Promulgacion:
    try:
        dictPromulgacion = getDictPromulgacion(xml_parser)
        jsonPromulgacion = getJson(dictPromulgacion)
        return Promulgacion(jsonPromulgacion['Texto'], jsonPromulgacion['FechaVersion'], jsonPromulgacion['Derogado'])
    except:
        return Promulgacion()

def setAtributos(xml_parser: BeautifulSoup) -> AtributosNorma:
    try:
        dictAtributos = getDictAtributosNorma(xml_parser)
        jsonAtributos = getJson(dictAtributos)
        return AtributosNorma(jsonAtributos['SchemaVersion'], jsonAtributos['NormaId'], jsonAtributos['FechaVersion'], jsonAtributos['Derogado'], jsonAtributos['EsTratado'])
    except:
        return AtributosNorma()

def soupConsultarLey(idLey: str) -> BeautifulSoup:
    try:
        url = 'http://www.leychile.cl/Consulta/obtxml?opt=7&idLey=' + str(idLey)
        xml_data = requests.get(url).content  # Conseguir el contenido en xml
        print(f"Solicitud exitosa para ley: {str(idLey)}")
        return BeautifulSoup(xml_data, "xml")  # objeto que contiene la sopita
    except:
        return None

'''----------------------IDENTIFICADOR-------------------------------'''

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

'''--------------------------ANEXOS---------------------------------'''

def getDictAnexos(xml_parser: BeautifulSoup) -> dict:
    try:
        texto = xml_parser.Anexos.Anexo.Texto.contents[0]
    except:
        texto = None
    try:
        idParte = xml_parser.Anexos.Anexo['idParte']
    except:
        idParte = None
    try:
        fechaVersion = datetime.strptime(xml_parser.Anexo['fechaVersion'], '%Y-%m-%d')
    except:
        fechaVersion = None
    try:
        derogado = xml_parser.Anexos.Anexo['derogado']
    except:
        derogado = None
    try:
        transitorio = xml_parser.Anexos.Anexo['transitorio']
    except:
        transitorio = None
    metadatoAnexo = getDictMetadatoAnexo(xml_parser)
    anexo = {
        'Texto' : texto,
        'MetadatoAnexo' : metadatoAnexo,
        'IdParte' : idParte,
        'FechaVersion' : fechaVersion,
        'Derogado' : derogado,
        'Transitorio' : transitorio
    }
    return anexo

def getDictMetadatoAnexo(xml_parser: BeautifulSoup) -> dict:
    #Titulo Anexo
    try:
        tituloAnexo = xml_parser.Anexo.Titulo.contents[0]
    except:
        tituloAnexo = ""
    #Lista Materias
    try:
        listaMaterias = []
        materias_parser = xml_parser.Anexo.Materias
        for materia in materias_parser:
            if materia != "\n":
                listaMaterias.append(materia.contents[0])
    except:
        listaMaterias = []
    #Fecha Derogacion
    try:
        fechaDerogacion = datetime.strptime(xml_parser.Anexo['fechaDerogacion'], '%Y-%m-%d')
    except:
        fechaDerogacion = datetime(1800,1,1)
    
    metadatoAnexo ={
        'tituloAnexo' : tituloAnexo,
        'Materias'  : listaMaterias,
        'fechaDerogacion' : fechaDerogacion
    }
    return metadatoAnexo

'''------------------------ENCABEZADO---------------------------------'''

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

'''------------------------ORGANISMOS---------------------------------'''

def getOrganismos(identificador_parser: BeautifulSoup) -> list:
    organismos = []
    organismos_parser = identificador_parser.Organismos
    for organismo_parser in organismos_parser:
        if organismo_parser != "\n":
            organismos.append(organismo_parser.contents[0])
    return organismos


'''------------------------METADATOS---------------------------------'''

def getDictMetadatoNorma(xml_parser: BeautifulSoup) -> dict:
    metadatos_parser = xml_parser.Metadatos
    tituloNorma = metadatos_parser.TituloNorma.contents[0]
    try:
        materias = []
        listaMaterias = metadatos_parser.Materias
        for materia in listaMaterias:
            if materia != "\n":
                materias.append(materia.contents[0])
    except:
        materias = None

    identificacionFuente = xml_parser.find('IdentificacionFuente').contents[0]
    numeroFuente = xml_parser.find('NumeroFuente').contents[0]
    metadato = {
        'Titulo' : tituloNorma,
        'Materias' : materias,
        'IdentificacionFuente' : identificacionFuente,
        'NumeroFuente' : numeroFuente
    }
    return metadato

'''----------------------PROMULGACION---------------------------------'''
# TODO: Individualizar los Try/Except
def getDictPromulgacion (xml_parser: BeautifulSoup) -> dict:
    try:
        texto = xml_parser.Promulgacion.Texto.contents[0]
        fechaVersion = datetime.strptime(xml_parser.Promulgacion['fechaVersion'], '%Y-%m-%d')
        derogado = xml_parser.Promulgacion['derogado']
    except:
        texto = None
        fechaVersion = None
        derogado = None

    promulgacion = {
        'Texto' : texto,
        'FechaVersion' : fechaVersion,
        'Derogado' : derogado
    }
    return promulgacion

'''------------------------ATRIBUTOS---------------------------------'''
# TODO: Individualizar los Try/Except
def getDictAtributosNorma(xml_parser: BeautifulSoup) -> dict:
    try:
        schemaVersion = xml_parser.Norma['SchemaVersion']
        normaId = xml_parser.Norma['normaId']
        fechaVersion = datetime.strptime(xml_parser.Norma['fechaVersion'], '%Y-%m-%d')
        derogado = xml_parser.Norma['derogado']
        esTratado = xml_parser.Norma['esTratado']
    except:
        schemaVersion = None
        normaId = None
        fechaVersion = None
        derogado = None
        esTratado = None

    atributos = {
        'SchemaVersion' : schemaVersion,
        'NormaId' : normaId,
        'FechaVersion' : fechaVersion,
        'Derogado' : derogado,
        'EsTratado' : esTratado
    }
    return atributos
