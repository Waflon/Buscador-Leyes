from dataclasses import dataclass
from Articulo import Articulo


@dataclass
class Parrafo:
    numeroParrafo: int
    textoParrafo: str
    listaArticulos: list

    def __init__(self, numeroParrafo=None, textoParrafo=None,  listaArticulos=None) -> None:
        self.setNumeroParrafo(numeroParrafo)
        self.setTextoParrafo(textoParrafo)
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
    
    def setTextoParrafo(self, textoParrafo: str) -> None:
        if textoParrafo is None:
            self.textoParrafo = "Texto del párrafo no encontrado"
        else:
            self.textoParrafo = textoParrafo
 
    def getNumeroParrafo(self) -> int:
        return self.numeroParrafo

    def getListaArticulos(self) -> list:
        return self.listaArticulos

    def getTextoParrafo(self) -> str:
        return self.textoParrafo

    def agregarArticulo(self, articulo: Articulo) -> None:
        self.listaArticulos.append(articulo)