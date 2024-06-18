#creacion matriz
matriz = []

for i in range(4):
    matriz.append([])
    for j in range(8):
        matriz[i].append({})

posicion = 1

#creación diccionario
for i in range(4):
    for j in range(8):
        matriz[i][j] = {'numero asiento': posicion, 'precio': 0, 'nombre': "nada", 'apellido': "nada"}
        posicion += 1
        

print("\n-----------------------------------------------------------------------------------------------------------------------")
print("Bienvenido a Aerolíneas Peña y Lillo")
while True:


    #Menú
    print("1._Venta de boletos")
    print("2._Mostrar asientos disponibles")
    print("3._Mostrar información de asiento")
    print("4._Salir")    
    opcion = int(input("Respuesta: "))
    while opcion not in range(1,5):
        opcion = int(input("Opción no disponible, intente de nuevo\nRespuesta: "))


    #Salir
    if opcion == 4:
        print("\nGracias por elegirnos, vuelva pronto.")
        break


    #Venta de asientos
    elif opcion == 1:
        print("\n-----------------------------------------------------------------------------------------------------------------------\n")
        asiento = int(input("\nIngrese un asiento disponible: "))
        while asiento not in range(1,33):#[[
            asiento = int(input("\nLo sentimos, el asiento ingresado no está dentro del rango, intente de nuevo.\nIngrese un asiento disponible: "))

        valor_exclusivo = 1

        for i in range(4):
            for j in range(8):
                if asiento == matriz[i][j]['numero asiento']:
                    matriz[i][j]['nombre'] = str(input("Ingrese SOLO su nombre: "))                    
                    matriz[i][j]['apellido'] = str(input("Ingrese su apellido: "))                    
                    if valor_exclusivo <= 10:
                        matriz[i][j]['precio'] = 1000
                        valor_exclusivo += 1
                    else: matriz[i][j]['precio'] = 1500
                    print(f"\nReserva confirmada.\nAsiento n°{matriz[i][j]['numero asiento']} a nombre: {matriz[i][j]['nombre']} {matriz[i][j]['apellido']}, con un total de: {matriz[i][j]['precio']}\n")
                    print("-----------------------------------------------------------------------------------------------------------------------")


    #Mostrar asientos disponibles    
    elif opcion == 2:
        print("\n-----------------------------------------------------------------------------------------------------------------------")
        print("\nAsientos disponibles:")
        for i in range(4):
            for j in range(8):
                if (matriz[i][j]['nombre']) == 'nada':
                    print(f"Asiento n°{(matriz[i][j]['numero asiento'])}: Disponible")

                else: print(f"Asiento n°{(matriz[i][j]['numero asiento'])}: No disponible")
        print("\n-----------------------------------------------------------------------------------------------------------------------\n")


    #Mostrar información de asiento
    elif opcion == 3:
        print("\n-----------------------------------------------------------------------------------------------------------------------\n")
        asiento = int(input("\nIngrese un número de asiento: "))
        while asiento not in range(1,33):#[[
            asiento = int(input("\nLo sentimos, el asiento ingresado no está dentro del rango, intente de nuevo.\nIngrese un número de asiento: "))
        for i in range(4):
            for j in range(8):
                if (matriz[i][j]['numero asiento']) == asiento:
                    if matriz[i][j]['precio'] != 0:
                        print("El asiento no está disponible.")
                        print(f"El asiento n°{matriz[i][j]['numero asiento']} está a nombre de: {matriz[i][j]['nombre']} {matriz[i][j]['apellido']}")

                    else: print("El asiento está disponible.")
        print("\n-----------------------------------------------------------------------------------------------------------------------\n")