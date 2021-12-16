from dataclasses import dataclass
from datetime import datetime


@dataclass
class MetadatosNorma:
    tituloNorma: str
    materias: list
    nombresUsoComun: list
    paisesTratados: list
    tipoTratado: str
    fechaTratado: datetime
    fechaDerogacion: datetime
    identificacionFuente: str
    numeroFuente: str

    def __init__(self, tituloNorma=None, materias=None, nombresUsoComun=None, paisesTratados=None, tipoTratado=None, fechaTratado=None, fechaDerogacion=None, identificacionFuente=None, numeroFuente=None):
        self.setTituloNorma(tituloNorma)
        self.setMaterias(materias)
        self.setNombresUsoComun(nombresUsoComun)
        self.setPaisesTratados(paisesTratados)
        self.setTipoTratado(tipoTratado)
        self.setFechaTratado(fechaTratado)
        self.setFechaDerogacion(fechaDerogacion)
        self.setIdentificacionFuente(identificacionFuente)
        self.setNumeroFuente(numeroFuente)

# SETTERS
    def setTituloNorma(self, materias: str) -> None:
        if materias is None:
            self.materias = "Título de norma no encontrado"
        else:
            self.materias = materias

    def setMaterias(self, materias: list) -> None:
        if materias is None:
            self.materias = "Título de norma no encontrado"
        else:
            self.materias = materias

    def setNombresUsoComun(self, nombresUsoComun: list) -> None:
        if nombresUsoComun is None:
            self.nombresUsoComun = "Nombres de uso común no encontrados"
        else:
            self.nombresUsoComun = nombresUsoComun

    def setPaisesTratados(self, paisesTratados: list) -> None:
        if paisesTratados is None:
            self.paisesTratados = "Paises tratados no encontrados"
        else:
            self.paisesTratados = paisesTratados

    def setTipoTratado(self, tipoTratado: str) -> None:
        if tipoTratado is None:
            self.tipoTratado = "Tipo de tratado no encontrado"
        else:
            self.tipoTratado = tipoTratado

    def setFechaTratado(self, fechaTratado: datetime) -> None:
        if fechaTratado is None:
            self.fechaTratado = datetime(1800,1,1)  # Por defecto para errores
        else:
            self.fechaTratado = fechaTratado

    def setFechaDerogacion(self, fechaDerogacion: datetime) -> None:
        if fechaDerogacion is None:
            self.fechaDerogacion = datetime(1800,1,1)  # Por defecto para errores
        else:
            self.fechaDerogacion = fechaDerogacion

    def setIdentificacionFuente(self, identificacionFuente: str) -> None:
        if identificacionFuente is None:
            self.identificacionFuente = "Identificación fuente no encontrada"
        else:
            self.identificacionFuente = identificacionFuente

    def setNumeroFuente(self, numeroFuente: str) -> None:
        if numeroFuente is None:
            self.numeroFuente = "Número de fuente no encontrado"
        else:
            self.numeroFuente = numeroFuente

# GETTERS
    def getTituloNrma(self) -> str:
        return self.tituloNorma

    def getMaterias(self) -> list:
        return self.materias

    def getNombresUsoComun(self) -> list:
        return self.nombresUsoComun
    
    def getPaisesTratados(self) -> list:
        return self.paisesTratados

    def getTipoTratado(self) -> str:
        return self.tipoTratado

    def getFechaTratado(self) -> datetime:
        return self.fechaTratado

    def getFechaDerogacion(self) -> datetime:
        return self.fechaDerogacion

    def getIdentificacionFuente(self) -> str:
        return self.identificacionFuente

    def getNumeroFuente(self) -> str:
        return self.numeroFuente