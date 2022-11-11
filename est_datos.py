# estructuras de datos

'''Una lista es una colección ordenada de valores. Una lista puede contener 
cualquier cosa.
En Python, el tipo de datos que representa a las listas se llama list.
Sintaxis
Lista=[v1,v2,v3,…,vn'''

#ejemplo lista
'''
pares = [2,4,6,8,10]
decimales = [2.5, 3.4, 4.1, 5.3, 2.2]
animales = ["gato","perro","leon","vaca"]
persona = ["pedro", 20, 1.75,"Masculino"]

print(pares)
print(decimales)
print(animales)
print(persona)
'''

# operaciones sobre listas
#len
'''
pares = [2,4,6,8,10]
decimales = [2.5, 3.4, 4.1, 5.3, 2.2]
animales = ["gato","perro","leon","vaca"]
persona = ["pedro", 20, 1.75,"Masculino"]

print(len(pares))
print(len(decimales))
print(len(animales))
print(len(persona))
'''

# indice - positivo se cuenta a la derecha
'''
pares = [2,4,6,8,10]
decimales = [2.5, 3.4, 4.1, 5.3, 2.2]
animales = ["gato","perro","leon","vaca"]
persona = ["pedro", 20, 1.75,"Masculino"]

print (animales[0])
'''


# indice - negativo se cuenta a la izquierda
'''
pares = [2,4,6,8,10]
decimales = [2.5, 3.4, 4.1, 5.3, 2.2]
animales = ["gato","perro","leon","vaca"]
persona = ["pedro", 20, 1.75,"Masculino"]

print (animales[-3])

'''

#append - agrega un elemento al final de la lista
'''
animales = ["gato","perro","leon","vaca"]
animales.append("Caballo")

print(animales)
'''
#remove - elimina un elemento de la lista
'''
animales = ["gato","perro","leon","vaca"]
animales.remove("leon")
print(animales)

animales.append("Cobra")
print(animales)
'''

#remove - elimina un elemento de la lista
'''
animales = ["gato","perro","leon","vaca"]
del animales[1]
print(animales)
'''

#mofificar elemento de lista
'''
animales = ["gato","perro","leon","vaca"]
animales[1]="buffalo"
print(animales)
'''
#concatenar listas
'''
animal1=["leon","gato"]
animal2=["serpiente", "pato"]
animales = animal1+animal2

print(animales)
'''

#sub lista 
'''
animales = ["gato","perro","leon","vaca"]
print(animales[1,3])
'''

#voltear la lista - reverse
'''
numeros=[1,3,5,7,9]
numeros.reverse()

print (numeros)
'''

#contar algo en la lista - count
'''
numeros = list("me gusta programar en java")
print (numeros.count('a'))
'''
#recorrer lista for
'''
animales = ["gato","perro","leon","vaca"]
for animal in animales:
    print(animal)
'''

#desempaquetar lista - convertir a variables cada valor
'''
animales = ["gato","perro","leon","vaca"]
gato,perro,leon,vaca = animales
print(gato)
print(perro)
print(leon)
print(vaca)
'''

#tuplas - conjunto de datos de diferentes tipos 
persona1 = ("carlos", "contreras", 45)
persona2 = ("luis ", "suarez ", 28)

print(persona1)
print(persona2)
