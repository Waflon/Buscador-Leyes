from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetadatosArticulo:
    nombreParte: str
    tituloParte: str
    materias = list
    fechaTratado: datetime
    fechaDerogacion: datetime
    def __init__(self, nombreParte=None, tituloParte=None, materias=None, fechaTratado=None, fechaDerogacion=None):
        self.setTituloNorma(nombreParte)
        self.setTituloParte(tituloParte)
        self.setMaterias(materias)
        self.setFechaTratado(fechaTratado)
        self.setFechaDerogacion(fechaDerogacion)

# SETTERS
    def setTituloNorma(self, materias: str) -> None:
        if materias is None:
            self.materias = "Título de norma no encontrado"
        else:
            self.materias = materias

    def setTituloParte(self, tituloParte: list) -> None:
        if tituloParte is None:
            self.tituloParte = "Título Parte no encontrado"
        else:
            self.tituloParte = tituloParte

    def setMaterias(self, materias: list) -> None:
        if materias is None:
            self.materias = []
        else:
            self.materias = materias

    def setFechaTratado(self, fechaTratado: datetime) -> None:
        if fechaTratado is None:
            self.fechaTratado = datetime(1800,1,1)  # Por defecto para errores
        else:
            self.fechaTratado = fechaTratado

    def setFechaDerogacion(self, fechaDerogacion: datetime) -> None:
        if fechaDerogacion is None:
            self.fechaDerogacion = datetime(1800,1,1)  # Por defecto para errores
        else:
            self.fechaDerogacion = fechaDerogacion

# GETTERS
    def getTituloNrma(self) -> str:
        return self.tituloNorma

    def getTituloParte(self) -> str:
        return self.tituloParte

    def getMaterias(self) -> list:
        return self.materias

    def getFechaTratado(self) -> datetime:
        return self.fechaTratado

    def getFechaDerogacion(self) -> datetime:
        return self.fechaDerogacion
