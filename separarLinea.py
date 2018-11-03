class SepararLinea:

	def __init__(self):
		self.mnemonico=''
		self.etiqueta=''
		self.variable=[]

	def Separando(self, cadena):
		cadena=cadena+' '
		if '        ' in cadena:
			cadena = cadena[8:len(cadena)]
			cadena = '\t' + cadena
		self.mnemonico=''
		self.etiqueta=''
		self.variable=[]
		self.direccionamiento = ''
		if(cadena.lower().find('equ') != -1):
			#Esta constante es de ayuda
			var = ''
			#Quitamos los espacios del renglon
			for aux in cadena.lower():
				if (aux != ' '):
					var = var + aux
			#Como equ esta entre el nombre de la varibale y su direccion, aprovechando eso para agregar al diccionario
			#En una sola sentencia
			self.variable = [var[0:var.index('equ')], var[var.index('equ')+3:len(var)]]
		elif ( cadena[0]=='\t'):
			#separando mnemonico y direccionamiento  

			if (cadena.find('*') > 0):
				comentario = cadena[cadena.find('*'):len(cadena)]
				cadena=cadena[0:cadena.find('*')]
				
			#separando mnemonico y direccionamiento  
			contaba=0
			a=0
			#eliminar espacios en blanco antes del mnemonico

			while a<len(cadena):

				if(cadena[a]!=' ' or cadena[a]!='\t') and (type('a')==type(cadena[a])):
					a=len(cadena)
				a=a+1
				contaba=contaba+1

			cadena = cadena[contaba:len(cadena)]
			a=0
			cont=-1
			contaba=0

			while contaba < len(cadena):
				if(cadena[contaba]==' ' or cadena[contaba] =='\t'):
					contaba=len(cadena)
				contaba=contaba+1
				cont=cont+1


			mnemo=cadena[0:cont]
			self.mnemonico=mnemo
			cadena=cadena[cont:len(cadena)]
			direc=cadena.strip()
			self.direccionamiento=direc
		else:
			if(len(cadena[0].split()) == 1):
				if (type(cadena[0]) == type('a') and cadena[0]!='\n' and cadena.count('*',0,len(cadena)-1)<1 and cadena.count('#',0,len(cadena)-1)<1 and cadena.count('$',0,len(cadena)-1)<1):
					self.etiqueta = cadena

	def GettMnemonico(self):
		return self.mnemonico
	def GettDireccionamiento(self):
		return self.direccionamiento.strip()
	def GettEtiqueta(self):
		return self.etiqueta.strip()
	def GettVariable(self):
		return self.variable