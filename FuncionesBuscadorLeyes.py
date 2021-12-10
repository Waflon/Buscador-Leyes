from bs4 import BeautifulSoup
import requests


def buscarLey(ley: str):
  url = 'http://www.leychile.cl/Consulta/obtxml?opt=7&idLey=' + ley
  xml_data = requests.get(url).content  # Conseguir el contenido en xml

  soup = BeautifulSoup(xml_data, "xml")  # Parsear
  TituloNorma = soup.find('TituloNorma')
  EstructurasFuncionales = soup.find('EstructurasFuncionales')
  Texto = EstructurasFuncionales.findAll('Texto')

  lista = []
  for i in Texto:
    lista.append(str(i.contents[0]))  # Transformar el contenido en un string para mejor manejo fuera de la clase

  print(f"Norma: {TituloNorma.contents[0]}")  # Nombre de la Norma

  return lista


def mostrarLey(lista: list):
  for i in range(len(lista)):
    print(lista[i])


ley = str(input("Ingrese Ley a buscar: "))
lista = buscarLey(ley)
mostrarLey(lista)



