'''
Calcular Si el Numero entero Positivo, que pueda ser Mayor que 100 o
Cualquier Numero Positivo que sea Múltiplo de 3
'''
    
while True:
    try:
        numero = int(input("Escribe un numero : "))
    except ValueError:
        print("debes escribir un numero.")
        continue
    else:
        break
    #como las temperaturas pueden ser negativas no validamos la negatividad del numero



def esMayorQue100(numero):
    '''Comprueba si el numero es mayor que 100'''
    return True if numero>100 else False


def esMultiploDe3(numero):
    '''comprueba si un numero es multiplo de 3 '''
    return True if numero%3 == 0 else False

def esPositivo(numero):
    '''Comprueba si un numero es positivo'''
    return True if numero>0 else False

print("Valor logico comprobacion si es positivo :", esPositivo(numero))
print("Valor logico comprobacion si es mayor que 100 :", esMayorQue100(numero))
print("Valor logico comprobacion si es multiplo de 3 :", esMultiploDe3(numero))

