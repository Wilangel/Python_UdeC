fact,i=1,2

n=int(input("digite el numero\n"))
if(n==0 or n==1):
    fact=1
else:
    while(i<=n):
        fact=fact*i
        i+=1

print("el factorial de ",n,"es",fact)