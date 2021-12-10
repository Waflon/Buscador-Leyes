from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


def soupConsultarLey(idLey: str) -> BeautifulSoup:
    try:
        url = 'http://www.leychile.cl/Consulta/obtxml?opt=7&idLey=' + str(idLey)
        xml_data = requests.get(url).content  # Conseguir el contenido en xml
        print(f"Solicitud exitosa para ley: {str(idLey)}")
        return BeautifulSoup(xml_data, "xml")  # objeto que contiene la sopita
    except:
        return None



@dataclass
class Ley:
    idLey: str
    idNorma: str
    tituloNorma: str
    organismo: str
    promulgacion: str
    txtPromulgacion: str
    publicacion: str
    derogacion: str
    anexos: str
    lista_titulos: list
    lista_parrafos: list
    lista_articulos: list
    lista_materias: list

    def __init__(self, idLey: str):
        self.idLey = str(idLey)
        self.lista_materias = []
        self.lista_titulos = []
        self.lista_parrafos = []
        self.lista_articulos = []
        self.getDatos()  # llenar el resto de elementos

    # Validaciones
    def setTituloNorma(self, soup: BeautifulSoup) -> None:
        try:
            self.tituloNorma = str(soup.find('TituloNorma').contents[0]).replace("\n", " ")
        except:
            self.tituloNorma = "vacio"

    def setOrganismo(self, soup: BeautifulSoup) -> None:
        try:
            self.organismo = soup.find("Organismo").contents[0]
        except:
            self.organismo = "vacio"

    def setIdNorma(self, soup: BeautifulSoup) -> None:
        try:
            self.idNorma = soup.find_all("Norma")[0]['normaId']
        except:
            self.idNorma = "vacio"

    def setPromulgacion(self, soup: BeautifulSoup) -> None:
        try:
            self.promulgacion = soup.find_all("Identificador")[0]['fechaPromulgacion']
        except:
            self.promulgacion = "vacio"

    def setPublicacion(self, soup: BeautifulSoup) -> None:
        try:
            self.publicacion = soup.find_all("Identificador")[0]['fechaPublicacion']
        except:
            self.publicacion = "vacio"

    def setListaMaterias(self, soup: BeautifulSoup) -> None:
        try:
            materias = soup.find_all("Materias")[0].find_all("Materia")
            self.lista_materias = [(str(m.contents[0])) for m in materias]  # List comprehension
        except:
            print("No hay materias para esta ley")

    def setListaTitulos(self, titulo: BeautifulSoup) -> None:
        try:
            titulos = titulo.find_all('EstructuraFuncional', tipoParte="Título")
            self.lista_titulos = [t for t in titulos]  # List comprehension
        except:
            print("No hay titulos para esta ley")

    def setListaParrafos(self, titulo: BeautifulSoup) -> None:
        try:
            parrafos = titulo.findAll('EstructuraFuncional', tipoParte="Párrafo")
            self.lista_parrafos = [parrafo for parrafo in parrafos]  # List comprehension
        except:
            print("No hay parrafos para esta ley")

    def setListaArticulos(self, soup: BeautifulSoup) -> None:
        try:
            articulos = soup.find_all("EstructuraFuncional", tipoParte="Artículo")
            self.lista_articulos = [str(articulo.Texto.contents[0]).replace("\n", " ") for articulo in articulos]  # List comprehension
        except:
            print("No hay articulos para esta ley")

    def setDerogacion(self, soup: BeautifulSoup) -> None:
        try:
            if str(soup.Promulgacion['derogado']) == 'no derogado':
                self.derogacion = 'no derogado'
            else:
                self.derogacion = "derogado con fecha " + str(soup.Promulgacion["fechaVersion"])
        except:
            self.derogacion = "vacio"
            print("Ley probablemente vacia")

    def getDatos(self) -> None:  # Llena los elementos de la Ley
        soup = soupConsultarLey(self.idLey)  # Obtener soup
        self.setTituloNorma(soup)
        self.setOrganismo(soup)
        self.setIdNorma(soup)
        self.setPromulgacion(soup)
        self.setPublicacion(soup)
        self.setListaMaterias(soup)
        titulo = soup.find('EstructurasFuncionales')
        self.setListaTitulos(titulo)
        self.setListaParrafos(titulo)
        self.setListaArticulos(soup)
        self.setDerogacion(soup)
        self.txtPromulgacion = soup.find("Promulgacion").Texto.contents[0]

    def mostrarArticulos(self) -> None:
        for a in self.lista_articulos:
            print(a)

    def mostrarDatos(self) -> None:
        print("Ley " + self.idLey)
        print( "-------------------------------------------------------------------------------------------------------------------------")
        print("Norma: " + self.idNorma)
        print( "-------------------------------------------------------------------------------------------------------------------------")
        print("Titulo Norma: " + self.tituloNorma)
        print("Organismo: " + self.organismo)
        print("Materias: " + str(self.lista_materias[:]))
        print( "-------------------------------------------------------------------------------------------------------------------------")
        print("Cantidad de titulos: " + str(len(self.lista_titulos)))
        print("Cantidad de parrafos: " + str(len(self.lista_parrafos)))
        print("Cantidad de articulos: " + str(len(self.lista_articulos)))
        print("Fecha de publicación: " + self.publicacion)
        print("Fecha de promulgación: " + self.promulgacion)
        print("Estado: " + self.derogacion)
        print( "-------------------------------------------------------------------------------------------------------------------------")
        print(f"Promulgación: \n {self.txtPromulgacion}")
        print( "-------------------------------------------------------------------------------------------------------------------------")