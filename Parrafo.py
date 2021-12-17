from Articulo import *


@dataclass
class Parrafo:
    numeroParrafo: str
    textoParrafo: str
    listaArticulos: list

    def __init__(self, numeroParrafo=None, textoParrafo=None,  listaArticulos=None) -> None:
        self.setNumeroParrafo(numeroParrafo)
        self.setTextoParrafo(textoParrafo)
        self.listaArticulos = []
        self.setListaArticulos(listaArticulos)


    def setNumeroParrafo(self, numeroParrafo: str) -> None:
        if numeroParrafo is None:
            self.numeroParrafo = "0" # Parrafo vacio por defecto
        else:
            self.numeroParrafo = numeroParrafo

    def setTextoParrafo(self, textoParrafo: str) -> None:
        if textoParrafo is None:
            self.textoParrafo = "Texto del párrafo no encontrado"
        else:
            self.textoParrafo = textoParrafo

    def setListaArticulos(self, listaArticulos: list) -> None:
        if listaArticulos is None:
            self.listaArticulos = []
        else:
            self.listaArticulos = listaArticulos
 
    def getNumeroParrafo(cls) -> str:
        return cls.numeroParrafo

    def getTextoParrafo(self) -> str:
        return self.textoParrafo

    def getListaArticulos(cls) -> list:
        return cls.listaArticulos

    def agregarArticulo(self, articulo: Articulo) -> None:
        self.listaArticulos.append(articulo)