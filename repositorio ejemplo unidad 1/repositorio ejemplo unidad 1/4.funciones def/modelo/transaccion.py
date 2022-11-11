def iva(compra):
    return compra*0.19
def transaccion(compra):
    return int(compra+iva(compra))



