from dataclasses import dataclass
from TipoNumero import TipoNumero
from datetime import datetime


@dataclass
class Identificador:
    tipoNumero: TipoNumero
    organismos: list
    fechaPublicacion: datetime
    fechaPromulgacion: datetime

    def __init__(self, tipoNumero=None, organismos=None, fechaPublicacion=None, fechaPromulgacion=None):
        # Validación de datos
        self.setTipoNumero(tipoNumero)
        self.setOrganismos(organismos)
        self.setFechaPublicacion(fechaPublicacion)
        self.setFechaPromulgacion(fechaPromulgacion)

    def setTipoNumero(self, tipoNumero: TipoNumero):
        if tipoNumero is None:
            self.tipoNumero = TipoNumero(None, None)  # TipoNumero por defecto
        else:
            self.tipoNumero = tipoNumero

    def setOrganismos(self, organismos: list):
        if organismos is None:
            self.organismos = []
        else:
            self.organismos = organismos

    def setFechaPublicacion(self, fechaPublicacion: datetime):
        if fechaPublicacion is None:
            self.fechaPublicacion = datetime(1900,1,1) # Fecha por defecto por si se desconoce
        else:
            self.fechaPublicacion = fechaPublicacion

    def setFechaPromulgacion(self, fechaPromulgacion: datetime):
        if fechaPromulgacion is None:
            self.fechaPromulgacion = datetime(1900,1,1) # Fecha por defecto por si se desconoce
        else:
            self.fechaPromulgacion = fechaPromulgacion


    def getTipoNumero(self) -> str:
        return self.tipoNumero

    def getOrganismos(self) -> list:
        return self.organismos

    def getFechaPublicacion(self) -> datetime:
        return self.fechaPublicacion

    def getFechaPromulgacion(self) -> datetime:
        return self.fechaPromulgacion
