'''Practica de Python inicial'''

# Imprimir un Hola Mundo
print("Hola Mundo Nojoda.")

# crear variables y Sumar 2 Numeros
num1 = 1
num2 = 2
Sum = num1+num2

# El metodo type nos muestra el tipo de dato de la variable
print(type(Sum))

# Para concatenar Textos con numeros debemos acudir al metodo str que muestra la representacion del numero en texto
print('la suma es ' + str(Sum))

# Para pedir datos por teclado usamos el metodo Input y usamos el metodo upper para colocar los caracteres en mayuscula
'''print('Inserte Articulo: ')
articulo = input().upper()
print(articulo)'''

# Tipos de datos
a = False  # Tipo Booleano
b = 'Hola'  # tipo String
c = 2.5  # tipo Decimal
d = 5  # tipo Entero

print('a es tipo ' + str(type(a)))
print('b es tipo ' + str(type(b)))
print('c es tipo ' + str(type(c)))
print('d es tipo ' + str(type(d)))

# asignacion de valores a multiples Variables
x, y, z = 'pera', 'limon', 'fresa'

print(x)
print(y)
print(z)

# asignacion de mismo valor a multiples variables
x = y = z = 'orange'

print(x)
print(y)
print(z)

# crear tupla o coleccion y desempaquetarla en varias variables

# crear coleccion
frutas = ['watermelon', 'passionfruit', 'pineapple']

# desempaquetar en variables
x, y, z = frutas
print('imprimiendo coleccion de variables')
print(x)
print(y)
print(z)

# operadores aritmeticos
base = 2
exponente = 3

# potencia
potencia = base**exponente

print('base ' + str(base))
print('exponente ' + str(exponente))

print('potencia ' + str(potencia))

# operadores logicos and, or, not

nombre = 'juan perez'
edad = 38

result1 = (nombre == 'carlos') and (edad == 38)  # operador and
result2 = (nombre == 'carlos') or (edad == 38)  # operador or
result3 = not ((nombre == 'carlos') and (edad == 38))  # operador not

print(result1)
print(result2)
print(result3)

# concatenar con +
lenguaje = "python"
mensaje = "me gusta programar con " + lenguaje
print(mensaje)

# concatenar con espacio
mensaje = "hola " "hoy"
print(mensaje)

# manejo de cadenas

lenguaje = "python"
tam = len(lenguaje)
c1 = lenguaje[0] #primera posicion de la cadena de izquierda a derecha
c2 = lenguaje[tam-1] #ultima posicion de la cadena de izquierda a derecha
c3 = lenguaje[-2]# segunda posicion de derecha a izquierda

print(c1)
print(c2)
print(c3)

# substring
lenguaje = "python"

print(lenguaje[:])
