print("LabFunciones listo")
def saludar(nombre):
    print("Hola,", nombre)

saludar("Frank")
saludar("Ana")

def sumar(a, b):
    return a + b

# Función 2: multiplicar
def multiplicar(a, b):
    return a * b

# Función 3: es_par
def es_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
print(sumar(3, 5))
print(multiplicar(4, 6))
print(es_par(4))
print(es_par(7))