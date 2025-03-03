texto = """En la tranquila ciudad de Pueblito, cada sábado, la anciana señora Marta adornaba su ventana con flores. 
Era su forma de recordar a su difunto esposo, quien solía cultivar un jardín exuberante. Una tarde, 
un joven vecino, Luis, notó su tristeza y plantó un girasol frente a su casa. Con el tiempo, más vecinos 
se unieron, convirtiendo el vecindario en un mar de colores. La sonrisa de Marta volvió, y la comunidad 
floreció con amor y solidaridad. El girasol se convirtió en un símbolo de esperanza, recordando que la 
belleza puede florecer incluso en los momentos más oscuros."""


with open ('Historia anciana', 'w', encoding = 'utf-8') as archivo:
    archivo.write(texto)
archivo.close()
