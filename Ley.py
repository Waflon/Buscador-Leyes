from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


def soupConsultarLey(idLey: str) -> BeautifulSoup:
    try:
        url = 'http://www.leychile.cl/Consulta/obtxml?opt=7&idLey=' + str(idLey)
        xml_data = requests.get(url).content  # Conseguir el contenido en xml
        print("Ley encontrada exitosamente")
        return BeautifulSoup(xml_data, "xml")  # objeto que contiene la sopita
    except:
        print("Ley no encontrada")


@dataclass
class Ley:
    idLey: str
    idNorma: str
    tituloNorma: str
    organismo: str
    promulgacion: str
    publicacion: str
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

        self.getDatos()

    def getDatos(self) -> None:  # Llena los elementos de la Ley
        try:
            soup = soupConsultarLey(self.idLey)  # Obtener soup

            self.tituloNorma = str(soup.find('TituloNorma').contents[0])
            self.organismo = soup.find("Organismo").contents[0]
            self.idNorma = soup.find_all("Norma")[0]['normaId']
            self.promulgacion = soup.find_all("Identificador")[0]['fechaPromulgacion']
            self.publicacion = soup.find_all("Identificador")[0]['fechaPublicacion']
            materias = soup.find_all("Materias")[0].find_all("Materia")

            titulo = soup.find('EstructurasFuncionales')
            titulos = titulo.find_all('EstructuraFuncional', tipoParte="Título")
            parrafos = titulo.findAll('EstructuraFuncional', tipoParte="Párrafo")
            articulos = soup.find_all("EstructuraFuncional", tipoParte="Artículo")

            # getListas
            for m in materias:
                self.lista_materias.append(str(m.contents[0]))

            for t in titulos:
                self.lista_titulos.append(str(t.Texto.contents[0]))

            for parrafo in parrafos:
                self.lista_parrafos.append(parrafo)

            for articulo in articulos:
                self.lista_articulos.append(str(articulo.Texto.contents[0]).replace("\n", " "))

            print("Datos obtenidos exitosamente")
        except:
            print("Hubo un error con la ley que buscaba")

    def mostrarArticulos(self) -> None:
        for a in self.lista_articulos:
            print(a)

    def mostrarDatos(self) -> None:
        print("Ley " + self.idLey)
        print("Norma: " + self.idNorma)
        print("Titulo Norma: " + self.tituloNorma)
        print("Organismo: " + self.organismo)
        print("Materias: " + str(self.lista_materias[:]))
        print("Cantidad de titulos: " + str(len(self.lista_titulos)))
        print("Cantidad de parrafos: " + str(len(self.lista_parrafos)))
        print("Cantidad de articulos: " + str(len(self.lista_articulos)))
        print("Fecha de promulgación: " + self.promulgacion)
        print("Fecha de publicación: " + self.publicacion)


