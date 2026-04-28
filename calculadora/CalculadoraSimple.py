### 27/4 CALCULADORA SIMPLE ###

# Consigna del trabajo
# 1. Crear una calculadora simple por consola que muestre un menú de operaciones y permita al usuario elegir entre sumar, restar, multiplicar y dividir.
# 2. Validar que la opción ingresada sea correcta antes de continuar con la operación.
# 3. Pedir dos números, realizar el cálculo correspondiente y mostrar el resultado en pantalla.
# 4. Evitar errores en la división por cero mostrando un mensaje adecuado.
# 5. Permitir repetir la operación tantas veces como el usuario desee.
# 6. Trabajar con una lista de alumnos que incluya nombre, edad, sexo y nota.
# 7. Mostrar los datos de cada alumno en una sola línea.
# 8. Calcular el promedio de las notas del grupo.
# 9. Indicar cuántos alumnos tienen 18 años o más.
# 10. Mostrar cuál es el alumno con la nota más alta.

while True: # Estructura de control repetitiva
    print(f"\nCALCULADORA SIMPLE\n" +
        f"<<<<<<<<<<<<<<<<< # >>>>>>>>>>>>>>>>>\n\n" +
        f"- A: Sumar\n" +
        f"- B: Restar\n" +
        f"- C: Multiplicar\n" +
        f"- D: Dividir\n")

    opcion = input(f"# Elija la letra de la operación que desea realizar: ").lower()

    while opcion not in ["a", "b", "c", "d"]: # Validación con while
        opcion = input("Opción incorrecta. Use A / B / C / D: ").lower() # Función para admitir minúsculas

    numero_1 = float(input(f"# Ingrese su primer número: "))
    numero_2 = float(input(f"# Ingrese su segundo número: "))

    match opcion: # Match-case
        case "a":
            resultado = numero_1 + numero_2
        case "b":
            resultado = numero_1 - numero_2
        case "c":
            resultado = numero_1 * numero_2
        case "d":
            if numero_2 == 0:
                print("Error: no se puede dividir por 0")
                continue # El programa continúa sin problema
            resultado = numero_1 / numero_2

    print(f"# El resultado es: {resultado}\n")

    continuar = input(f"Desea realizar otra operación? S/N: ").lower()

    while continuar not in ["s", "n"]:
        continuar = input("Opción incorrecta. Use S / N: ").lower()

    if continuar == "n":
        break # El programa se cierra forzadamente