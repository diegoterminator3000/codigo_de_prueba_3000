def area_circulo(radio):
    pi = 3.14159
    area = pi*(radio)**2
    return print(area)

def fahrenheit_celsius():
    grado_F = int(input("Ingrese su temperatura en grados Fahrenheit"))
    celcius = (grado_F-32)*(5/9)
    return print(celcius)

def celcius_fahrenheit():
    grado_C = int(input("Ingrese su temperatura en grados Celsius"))
    fahrenheit = (grado_C*(9/5)) + 32
    return print(fahrenheit)

#fibonacci

#listo
def nombre_usuario():    
    usuario = ""
    nombre = [str(input("Ingrese su nombre: "))]
    apellido = [str(input("Ingrese su apellido: "))]

    for letra in nombre:
        for letra_m in letra:
            usuario += letra_m
            break
    i = 0
    for letra in apellido:
        for letra_m in letra:
            usuario += letra_m
            i += 1
            if i == 3:
                break    
    return print(usuario)

#listo
def invertir_palabra():
    cadena = [str(input("Ingrese una palabra y se la invertiré: "))]
    palabra_inv=[]
    palabra_str = ""
    for palabra in cadena:
        for letra in palabra:
            palabra_inv.append(letra)
    palabra_inv.reverse()
    for letra in palabra_inv:
        palabra_str += letra        
    return print(palabra_str)


area_circulo()
fahrenheit_celsius()
celcius_fahrenheit()
invertir_palabra()
nombre_usuario()