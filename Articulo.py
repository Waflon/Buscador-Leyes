from dataclasses import dataclass


@dataclass
class Articulo:
    idLey: int
    textoArticulo: str
    numeroArticulo: int

    def __init__(self, idLey: str, numeroArticulo=None, textoArticulo=None) -> None:
        self.idLey = int(idLey)
        self.setTextoArticulo(textoArticulo)
        self.setNumeroArticulo(numeroArticulo)

    def setNumeroArticulo(self, numeroArticulo: int) -> None:
        if numeroArticulo is None:
          self.numeroArticulo = 0  # Defecto para error en número de artículo
        else:
          self.numeroArticulo = numeroArticulo

    def setTextoArticulo(self, textoArticulo: str) -> None:
        if textoArticulo is None:
          self.textoArticulo = "Artículo sin texto"
        else:
          self.textoArticulo = textoArticulo

    def getIdLey(self) -> int:
      return self.idLey

    def getNumeroArticulo(self) -> int:
      return self.numeroArticulo

    def getTextoArticulo(self) -> str:
      return self.textoArticulo