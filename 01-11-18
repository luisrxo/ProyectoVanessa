import csv

#global memoriaLoc=0;
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
			# Formato de banderas: 
			# [  1,  2,    3,     4,    5,    6,  7 ]
			# [IMM, DIR, IND,X, IND,Y, EXT, INH, REL]
			
			self.Diccionario[contador[1]] = banderas
		print(self.Diccionario)
	def getArchivo(self):
		return self.Diccionario

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
	
	def resetLineNumber(self):
		self.linea = -1

	def getLineNumber(self):
		return self.linea

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

class Direccionamiento:
	def __init__(self, DiccionarioDireccionamiento, dirMem):
		self.Direccionamientos = DiccionarioDireccionamiento
		self.dirMem = dirMem
		self.labels = {}
		#print(self.Direccionamientos)
	# Formato de banderas: 
	# [  1,  2,    3,     4,    5,    6,  7 ]
	# [IMM, DIR, IND,X, IND,Y, EXT, INH, REL]
	def buscarDireccionamiento(self, mnemonico, variable,relativo):
		bandera = [0]
		
		if (str(variable).find('$') != -1 and (str(variable).find('#')==-1)):
			if (len(variable[1:])%2 != 0):
				variable = '$' + '0' + variable[1:len(variable)]

		variable = str(variable)
		if(variable.find("\'") != -1):
			indice = variable.find("'")
			print(type(indice))
			variable = str(ord(variable[indice+1]))
			print("Código ASCII: "+variable)
		try:
			direccionamientos = self.Direccionamientos[mnemonico.lower()]
			if(str(variable).find('#')==-1):
				if str(variable) =='':
					# Direccionamiento inherente
					if(direccionamientos[5] != 0):
						bandera = direccionamientos[5]
						print("Direccionamiento inherente")
					else:
						print("Error")
				else:
					if(variable.find(',') == 3):
						if(variable.find('X') == 4):
							# Direccionamiento indexado respecto a X
							if len(variable) > 5:
								print('error longitud mayor')
							elif(direccionamientos[2] != 0):
								bandera = direccionamientos[2]
								print("Direccionamiento indexado respecto a X")
							else:
								print("Error")
						elif(variable.find('Y') == 4):
							# Direccionamiento indexado respecto a Y
							if len(variable) > 5:
								print('error longitud mayor')
							elif(direccionamientos[3] != 0):
								bandera = direccionamientos[3]
								print("Direccionamiento indexado respecto a Y")
							else:
								print("Error")
						else:
							# Error
							print("Error")
					elif(len(variable) >= 4):
						# Direccionamiento extendido
						if(direccionamientos[4] != 0):
							#hexadecimal
							if(variable[0]!='$' and type(variable[0])!=type('a')):
								hexa=hex(int(variable))
								variable=str(hexa).upper()
								variable=variable[2:len(variable)]
							if len(variable)>6:
								print ('Error longitud mayor')
							else:
								bandera = direccionamientos[4]
								print("Direccionamiento extendido")
						else:
							print("Error")
					elif(len(variable) >=1):
						# Direccionamiento directo
						if(direccionamientos[1] != 0):
							bandera = direccionamientos[1]
							print("Direccionamiento directo")
							#hexadecimal
							if(variable[0]!='$'):
								hexa=hex(int(variable))
								variable=str(hexa).upper()
								variable=variable[2:len(variable)]
							if len(variable) > 3:
								print('Error longitud mayor a la soportada')
							else:
								bandera = direccionamientos[1]
								print("Direccionamiento directo")
						else:
							print("Error")
			elif(direccionamientos[0]!=0):
				# Direccionamiento inmediato o relativo
					if(variable[1]!='$' and variable[1]!="'"):
						hexa=hex(int(variable))
						variable=str(hexa).upper()
						variable=variable[2:len(variable)]
					if len(variable) > 6 :
						print('error longitud mayor')
					bandera = direccionamientos[0]
			else:
				if (relativo != 0):
					if(direccionamientos[6]!=0):
						self.dirMem = self.dirMem + int(bandera[len(bandera)-1])

					
			print(str(self.dirMem)+", "+str(bandera))
			self.dirMem = self.dirMem + int(bandera[len(bandera)-1])
			print("OpCode, tamanio , direccionamiento  : "+str(bandera)+" : Variable " +str(variable)+" Mem: "+str(self.dirMem))
		
		except KeyError:
			print("Error 4")
	def direccionamientoRelativo(self, mnemonico, variable,listaEti):
		
		direccionamiento = self.Direccionamientos[mnemonico.lower()]
		if (not(variable in self.labels)):
			self.labels[variable] = self.dirMem
		else:
			variable=self.labels[variable]

		if(direccionamiento[6] != 0):
			bandera = direccionamiento[6]
			print("Direccionamiento relativo")
			salto=3 #hex(self.dirMem-self.listEti[variable])
			print("OpCode, tamanio , direccionamiento  : "+str(bandera)+" : Variable " +str(salto)+" Mem: "+str(self.dirMem))
		else:
			self.buscarDireccionamiento(mnemonico, variable,1)
	def GettDireccion(self):
		return self.dirMem



		
  

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
		self.etiqfinal[etiquetas[self.i]]=direccion
		self.i=self.i+1
	def GettEFinal(self):
		return self.etiqfinal


#main provicional
doc=Lector('68HC11.csv')
doc.CreandoDiccionario()
documento = doc.getArchivo()
documento=LectorTxt('START.asc')
Tlineas=LeerLineas(documento.getArchivoTxt())
analizadorDLinea = AnalizarLinea()
separadorDLinea = SepararLinea()
varocons = VariableOConstante()



#Codigo para crear la lista de variables y de etiquetas
for contador in range(1,145):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	if (separadorDLinea.GettEtiqueta() != ''):
		varocons.VarOEtiq(separadorDLinea.GettEtiqueta())
	if(separadorDLinea.GettVariable() != []):
		varocons.agregarVariable(separadorDLinea.GettVariable())

print("Las variables son: "+str(varocons.GettVariables()))
print("Las etiquetas son: "+str(varocons.GettEtiquetas()))

Tlineas.resetLineNumber()

#Encontrando el inicio
while(contador <145):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	if separadorDLinea.GettMnemonico() == 'ORG':
		direc=separadorDLinea.GettDireccionamiento()
		num=int(direc[1:]) 
		dirMemoriaActual=num
		print(dirMemoriaActual)
		contador=145


direccionador = Direccionamiento(doc.getArchivo(), dirMemoriaActual)
variables = varocons.GettVariables()
etiquetas = varocons.GettEtiquetas()


Tlineas.resetLineNumber()
for contador in range(1,145):

	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	print("\nLinea: "+str(Tlineas.getLineNumber()))
	if(etiquetas.count(separadorDLinea.GettEtiqueta()) != 0):
		print(direccionador.GettDireccion())
		varocons.AnadiendoDireccion(direccionador.GettDireccion())
		etiqueta = separadorDLinea.GettEtiqueta()
		print("Etiqueta: "+etiqueta)
	if(separadorDLinea.GettMnemonico()!=''):
		mnemonico = separadorDLinea.GettMnemonico()
		print("Mnemonico: "+mnemonico)

		if(separadorDLinea.GettDireccionamiento().lower() in variables):
			variable = variables[separadorDLinea.GettDireccionamiento().lower()]
		elif(etiquetas.count(separadorDLinea.GettDireccionamiento()) != 0):
			variable = "(Etiqueta) "+separadorDLinea.GettDireccionamiento()
		else:
			variable = separadorDLinea.GettDireccionamiento()

		if(variable!='' or mnemonico!=''):
			print("Variable: "+variable)
			if(variable.find("(Etiqueta)") == -1):
				direccionador.buscarDireccionamiento(mnemonico, variable,1)
			else:
				if separadorDLinea.GettMnemonico() == 'JMP':
					salto = varocons.GettEFinal()
					direccionador.buscarDireccionamiento(mnemonico,salto[separadorDLinea.GettDireccionamiento()],1)
				else:
					dic={}
					direccionador.direccionamientoRelativo(mnemonico, variable.strip("(Etiqueta) "),dic)

print("Las etiquetas son: "+str(varocons.GettEFinal()))
