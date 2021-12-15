from dataclasses import dataclass
from datetime import datetime


@dataclass
class AtributosAnexo:
    idParte: str
    fechaVersion: datetime
    derogado: str
    transitorio: str

    def __init__(self, idParte=None, fechaVersion=None, derogado=None, transitorio=None) -> None:
        self.setIdParte(idParte)
        self.setFechaVerision(fechaVersion)
        self.setDerogado(derogado)
        self.setTransitorio(transitorio)

    def setIdParte(self, idParte: str) -> None:
        if idParte is None:
            self.idParte = 0  # Error por defecto
        else:
            self.idParte = idParte

    def setFechaVerision(self, fechaVersion: datetime) -> None:
        if fechaVersion is None:
            self.fechaVersion = datetime(1800,1,1)
        else:
            self.fechaVersion = fechaVersion

    def setDerogado(self, derogado: str) -> None:
        if derogado is None:
            self.derogado = "desconocido"
        else:
            self.derogado = derogado

    def setTransitorio(self, transitorio: str) -> None:
        if transitorio is None:
            self.transitorio = "desconocido"
        else:
            self.transitorio = transitorio

    def getIdParte(self) -> str:
        return self.idParte

    def getFechaVersion(self) -> datetime:
        return self.fechaVersion

    def getDerogado(self) -> str:
        return self.derogado

    def getTransitorio(self) -> str:
        return self.transitorio