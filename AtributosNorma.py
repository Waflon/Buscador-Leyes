from dataclasses import dataclass
from datetime import datetime


@dataclass
class AtributosNorma:
    schemaVersion: str
    normaId: str
    fechaVersion: datetime
    derogado: str
    esTratado: str