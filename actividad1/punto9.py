'''
Programa el cual permita ingresar los valores de temperatura del promedio
de 3 días de la semana. Le programa debe calcular la temperatura promedio
y luego mostrar los siguientes mensajes:
a) Si el promedio es mayor a 35° mostrar el mensaje “que días tan calurosa”
b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan
delicioso”
c) Si el promedio es menor de 15° mostrar el mensaje “Que días tan fría”
'''
#pedimos datos
temperaturas = (int(input("Inserte temperatura 1: ")),int(input("Inserte temperatura 2: ")),int(input("Inserte temperatura 3: ")))

# calculamos promedio
promedio=(temperaturas[0]+temperaturas[1]+temperaturas[2])/3
print("promedio: {:.2f}".format(promedio))

if (promedio >= 35):
    print('que dias tan calurosos.')

if(promedio > 15 and promedio < 35):
    print("que clima tan delicioso.")

if(promedio<15):
    print("Que dias tan frios.")

