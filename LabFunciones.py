
def saludar(nombre):
    print(f"Hola, {nombre}")

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
    print("1. Saludar")
    print("2. Calculadora")
    print("3. Verificar mayoría de edad")
    print("4. Salir")
    print("="*40)
    
    opcion = input("Selecciona una opción (1-4): ")
    

    if opcion == "1":
        print("\n--- SALUDAR ---")
        nombre = input("Ingresa tu nombre: ")
        saludar(nombre)
    

    elif opcion == "2":
        print("\n--- CALCULADORA ---")
        print("Submenú:")
        print("   a) Sumar")
        print("   b) Multiplicar")
        print("   c) Verificar si un número es par/impar")
        
        sub_opcion = input("Elige una sub-opción (a/b/c): ").lower()
        
        if sub_opcion == "a":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = sumar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        
        elif sub_opcion == "b":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} × {num2} = {resultado}")
        
        elif sub_opcion == "c":
            numero = int(input("Ingresa un número entero: "))
            resultado = es_par(numero)
            print(f"El número {numero} es {resultado}")
        
        else:
            print("Opción no válida")
    

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