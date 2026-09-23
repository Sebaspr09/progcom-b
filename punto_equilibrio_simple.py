
print("==========================================")
print(" CALCULADORA DE PUNTO DE EQUILIBRIO ")
print("==========================================")
print("Ingresa los datos de tu negocio:")
print()

costos_fijos = -1
while costos_fijos <= 0:
    costos_fijos = float(input("Costos fijos totales del mes ($): "))
    if costos_fijos <= 0:
        print("El valor debe ser mayor a 0. Intenta de nuevo.")

precio_venta = -1
while precio_venta <= 0:
    precio_venta = float(input("Precio de venta por unidad ($): "))
    if precio_venta <= 0:
        print("El valor debe ser mayor a 0. Intenta de nuevo.")

costo_variable = -1
while costo_variable <= 0:
    costo_variable = float(input("Costo variable por unidad ($): "))
    if costo_variable <= 0:
        print("El valor debe ser mayor a 0. Intenta de nuevo.")

print()

if precio_venta <= costo_variable:
    print("AVISO: El precio de venta debe ser mayor al costo variable.")
    print("Con estos datos el negocio nunca llega al punto de equilibrio.")
else:

    unidades_equilibrio = costos_fijos / (precio_venta - costo_variable)
    dinero_equilibrio = unidades_equilibrio * precio_venta

    print("--- RESULTADOS ---")
    print("Debes vender", round(unidades_equilibrio), "unidades para llegar al equilibrio.")
    print("Esto equivale a $", round(dinero_equilibrio, 2), "en ventas.")
    print()

    print("--- SIMULACIÓN DE ESCENARIOS ---")

    unidades = unidades_equilibrio * 0.7
    ingresos = unidades * precio_venta
    costos_totales = costos_fijos + (unidades * costo_variable)
    utilidad = ingresos - costos_totales

    print()
    print("Vendiendo menos de lo necesario (", round(unidades), "unidades):")
    print("  Ingresos:", round(ingresos, 2))
    print("  Costos totales:", round(costos_totales, 2))
    if utilidad > 0:
        print("  Utilidad:", round(utilidad, 2), "-> Ganancia")
    elif utilidad < 0:
        print("  Pérdida:", round(abs(utilidad), 2), "-> Pérdida")
    else:
        print("  Utilidad: 0 -> Ni gana ni pierde")

    unidades = unidades_equilibrio
    ingresos = unidades * precio_venta
    costos_totales = costos_fijos + (unidades * costo_variable)
    utilidad = ingresos - costos_totales

    print()
    print("Vendiendo justo el punto de equilibrio (", round(unidades), "unidades):")
    print("  Ingresos:", round(ingresos, 2))
    print("  Costos totales:", round(costos_totales, 2))
    if utilidad > 0:
        print("  Utilidad:", round(utilidad, 2), "-> Ganancia")
    elif utilidad < 0:
        print("  Pérdida:", round(abs(utilidad), 2), "-> Pérdida")
    else:
        print("  Utilidad: 0 -> Ni gana ni pierde")

    unidades = unidades_equilibrio * 1.3
    ingresos = unidades * precio_venta
    costos_totales = costos_fijos + (unidades * costo_variable)
    utilidad = ingresos - costos_totales

    print()
    print("Vendiendo más de lo necesario (", round(unidades), "unidades):")
    print("  Ingresos:", round(ingresos, 2))
    print("  Costos totales:", round(costos_totales, 2))
    if utilidad > 0:
        print("  Utilidad:", round(utilidad, 2), "-> Ganancia")
    elif utilidad < 0:
        print("  Pérdida:", round(abs(utilidad), 2), "-> Pérdida")
    else:
        print("  Utilidad: 0 -> Ni gana ni pierde")
