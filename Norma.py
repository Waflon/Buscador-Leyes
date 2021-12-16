from dataclasses import dataclass
from Identificador import Identificador
from MetadatoNorma import MetadatoNorma
from Promulgacion import Promulgacion
from AtributosNorma import AtributosNorma
from Encabezado import Encabezado


@dataclass
class Norma:
    identificador: Identificador
    metadato: MetadatoNorma
    encabezado: Encabezado
    promulgacion: Promulgacion
    listaTitulos: list
    listaAnexos: list
    archivosBinarios : str
    atributos: AtributosNorma

    def __init__(self, identificador=None, metadato=None, encabezado=None, promulgacion=None, listaTitulos=None, listaAnexos=None, archivosBinarios=None, atributos=None) -> None:
        self.setIdentificador(identificador)
        self.setMetadato(metadato)
        self.setEncabezado(encabezado)
        self.setPromulgacion(promulgacion)
        self.setListaTitulos(listaTitulos)
        self.setListaAnexos(listaAnexos)
        self.setArchivosBinarios(archivosBinarios)
        self.setAtributos(atributos)

    def setIdentificador(self, identificador: Identificador) -> None:
        if identificador is None:
            self.identificador = Identificador()  # Identificador por defecto
        else:
            self.identificador = identificador

    def setMetadato(self, metadato: MetadatoNorma) -> None:
        if metadato is None:
            self.metadato = MetadatoNorma()
        else:
            self.metadato = metadato

    def setEncabezado(self, encabezado: Encabezado) -> None:
        if encabezado is None:
            self.encabezado = Encabezado()
        else:
            self.encabezado = encabezado

    def setPromulgacion(self, promulgacion: Promulgacion) -> None:
        if promulgacion is None:
            self.promulgacion = Promulgacion()
        else:
            self.promulgacion = promulgacion

    def setListaTitulos(self, listaTitulos: list) -> None:
        if listaTitulos is None:
            self.listaTitulos = "Titulos no encontrados"
        else:
            self.listaTitulos = listaTitulos

    def setListaAnexos(self, listaAnexos: list) -> None:
        if listaAnexos is None:
            self.listaAnexos = []
        else:
            self.listaAnexos = listaAnexos
       
    def setArchivosBinarios(self, archivosBinarios: str) ->None:
        if archivosBinarios is None:
            self.archivosBinarios = "Vacios"
        else:
            self.archivosBinarios = archivosBinarios

    def setAtributos(self, atributos: AtributosNorma) -> None:
        if atributos is None:
            self.atributos = {}
        else:
            self.atributos = atributos

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getMetadato(self) -> MetadatoNorma:
        return self.metadato

    def getEncabezado(self) -> str:
        return self.encabezado

    def getPromulgacion(self) -> Promulgacion:
        return self.promulgacion

    def getListaTitulos(self) -> list:
        return self.listaTitulos

    def getListaAnexos(self) -> list:
        return self.listaAnexos

    def getArchivosBinarios(self) -> str:
        return self.archivosBinarios

    def getAtributos(self) -> AtributosNorma:
        return self.atributos