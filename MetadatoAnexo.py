from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetadatoAnexo:
    tituloAnexo: str
    materias: list
    fechaDerogacion: datetime

    def __init__(self, tituloAnexo=None, materias=None, fechaDerogacion=None):
        self.setTituloAnexo(tituloAnexo)
        self.setMaterias(materias)
        self.setFechaDerogacion(fechaDerogacion)

    def setTituloAnexo(self, tituloAnexo: str) -> None:
        if tituloAnexo is None:
            self.tituloAnexo = "Título de anexo no encontrado"
        else:
            self.tituloAnexo = tituloAnexo

    def setFechaDerogacion(self, fechaDerogacion: datetime) -> None:
        if fechaDerogacion is None:
            self.fechaDerogacion = datetime(1800, 1, 1)
        else:
            self.fechaDerogacion = fechaDerogacion

    def setMaterias(self, materias: list) -> None:
        if materias is None:
            self.materias = []
        else:
            self.materias = materias

    def getTituloAnexo(self) -> str:
        return self.tituloAnexo

    def setFechaDerogacion(self) -> datetime:
        return self.fechaDerogacion