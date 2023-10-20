import division
import suma
import multiplicacion
import resta

while True:
    # Mostrar el menú
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    try:
        # Obtener la elección del usuario
        eleccion = input("Ingrese el número de la operación que desea realizar: ")
    except Exception as e:
        # Manejo de excepciones generales (cualquier otra excepción)
        print("Introduce solo numeros", str(e))
    # Verificar si el usuario quiere salir
    if eleccion == '5':
        print("¡Hasta luego!")
        break

    try:
        # Obtener los números de entrada
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except Exception as e:
        # Manejo de excepciones generales (cualquier otra excepción)
        print("Introduce solo numeros", str(e))
    # Realizar la operación seleccionada
    if eleccion == '1':
        print("Resultado: ", suma.suma(num1, num2))
    elif eleccion == '2':
        print("Resultado: ", resta.resta(num1, num2))
    elif eleccion == '3':
        print("Resultado: ", multiplicacion.multiplicacion(num1, num2))
    elif eleccion == '4':
        print("Resultado: ", division.division(num1, num2))
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
        