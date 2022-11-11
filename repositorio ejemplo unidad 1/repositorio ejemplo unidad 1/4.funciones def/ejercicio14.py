def calculoIva(compra):
    return compra*0.19


compra=int(input("digite la compra\n"))
iva=calculoIva(compra)
print("compra",compra,"iva",iva)