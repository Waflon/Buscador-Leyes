from dataclasses import dataclass


@dataclass
class MetadatoAnexo:
    tituloAnexo: str
    textoAnexo: str

    def __init__(self, tituloAnexo=None, textoAnexo=None):
        self.setTituloAnexo(tituloAnexo)
        self.setTextoAnexo(textoAnexo)

    def setTituloAnexo(self, tituloAnexo: str) -> None:
        if tituloAnexo is None:
            self.tituloAnexo = "Título de anexo no encontrado"
        else:
            self.tituloAnexo = tituloAnexo

    def setTextoAnexo(self, textoAnexo: str) -> None:
        if textoAnexo is None:
            self.textoAnexo = "Contenido de anexo no encontrado"
        else:
            self.textoAnexo = textoAnexo

    def getTituloAnexo(self) -> str:
        return self.tituloAnexo

    def getTextoAnexo(self) -> str:
        return self.textoAnexo