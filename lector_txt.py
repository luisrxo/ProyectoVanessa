#Clase que abre el archivo TXT
class LectorTxt:

	def __init__(self,archivo):
		self.abierto = open(archivo)

	def getArchivoTxt(self):
		return self.abierto