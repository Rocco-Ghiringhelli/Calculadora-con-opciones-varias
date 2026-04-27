historial = []

'''
MENU
'''

def menu_historial():

    while True:
        print("\n--- HISTORIAL ---")
        print("1 - Ver historial")
        print("2 - Limpiar historial")
        print("0 - Volver")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            ver_historial()
        elif opcion == "2":
            limpiar_historial()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_operaciones():

    while True:
        print("\n--- OPERACIONES MATEMÁTICAS ---")
        print("1 - Calculadora")
        print("2 - Potencias")
        print("3 - Factorial")
        print("4 - Promedio")
        print("0 - Volver al menú principal")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            calculadora()
        elif opcion == "2":
            potencias()
        elif opcion == "3":
            factorial()
        elif opcion == "4":
            promedio()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_numeros():

    while True:
        print("\n--- NÚMEROS ---")
        print("1 - Par o impar")
        print("2 - Número primo")
        print("3 - Factorización")
        print("4 - MCD")
        print("5 - MCM")
        print("0 - Volver al menú principal")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            par_impar()
        elif opcion == "2":
            es_primo()
        elif opcion == "3":
            factorizar_numero()
        elif opcion == "4":
            mcd_opcion()
        elif opcion == "5":
            mcm_opcion()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu_conversiones():

    while True:
        print("\n--- CONVERSIONES ---")
        print("1 - Conversion de unidades")
        print("0 - Volver al menú principal")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            conversion_unidades()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")


def menu():

    while True:
        print("\n" + "-"*30)
        print("MENU PRINCIPAL")
        print("1 - Operaciones Matemáticas")
        print("2 - Numeros")
        print("3 - Conversiones")
        print("4 - Historial")
        print("0 - Salir")
        print("-"*30)

        opcion = input("Elija una opción: ")

        if opcion == "1":
            menu_operaciones()
        elif opcion == "2":
            menu_numeros()
        elif opcion == "3":
            menu_conversiones()
        elif opcion == "4":
            menu_historial()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción Invalida")
    

'''
Funciones auxiliares
'''

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("\nError: ingrese un número entero\n")


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("\nError: ingrese un número\n")


def pausar():
    input("\nPresione ENTER para volver al menú...\n")


def agregar_historial(texto):
    historial.append(texto)


'''
CALCULADORA
'''      

def calculadora():

    print("\nCalculadora Basica. \n")
    
    numero1 = pedir_entero("\nIntroduzca el primer valor: ")
    numero2 = pedir_entero("Introduzca el segundo valor: ")
    
    operacion = input("Introduzca la operacion +,-,/,* : ")
    
    if operacion == '+' or operacion == "sumar":
        resultado = numero1 + numero2
        print(f"\nEl resultado es: {resultado}\n")
        agregar_historial(f"Calculadora: {numero1} + {numero2} = {resultado}")

    elif operacion == '/' or operacion == "dividir":
        if numero2 == 0:
            print("\nNo se puede dividir por 0\n")
        else:
            resultado = numero1 / numero2
            print(f"\nEl resultado es: {resultado}\n")
            agregar_historial(f"Calculadora: {numero1} / {numero2} = {resultado}")

    elif operacion == '*' or operacion == "multiplicar":
        resultado = numero1 * numero2
        print(f"\nEl resultado es: {resultado}\n")
        agregar_historial(f"Calculadora: {numero1} * {numero2} = {resultado}")

    elif operacion == '-' or operacion == "restar":
        resultado = numero1 - numero2
        print(f"\nEl resultado es: {resultado}\n")
        agregar_historial(f"Calculadora: {numero1} - {numero2} = {resultado}")
    
    else:
        print("\nOperacion incorrecta...\n")

    pausar()


'''
PAR O IMPAR 
'''

def par_impar():

    print("\nComprobacion de numeros pares.")
   
    resultado = pedir_entero("\nIngrese el numero entero: ")
    
    if resultado % 2 == 0:
        print("\nEl numero es par\n")
        agregar_historial(f"Par/Impar: {resultado} es par")
    else:
        print("\nEs impar\n")
        agregar_historial(f"Par/Impar: {resultado} es impar")

    pausar()


'''
MCD (a, b)
'''

def mcd(a, b):

    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a


'''
MCM
'''

def mcm_opcion():
    
    print("\nCalculo de MCM.\n")

    num1 = pedir_entero("Ingrese el primer valor: ")
    num2 = pedir_entero("Ingrese el segundo valor: ")
    
    resultado_mcd = mcd(num1, num2)
    resultado_mcm = (num1 * num2) // resultado_mcd

    if num1 == 0 or num2 == 0:
        print("\nEl MCM con 0 es 0\n")
        agregar_historial(f"MCM: ({num1}, {num2}) = 0")
        pausar()
        return


    print(f"\nEl MCM es: {resultado_mcm}\n")
    agregar_historial(f"MCM: ({num1}, {num2}) = {resultado_mcm}")

    pausar()


'''
MCD
'''

def mcd_opcion():

    print("\nCalculo de MCD.\n")

    num1 = pedir_entero("Ingrese el primer valor: ")
    num2 = pedir_entero("Ingrese el segundo valor: ")

    resultado = mcd(num1, num2)

    print(f"\nEl MCD es: {resultado}\n")
    agregar_historial(f"MCD: ({num1}, {num2}) = {resultado}")

    pausar()


'''
Potencias
'''

def potencias():

    print("\nCalculadora de potencias.\n")

    base = pedir_entero("Ingrese el valor de la base: ")
    exponente = pedir_entero("Ingrese el valor del exponente: ")
    
    resultado = base ** exponente 

    print(f"\nEl resultado de {base} ^ {exponente} es: {resultado}\n")
    agregar_historial(f"Potencia: {base}^{exponente} = {resultado}")

    pausar()


'''
Factorial
'''

def factorial():

    numero = pedir_entero("Ingrese un numero entero: ")
    
    if numero < 0:
        print("\nError: No se puede calcular el factorial de un numero negativo\n")
        pausar()
        return
    
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i

    print(f"\nEl factorial de {numero} es: {resultado}\n")
    agregar_historial(f"Factorial: {numero}! = {resultado}")

    pausar()


'''
Factorizar un valor
'''

def factorizar_numero():

    print("\nFactorizacion de un numero entero.\n")

    numero = pedir_entero("Ingrese el numero entero a factorizar: ")
    
    if numero < 2:
        print("\nError: El numero debe ser mayor que 1.\n")
        pausar()
        return

    n = numero 
    factores = []
    divisor = 2

    while divisor <= n:                              # mientras el divisor sea menor o igual a n, seguimos intentando.
        if n % divisor == 0:                         # verifica si n es divisible por divisor (resto 0).
            factores.append(divisor)                 # agrega el divisor a la lista de factores.
            n = n // divisor                         # divide n por el divisor y sigue factorizando el resultado.
        else:
            divisor += 1                             # si no se puede dividir, probamos con el siguiente número.         #map(str, factores) → convierte cada número de la lista factores a cadena de texto, porque .join() solo funciona con strings. - une todos los factores con el símbolo × para que se vea bonito.
                                                     
    texto_factores = " x ".join(map(str, factores))
    print(f"\nLa factorizacion de {numero} es: {texto_factores}\n")
    agregar_historial(f"Factorización: {numero} = {texto_factores}")
    
    pausar()


'''
Primos
'''

def es_primo():
    
    print("\nComprobar numeros primos\n")

    numero = pedir_entero("Ingrese un numero entero mayor que 1: ")
    
    if numero < 2:
        print("\nError: El numero debe ser mayor que 1.\n")
        pausar()
        return
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            print(f"\n{numero} NO es primo.\n")
            agregar_historial(f"Primo: {numero} no es primo")
            pausar()
            return
        
    print(f"\nEl {numero} ES primo.\n")
    agregar_historial(f"Primo: {numero} es primo")

    pausar()


'''
Conversion de unidades
'''

def conversion_unidades():

    print("\nConversion de Unidades Simples.\n")

    print("Opciones: \n1 - cm a m \n2 - m a cm \n3 - km a m \n4 - m a km")
    opcion = input("Elija una opcion: ")

    valor = pedir_float("Ingrese el valor a convertir: ")

    if opcion == "1":
        resultado = valor / 100
        print(f"\n{valor} cm = {resultado} m\n")
        agregar_historial(f"Conversión: {valor} cm → {resultado} m")
    elif opcion == "2":
        resultado = valor * 100
        print(f"\n{valor} m = {resultado} cm\n")
        agregar_historial(f"Conversión: {valor} m → {resultado} cm")
    elif opcion == "3":
        resultado = valor * 1000
        print(f"\n{valor} km = {resultado} m\n")
        agregar_historial(f"Conversión: {valor} km → {resultado} m")
    elif opcion == "4":
        resultado = valor / 1000
        print(f"\n{valor} m = {resultado} km\n")
        agregar_historial(f"Conversión: {valor} m → {resultado} km")
    else:
        print("\nOpcion invalida.\n")

    pausar()


'''
Promedio
'''

def promedio():

    print("\nCalculo de promedio.")
    print("Ingrese numeros uno por uno")
    print("Presione 0 para finalizar\n")

    numeros = []

    while True:
        try:
            num = pedir_float("Ingrese un numero: ")
        except ValueError:
            print("\nError: Debe ingresar un numero\n")
            continue

        if num == 0:
            break

        numeros.append(num)

    if len(numeros) == 0:
        print("\nNo se ingresaron numeros\n")
        pausar()
        return
    
    resultado = sum(numeros) / len(numeros)

    print(f"\nEl promedio es: {resultado}\n")
    agregar_historial(f"Promedio: {numeros} = {resultado}")

    pausar()


'''
Historial
'''

def ver_historial():

    print("\n--- HISTORIAL DE OPERACIONES ---\n")

    if len(historial) == 0:
        print("No hay operaciones registradas.\n")
        pausar()
        return

    for i, operacion in enumerate(historial, start=1):
        print(f"{i}. {operacion}")

    pausar()

def limpiar_historial():
    historial.clear()
    print("\nHistorial eliminado correctamente.\n")
    pausar()


menu()
