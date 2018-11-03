#Metodo que analiza la linea 
class AnalizarLinea:

	def __init__(self):
		self.mnemonico=''

	def Analizar(self,linea):
		self.mnemonico = ''
		if (linea[0] != '\n'):
			linea = linea[0:len(linea)-1]
		else:
			return '\0'

		for a in linea:
			if (a == '*' and self.mnemonico==''):
				return linea
			else:
				if (linea[0]==' ' or linea[0]=='\t'):
					self.mnemonico = self.mnemonico + a
					linea=linea[1:]
				else:
					if (type('a')==type(a)):
						self.mnemonico = self.mnemonico + a			
		return self.mnemonico