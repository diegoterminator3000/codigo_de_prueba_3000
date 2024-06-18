import time
from random import choice
opciones = [1,2,3,4,5,6]

coca_cola = [800, 10]
coca_cola_zero = [800, 10]
agua_c_gas = [900, 10]
agua_s_gas = [900, 10]
redbull = [1500, 10]
fanta = [750, 10]

total = 0; total_beb = 0

print("----------------------------------------------------------------")
print("Máquina expendedora\nQué quieres llevar?")

while True:
    print("----------------------------------------------------------------")
    print(f"1._Coca Cola ${coca_cola[0]}\n2._Coca Cola Zero ${coca_cola_zero[0]}\n3._Agua con gas ${agua_c_gas[0]}\n4._Agua sin gas ${agua_s_gas[0]}\n5._RedBull ${redbull[0]}\n6._Fanta ${fanta[0]}")    
    resp = int(input("\nRespuesta: "))
    print("----------------------------------------------------------------")
    while resp not in opciones:
        resp = int(input("Su respuesta no es válida, intente de nuevo.\nRespuesta: "))

    #Cocacola
    if resp == 1:        
        coca_cola[1] = coca_cola[1]- 1; total += coca_cola[0]; total_beb += 1

    #coca cola zero
    elif resp == 2:        
        coca_cola_zero[1] = coca_cola_zero[1] - 1 ; total += coca_cola_zero[0]; total_beb += 1
        
        

    #Agua con gas 
    elif resp == 3:        
        agua_c_gas[1] = agua_c_gas[1] - 1
        total += agua_c_gas[0]
        total_beb += 1

    #Agua sin gas 
    elif resp == 4:        
        agua_s_gas[1] = agua_s_gas[1] - 1; total += agua_s_gas[0]; total_beb += 1

    #Redbull
    elif resp == 5:        
        redbull[1] = redbull[1] - 1; total += redbull[0]; total_beb += 1

    #Fanta
    elif resp == 6:        
        fanta[1] = fanta[1] - 1; total += fanta[0]; total_beb += 1
        
        


    otra= int(input(f"\nDesea comprar otra? su total actual es de: {total}\n1._Sí\n2._No\nRespuesta: "))

    while otra not in [1,2]:
        otra= int(input(f"Su opción ingresada es incorrecta, intente de nuevo.\nDesea comprar otra? su total actual es de: {total}\n1._Sí\n2._No\nRespuesta: "))
    if otra == 1:
        True
    else:
        break

#pago
pago = int(input("\n¿Cómo cancela? \n1._Tarjeta de Débito\n2._Tarjeta de Crédito\n3._Efectivo\nRespuesta: "))
while pago not in [1,2,3]:
    pago = int(input("Su opción marcada no es válida, intente de nuevo.\n\n¿Cómo cancela? \n1._Tarjeta de Débito\n2._Tarjeta de Crédito\n3._Efectivo\nRespuesta: "))
print("----------------------------------------------------------------")
if pago in [1,2]:
    estado_pago = ["Aprobado", "Rechazado"]
    while True:
        pin = int(input("Ingrese su pin de cuatro dígitos: "))
        
        while pin not in range(0000, 9999):
            pin = int(input("El largo de su pin es mayor a 4, Intente de nuevo.\nIngrese su pin de cuatro dígitos: "))

        for _ in range(8):
            time.sleep(0.5)
            print(".")

        estado_pago_rand = choice(estado_pago)
        print(f"Estado Pago: {estado_pago_rand}")
        if estado_pago_rand == estado_pago[1]:
            print("Pago Rechazado, intente de nuevo.")
            True
        else:
            print("Gracias por comprar, vuelva pronto")
            break
else:
    print("Gracias por comprar, vuelva pronto")