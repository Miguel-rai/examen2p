import funcionesexamen
estudiantes = {} 
promedios = {}
aprobados = 0
desaprobados = 0

while True:
    funcionesexamen.mostrarmenu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        funcionesexamen.registrar_estudiante(estudiantes)
        aprobados, desaprobados = funcionesexamen.calcular_promedio(estudiantes, promedios, aprobados, desaprobados)
    elif opcion == "2":
        funcionesexamen.mostrar_estudiantes(estudiantes)
    elif opcion == "3":
        funcionesexamen.consultar_estudiante(estudiantes, promedios)
    elif opcion == "4":
        funcionesexamen.mostrar_estadisticas(estudiantes, promedios, aprobados, desaprobados)
    elif opcion == "5":
        aprobados, desaprobados = funcionesexamen.eliminar_estudiante(estudiantes, promedios, aprobados, desaprobados)
    elif opcion == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")