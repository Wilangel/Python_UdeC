def resultado(n1=None):
    if(n1==None):
        print("Error Parametro Vacio!!")
    else:
        cuadrado=n1**2
        raizcuadrado=n1**0.5
        return cuadrado,raizcuadrado
    

n=int(input("digite un numero\n"))
resultados=resultado(n)
print(n," elevado a la 2 ",resultados[0])
print(n," elevado a la 2 ",resultados[1])


