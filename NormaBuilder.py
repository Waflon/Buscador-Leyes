from Setters.NormaSetters import *

'''------------------------BUILDER---------------------------------'''

def crearNormaConLey(idLey: str) -> Norma:
    xml_parser = soupConsultarLey(idLey)
    identificador = setIdentificador(xml_parser) # Identificado
    metadato = setMetadatoNorma(xml_parser) # Metadato
    listaAnexos = setListaAnexos(xml_parser)  # Anexo
    promulgacion = setPromulgacion(xml_parser)  # Promulgacion 
    atributos = setAtributos(xml_parser)  # Atributos
    encabezado = setEncabezado(xml_parser)
    return Norma(identificador, metadato, encabezado, promulgacion, [], listaAnexos, "binarios", atributos)


norma = crearNormaConLey(4808)