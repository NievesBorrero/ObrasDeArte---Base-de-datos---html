#-*-coding: utf8-*-

from Obra import Obra
import MySQLdb


def crearObra():
	conexion = MySQLdb.connect("localhost","root","bd130","obras")
	obra= Obra(raw_input('Título:'), raw_input('Autor:'), int(raw_input('código: ')))
	titulo= obra.getTitulo()
	autor= obra.getAutor()
	codigo= obra.getCodigo()
	cursor=conexion.cursor()
	cursor.execute(("INSERT INTO OBRAS(CODIGO,TITULO,AUTOR) VALUES('%d','%s','%s')") % (codigo,titulo,autor))
	cursor.close()
	conexion.commit()
	conexion.close()

def mostrarObras():
	conexion = MySQLdb.connect("localhost","root","bd130","obras")
	cursor = conexion.cursor()
	filas = cursor.execute("SELECT * FROM OBRAS")
	for x in range(filas):
		resultado  = cursor.fetchone()
		print resultado
	cursor.close()
	conexion.close()

def borrarObras():
	conexion = MySQLdb.connect("localhost","root","bd130","obras")
	mostrarObras()
	codigo = int(raw_input("Codigo de la obra a borrar: "))

	cursor = conexion.cursor()
	cursor.execute("DELETE FROM OBRAS WHERE CODIGO ='%s' " % codigo)
	conexion.commit()
	cursor.close()
	conexion.close()

def modificarObra():
	conexion = MySQLdb.connect("localhost", "root", "bd130", "obras")
	mostrarObras()
	codigo= raw_input("Codigo de la obra a modificar: ")
	cursor = conexion.cursor()
	menuModificar()
	consulta= gestionarMenuModificar(int(raw_input("opción: ")), codigo)
	cursor.execute(consulta)
	conexion.commit()
	cursor.close()
	conexion.close()


def menuModificar():
	opciones= "¿Qué deseas modificar?\n"
	opciones += "1-Título\n"
	opciones += "2-Autor\n"
	opciones += "3-código\n"
	print opciones

def gestionarMenuModificar(opcion, codigo):
    if opcion==1:
        titulo=raw_input("Introduce el nuevo título: ")
        consulta= "UPDATE OBRAS SET titulo='%s' where codigo='%i'" % (titulo, int(codigo))
        return consulta
    if opcion==2:
        autor=raw_input("Introduce el nuevo autor: ")
        consulta= "UPDATE OBRAS SET autor='%s' where codigo='%i'" % (autor, int(codigo))
        return consulta
    if opcion==3:
        codigoNuevo= int(raw_input("Introduce el nuevo código: "))
        consulta= "UPDATE OBRAS SET codigo= '%i' where codigo='%i'" % (int(codigoNuevo), int(codigo))
        return consulta


def imprimirOpcionesMenu():
    opciones = "--MENU--\n"
    opciones += "1- Crear nueva obra de arte.\n"
    opciones += "2- Mostrar obras de arte.\n"
    opciones += "3- Borrar obra de arte.\n"
    opciones+= "4- Modificar datos de una obra.\n"
    opciones += "5- Salir."
    print opciones

def gestionarOpcionesMenu(opcion):
    if opcion== 1:
    	#try:
            crearObra()
        #except:
        	#print "Error al crear la nueva obra."
    elif opcion == 2:
        mostrarObras()
    elif opcion == 3:
        borrarObras()
    elif opcion==4:
    	modificarObra()


def solicitarOpcionesMenu():
    while True:
        imprimirOpcionesMenu()
        opcion = int (raw_input("Opcion: "))
        gestionarOpcionesMenu(opcion)
        if(opcion == 5):
            break

solicitarOpcionesMenu()
