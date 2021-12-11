from dataclasses import dataclass


@dataclass
class Metadato:
    tituloNorma: str
    materias: list
    identificacionFuente: str  # ejemplo: Diario oficial
    numeroFuente: str

    def __init__(self, tituloNorma=None, materias=None, identificacionFuente=None, numeroFuente=None):
        self.setTituloNorma(tituloNorma)
        self.setMaterias(materias)
        self.setIdentificacionFuente()
        self.setNumeroFuente(numeroFuente)

    def setTituloNorma(self, tituloNorma: str):
        pass

    def setMaterias(self, materias: list):
        pass

    def setIdentificacionFuente(self, identificacionFuente: str):
        pass

    def setNumeroFuente(self, numeroFuente: str):
        pass

    def getTituloNorma(self):
        return self.tituloNorma

    def getMaterias(self):
        return self.tituloNorma

    def getIdentificacionFuente(self):
        return self.identificacionFuente

    def getNumeroFuente(self):
        return  self.numeroFuente