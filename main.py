while True:
    # Mostrar el menú
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    # Obtener la elección del usuario
    eleccion = input("Ingrese el número de la operación que desea realizar: ")

    # Verificar si el usuario quiere salir
    if eleccion == '5':
        print("¡Hasta luego!")
        break

    # Obtener los números de entrada
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la operación seleccionada
    if eleccion == '1':
        print("Resultado: ", suma(num1, num2))
    elif eleccion == '2':
        print("Resultado: ", resta(num1, num2))
    elif eleccion == '3':
        print("Resultado: ", multiplicacion(num1, num2))
    elif eleccion == '4':
        print("Resultado: ", division(num1, num2))
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")