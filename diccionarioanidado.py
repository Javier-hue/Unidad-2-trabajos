alumnos = {}

alumnos = {
    "A001": {"nombre": "Rose Park", "carrera": "Ingeniería", "edad": 20, "cuatrimestre": 4},
    "A002": {"nombre": "Lisa Manobal", "carrera": "Diseño", "edad": 21, "cuatrimestre": 5},
    "A003": {"nombre": "Jisoo kim", "carrera": "Negocios", "edad": 22, "cuatrimestre": 6}
}

matricula = input("Ingresa la matrícula del alumno: ")

if matricula in alumnos:
    info = alumnos[matricula]
    print(f"Nombre: {info['nombre']}")
    print(f"Carrera: {info['carrera']}")
    print(f"Edad: {info['edad']}")
    print(f"Cuatrimestre: {info['cuatrimestre']}")
else:
    print("No se encontró información para la matrícula ingresada.")
