from dataclasses import dataclass
from Identificador import Identificador

@dataclass
class Norma:
    idNorma: int
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
=======
>>>>>>> Stashed changes
    identificador: Identificador
    encabezado: str
    textoPromulgación: str
    listaTitulos: list

    def __init__(self, idNorma: int):
        self.idNorma = idNorma
<<<<<<< Updated upstream
        identificador = Identificador()
>>>>>>> Stashed changes
=======
        identificador = Identificador()
>>>>>>> Stashed changes
