def num_caracteres(lista):
    # Devuelve una lista con la longitud, en caracteres, de las líneas de una lista
    caracteres_por_linea = []
    for elemento in lista:
        caracteres_por_linea.append(len(elemento))
    return caracteres_por_linea

def num_palabras(lista):
    # Devuelve una lista con la longitud, en palabras, de las líneas de una lista
    palabras_por_linea = []
    for elemento in lista:
        lista_de_palabras = elemento.split()
        palabras_por_linea.append(len(lista_de_palabras))
    return palabras_por_linea

def estadisticas_fichero(ruta):
    # Saca las estadísticas de caracteres y palabras por línea de un fichero
    lineas = fichero_a_lista(ruta)
    print("Estadísticas del fichero", ruta)
    print("-" * 60)
    palabras = num_palabras(lineas)
    caracteres = num_caracteres(lineas)
    i = 1
    for linea in lineas:
        print("Línea", i)
        print("Contenido:", linea)
        print("Número de palabras:", palabras[i-1])
        print("Número de caracteres:", caracteres[i-1])
        i = i + 1