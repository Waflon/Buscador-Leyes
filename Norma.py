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
    listaArticulosTransitorios: list

    def __init__(self, idNorma: int, identificador=None, metadato=None, encabezado=None, textoPromulgacion=None, listaTitulos=None, listaAnexos=None, listaArticulosTransitorios=None) -> None:
        self.idNorma = idNorma
        self.setIdentificador(identificador)
        self.setMetadato(metadato)
        self.setEncabezado(encabezado)
        self.setTextoPromulgacion(textoPromulgacion)
        self.setListaTitulos(listaTitulos)
        self.setListaAnexos(listaAnexos)
        self.setListaArticulosTransitorios(listaArticulosTransitorios)

    def setIdentificador(self, identificador: Identificador) -> None:
        if identificador is None:
            self.identificador = Identificador()  # Identificador por defecto
        else:
            self.identificador = identificador

    def setMetadato(self, metadato: Metadato) -> None:
        if metadato is None:
            self.metadato = Metadato()
        else:
            self.metadato = metadato

    def setEncabezado(self, encabezado: str) -> None:
        if encabezado is None:
            self.encabezado = "Encabezado no encontrado"
        else:
            self.encabezado = encabezado

    def setTextoPromulgacion(self, textoPromulgacion: str) -> None:
        if textoPromulgacion is None:
            self.textoPromulgacion = "Promulgacion no encontrada"
        else:
            self.textoPromulgacion = textoPromulgacion

    def setListaTitulos(self, listaTitulos: list) -> None:
        if listaTitulos is None:
            self.listaTitulos = "Titulos no encontrados"
        else:
            self.listaTitulos = listaTitulos

    def setListaAnexos(self, listaAnexos: list) -> None:
        if listaAnexos is None:
            self.listaAnexos = []
        else:
            self.llistaAnexos = listaAnexos

    def setListaArticulosTransitorios(self, listaArticulosTransitorios: list) -> None:
        if listaArticulosTransitorios is None:
            self.listaArticulosTransitorios = []
        else:
            self.listaArticulosTransitorios = listaArticulosTransitorios            

    def getIdentificador(self) -> Identificador:
        return self.identificador

    def getMetadato(self) -> Metadato:
        return self.metadato

    def getEncabezado(self) -> str:
        return self.encabezado

    def getTextoPromulgacion(self) -> str:
        return self.textoPromulgacion

    def getListaTitulos(self) -> list:
        return self.listaTitulos

    def getListaAnexos(self) -> list:
        return self.listaAnexos
