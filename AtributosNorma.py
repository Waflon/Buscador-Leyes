from dataclasses import dataclass
from datetime import datetime


@dataclass
class AtributosNorma:
    schemaVersion: str
    normaId: str
    fechaVersion: datetime
    derogado: str
    esTratado: str


    def __init__(self, schemaVersion=None, normaId=None, fechaVersion=None, derogado=None, esTratado=None) -> None:
        self.setSchemaVerion(schemaVersion)
        self.setNormaId(normaId)
        self.setFechaVerision(fechaVersion)
        self.setDerogado(derogado)
        self.setEsTratado(esTratado)

    def setSchemaVerion(self, schemaVersion: str) -> None:
        if schemaVersion is None:
            self.schemaVersion = 0  # Error por defecto
        else:
            self.schemaVersion = schemaVersion

    def setNormaId(self, normaId: str) -> None:
        if normaId is None:
            self.normaId = ""  # Error por defecto
        else:
            self.normaId = normaId

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

    def setEsTratado(self, esTratado: str) -> None:
        if esTratado is None:
            self.esTratado = "desconocido"
        else:
            self.esTratado = esTratado

    def getSchemaVerion(self) -> str:
        return self.schemaVersion

    def getNormaId(self) -> str:
        return self.normaId

    def getFechaVersion(self) -> datetime:
        return self.fechaVersion

    def getDerogado(self) -> str:
        return self.derogado

    def getEsTratado(self) -> str:
        return self.esTratado