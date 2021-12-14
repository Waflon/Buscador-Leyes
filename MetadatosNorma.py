from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetadatosNorma:
    tituloNorma: str
    materias: list
    nombresUsoComun: list
    paisesTratados: list
    tipoTratado: str
    fechaTratado: datetime
    fechaDerogacion: datetime
    identificacionFuente: str
    numeroFuente: str