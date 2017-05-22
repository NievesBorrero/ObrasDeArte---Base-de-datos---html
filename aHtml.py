# -*- coding: utf-8 *-*

import MySQLdb
import webbrowser

def ejecutarConsulta(consulta=''):
	conexion = MySQLdb.connect('localhost', 'root', 'bd130', 'obras')  # Abro la conexión
	cursor= conexion.cursor()
	cursor.execute(consulta)
	if consulta.upper().startswith('SELECT'):
		datos = cursor.fetchall()
	else:
		#conexion.commit()
		datos = none
	cursor.close()
	conexion.close()
	return datos

def head(title):
	return '<html><head>\n<meta charset="UTF-8"><title>'+title+'</title></head><body>\n'

def parrafo(cadena):
	return '<p>'+cadena+'</p>\n'

def encabezado(cadena):
	return '<h1>'+cadena+'</h1>'

def tabla (filas):
    temp = '<table border="1"  cellspacing=0><tr><th>Obra</th><th>Autor</th><th>codigo</th>\n'
    for fila in filas:
        temp = temp + '<tr>'
        for celda in fila:
            temp = temp + '<td>' + str(celda) + '</td>\n'
        temp = temp + '</tr>'
    return temp + '</table>\n'

def final():
	return '</body> </html>'

#Escribimos el fichero
fichero= open('obras.html', 'w')
fichero.write(head('Galería de obras'))
fichero.write(encabezado('OBRAS DE ARTE'))
fichero.write(parrafo('Lista de obras ordenadas por título'))
fichero.write(tabla(ejecutarConsulta('SELECT * FROM OBRAS ORDER BY titulo')))
fichero.write(parrafo('Lista de obras ordenadas por codigo'))
fichero.write(tabla(ejecutarConsulta('SELECT * FROM OBRAS ORDER BY codigo')))
fichero.write(final())
fichero.close()

webbrowser.open_new_tab('obras.html')