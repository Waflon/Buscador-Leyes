from dataclasses import dataclass


@dataclass
class TipoNumero:
    tipoNorma: str  # También conocido como tipoLey
    numeroNorma: int

    def __init__(self, tipoNorma: str, numeroNorma: int):
        # Validación de datos
        self.setNumeroNorma(numeroNorma)
        self.setTipoNorma(tipoNorma)

    def setTipoNorma(self, tipoNorma: str):
        if tipoNorma:
            self.tipoNorma = str(tipoNorma)
        else:
            self.tipoNorma = "Tipo de norma no encontrado"

    def setNumeroNorma(self, numeroNorma: int):
        if numeroNorma:
            self.numeroNorma = int(numeroNorma)
        else:
            self.numeroNorma = "Número de norma no encontrado"

    def getTipoNorma(self):
        return self.tipoNorma

    def getNumeroNorma(self):
        return self.numeroNorma

    def mostrarDatos(self):
        print(f"Norma de tipo: {self.tipoNorma}")
        print(f"Número de norma: {self.numeroNorma}")
