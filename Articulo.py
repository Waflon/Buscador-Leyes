from MetadatoArticulo import *

@dataclass
class Articulo:
    textoArticulo: str
    metadatosArticulo: MetadatoArticulo
    idParte: str  #Elemento unico usado por la BCN en sus servicios

    def __init__(self, textoArticulo=None, metadatosArticulo=None, idParte=None) -> None:
        self.setTextoArticulo(textoArticulo)
        self.setMetadatosArticulo(metadatosArticulo)
        self.setIdParte(idParte)

    def setIdParte(self, idParte: int) -> None:
        if idParte is None:
          self.idParte = "0"  # Defecto para error en número de artículo
        else:
          self.idParte = idParte

    def setTextoArticulo(self, textoArticulo: str) -> None:
        if textoArticulo is None:
          self.textoArticulo = "Artículo sin texto"
        else:
          self.textoArticulo = textoArticulo

    def setMetadatosArticulo(self, metadatosArticulo: MetadatoArticulo) -> None:
        if metadatosArticulo is None:
          self.metadatosArticulo = MetadatoArticulo()
        else:
          self.metadatosArticulo = metadatosArticulo

    def getIdParte(self) -> str:
      return self.idParte

    def getTextoArticulo(self) -> str:
      return self.textoArticulo

    def getMetadatosArticulo(self) -> MetadatoArticulo:
      return self.metadatosArticulo