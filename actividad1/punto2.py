'''
Desarrolle el algoritmo de la empresa XYZ, que permita calcular la nómina
semanal de 5 obreros, con la siguiente características:
• Valor Hora 1000 pesos.
• Digitar el Número de Horas Trabajadas por semana por cada Obrero
• Calcular el valor a pagar por cada obrero
• Calcular el Valor Total Pagados a Todos los Obreros.
'''
valorHora = 1000

horaObrero1 = int(input("Ingrese numero de horas de Obrero 1. "))
horaObrero2 = int(input("Ingrese numero de horas de Obrero 2. "))
horaObrero3 = int(input("Ingrese numero de horas de Obrero 3. "))
horaObrero4 = int(input("Ingrese numero de horas de Obrero 4. "))
horaObrero5 = int(input("Ingrese numero de horas de Obrero 5. "))

# para calcular el pago generamos variables para cada obrero
print("calculando...")

pagoObrero1 = horaObrero1 * valorHora
print("al obrero 1 se le pagan: $", pagoObrero1," pesos.")

pagoObrero2 = horaObrero2 * valorHora
print("al obrero 2 se le pagan: $", pagoObrero2," pesos.")

pagoObrero3 = horaObrero3 * valorHora
print("al obrero 3 se le pagan: $", pagoObrero3," pesos.")

pagoObrero4 = horaObrero4 * valorHora
print("al obrero 4 se le pagan: $", pagoObrero4," pesos.")

pagoObrero5 = horaObrero5 * valorHora
print("al obrero 5 se le pagan: $", pagoObrero5," pesos.")

pagoTotal = pagoObrero1 + pagoObrero2 + pagoObrero3 + pagoObrero4 + pagoObrero5
print("el total del los pagos fue: $", pagoTotal," pesos.")
