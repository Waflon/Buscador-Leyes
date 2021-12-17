from Parrafo import *

@dataclass
class Titulo:
    numeroTitulo: str
    nombreTitulo: str
    listaParrafos: list

    def __init__(self, numeroTitulo=None, nombreTitulo=None, listaParrafos=None) -> None:
        self.setNombreTitulo(nombreTitulo)
        self.setNumeroTitulo(numeroTitulo)
        self.listaParrafos = []
        self.setListaParrafos(listaParrafos)

    def setNumeroTitulo(self, numeroTitulo: str) -> None:
        if numeroTitulo is None:
            self.numeroTitulo = "Sin Número"
        else:
            self.numeroTitulo = numeroTitulo

    def setNombreTitulo(self, nombreTitulo: str) -> None:
        if nombreTitulo is None:
            self.nombreTitulo = "Sin Título"
        else:
            self.nombreTitulo = nombreTitulo

    def setListaParrafos(self, listaParrafos: list) -> None:
        if listaParrafos is None:
            self.listaParrafos = []
        else:
            self.listaParrafos = listaParrafos

    def getNumeroTitulo(self) -> str:
        return self.numeroTitulo

    def getNombreTitulo(self) -> str:
        return self.nombreTitulo

    def getListaParrafos(self) -> list:
        return self.listaParaffos

    def agregarParrafo(self, parrafo: Parrafo) -> None:
        self.listaParrafos.append(parrafo)