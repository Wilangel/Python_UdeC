def iva(compra):
    return compra*0.19
def transaccion(compra):
    return compra+iva(compra)
def entradaCompra():
    op='s'
    total=0
    productos=[]
    valores=[]
    while(op!='n'):
        producto=input("digite el producto\n")
        valor=int(input("digite el valor\n"))
        productos.append(producto)
        valores.append(valor)
        op=input("desea continuar s/n\n").lower()    
    
    for i in range(len(productos)):
        print(productos[i],valores[i])
        total=total+int(valores[i])
    
    print("total a pagar ",transaccion(total))



entradaCompra()
    
    


