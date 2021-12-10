from bs4 import BeautifulSoup
from Articulo import Articulo
from Ley import Ley
from Ley import soupConsultarLey

lista_titulos = list()
lista_parrafos = list()
lista_articulos = list()
ley = 20000
soup = soupConsultarLey(ley)
titulos = soup.find_all("EstructuraFuncional",  tipoParte="Título")
for t in titulos:
  lista_titulos.append(t)
print(f"Cantidad de Titulos: {len(lista_titulos)}")  #Largo para titulos

for i in range(len(lista_titulos)):
  #print(len(lista_titulos[i]))
  output = lista_titulos[i].find_all("EstructuraFuncional", tipoParte="Párrafo")
  if output:
    lista_parrafos.append(output)
    totalTitulosConParrafos= i+1  # Obtener el total real de paginas con parrafos
  else:
    lista_parrafos.append(lista_titulos[i])
    #lista_parrafos[i].append(lista_titulos[i].find_all("EstructuraFuncional", tipoParte="Artículo"))  # Posible problema, pero por ahora sirve
print(len(lista_parrafos))
print(f"La cantidad de listas de titulos con parrafos son: {totalTitulosConParrafos}")

for i in range(totalTitulosConParrafos):  # totalParrafos es la cantidad de elementos con el valor parrafo
  totalTitulosConParrafos = len(lista_parrafos[i])
  for j in range(totalTitulosConParrafos):  #
    print(f"Titulo: {i+1} Parrafo {j+1}")
    print("----------------------------")
    #print(lista_parrafos[i][j].Texto)
    titulo = str(lista_titulos[i].Texto.contents[0]).lstrip()
    parrafo = lista_parrafos[i][j].Texto.contents[0]
    articulos = lista_parrafos[i][j].find_all("EstructuraFuncional", tipoParte="Artículo")
    for articulo in articulos:
      textoArticulo= articulo.Texto
      numeroArticulo = str(textoArticulo.contents[0])
      articulo = numeroArticulo[0:17].lstrip().replace('.','')  # lstrip() para remover espacios inecesario y replace para evitar los puntos
      print(textoArticulo.contents[0])
      print("-----------------------------------------------------")
      a = Articulo(ley, titulo , parrafo, articulo, textoArticulo.contents[0])
      
      lista_articulos.append(a)