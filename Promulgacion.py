from dataclasses import dataclass
from datetime import datetime


@dataclass
class Promulgacion:
    texto: str
    fechaVersion: datetime
    derogacion: str