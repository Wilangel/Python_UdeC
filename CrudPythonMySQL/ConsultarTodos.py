import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='persona')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			cursor.execute("SELECT id, nombre, apellido, telefono FROM datospersona;")
 
			# Con fetchall traemos todas las filas
			persona = cursor.fetchall()
 
			# Recorrer e imprimir
			for persona in persona:
				print(persona)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)