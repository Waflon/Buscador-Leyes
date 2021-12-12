from dataclasses import dataclass


@dataclass
class TipoNumero:
    tipoNorma: str  # También conocido como tipoLey
    numeroNorma: int

    def __init__(self, tipoNorma=None, numeroNorma=None):  # Inician vacios por si hay algún problema, puede iniciarse con o sin datos
        # Validación de datos
        self.setNumeroNorma(numeroNorma)
        self.setTipoNorma(tipoNorma)

    def setTipoNorma(self, tipoNorma: str) -> None:
        if tipoNorma is None:
            self.tipoNorma = "Tipo de norma no encontrada"
        else:
            self.tipoNorma = str(tipoNorma)

    def setNumeroNorma(self, numeroNorma: int) -> None:
        if numeroNorma is None:
            self.numeroNorma = 0
        else:
            self.numeroNorma = int(numeroNorma)


    def getTipoNorma(self) -> str:
        return self.tipoNorma

    def getNumeroNorma(self) -> int:
        return self.numeroNorma