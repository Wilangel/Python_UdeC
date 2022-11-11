def computoAsignatura(*args,**kwargs):
    '''la funcion recibe un argumento por posicion y nombre'''
    total=0 
    for k in kwargs:
         print(kwargs[k])
    for arg in args:
         total+=arg
    definitiva=total/3    
    print("definitiva","{0:.2f}".format(definitiva))

#llamado a la funcion
computoAsignatura(3.2,2.3,4.0,nomapel="juan",apellido="perez",programa="ing software")
