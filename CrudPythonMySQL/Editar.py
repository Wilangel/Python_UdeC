import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='persona')
	try:
		with conexion.cursor() as cursor:        
			consulta = "UPDATE datospersona SET nombre = %s WHERE id = %s;"
            
			nuevo_dato = input("Inserte el nuevo dato: ")
			id_editar = input("Seleccione el id a editar: ")
            
			cursor.execute(consulta, (nuevo_dato, id_editar))
 
		# No olvidemos hacer commit cuando hacemos un cambio a la BD
		conexion.commit()
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)