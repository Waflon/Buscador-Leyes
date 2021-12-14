from dataclasses import dataclass
from datetime import datetime


@dataclass
class Encabezado:
    texto: str
    fechaVersion: datetime
    derogado: str