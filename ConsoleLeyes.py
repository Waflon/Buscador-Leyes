from Articulo import Articulo
from Parrafo import Parrafo


parrafo = Parrafo(20500, ["1","2","b"])

lista = parrafo.getListaArticulos()

print(lista)

a = Articulo(20000)

parrafo.agregarArticulo(a)
parrafo.agregarArticulo(a)
print(lista)