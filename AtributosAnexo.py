from dataclasses import dataclass
from datetime import datetime


@dataclass
class AtributosAnexo:
    idParte: str
    fechaVersion: datetime
    derogado: str
    transitorio: str