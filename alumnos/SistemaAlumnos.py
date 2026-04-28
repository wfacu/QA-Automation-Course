### 27/4 SISTEMA DE ALUMNOS ###

# Consigna del trabajo
# 1. Crear una lista llamada alumnos donde se almacenarán varios estudiantes.
# 2. Cada alumno debe representarse como un diccionario con las claves: "nombre", "edad", "notas" (lista) y "datos_fijos" (tupla con DNI y año de ingreso).
# 3. Cargar al menos 3 alumnos con datos de ejemplo dentro de la lista.
# 4. Mostrar todos los alumnos en pantalla, recorriendo la lista y accediendo a sus datos.
# 5. Calcular y mostrar el promedio de notas de cada alumno.
# 6. Determinar y mostrar cuál es el alumno con el mayor promedio.
# 7. Permitir agregar una nueva nota a un alumno (modificando su lista de notas).
# 8. Ordenar los alumnos por promedio de mayor a menor.
# 9. Mostrar solo los alumnos cuyo promedio sea mayor o igual a 7.
alumnos = [
    {
        "nombre": "Luis",
        "edad": 23,
        "notas": [10, 7, 8],
        "datos_fijos": (40879771, 2020)
    },

    {
        "nombre": "Ana",
        "edad": 20,
        "notas": [9, 6, 7],
        "datos_fijos": (41234567, 2021)
    },
    {
        "nombre": "Carlos",
        "edad": 25,
        "notas": [8, 8, 9],
        "datos_fijos": (39999888, 2019)
    },
    {
        "nombre": "Lucia",
        "edad": 22,
        "notas": [7, 7, 8],
        "datos_fijos": (42123456, 2022)
    },
    {
        "nombre": "Facundo",
        "edad": 23,
        "notas": [10, 10, 10],
        "datos_fijos": (45043145, 2025)
    }]

for alumno in alumnos:
    alumno["promedio"] = round(sum(alumno["notas"]) / len(alumno["notas"]), 2)

while True:
    print(f"""SISTEMA DE ALUMNOS\n
        Menú principal
        1. Mostrar alumnos actuales
        2. Mostrar el alumno con mejor promedio
        3. Terminar programa
        """)

    opcion_menu = input("Por favor, ingrese la opción que desea ejecutar: ")

    match opcion_menu:
        case "1":
            for alumno in alumnos:
                nombre_alumno = alumno["nombre"]
                edad_alumno = alumno["edad"]
                notas_alumno = alumno["notas"]
                dni_alumno, año_ingreso_alumno = alumno["datos_fijos"]
                promedio_notas = alumno["promedio"]

                print(f"""
                - Nombre: {nombre_alumno}
                - Edad: {edad_alumno}
                - Notas: {notas_alumno}
                - DNI: {dni_alumno}
                - Año de ingreso: {año_ingreso_alumno}
                - Promedio de notas: {promedio_notas}
                """)

        case "2":
            mejor_alumno = alumnos[0]

            for alumno in alumnos:
                if alumno["promedio"] > mejor_alumno["promedio"]:
                    mejor_alumno = alumno

            print(f"El mejor alumno es {mejor_alumno['nombre']} ya que cuenta con un promedio de {mejor_alumno['promedio']}.\n")

        case "3":
            print("Programa finalizado. ¡Hasta luego!")
            break

        case _:
            print("Opción incorrecta. Por favor, ingrese una opción válida (1, 2 o 3).\n")