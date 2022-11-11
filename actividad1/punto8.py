'''
Convertir Centigrados a Farenheit
F=9/5*C+32
'''


#pedimos y validamos dato
    
while True:
    try:
        C = int(input("Escribe el valor de la temperatura en grados Celcius : "))
    except ValueError:
        print("debes escribir un numero.")
        continue
    else:
        break
    #como las temperaturas pueden ser negativas no validamos la negatividad del numero

#calculamos la conversion

F=9/5*C+32

# mostramos la respuesta
print("para ",C," grados Celcius, serian {:.2f} grados Fahrenheit ".format(F))