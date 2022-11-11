'''
La presión, el volumen y la temperatura de una masa de aire se relacionan
por la formula:
masa = (presión * volumen)/(0.37 * (temperatura + 460))
'''
#pedimos y validamos valores
#presion
while True:
    try:
        presion = int(input("Escribe el valor de la presion: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if presion < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

#volumen.
while True:
    try:
        volumen = int(input("Escribe el valor del volumen: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if volumen < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

#temperatura
while True:
    try:
        temperatura = int(input("Escribe el valor en grados celsius de la temperatura: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if temperatura < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

#Calculamos la Masa

masa = (presion * volumen)/(0.37 * (temperatura + 460))

#mostramos la respuesta
print("para los valores dados la masa es : {:.2f}".format(masa))