# Agenda con base de datos Pymysql
# Primero importamos los paquetes necesarios para poder trabajar
import pymysql
from db import create_db, connect, get_data, get_all_data, update_data, insert_data


# En este archivo definimos las clases asociadas a la solución del problema
#PROBANDO PROBANDO
# Creamos nuestra clase agenda
class Agenda:
    # Iniciamos nuestra clase
    def __init__(self):
        # rearemos una lista donde guardaremos los datos de nuestra agenda
        self.contactos = []
        connect()
        create_db()

    # Menu del programa
    def menu(self):
        print()
        menu = [
            ['Agenda Personal'],
            ['1. Añadir Contacto', "anadir"],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Cerrar agenda']
        ]
        

        for x in range(6):
            print(menu[x][0])

        opcion = int(input("Introduzca la opción deseada: "))
        if opcion == 1:
            self.anadir()
        elif opcion == 2:
            self.lista()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            self.editar()
        elif opcion == 5:
            print("Saliendo de la agenda ...")
            exit()

        # Volvemos a llamar al menú
        self.menu()

    # Función para añadir un contacto

    def anadir(self):
        print("---------------------")
        print("Añadir nuevo contacto")
        print("---------------------")
        nombre = input("Introduzca el nombre: ")
        apellidos = input("Introduzca el apellido: ")
        telefono = input("Introduzca el teléfono: ")
        email = input("Introduzca el email: ")
        #self.contactos.append({'nombre': nom, 'telf': telf, 'email': email})
        insert_data(nombre,apellidos, telefono, email)

    # Función para imprimir la lista de contactos
    # En este caso imprimiremos solo los nombres de los contactos
    # Con ellos podremos buscar luego un contacto

    def lista(self):
        print("------------------")
        print("Lista de contactos")
        print("------------------")
        get_all_data()

    # Función para buscar un contacto a través del nombre

    def buscar(self):
        print("---------------------")
        print("Buscador de contactos")
        print("---------------------")
        nombre = input("Introduzca el nombre del contacto: ")
        get_data(nombre)
        '''for x in range(len(self.contactos)):
            if nom == self.contactos[x]['nombre']:
                print("Datos del contacto")
                print("Nombre: ", self.contactos[x]['nombre'])
                print("Teléfono: ", self.contactos[x]['telf'])
                print("E-mail: ", self.contactos[x]['email'])
                return x
        '''

    # Función para editar los datos de un contacto

    def editar(self):
        print("---------------")
        print("Editar contacto")
        print("---------------")
        nom_buscado= input("Introduzca el nombre del contacto: ")
        get_data(nom_buscado)
        print('A continuacion solicitaremos que ingrese los datos para actualizarlos')
        nombre = input("Introduzca el nuevo nombre: ")
        apellido = input("Introduzca el nuevo apellido: ")
        telefono = input("Introduzca el nuevo teléfono: ")
        email = input("Introduzca el nuevo email: ")
        update_data(nom_buscado, nombre, apellido, telefono, email)
        '''condition = False
        while condition == False:
            print("Selecciona que quieres editar: ")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. E-mail")
            print("4. Volver")
            option = int(input("Introduzca la opción deseada: "))
            if option == 1:
                nom = input("Introduzca el nuevo nombre: ")
                self.contactos[data]['nombre'] = nom
            elif option == 2:
                telf = input("Introduzca el nuevo teléfono: ")
                self.contactos[data]['telf'] = telf
            elif option == 3:
                email = input("Introduzca el nuevo email: ")
                self.contactos[data]['email'] = email
            elif option == 4:
                condition = True'''


# Bloque principal
agenda = Agenda()
agenda.menu()
