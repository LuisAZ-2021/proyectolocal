# Agenda con base de datos Sqlite3
import pymysql

def create_db():
    '''Creación de la Base de datos'''

    conexion = pymysql.connect(host='localhost', #127.0.0.1
                                user='root',      #admin o cualquier otro usuario
                                password='Anabel08.',
                                db='agenda')
    consulta = conexion.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS contactos(id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre VARCHAR(20) NOT NULL, apellidos VARCHAR(20) NOT NULL, telefono VARCHAR(14) NOT NULL, email VARCHAR(20) NOT NULL)'
    try:
        consulta.execute(sql)
        print('La tabla fue creada con éxito')
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("No se pudo crear la tabla: ", e)
    conexion.close()


def connect():
    '''Conexión a la Base de datos'''

    try:
        conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='Anabel08.',
                                    db='agenda')
        print("Conexión correcta")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)


def insert_data(nombre, apellidos, telefono, email):
    '''Agregar datos en la Base de Datos'''

    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='Anabel08.',
                                db='agenda')

    consulta = conexion.cursor()

    datos = (nombre, apellidos, telefono, email)
    sql = 'INSERT INTO contactos(nombre,apellidos,telefono,email) VALUES (%s,%s,%s,%s)'

    try:
        consulta.execute(sql, datos)
        print("Datos guardados con exito")
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al intentar guardar los datos: ", e)
    conexion.commit()
    conexion.close()

def update_data(nombre, apellidos, telefono, email, nom_buscado):
    '''Actualizar datos en la Base de Datos'''
    # Falta Try-Except
    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='Anabel08.',
                                db='agenda')
    consulta = conexion.cursor()
    consulta.execute('UPDATE contactos SET nombre = %s ,apellidos = %s,telefono = %s,email = %s WHERE nombre= %s',nom_buscado)
    consulta.close()
    conexion.commit()
    conexion.close()

def delete_data(nombre, apellidos, telefono, email, nom_buscado):
    '''Eliminar datos en la Base de Datos'''
    # Falta Try-Except
    conexion = pymysql.connect(host='localhost',
                                user='root',
                                password='Anabel08.',
                                db='agenda')
    consulta = conexion.cursor()
    consulta.execute('DELETE FROM contactos WHERE nombre= %s',nom_buscado)
    consulta.close()
    conexion.commit()
    conexion.close()

def get_all_data():
    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='Anabel08.',
                                    db='agenda')

        sql_select_Query = "select * from contactos"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()

        for row in records:
           if row=='':
               print("No hay contactos...")
           else:
               print('[+]ID:',row[0],'\n[+]Nombres:',row[1],'\n[+]Apellidos:',row[2],'\n[+]Telefono:',row[3],'\n[+]E-mail:',row[3],"\n----------")  #Mostramos La lista)

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error reading data from MySQL table", e)
    finally:
        connection.close()
        cursor.close()
        print("MySQL connection is closed")

def get_data(nombre):
    '''Buscar un solo valor en la Base de Datos'''
    try:
        conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='Anabel08.',
                                    db='agenda')
        try:
            #cursor=conexion.cursor()
            with conexion.cursor() as cursor:
                consulta = 'SELECT * FROM contactos WHERE nombre = %s'
                cursor.execute(consulta, nombre)
                lista_contactos = cursor.fetchall()
                for lista in lista_contactos:
                    print(lista)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Error consultando la tabla:", e)