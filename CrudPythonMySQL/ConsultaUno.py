import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='persona')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "SELECT id, nombre, apellido, telefono FROM datospersona WHERE id = %s;"
			cursor.execute(consulta, (input("Inserte Id: ")))
 
			# Con fetchall traemos todas las filas
			persona = cursor.fetchall()
 
			# Recorrer e imprimir
			for persona in persona:
				print(persona)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)