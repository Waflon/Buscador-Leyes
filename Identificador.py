from dataclasses import dataclass
from TipoNumero import TipoNumero
from datetime import datetime


@dataclass
class Identificador:
    tipoNumero: TipoNumero
    organismos: list
    fechaPublicacion: datetime
    fechaPromulgacion: datetime

    def __init__(self, tipoNumero=TipoNumero, organismos=None, fechaPublicacion=None, fechaPromulgacion=None):
        # Validación de datos
        self.tipoNumero = tipoNumero
        self.setOrganismos(organismos)
        self.setFechaPublicacion(fechaPublicacion)
        self.setFechaPromulgacion(fechaPromulgacion)


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


    def getTipoNumero(self):
        return self.tipoNumero

    def getOrganismos(self):
        return self.organismos

    def getFechaPublicacion(self):
        return self.fechaPublicacion

    def getFechaPromulgacion(self):
        return self.fechaPromulgacion
