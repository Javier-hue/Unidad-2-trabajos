alumnos = {}

alumnos = {
    "A001": {"nombre": "Juan Pérez", "carrera": "Ingeniería", "edad": 20, "cuatrimestre": 4},
    "A002": {"nombre": "Ana López", "carrera": "Diseño", "edad": 21, "cuatrimestre": 5},
    "A003": {"nombre": "Luis Martínez", "carrera": "Negocios", "edad": 22, "cuatrimestre": 6}
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