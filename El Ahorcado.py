import random


def seleccion_palabra():
    # Lista de palabras para adivina.
    palabras = [
    'anticonstitucionalisimo', 'desproporcionadamente', 'hipopotomonstrosesquipedaliofobia',
    'electroencefalografista', 'pseudopseudohemofilia', 'hidroclorotiazida', 'neumoultramicroscopicovolcaniconiosis',
    'paralelepipedo', 'psiconeuroinmunologia', 'superextraordinarísimamente', 'anticonstitucionalmente',
    'inconstitucionalidad', 'esternocleidomastoideo', 'ultramicroscopico', 'inmunoelectroforesis',
    'hipopotomonstrosesquipedaliofobico', 'hipopotomonstrosesquipedaliano', 'desoxirribonucleico', 'radiosensibilización',
    'anticonstitucionalidad', 'superextraordinario', 'inmunoelectroforesis', 'ultramicroscopico',
    'esternocleidomastoideo', 'desoxirribonucleico', 'radiosensibilizacion', 'anticonstitucional', 'pseudopseudohemofilia',
    'esternocleidomastoideo', 'superextraordinarísimamente', 'neumoultramicroscopicovolcaniconios',
    'anticonstitucionalisimo', 'desoxirribonucleico', 'electroencefalografista', 'inconstitucionalmente',
    'pseudopseudohemofilia', 'superextraordinario', 'hipopotomonstrosesquipedaliofobico',
    'inmunoelectroforesis', 'pseudopseudohemofilia', 'desoxirribonucleico', 'paralelepipedo',
    'ultramicroscopico', 'electroencefalografista', 'esternocleidomastoideo', 'superextraordinarísimamente',
    'pseudopseudohemofilia', 'inmunoelectroforesis', 'radiosensibilización', 'ultramicroscopico',
    'superextraordinario', 'pseudopseudohemofilia', 'hipopotomonstrosesquipedaliofobico', 'esternocleidomastoideo',
    'inmunoelectroforesis', 'desoxirribonucleico', 'radiosensibilizacion', 'anticonstitucional', 'paralelepipedo',
    'desoxirribonucleico', 'superextraordinarísimamente', 'pseudopseudohemofilia', 'electroencefalografista',
    'esternocleidomastoideo', 'ultramicroscopico', 'anticonstitucionalisimo', 'desoxirribonucleico',
    'electroencefalografista', 'radiosensibilización', 'pseudopseudohemofilia', 'inmunoelectroforesis',
    'paralelepipedo', 'ultramicroscopico', 'superextraordinarísimamente', 'desoxirribonucleico',
    'inmunoelectroforesis', 'anticonstitucional', 'electroencefalografista', 'radiosensibilizacion',
    'esternocleidomastoideo', 'pseudopseudohemofilia', 'inmunoelectroforesis', 'ultramicroscopico',
    'superextraordinario', 'hipopotomonstrosesquipedaliofobico', 'desoxirribonucleico', 'radiosensibilización',
    'inmunoelectroforesis', 'pseudopseudohemofilia', 'superextraordinario', 'hipopotomonstrosesquipedaliofobico',
    'desoxirribonucleico', 'radiosensibilizacion', 'paralelepipedo', 'anticonstitucional', 'superextraordinarísimamente',
    'pseudopseudohemofilia', 'electroencefalografista', 'esternocleidomastoideo', 'ultramicroscopico',
    'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis', 'paralelepipedo', 'radiosensibilización',
    'desoxirribonucleico', 'superextraordinario', 'electroencefalografista', 'pseudopseudohemofilia',
    'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis', 'ultramicroscopico', 'anticonstitucional',
    'superextraordinarísimamente', 'pseudopseudohemofilia', 'desoxirribonucleico', 'electroencefalografista',
    'esternocleidomastoideo', 'ultramicroscopico', 'inmunoelectroforesis', 'superextraordinario',
    'pseudopseudohemofilia', 'hipopotomonstrosesquipedaliofobico', 'desoxirribonucleico', 'radiosensibilización',
    'inmunoelectroforesis', 'anticonstitucional', 'superextraordinarísimamente', 'electroencefalografista',
    'esternocleidomastoideo', 'ultramicroscopico', 'pseudopseudohemofilia', 'hipopotomonstrosesquipedaliofobico',
    'inmunoelectroforesis', 'desoxirribonucleico', 'radiosensibilizacion', 'superextraordinario', 'anticonstitucional',
    'pseudopseudohemofilia', 'esternocleidomastoideo', 'ultramicroscopico', 'electroencefalografista',
    'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis', 'desoxirribonucleico', 'radiosensibilización',
    'superextraordinarísimamente', 'anticonstitucional', 'pseudopseudohemofilia', 'electroencefalografista',
    'esternocleidomastoideo', 'ultramicroscopico', 'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis',
    'desoxirribonucleico', 'radiosensibilizacion', 'superextraordinario', 'anticonstitucional',
    'pseudopseudohemofilia', 'esternocleidomastoideo', 'ultramicroscopico', 'electroencefalografista',
    'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis', 'desoxirribonucleico', 'radiosensibilización',
    'superextraordinarísimamente', 'anticonstitucional', 'pseudopseudohemofilia', 'electroencefalografista',
    'esternocleidomastoideo', 'ultramicroscopico', 'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis',
    'desoxirribonucleico', 'radiosensibilizacion', 'superextraordinario', 'anticonstitucional',
    'pseudopseudohemofilia', 'esternocleidomastoideo', 'ultramicroscopico', 'electroencefalografista',
    'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis', 'desoxirribonucleico', 'radiosensibilización',
    'superextraordinarísimamente', 'anticonstitucional', 'pseudopseudohemofilia', 'electroencefalografista',
    'esternocleidomastoideo', 'ultramicroscopico', 'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis',
    'desoxirribonucleico', 'radiosensibilizacion', 'superextraordinario', 'anticonstitucional',
    'pseudopseudohemofilia', 'esternocleidomastoideo', 'ultramicroscopico', 'electroencefalografista',
    'hipopotomonstrosesquipedaliofobico', 'inmunoelectroforesis', 'desoxirribonucleico', 'radiosensibilidad'
    
    ]

    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    # Mostrar el estado actual del tablero del ahorcado.
    tablero = [letra if letra in letras_adivinadas else '_' for letra in palabra]
    print(' '.join(tablero))

def mostrar_letras_restantes(palabra, letras_adivinadas): 
    # Calcular y mostrar las letras restantes que aún no han sido adivinadas. 
    letras_restante = set(palabra) - letras_adivinadas
    if len(letras_restante) > 0: 
        print(f"Letras restantes por adivinar: {len(letras_restante)}")

def juego_ahorcado():
    palabra = seleccion_palabra()
    letras_adivinadas = set()
    vidas = 8
    print("Bienvenido al juego del ahorcado. ¡Intenta adivinar la palabra!")
    while vidas > 0 and set(palabra) != letras_adivinadas:
        mostrar_tablero(palabra, letras_adivinadas)
        mostrar_letras_restantes(palabra, letras_adivinadas)
        print(f"Vidas restantes: {vidas}")
        intento = input("Ingresa una letra: ").lower()
        
        if intento in letras_adivinadas:
            print("Ya has intentando esa letra. Elige una diferente.")
        elif intento in palabra:
            letras_adivinadas.add(intento)
            print("¡Correcto!")
        else: 
            vidas -= 1
        
        if vidas == 0:
            print(f"Perdiste. La palabra era: {palabra}")
        elif set(palabra) == letras_adivinadas:
            mostrar_tablero(palabra, letras_adivinadas)
            print(f"¡Felicitaciones! Has adivinado la palabra: {palabra}")

if __name__ == '__main__':
    juego_ahorcado()
            
        