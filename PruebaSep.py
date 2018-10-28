import csv


#Clase que abre el archivo TXT
class LectorTxt:

	def __init__(self,archivo):
		self.abierto = open(archivo)

	def getArchivoTxt(self):
		return self.abierto


#Clase que lee el archivo cvs
class Lector:
	Diccionario={}
	def __init__(self, archivo):
		self.documento = open(archivo)
		self.mnemonicos=csv.reader(self.documento)
#Metodo usado para devolver el archivo leido. 
	def CreandoDiccionario(self):
		for contador in self.mnemonicos:
			banderas = list()
			#print("Contador[1]: |"+contador[1]+"|  Contador[2]: |"+contador[2]+"|  Contador[3]: |"+contador[3]+"|  Contador[4]: |"+contador[4]+"|  Contador[5]: |"+contador[5]+"|  Contador[6]: |"+contador[6]+"|  Contador[7]: |"+contador[7]+"|  Contador[8]: |"+contador[8]+"|  Contador[9]: |"+contador[9])
			if(contador[2] == "-- " and contador[3] == "-- " and contador[4] == "-- "):
				banderas.append(0)
			else:
				banderas.append([contador[2], contador[4]])
			if(contador[5] == "-- " and contador[6] == "-- " and contador[7] == "-- "):
				banderas.append(0)
			else:
				banderas.append([contador[5], contador[7]])
			if(contador[8] == "-- " and contador[9] == "-- " and contador[10] == "-- "):
				banderas.append(0)
			else:
				banderas.append([contador[8], contador[10]])
			if(contador[11] == "-- " and contador[12] == "-- " and contador[13] == "-- "):
				banderas.append(0)
			else:
				banderas.append([contador[11], contador[13]])
			if(contador[14] == "-- " and contador[15] == "-- " and contador[16] == "-- "):
				banderas.append(0)
			else:
				banderas.append([contador[14], contador[16]])
			if(contador[17] == "-- " and contador[18] == "-- " and contador[19] == "-- "):
				banderas.append(0)
			else:
				banderas.append([contador[17], contador[19]])
			if(contador[20] == "-- " and contador[21] == "-- " and contador[22] == "-- "):
				banderas.append(0)
			else:
				banderas.append([contador[20], contador[22]])
			
			
			self.Diccionario[contador[1]] = banderas
		print(self.Diccionario)
	def getArchivo(self):
		return self.Diccionario


#Clase que busca el mnemonico en el archivo cvs
class BuscarMnemonico:

	def __init__(self,diccionario):
		self.mnemonicos = diccionario
		self.buscarD = buscarDireccionamiento(diccionario)
#Metodo que busca el mnemonico en todo el set de instrucciones
	def buscarMnemonico(self,mnemonico):
		try:
			self.buscarD.metodoDeDireccionamiento(self.mnemonicos[mnemonico])
		except KeyError:
			#Aqui van las directivas
			print('Error 4')
			

#Clase que busca el metodo de direccionamiento
class buscarDireccionamiento:

	def __init__(self,diccionario):
		self.mnemonicos = diccionario

#Metodo que busca el metodo de direccionamiento
	def metodoDeDireccionamiento(self,lista):
		print(lista,'\n')

class LectorTxt:

	def __init__(self,archivo):
		self.abierto = open(archivo)

	def getArchivoTxt(self):
		return self.abierto

#Metodo que devuelve la linea a analizar
class LeerLineas:
	linea = -1

	def __init__(self,archivo):
		self.documento = archivo
		self.lineas = self.documento.readlines()

	def MandarLinea(self):
		self.linea = self.linea+1
		return self.lineas[self.linea]

#Metodo que analiza la linea (Incompleto)
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

class SepararLinea:

	def __init__(self):
		self.mnemonico=''
		self.direccionamiento=[0]*7
		self.etiqueta=''

	def Separando(self, cadena):
		if ( cadena[0]=='\t'):
			#separando mnemonico y direccionamiento  
			contaba=0
			a=0
			#eliminar espacios en blanco antes del mnemonico

			while a<len(cadena):
				contaba=contaba+1
			
				if(cadena[a]!=' ' or cadena[a]!='\t') and (type('a')==type(cadena[a])):
					a=len(cadena)
				a=a+1


			a=0
			cont=contaba
			inicio=contaba
			while contaba < len(cadena):

				cont=cont+1
				if(cadena[contaba]==' ' or cadena[contaba] =='\t'):
					#sale del for 
					contaba=len(cadena)
				contaba=contaba+1

			mnemo=cadena[inicio:cont-1]
			self.mnemonico=mnemo
			con=cont
			conta=cont

			while con < len(cadena):

				conta=conta+1
				if(type('a')==type(cadena[con])):
					con=len(cadena)
				con=con+1

			direc=cadena[conta-1:len(cadena)]
			self.direccionamiento = direc

		#si la linea empieza con algun caracter es una variable constante o etiqueta :)

		else:
			if(len(cadena[0].split()) == 1):
				if (type(cadena[0]) == type('a') and cadena[0]!='\n' and cadena.count('*',0,len(cadena)-1)<1 and cadena.count('#',0,len(cadena)-1)<1 and cadena.count('$',0,len(cadena)-1)<1):
					self.etiqueta = cadena

	def GettMnemonico(self):
		return self.mnemonico
	def GettDireccionamiento(self):
		return self.direccionamiento
	def GettEtiqueta(self):
		return self.etiqueta

#Case que separar las variables/constantes de las etiquetas
class VariableOConstante:
	#En este diccionario se guardaran todas las variables o constantes
	variables = {}
	etiquetas = []

	#Esta funcion nos determina si es etiqueta o variable
	def VarOEtiq(self,sentencia):
		#Si es una variable entrara aqui

		if (sentencia.lower().find('equ') != -1 ):
		
			#Mandamos a llamar una funcion interna que procesara la variable o etiqueta
			self.Variable(sentencia.lower())
		#Si es etiqueta entrara aqui 
		else:
			#Se mandara a un funcion interna que la procesara la etiqueta
			self.Etiqueta(sentencia)
		#Funcion que procesara la sentencia de variable
	def Variable(self,variab):
		#Esta constante es de ayuda
		var = ''
		#Quitamos los espacios del renglon
		for aux in variab:
			if (aux != ' '):
				var = var + aux
		#Como equ esta entre el nombre de la varibale y su direccion, aprovechando eso para agregar al diccionario
		#En una sola sentencia
		self.variables[var[0:var.index('equ')]] = var[var.index('equ')+3:len(var)]

	def Etiqueta(self,etiqueta):
		if (etiqueta != '\x00'):
			if ((etiqueta in self.etiquetas) == False):
				self.etiquetas.append(etiqueta)
	def GettEtiquetas(self):
		return self.etiquetas
	def GettVariables(self):
		return self.variables


#main provicional
doc=Lector('68HC11.csv')
doc.CreandoDiccionario()
documento = doc.getArchivo()
bMnemonicos = BuscarMnemonico(documento)
documento=LectorTxt('START.asc')
Tlineas=LeerLineas(documento.getArchivoTxt())
analizadorDLinea = AnalizarLinea()
separadorDLinea = SepararLinea()
varocons = VariableOConstante()


"""

#Codigo para crear la lista de variables y de etiquetas
for contador in range(1,145):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	if (separadorDLinea.GettEtiqueta() != ''):
		varocons.VarOEtiq(separadorDLinea.GettEtiqueta())

print('Estas son las etiquetas:\n', varocons.GettEtiquetas())
print('Estas son las variables:\n',varocons.GettVariables()) 

for contador in range(1,144):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	print("Label: "+separadorDLinea.GettEtiqueta())
	print("Direccionamiento: "+str(separadorDLinea.GettDireccionamiento()))
		"""