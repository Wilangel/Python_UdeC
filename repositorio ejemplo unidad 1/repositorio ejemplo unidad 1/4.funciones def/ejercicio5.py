def indeterminados_posicion(*parametros):
    '''funcion que recibe parametros por posicion en 
    tuplas'''
    for parametro in parametros:
        print(parametro)

indeterminados_posicion("juan","perez",41,[1,2,3,4,5],True)