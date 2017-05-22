#-*-coding: utf8-*-

class Obra (object):

	#Constructor que crea un objeto obra de arte
	def __init__(self, titulo, autor, codigo):
		self.codigo=codigo
		self.titulo=titulo
		self.autor=autor

	def getTitulo(self):
		return self.titulo

	def getAutor(self):
		return self.autor

	def getCodigo(self):
		return self.codigo

	# Método tipo toString
	def __str__(self):  
		return 'título:'+self.titulo+', autor: '+self.autor+', código: '+str(self.codigo)


#obra= Obra('La Primavera', 'Botticelli', 1)

#print str(obra)