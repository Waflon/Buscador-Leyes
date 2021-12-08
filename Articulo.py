from dataclasses import dataclass
from bs4 import BeautifulSoup

@dataclass
class Articulo:
    idLey: str
    titulo: str
    parrafo: str
    textoArticulo: str
    numeroArticulo: str

    def __init__(self, idLey: str, titulo: str, parrafo: str, numeroArticulo: str, textoArticulo: str):
        self.idLey = str(idLey)
        self.validarDatos(titulo, parrafo, numeroArticulo, textoArticulo)
    
    def setTitulo(self, titulo: str) -> None:
        if titulo:
          self.titulo = titulo
        else:
          self.titulo = "Sin Título"

    def setParrafo(self, parrafo: str) -> None:
        if not parrafo:
          self.parrafo = "Sin Párrafo"
        else:
          self.parrafo = parrafo

    def validarDatos(self, titulo: str, parrafo: str, numeroArticulo: str, textoArticulo: str) -> None:
      try:
        self.setTitulo(titulo)
        self.setParrafo(parrafo)
        self.textoArticulo = textoArticulo
        self.numeroArticulo = numeroArticulo
      except:
        print("Error Validando datos")
        self.textoArticulo = "vacio"
        self.numeroArticulo = "vacio"

    def mostrarDatos(self) -> None:
        print(f"Ley: {self.idLey}")
        print(self.titulo)
        print(self.parrafo)
        print(self.numeroArticulo)
        print(self.textoArticulo)