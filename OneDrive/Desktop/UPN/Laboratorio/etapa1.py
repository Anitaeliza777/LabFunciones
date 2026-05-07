numeros = [5, 12, 8, 23, 4, 17, 9, 31, 6, 20]

print("=== Lista original ===")
for i in range(len(numeros)):
    print(f"Posición [{i}]: {numeros[i]}")

try:
    nuevo = int(input("\nIngresa un nuevo valor para la posición 2: "))
    numeros[2] = nuevo
except ValueError:
    print("Error: Debes ingresar un número válido.")

print(f"Lista actualizada: {numeros}")

try:
    buscar = int(input("\nIngresa el número que quieres buscar: "))
except ValueError:
    print("Error: Debes ingresar un número válido.")
    buscar = None

if buscar is not None:
    encontrado = False
    for i in range(len(numeros)):
        if numeros[i] == buscar:
            print(f"Encontrado en la posición {i}.")
            encontrado = True
            break

    if not encontrado:
        print("El número no está en la lista.")