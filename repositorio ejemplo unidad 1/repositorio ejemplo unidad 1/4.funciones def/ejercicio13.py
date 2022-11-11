def contarNumeros():
    '''funcion para contar numero pares 
    es impares digitados'''
    contpar=0
    contimp=0
    op=1
    n=0;
    while(op!='n'):
        n=int(input("digite n\n"))
        if(n%2==0):
            contpar+=1
        else:
            contimp+=1   
        while(op!='n'):
            op=input("desea continuar s/n\n").lower()
            booleano=(ord(op[0])==115) or (ord(op[0])==110)
            if(booleano==False):
                print("opcion invalida!!")
                continue
            elif(booleano==True):
                    break        
            

    print("par",contpar,"impar",contimp)

contarNumeros();