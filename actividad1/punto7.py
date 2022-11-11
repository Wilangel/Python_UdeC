'''
Convertir Farenheit a Centigrados
C=5/9*(f-32)
'''
#pedimos y validamos dato
    
while True:
    try:
        f = int(input("Escribe el valor de la temperatura en grados Farenheit: "))
    except ValueError:
        print("debes escribir un numero.")
        continue
    else:
        break
    #como las temperaturas pueden ser negativas no validamos la negatividad del numero

#calculamos la conversion

C=5/9*(f-32)

# mostramos la respuesta
print("para ",f," grados farenheit, serian {:.2f} grados centigrados ".format(C))

