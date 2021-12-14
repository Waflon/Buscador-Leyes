from dataclasses import dataclass
from MetadatosArticulo import MetadatosArticulo

@dataclass
class Articulo:
    textoArticulo: str
    metadatosArticulo: MetadatosArticulo
    idParte: int  #Elemento unico usado por la BCN en sus servicios

    def __init__(self, textoArticulo=None, metadatosArticulo=None, idParte=None) -> None:
        self.setTextoArticulo(textoArticulo)
        self.setMetadatosArticulo(metadatosArticulo)
        self.setIdParte(idParte)

    def setIdParte(self, idParte: int) -> None:
        if idParte is None:
          self.idParte = 0  # Defecto para error en número de artículo
        else:
          self.idParte = idParte

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

    def getIdParte(self) -> int:
      return self.idParte

    def getTextoArticulo(self) -> str:
      return self.textoArticulo

    def getMetadatosArticulo(self) -> MetadatosArticulo:
      return self.metadatosArticulo