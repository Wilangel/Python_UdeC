'''
Programa para determinar si un deportista es aceptado en el equipo de
baloncesto de Bogotá. Las condiciones para ser aceptado son: 
a) La edad debe ser menor o igual a 18 años 
b) La estatura debe ser mayor a 180 cm 
c) El peso debe ser menor o igual a 80 kg 

Si el aspirante cumple las 3 condiciones
'''
#pedimos y validamos datos
#edad
while True:
    try:
        edad = int(input("Escribe la edad del jugador: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if edad < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break
#estatura
while True:
    try:
        estatura = int(input("Escribe la estatura del jugador: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if estatura < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break
#peso
while True:
    try:
        peso = int(input("Escribe el peso del jugador: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if peso < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

    #definimos funciones de comprobacion
def esMayorDeEdad(edad):
    '''Comprueba si el jugador es mayor de edad '''
    return True if edad >= 18 else False

def compruebaPeso(peso):
    '''Comprueba el peso del jugador'''
    return True if peso <= 80 else False

def compruebaEstatura(estatura):
    '''Comprueba estatura del jugador'''
    return True if estatura > 180 else False

if(esMayorDeEdad and compruebaPeso and compruebaEstatura):
    print("el jugador cumple, es adminido")
else:
    print("Jugador no admitido")
