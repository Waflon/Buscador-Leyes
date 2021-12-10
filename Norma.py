from dataclasses import dataclass
from Identificador import Identificador

@dataclass
class Norma:
    idNorma: int
<<<<<<< Updated upstream
=======
    identificador: Identificador
    encabezado: str
    textoPromulgación: str
    listaTitulos: list

    def __init__(self, idNorma: int):
        self.idNorma = idNorma
        identificador = Identificador()
>>>>>>> Stashed changes
