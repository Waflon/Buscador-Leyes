from dataclasses import dataclass
from MetadatosArticulo import MetadatosArticulo

@dataclass
class Articulo:
    textoArticulo: str
    numeroArticulo: int
    metadatosArticulo: MetadatosArticulo
    idParte: int  #Elemento unico usado por la BCN en sus servicios

    def __init__(self, numeroArticulo=None, textoArticulo=None, metadatosArticulo=None) -> None:
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

    def setMetadatosArticulo(self, metadatosArticulo: MetadatosArticulo) -> None:
        if metadatosArticulo is None:
          self.metadatosArticulo = MetadatosArticulo()
        else:
          self.metadatosArticulo = metadatosArticulo

    def getIdLey(self) -> int:
      return self.idLey

    def getNumeroArticulo(self) -> int:
      return self.numeroArticulo

    def getTextoArticulo(self) -> str:
      return self.textoArticulo

    def getMetadatosArticulo(self) -> MetadatosArticulo:
      return self.metadatosArticulo