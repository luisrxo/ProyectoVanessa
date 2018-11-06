#Metodo que devuelve la linea a analizar
class LeerLineas:
	linea = -1

	def __init__(self,archivo):
		self.documento = archivo
		self.lineas = self.documento.readlines()

	def MandarLinea(self):
		self.linea = self.linea+1
		return self.lineas[self.linea].replace("       ", '\t')
	
	def resetLineNumber(self):
		self.linea = -1

	def getLineNumber(self):
		return self.linea
	def getlin(self):
		return self.lineas
