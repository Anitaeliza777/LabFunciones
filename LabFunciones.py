print("LabFunciones listo")

def saludar(nombre):
    print("Hola,", nombre)

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def es_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def verificar_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"


while True:
    print("\n" + "="*40)
    print("          MENÚ PRINCIPAL")
    print("="*40)
    print("1. Saludar (ejecutar pruebas)")
    print("2. Calculadora")
    print("3. Verificar mayoría de edad")
    print("4. Salir")
    print("="*40)
    
    opcion = input("Selecciona una opción (1-4): ")
    
 
    if opcion == "1":
        print("\n--- EJECUTANDO SALUDOS ---")
        saludar("Frank")
        saludar("Ana")
    
   
    elif opcion == "2":
        print("\n--- EJECUTANDO CALCULADORA ---")
        print(f"Suma: 3 + 5 = {sumar(3, 5)}")
        print(f"Multiplicación: 4 × 6 = {multiplicar(4, 6)}")
        print(f"Número 4 es: {es_par(4)}")
        print(f"Número 7 es: {es_par(7)}")
    

    elif opcion == "3":
        print("\n--- VERIFICAR EDAD ---")
        nombre = input("Ingresa tu nombre: ")
        edad = int(input("Ingresa tu edad: "))
        resultado = verificar_edad(edad)
        print(f"{nombre}, tienes {edad} años. Eres {resultado}.")
    
    
    elif opcion == "4":
        print("\n¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor elige 1, 2, 3 o 4.")