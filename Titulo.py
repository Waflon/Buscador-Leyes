from dataclasses import dataclass
from Parrafo import Parrafo

@dataclass
class Titulo:
    nombreTitulo: str
    numeroTitulo: int
    listaParrafos: list

    def __init__(self, nombreTitulo=None, numeroTitulo=None, listaParrafos=None) -> None:
        self.setNombreTitulo(nombreTitulo)
        self.setNumeroTitulo(numeroTitulo)
        self.setListaParrafos(listaParrafos)

    def setNombreTitulo(self, nombreTitulo: str) -> None:
        if nombreTitulo is None:
            self.nombreTitulo = "Sin Título"
        else:
            self.nombreTitulo = nombreTitulo

    def setNumeroTitulo(self, numeroTitulo: int) -> None:
        if numeroTitulo is None:
            self.numeroTitulo = "Sin Número"
        else:
            self.numeroTitulo = numeroTitulo

    def setListaParrafos(self, listaParrafos: str) -> None:
        if listaParrafos is None:
            self.listaParrafos = []
        else:
            self.listaParrafos = listaParrafos

    def getNombreTitulo(self) -> str:
        return self.nombreTitulo

    def getNumeroTitulo(self) -> int:
        return self.numeroTitulo

    def getListaParrafos(self) -> list:
        return self.listaParaffos

    def agregarParrafo(self, parrafo: Parrafo) -> None:
        self.listaParrafos.append(parrafo)