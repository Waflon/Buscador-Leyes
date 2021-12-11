from dataclasses import dataclass
from Identificador import Identificador
from Metadato import Metadato

@dataclass
class Norma:
    idNorma: int
    identificador: Identificador
    metadato: Metadato
    encabezado: str
    textoPromulgacion: str
    listaTitulos: list
    listaAnexos: list

    def __init__(self, idNorma: int, identificador=None, metadato=None, encabezado=None, textoPromulgacion=None, listaTitulos=None, listaAnexos=None):
        self.idNorma = idNorma
        self.setIdentificador(identificador)
        self.setMetadato(metadato)
        self.setEncabezado(encabezado)
        self.setTextoPromulgacion(textoPromulgacion)
        self.setListaTitulos(listaTitulos)
        self.setListaAnexos(listaAnexos)

    def setIdentificador(self, identificador: Identificador):
        if identificador is None:
            self.identificador = Identificador()  # Identificador por defecto
        else:
            self.identificador = identificador

    def setMetadato(self, metadato: Metadato):
        if metadato is None:
            self.metadato = Metadato()
        else:
            self.metadato = metadato

    def setEncabezado(self, encabezado: str):
        if encabezado is None:
            self.encabezado = "Encabezado no encontrado"
        else:
            self.encabezado = encabezado

    def setTextoPromulgacion(self, textoPromulgacion: str):
        if textoPromulgacion is None:
            self.textoPromulgacion = "Promulgacion no encontrada"
        else:
            self.textoPromulgacion = textoPromulgacion

    def setListaTitulos(self, listaTitulos: str):
        if listaTitulos is None:
            self.listaTitulos = "Titulos no encontrados"
        else:
            self.listaTitulos = listaTitulos

    def setListaAnexos(self, listaAnexos: str):
        if listaAnexos is None:
            self.listaAnexos = []
        else:
            self.llistaAnexos = listaAnexos

    def getIdentificador(self):
        return self.identificador

    def getMetadato(self):
        return self.metadato

    def getEncabezado(self):
        return self.encabezado

    def getTextoPromulgacion(self):
        return self.textoPromulgacion

    def getListaTitulos(self):
        return self.listaTitulos

    def getListaAnexos(self):
        return self.listaAnexos