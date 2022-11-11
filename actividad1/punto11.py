'''
 Programa que permita calcular el valor final a pagar en una súper tienda en
donde se aplican los siguientes descuentos:
a) Por compras entre 10000 y 20000 el 10%
b) Por compras entre 20001 y 50000 el 30%
c) Por compras superiores a 50000 el 50%
'''

while True:
    try:
        valorCompra = int(input("Escribe el valor de la Compra: "))
    except ValueError:
        print("Debes escribir un número.")
        continue

    if valorCompra < 0:
        print("Debes escribir un número positivo.")
        continue
    else:
        break

if (valorCompra >= 10000 and valorCompra <=20000):
    descuento=10
    print("el descuento es del ",descuento,"%, el total a pagar es ", valorCompra - (valorCompra*(descuento/100)))

if(valorCompra > 20000 and valorCompra <= 50000):
    descuento=30
    print("el descuento es del ",descuento,"%, el total a pagar es ", valorCompra - (valorCompra*(descuento/100)))

if(valorCompra>50000):
    descuento=50
    print("el descuento es del ",descuento,"%, el total a pagar es ", valorCompra - (valorCompra*(descuento/100)))