from dataclasses import dataclass
from MetadatoAnexo import MetadatoAnexo
from datetime import datetime
from AtributosAnexo import AtributosAnexo

@dataclass
class Anexo:
    fechaVersion: datetime 
    metadatoAnexo: MetadatoAnexo
    atributos: AtributosAnexo

    def __init__(self, fechaVersion=None, metadatoAnexo=None, atributos=None) -> None:  # Inician vacios por si hay algún problema, puede iniciarse con o sin datos
        # Validación de datos
        self.setFechaVersion(fechaVersion)
        self.setMetadatoAnexo(metadatoAnexo)
        self.setAtributos(atributos)

    def setFechaVersion(self, fechaVersion: datetime) -> None:
        if fechaVersion is None:
            self.fechaVersion = "Fecha no encontrada"
        else:
            self.fechaVersion = fechaVersion

    def setMetadatoAnexo(self, metadatoAnexo: MetadatoAnexo) -> None:
        if metadatoAnexo is None:
            self.metadatoAnexo = MetadatoAnexo()
        else:
            self.metadatoAnexo = metadatoAnexo

    def setAtributos(self, atributos: AtributosAnexo) -> None:
        if atributos is None:
            self.atributos = AtributosAnexo()
        else:
            self.atributos = atributos

    def getFechaVersion(self) -> datetime:
        return self.fechaVersion

    def getMetadatoAnexo(self) -> MetadatoAnexo:
        return self.metadatoAnexo

    def getAtributos(self) -> AtributosAnexo:
        return self.atributos