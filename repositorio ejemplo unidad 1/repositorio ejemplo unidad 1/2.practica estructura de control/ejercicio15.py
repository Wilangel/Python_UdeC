op='s'
while(op!='n'):
    op=input("digite letra\n").lower()
    booleano=(ord(op[0])==115) or (ord(op[0])==110)
    if(booleano==False):
        print("opcion invalida!!")
        continue
print(booleano)