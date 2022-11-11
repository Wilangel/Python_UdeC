#practica estructuras de control

#if 
'''
n = int (input("Digite un numero: \n"))
if (n>0) :
    print (n , "El Numero es positivo")

'''

# if else
'''
n = int (input("Digite un numero: \n"))
if (n>0) :
    print (n , "El Numero es positivo")
else:
    print(n, "El numero es negativo ")

'''

# if - elif - else

'''
edad= int (input("Digitar Edad "))
if(edad >= 18):
    print("Es mayor de edad")
elif(edad>0 and edad < 18):
    print("es menor de edad. ")
else:
    print("no se acepta edad negativa ")

'''

#for en una lista
'''
animales={"perro","gato","armadillo","conejo","vaca"}
for animal in animales:
    print(animal, len(animal))
'''

#for con rango sin restriccion
 
'''
for x in range(6):
    print(x)
'''
# for con rango restringido
'''
for x in range (2,6):
    print(x)
'''

# for con rango restringido e incremento de 2
'''
for x in range (2,30,2):
    print(x)
'''

# for con rango restringido e decremento de 
'''
for x in range (10,0,-1):
    print(x)
'''

# else en ciclo for 
'''
for x in range(6):
    print(x)
else:
    print("Finalizo el ciclo")
'''
# break en ciclo for
'''
for x in range(6):
    if(x%2==0):
        if(x==2):
            break
        else:
            print(x," es par.")
'''

#continue en ciclo for
'''
for x in range(6):
    if(x%2==0):
        if(x==2):
            continue
        else:
            print(x," es par.")
'''

# La sentencia pass no hace nada. Se puede usar cuando una sentencia es requerida por la sintaxis pero el programa no requiere ninguna acción.
'''
for x in range(6):
    pass
'''
# uso de while contador mientras op es diferente de 0
'''
contpar = 0
contimp = 0
op = 1
n=0
while(op!=0):
    n=int(input("Digite n"))
    if(n%2 == 0):
        contpar += 1
    else:
        contimp += 1
    op = int (input("Desea Continuar 1/0"))

print("par ", contpar, " impar ",contimp)

'''

#aplicacion factorial con while

'''
fact, i = 1, 2

n = int(input("Digite el numero para factorial: "))

if(n==0 or n==1):
    fact = 1
else:
    while(i<=n):
        fact = fact * i
        i += 1

print("el factorial de: ", n , "es: ", fact)
'''


