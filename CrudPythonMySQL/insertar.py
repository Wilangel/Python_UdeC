# importamos conector
import pymysql

try:
    # intentamos conexion
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='persona')
    try:
        # creamos el cursor para ejecutar consultas
        with conexion.cursor() as cursor:
            # establecemos la consulta
            consulta = "INSERT INTO `datospersona` (`nombre`, `apellido`, `telefono`) VALUES (%s, %s, %s);"
            # usamos el metodo execute del cursor para insertar los datos
            cursor.execute(consulta, (input("inserte nombre: "), input(
                "inserte Apellido: "), input("inserte telefono: ")))
    # realizamos commit de la insercion
        conexion.commit()
    finally:
        # cerramos la conexion
        conexion.close()
    #reportamos insercion correcta
    print("insercion Correcta...")
# capturamos el error si lo hay.
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
