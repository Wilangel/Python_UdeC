'''
Calcular el numero de pulsaciones que una persona debe tener por cada 10
segundos de ejercicio, si la formula es:
num. pulsaciones = (220 - edad)/10
'''
# pedimos y validamos edad
while True:
    try:
        edad = int(input("Escribe la edad: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if edad < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

#calculamos numero de pulsaciones con la formula dada

numPulsaciones = (220 - edad)/10

# mostramos el resultado
print("una persona de ", edad , " años, deberia tener ", numPulsaciones, "Pulsaciones por cada 10 segundos de ejercicio.")