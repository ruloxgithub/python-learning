#1) Imprimir todas las combinaciones posibles de 2 dígitos sin repetirse en otro orden diferente
#2) Separar los números por "," y "espacio"
#3) Los números se deben imprimir de forma ascendente

"""
Proceso Lógico

1. Definir el rango de la posición 01 a 90.
2. Agregar los dígitos a una lista.
3. Convertir la lista a string.
4. Eliminar las combinaciones repetidas.
5. 
"""

for i in range(8):
    for j in range(i+1,10):
        print(f"{i}{j}", end=", ")
print("89")    