def suma(n1=None,n2=None):
    '''la funcion realiza la suma 
    de dos numero por nombre comprobar
    si tiene parametros'''
    if(n1==None or n2==None):
        print("Error al Enviar parametros estan vacios!!")
        return
    return n1+n2


print(suma())


