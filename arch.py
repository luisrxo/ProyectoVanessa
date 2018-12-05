class Archivo:
	
	def __init__(self,archivo):
		self.abierto = open(archivo)
	def getArchivo(self):
		return self.abierto
