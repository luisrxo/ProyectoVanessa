#Case que separar las variables/constantes de las etiquetas
class VariableOConstante:
	#En este diccionario se guardaran todas las variables o constantes
	variables = {}
	etiquetas = []
	etiqfinal={}
	i=0

	def VarOEtiq(self,sentencia):
		#Se mandara a un funcion interna que la procesara la etiqueta
		self.Etiqueta(sentencia)

	def agregarVariable(self, variable):
		self.variables[variable[0]] = variable[1]

	def Etiqueta(self,etiqueta):
		if (etiqueta != '\x00'):
			if ((etiqueta in self.etiquetas) == False):
				self.etiquetas.append(etiqueta)
	def GettEtiquetas(self):
		return self.etiquetas
	def GettVariables(self):
		return self.variables
	def AnadiendoDireccion(self,direccion):
		print("self.etiqfinal: "+str(self.etiqfinal))
		print("self.i: "+str(self.i))
		print("direccion: "+str(direccion))
		print("etiquetas[self.i]: "+str(self.etiquetas[self.i]))
		self.etiqfinal[self.etiquetas[self.i]]=direccion
		self.i=self.i+1
	def GettEFinal(self):
		return self.etiqfinal