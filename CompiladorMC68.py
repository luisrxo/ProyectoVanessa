import csv

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
documento=LectorTxt('START.asc')
manejoE=Errores()
Tlineas=LeerLineas(documento.getArchivoTxt())
analizadorDLinea = AnalizarLinea()
separadorDLinea = SepararLinea()
varocons = VariableOConstante()



#Codigo para crear la lista de variables y de etiquetas
for contador in range(1,150):
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
while(contador <150):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	if separadorDLinea.GettMnemonico() == 'ORG':
		direc=separadorDLinea.GettDireccionamiento()
		num=hex(int("0x"+direc[1:], 16))
		dirMemoriaActual=num
		print("dirMemoriaActual: "+str(dirMemoriaActual))
		contador=150

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

for contador in range(1,150):
	separadorDLinea.Separando(analizadorDLinea.Analizar(Tlineas.MandarLinea()))
	print("\nLinea: "+str(Tlineas.getLineNumber()))
	if(etiquetas.count(separadorDLinea.GettEtiqueta()) != 0):
		print("direccionador.GettDireccion(): "+str(direccionador.GettDireccion()))
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
				direccionador.buscarDireccionamiento(mnemonico, variable,1,manejoE,Tlineas.getLineNumber())
			else:
				if separadorDLinea.GettMnemonico() == 'JMP':
					salto = varocons.GettEFinal()
					direccionador.buscarDireccionamiento(mnemonico,salto[separadorDLinea.GettDireccionamiento()],1,manejoE,Tlineas.getLineNumber())
				else:
					dic={}
					direccionador.direccionamientoRelativo(mnemonico, variable.strip("(Etiqueta) "),dic,manejoE,Tlineas.getLineNumber(), segFor)

dicEtiq = varocons.GettEFinal()

print("Las etiquetas son: "+str(dicEtiq))

Tlineas.resetLineNumber()
direccionador.resetDirMem(dirMemoriaActual)
# 2da Compilacion
segFor = 1
print("\n--- SEGUNDA PASADA ---")
for contador in range(1,150):
	lineaAsc = Tlineas.MandarLinea()
	noLineaAsc = str(Tlineas.getLineNumber())
	separadorDLinea.Separando(analizadorDLinea.Analizar(lineaAsc))
	if(etiquetas.count(separadorDLinea.GettEtiqueta()) != 0):
		direccion = direccionador.GettDireccion()
		direccion = direccion[2:]
		etiqueta = separadorDLinea.GettEtiqueta()
	if(separadorDLinea.GettMnemonico()!=''):
		mnemonico = separadorDLinea.GettMnemonico()

		if(separadorDLinea.GettDireccionamiento().lower() in variables):
			variable = variables[separadorDLinea.GettDireccionamiento().lower()]
		elif(etiquetas.count(separadorDLinea.GettDireccionamiento()) != 0):
			aux = dicEtiq[separadorDLinea.GettDireccionamiento()]
			variable = aux[2:]
		else:
			variable = separadorDLinea.GettDireccionamiento()

		if(variable!='' or mnemonico!=''):
			if(variable.find("(Etiqueta)") == -1):
				direccionador.buscarDireccionamiento(mnemonico, variable,1,manejoE,Tlineas.getLineNumber())
			else:
				if separadorDLinea.GettMnemonico() == 'JMP':
					salto = int("0x"+direccionador) - variable
					direccionador.buscarDireccionamiento(mnemonico,salto[separadorDLinea.GettDireccionamiento()],1,manejoE,Tlineas.getLineNumber())
				else:
					dic={}
					direccionador.direccionamientoRelativo(mnemonico, variable.strip("(Etiqueta) "),dic,manejoE,Tlineas.getLineNumber(), segFor)

#print("Las etiquetas son: "+str(varocons.GettEFinal()))
#ya lo cambie
