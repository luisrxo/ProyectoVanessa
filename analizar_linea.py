#Metodo que analiza la linea (Incompleto)
class AnalizarLinea:

	def __init__(self):
		self.contador=0
		self.mnemonico=''

	def Analizar(self,linea):
		#asignacion variable
		self.mnemonico = ''
		#si no es salto de linea corta cadena
		if (linea[0] != '\n'):
			linea = linea[0:len(linea)-1]
		else:
		#regresa salto 
			return '\n'
		for a in linea:
			#si es comentario regresa toda la linea o comentario 
			if (a == '*'):
				return linea
			else:
				# si el elemento es espacio o tabulador y el contador auxiliar es =0
				if (a==' ' or a=='\t' and self.contador==0):
					#incrementa el contador 
					self.contador = self.contador+1
					#añade elemento a la cadena
					self.mnemonico = self.mnemonico + a
				else:
					#si ya acabo con espacio y tabulador acumula elemento a la cadena 
					if (type('a')==type(a) and self.contador != 0):
						self.mnemonico = self.mnemonico + a
		return self.mnemonico