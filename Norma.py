from dataclasses import dataclass
from Identificador import Identificador

@dataclass
class Norma:
    idNorma: int

    identificador: Identificador
    encabezado: str
    textoPromulgacion: str
    listaTitulos: list

    def __init__(self, idNorma: int, identificador=None, encabezado=None, textoPromulgacion=None, listaTitulos=None):
        self.idNorma = idNorma
        self.setIdentificador(identificador)
        self.setEncabezado(encabezado)
        self.setTextoPromulgacion(textoPromulgacion)
        self.setListaTitulos(listaTitulos)

    def setIdentificador(self, identificador: Identificador):
        if identificador is None:
            self.identificador = Identificador()  # Identificador por defecto