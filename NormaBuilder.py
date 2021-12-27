from Setters.NormaSetters import *

'''------------------------BUILDER---------------------------------'''

def crearNormaConLey(idLey: str) -> Norma:
    xml_parser = soupConsultarLey(idLey)
    atributos = setAtributos(xml_parser)  # Atributos
    identificador = setIdentificador(xml_parser) # Identificado
    metadato = setMetadatoNorma(xml_parser) # Metadato
    listaAnexos = setListaAnexos(xml_parser)  # Anexo
    promulgacion = setPromulgacion(xml_parser)  # Promulgacion 
    encabezado = setEncabezado(xml_parser)
    return Norma(atributos, identificador, metadato, encabezado, promulgacion, listaAnexos, "binarios")


norma = crearNormaConLey(4808)
print("------------------------------------------------------------------------------------------------")
print(norma.identificador)
print("------------------------------------------------------------------------------------------------")
print(norma.atributos)
print("------------------------------------------------------------------------------------------------")
print(norma.metadato)
print("------------------------------------------------------------------------------------------------")
print(norma.encabezado)
print("------------------------------------------------------------------------------------------------")
print(norma.listaAnexos)
print("------------------------------------------------------------------------------------------------")

