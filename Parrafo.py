from dataclasses import dataclass
from Articulo import Articulo


@dataclass
class Parrafo:
    numeroParrafo: int
    listaArticulos: list

    def __init__(self, numeroParrafo=None,  listaArticulos=None) -> None:
        self.setNumeroParrafo(numeroParrafo)
        self.setListaArticulos(listaArticulos)

    def setNumeroParrafo(self, numeroParrafo: int) -> None:
        if numeroParrafo is None:
            self.numeroParrafo = 0 # Parrafo vacio por defecto
        else:
            self.numeroParrafo = numeroParrafo

    def setListaArticulos(self, listaArticulos: list) -> None:
        if listaArticulos is None:
            self.listaArticulos = []
        else:
            self.listaArticulos = listaArticulos

    def getNumeroParrafo(self) -> int:
        return self.numeroParrafo

    def getListaArticulos(self) -> list:
        return self.listaArticulos

    def agregarArticulo(self, articulo: Articulo) -> None:
        self.listaArticulos.append(articulo)