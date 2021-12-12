from dataclasses import dataclass


@dataclass
class Metadato:
    tituloNorma: str
    materias: list
    identificacionFuente: str  # ejemplo: Diario oficial
    numeroFuente: int

    def __init__(self, tituloNorma=None, materias=None, identificacionFuente=None, numeroFuente=None):
        self.setTituloNorma(tituloNorma)
        self.setMaterias(materias)
        self.setIdentificacionFuente(identificacionFuente)
        self.setNumeroFuente(numeroFuente)

    def setTituloNorma(self, tituloNorma: str) -> None:
        if tituloNorma is None:
            self.tituloNorma = "Titulo Vacio"
        else:
            self.tituloNorma = tituloNorma

    def setMaterias(self, materias: list) -> None:
        if materias is None:
            self.materias = []
        else:
            self.materias = materias

    def setIdentificacionFuente(self, identificacionFuente: str) -> None:
        if identificacionFuente is None:
            self.identificacionFuente = "Identificación Fuente no encontrada"
        else:
            self.identificacionFuente = identificacionFuente

    def setNumeroFuente(self, numeroFuente: int) -> None:
        if numeroFuente is None:
            self.numeroFuente = "Número no encontrado"
        else:
            self.numeroFuente =  numeroFuente

    def getTituloNorma(self) -> str:
        return self.tituloNorma

    def getMaterias(self) -> str:
        return self.tituloNorma

    def getIdentificacionFuente(self) -> str:
        return self.identificacionFuente

    def getNumeroFuente(self) -> int:
        return  self.numeroFuente