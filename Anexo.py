from MetadatoAnexo import *


@dataclass
class Anexo:
    texto: str
    metadatoAnexo: MetadatoAnexo
    idParte: str
    fechaVersion: datetime
    derogado: str
    transitorio: str

    def __init__(self, texto=None, metadatoAnexo=None, idParte=None, fechaVersion=None, derogado=None, transitorio=None):  # Inician vacios por si hay algún problema, puede iniciarse con o sin datos
        # Validación de datos
        self.setTexto(texto)
        self.setMetadatoAnexo(metadatoAnexo)
        self.setIdParte(idParte)
        self.setFechaVersion(fechaVersion)
        self.setDerogado(derogado)
        self.setTransitorio(transitorio)

    def setTexto(self, texto: str) -> None:
        if texto is None:
            self.texto = "Texto Anexo no encontrado"
        self.texto = texto

    def setMetadatoAnexo(self, metadatoAnexo: MetadatoAnexo) -> None:
        if metadatoAnexo is None:
            self.metadatoAnexo = MetadatoAnexo()
        else:
            self.metadatoAnexo = metadatoAnexo

    def setIdParte(self, idParte: str) -> None:
        if idParte is None:
            self.idParte = "0"  # Error por defecto
        else:
            self.idParte = idParte

    def setFechaVersion(self, fechaVersion: datetime) -> None:
        if fechaVersion is None:
            self.fechaVersion = datetime(1800,1,1)
        else:
            self.fechaVersion = fechaVersion

    def setDerogado(self, derogado: str) -> None:
        if derogado is None:
            self.derogado = "derogado: desconocido"
        else:
            self.derogado = derogado

    def setTransitorio(self, transitorio: str) -> None:
        if transitorio is None:
            self.transitorio = "transitorio: desconocido"
        else:
            self.transitorio = transitorio

    def getTexto(self) -> str:
        return self.texto

    def getMetadatoAnexo(self) -> MetadatoAnexo:
        return self.metadatoAnexo

    def getIdParte(self) -> str:
        return self.idParte

    def getFechaVersion(self) -> datetime:
        return self.fechaVersion

    def getDerogado(self) -> str:
        return self.derogado

    def getTransitorio(self) -> str:
        return self.transitorio

