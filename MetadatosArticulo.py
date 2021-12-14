from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetadatosArticulo:
    nombreParte: str
    tituloParte: str
    materias = []
    fechaTratado: datetime
    fechaDerogacion: datetime