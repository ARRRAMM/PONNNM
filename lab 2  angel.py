# Solicita al usuario ingresar una serie de números separados por espacios
entrada = input("Ingresa una serie de números separados por espacios: ")

# Convierte la entrada en una lista de números
numeros = [float(numero) for numero in entrada.split()]

# Implementa el algoritmo de ordenamiento de selección
n = len(numeros)
for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
        if numeros[j] < numeros[min_idx]:
            min_idx = j
    numeros[i], numeros[min_idx] = numeros[min_idx], numeros[i]

# Imprime la lista de números ordenados
print("Números ordenados en orden ascendente:")
for numero in numeros:
    print(numero, end=" ")



