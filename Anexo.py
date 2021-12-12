from dataclasses import dataclass
from MetadatoAnexo import MetadatoAnexo
from datetime import datetime


@dataclass
class Anexo:
    fechaVersion: datetime 
    metadatoAnexo: MetadatoAnexo

    def __init__(self, fechaVersion=None, metadatoAnexo=None):  # Inician vacios por si hay algún problema, puede iniciarse con o sin datos
        # Validación de datos
        self.setFechaVersion(fechaVersion)
        self.setMetadatoAnexo(metadatoAnexo)

    def setFechaVersion(self, fechaVersion: datetime):
        if fechaVersion is None:
            self.fechaVersion = "Fecha no encontrada"
        else:
            self.fechaVersion = fechaVersion

    def setMetadatoAnexo(self, metadatoAnexo: MetadatoAnexo):
        if metadatoAnexo is None:
            self.metadatoAnexo = MetadatoAnexo()
        else:
            self.metadatoAnexo = metadatoAnexo

    def getFechaVersion(self):
        return self.fechaVersion

    def getMetadatoAnexo(self):
        return self.metadatoAnexo