'''
Realiza un Algoritmos que Convierta de Décadas (10 años) a Días.
'''
# convertidor de años a dias

#pedimos un numero y nos aseguramos que sea un numero
while True:
    try:
        numeroAños = int(input("Escribe el numero de años: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if numeroAños < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

# calculamos de años a dias
cantidadDias = 365 * numeroAños

#mostramos la respuesta
print("en ", numeroAños, " años, hay ", cantidadDias , " dias.")