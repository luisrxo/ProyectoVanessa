from direccionamiento import Direccionamiento
from separarLinea import SepararLinea
from lectorTxt import LectorTxt
from lector import Lector
from leerLineas import LeerLineas
from analizarLinea import AnalizarLinea
from variableOconstante import VariableOConstante
from errores import Errores

#main provicional
doc=Lector('68HC11.csv')
doc.CreandoDiccionario()
documento = doc.getArchivo()
exito = 0
while(exito==0):
	try:
		rutaArchivoAsc = input("Nombre de archivo.asc: ")
		documento=LectorTxt(rutaArchivoAsc)
		exito = 1
	except FileNotFoundError:
		print("\n\tArchivo "+rutaArchivoAsc+" no existe. Intente de nuevo.\n")


manejoE=Errores()
Tlineas=LeerLineas(documento.getArchivoTxt())
analizadorDLinea = AnalizarLinea()
separadorDLinea = SepararLinea()
varocons = VariableOConstante()
varc=0
lain=Tlineas.getlin()
for conli in lain:
	varc=varc+1


#Codigo para crear la lista de variables y de etiquetas
for contador in range(1,varc):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	if (separadorDLinea.GettEtiqueta() != ''):
		varocons.VarOEtiq(separadorDLinea.GettEtiqueta())
	if(separadorDLinea.GettVariable() != []):
		varocons.agregarVariable(separadorDLinea.GettVariable())

print("Las variables son: "+str(varocons.GettVariables()))
print("Las etiquetas son: "+str(varocons.GettEtiquetas()))

Tlineas.resetLineNumber()

dirMemoriaActual= hex(0)

#Encontrando el inicio
while(contador <varc):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	if separadorDLinea.GettMnemonico() == 'ORG':
		direc=separadorDLinea.GettDireccionamiento()
		num=hex(int("0x"+direc[1:], 16))
		dirMemoriaActual=num
		print("dirMemoriaActual: "+str(dirMemoriaActual))
		contador=150
	else:
		dirMemoriaActual = "0x8000"
# Hay que contemplar caso en el que no hay ORG


direccionador = Direccionamiento(doc.getArchivo(), dirMemoriaActual)
variables = varocons.GettVariables()
etiquetas = varocons.GettEtiquetas()

Tlineas.resetLineNumber()
segFor = 0
print("\n--- PRIMERA PASADA ---")

"""for contador in range(1,150):
    separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
    if(etiquetas.count(separadorDLinea.GettEtiqueta()) != 0):
        varocons.AnadiendoDireccion(direccionador.GettDireccion())
        etiqueta = separadorDLinea.GettEtiqueta()
		#print("Etiqueta: "+etiqueta)
Tlineas.resetLineNumber()"""

banderaEtiqueta  = False
label = ""
banderaAux = False

for contador in range(1,varc):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	print("\nLinea: "+str(Tlineas.getLineNumber()))
	if banderaAux:
		banderaAux = False
		varocons.AnadiendoDireccion(direccionador.GettDireccion())
		print("Etiqueta: "+label)
		label = ""
	if(etiquetas.count(separadorDLinea.GettEtiqueta()) != 0):
		print("direccionador.GettDireccion(): "+str(direccionador.GettDireccion()))
		banderaEtiqueta = True
		label = separadorDLinea.GettEtiqueta()
	if(separadorDLinea.GettMnemonico()!=''):
		mnemonico = separadorDLinea.GettMnemonico()
		if banderaEtiqueta:
			banderaAux = True
			banderaEtiqueta = False
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
				direccionador.buscarDireccionamiento(mnemonico, variable,1,manejoE,Tlineas.getLineNumber())
			else:
				if separadorDLinea.GettMnemonico() == 'JMP':
					salto = varocons.GettEFinal()
					# Parámetros: buscarDireccionamiento(mnemonico, variable,relativo,manejo,lineas)
					direccionador.direccionamientoRelativo(mnemonico,1,manejoE,Tlineas.getLineNumber())
				else:
					dic={}
					# Parámetros: direccionamientoRelativo(mnemonico, variable, manejo, lineas, salto=0)
					direccionador.direccionamientoRelativo(mnemonico, variable.strip("(Etiqueta) "), manejoE, Tlineas.getLineNumber())

dicEtiq = varocons.GettEFinal()

print("Las etiquetas son: "+str(dicEtiq))

direcciones=[]
aqui=''

Tlineas.resetLineNumber()
direccionador.resetDirMem(dirMemoriaActual)
# 2da Compilacion
segFor = 1
print("\n--- SEGUNDA PASADA ---")
etiqueta = ""
mnemonico = ""
variable = ""
obj = ""
listado = ""
indice = 0

for contador in range(1,varc):
	codigo_objeto = ""
	lineaAsc = Tlineas.MandarLinea()
	noLineaAsc = str(Tlineas.getLineNumber() + 1)
	separadorDLinea.Separando(analizadorDLinea.Analizar(lineaAsc))
	direccion = direccionador.GettDireccion()
	direccion = direccion[2:]
	if(len(lineaAsc.strip(' \t\n')) != 0):
		if(etiquetas.count(separadorDLinea.GettEtiqueta()) != 0):
			etiqueta = separadorDLinea.GettEtiqueta()
		if(separadorDLinea.GettMnemonico()!=''):
			mnemonico = separadorDLinea.GettMnemonico()

			if(separadorDLinea.GettDireccionamiento().lower() in variables):
				# Instrucción tiene un operando que es una variable o constante
				variable = variables[separadorDLinea.GettDireccionamiento().lower()]
				# Parámetros: buscarDireccionamiento(mnemonico, variable, relativo, manejo, lineas)
				direccionador.buscarDireccionamiento(mnemonico, variable, 1, manejoE, Tlineas.getLineNumber())
				codigo_objeto = direccionador.getObjCode()
			elif(etiquetas.count(separadorDLinea.GettDireccionamiento()) != 0):
				# Instrucción tiene un operando que es una etiqueta. Puede tener modo de direccionamiento relativo.
				aux = dicEtiq[separadorDLinea.GettDireccionamiento()]
				variable = aux[2:]
				salto = hex((int("0x"+variable, 16)) - (int("0x"+direccion, 16)) )
				if(int(salto, 16)<0):
					salto = hex(int(salto, 16) - 2)
				print("Salto: "+salto)
				print("Variable: "+variable)
				print("Direccion: "+direccion)
				# Se busca modo de direccionamiento, empezando por direccionamiento relativo. En caso de que no sea relativo,
				# el método buscarDireccionamientoRelativo invocará otro método para buscar otros posibles modos de direccionamiento.
				# Parámetros: direccionamientoRelativo(mnemonico, variable, manejo, lineas, salto=0)
				direccionador.direccionamientoRelativo(mnemonico, variable, manejoE, Tlineas.getLineNumber(), salto)
				codigo_objeto = direccionador.getObjCode()
				"""if separadorDLinea.GettMnemonico() == 'JMP':
					direccionador.buscarDireccionamiento(mnemonico, salto, 1, manejoE, Tlineas.getLineNumber())
				else:
					direccionador.direccionamientoRelativo(mnemonico, salto, dic, manejoE, Tlineas.getLineNumber(), segFor)"""
			else:
				# Instrucción tiene un operando que es un valor hard-coded en la misma línea de código
				variable = separadorDLinea.GettDireccionamiento()
				# Parámetros: buscarDireccionamiento(mnemonico, variable, relativo, manejo, lineas)
				direccionador.buscarDireccionamiento(mnemonico, variable, 0, manejoE, Tlineas.getLineNumber())
				codigo_objeto = direccionador.getObjCode()
		
	"""else:
		codigo_objeto = """""
	# Formato del archivo listado
	lineaListado = noLineaAsc + ": " + direccion + " (" + codigo_objeto + ")   :   " + lineaAsc + "\n"
	listado = listado + lineaListado
	conthex=0
	#Guarde todos los codigos objeto en una lista de dos en dos, y si encontraba un org entonces tambien lo agregaba a la lista
	if (lineaAsc.find('ORG')!=-1):
		aqui=separadorDLinea.GettDireccionamiento()
		direcciones.append(aqui[1:])
	for a in codigo_objeto:
		if conthex == 1:
			direcciones.append(codigo_objeto[0:2])
			conthex=0
			codigo_objeto = codigo_objeto[2:]
		else:
			conthex = conthex+1
	print("LST: "+lineaListado)
	#Con el programa de abajo fui recorrientdo la lista, si un elemento tenia una longitud mayor a dos entonces es un org
#Y modifique la linea para que empezara desde esa linea
#Espero que sea intuitivo
conthex=0
actual=''
for a in direcciones:
	if (len(a)>2):
		obj=obj+'\n'
		obj=obj+'<'+a+'>'
		actual = a
	else:
		obj=obj+' '+a
		conthex=conthex+1
		if conthex==16:
			obj = obj+'\n'
			obj = obj + '<'+str(hex(int("0x"+actual, 16)+16))[2:]+'>'
			actual = hex(int("0x"+actual, 16)+16)[2:]
			conthex=0
print (direcciones)
try:
	archivo = open(rutaArchivoAsc[0:-4]+'.lst', 'w') 
	archivo.write(listado)
	archivo.close()
	archivo = open(rutaArchivoAsc[0:-4]+'.hex', 'w') 
	archivo.write(obj)
	archivo.close()
except Exception:
	print("Hubo un error al guardar archivos")
