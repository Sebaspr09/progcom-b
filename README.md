agenda = []

while True:

    print("\n===== GUILD WARS =====")
    print("1. Ver agenda")
    print("2. Agregar actividad")
    print("3. Buscar actividad")
    print("4. Eliminar actividad")
    print("5. Mostrar cantidad de actividades")
    print("6. Ver primera actividad")
    print("7. Ver última actividad")
    print("8. Ordenar agenda")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Ver agenda
        pass

    elif opcion == "2":
        # Agregar actividad
        nombre = input("Nombre de la actividad: ")
        fecha = input("Fecha: ")
        hora = input("Hora: ")

        actividad = {
            "nombre": nombre,
            "fecha": fecha,
            "hora": hora
        }

        agenda.append(actividad)

    elif opcion == "3":
        # Buscar actividad
        pass

    elif opcion == "4":
        # Eliminar actividad
        pass

    elif opcion == "5":
        # Cantidad de actividades
        print("Cantidad:", len(agenda))

    elif opcion == "6":
        # Primera actividad
        pass

    elif opcion == "7":
        # Última actividad
        pass

    elif opcion == "8":
        # Ordenar agenda
        pass

    elif opcion == "9":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")
