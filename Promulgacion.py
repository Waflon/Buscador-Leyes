from dataclasses import dataclass
from datetime import datetime


@dataclass
class Promulgacion:
    texto: str
    fechaVersion: datetime
    derogado: str

    def __init__(self, texto=None, fechaVersion=None, derogado=None) -> None:
        self.setTexto(texto)
        self.setFechaVersion(fechaVersion)
        self.setDerogado(derogado)

    def setTexto(self, texto: str) -> None:
        if texto is None:
            self.texto = ""
        else:
            self.texto = texto

    def setFechaVersion(self, setFechaVersion: str) -> None:
        if setFechaVersion is None:
            self.fechaVersion = datetime(1800,1,1)
        else:
            self.fechaVersion = setFechaVersion

    def setDerogado(self, derogado: str) -> None:
        if derogado is None:
            self.derogado = ""
        else:
            self.derogado = derogado

    def getTexto(self):
        return self.texto

    def getFechaVersion(self) -> datetime:
        return self.fechaVersion

    def getDerogado(self) -> str:
        return self.derogado