import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='persona')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "DELETE FROM datospersona WHERE nombre = %s;"
			nombre = input()
			cursor.execute(consulta, (nombre))
 
		# No olvidemos hacer commit cuando hacemos un cambio a la BD
		conexion.commit()
  
	finally:
		conexion.close()
        
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

print("Eliminacion Exitosa")