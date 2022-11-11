def indeterminados_nombre(**parametros):
    '''funcion que recibe parametros por nombre 
    con diccionario'''
    for k in parametros:
        print(parametros[k])

indeterminados_nombre(nombre="juan",apellido="perez",edad=41,
lista=[1,2,3,4,5],decision=True)