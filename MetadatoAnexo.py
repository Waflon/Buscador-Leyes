from dataclasses import dataclass


@dataclass
class MetadatoAnexo:
    tituloAnexo: str
    materias: list
    textoAnexo: str

    def __init__(self, tituloAnexo=None, materias=None, textoAnexo=None):
        self.setTituloAnexo(tituloAnexo)
        self.setMaterias(materias)
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

    def setMaterias(self, materias: list) -> None:
        if materias is None:
            self.materias = []
        else:
            self.materias = materias

    def getTituloAnexo(self) -> str:
        return self.tituloAnexo

    def getTextoAnexo(self) -> str:
        return self.textoAnexo