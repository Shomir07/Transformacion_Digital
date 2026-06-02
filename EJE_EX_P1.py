def calcular_promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
        lista_numeros (list): Lista de valores numéricos.

    Retorna:
        float: Promedio de los números de la lista.
    """
    
    return sum(lista_numeros) / len(lista_numeros)


# Ejemplo de uso
numeros = [10, 8, 9, 7, 6]
promedio = calcular_promedio(numeros)

print("El promedio es:", promedio)