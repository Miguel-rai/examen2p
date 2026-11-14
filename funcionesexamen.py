def mostrarmenu():
    print("=== sistema de calificaaciones ===")
    print("1. registar estudiante")
    print("2. mostrar estudiantes")
    print("3.consultar estudiante")
    print("4.mostrar estadisticas")
    print("5.eliminar estudiantes por ID")
    print("6. Salir")

def registrar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    Id = input("Ingrese el ID del estudiante: ")
    if Id in estudiantes:
        print(f"El estudiante con ID {Id} ya está registrado.")
        return
    calificacions = []
    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i+1} del estudiante: "))
        if calificacion < 0 or calificacion > 100:
            print("La calificación debe estar entre 0 y 100. Intente nuevamente.")
            return 
        calificacions.append(calificacion)
    estudiantes[Id] = (nombre, calificacions)
    print(f"Estudiante {nombre} registrado con calificaciones {calificacions}.")

def calcular_promedio(estudiantes, promedios, aprobados, desaprobados):         
    ultimos_nombre = list(estudiantes.keys())[-1] 
    nombre, calificaciones = estudiantes[ultimos_nombre]
    promedio = sum(calificaciones) / len(calificaciones)
    promedios[ultimos_nombre] = promedio
    if promedio >= 70:
            aprobados = aprobados + 1
            print(f"El estudiante {nombre} ha aprobado con un promedio de {promedio:.2f}.")
    else:
            desaprobados = desaprobados + 1
            print(f"El estudiante {nombre} ha desaprobado con un promedio de {promedio:.2f}.")
    return aprobados, desaprobados
def mostrar_estudiantes(estudiantes):
    if estudiantes:
        print("=== Lista de Estudiantes ===")
        for Id, (nombre, calificaciones) in estudiantes.items():
            print(f"Nombre: {nombre}, ID: {Id}, Calificaciones: {calificaciones}")
    else:
        print("No hay estudiantes registrados.")

def consultar_estudiante(estudiantes, promedios):
    Id = input("Ingrese el ID del estudiante a consultar: ")
    if Id in estudiantes:
        nombre, calificaciones = estudiantes[Id]
        print(f"Estudiante: {nombre}, ID: {Id}, Calificaciones: {calificaciones}")
        if Id in promedios:
            print(f"Promedio: {promedios[Id]:.2f}")
        if promedios.get(Id, 0) >= 70:
            print("Estado: Aprobado")
        else:
            print("Estado: Desaprobado")
    else:
        print(f"Estudiante con ID {Id} no encontrado.")

def mostrar_estadisticas(estudiantes, promedios, aprobados, desaprobados):
    if estudiantes:
        total_estudiantes = len(estudiantes)
        promedio_mas_alto = max(promedios.values()) 
        promedio_general = sum(promedios.values()) / len(promedios) 
        print(f"Total de estudiantes: {total_estudiantes}")
        print(f"Promedio más alto: {promedio_mas_alto:.2f}")
        print(f"Promedio general de calificaciones: {promedio_general:.2f}")
        print(f"Estudiantes aprobados: {aprobados}")
        print(f"Estudiantes desaprobados: {desaprobados}")

    else:
        print("No hay estudiantes registrados para mostrar estadísticas.")

def eliminar_estudiante(estudiantes, promedios, aprobados, desaprobados):
    Id_estudiante = input("Ingrese el ID del estudiante a eliminar: ")
    if Id_estudiante in estudiantes:
        del estudiantes[Id_estudiante]
        if Id_estudiante in promedios:
            promedio = promedios.pop(Id_estudiante)
            if promedio >= 70:
                aprobados = aprobados - 1
            else:
                desaprobados = desaprobados - 1
            
        print(f"Estudiante con ID {Id_estudiante} eliminado.")
    else:
        print(f"No se encontró un estudiante con ID {Id_estudiante}.")
    return aprobados, desaprobados