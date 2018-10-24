import csv
from analizar_linea import AnalizarLinea
from buscar_direccionamiento import buscarDireccionamiento
from buscar_mnemonico import BuscarMnemonico
from lector_txt import LectorTxt
from lector import  Lector
from leer_lineas import LeerLineas

#instancia lector con programa a leer
documento=LectorTxt('START.asc')
#instancia objeto clase Leer Lineas y pasa como atributo el texto abierto 
Tlineas=LeerLineas(documento.getArchivoTxt())
#instancia objeto de la clase Analizar linea
analizadorDLinea = AnalizarLinea()
#for para incrementar linea
i=0
conta=0
cont=0
con=0
for contador in range(1,80):
	#manda linea a anlizar del archivo 
	validado = analizadorDLinea.Analizar(Tlineas.MandarLinea())
	#si la linea empieza  con un espacio o tabulador es un mnemonico  se quito validado[0] == ' ' or
	if ( validado[0]=='\t'):
		print('Mnemonico: ' + validado)
		#separando mnemonico y direccionamiento  
		contaba=0
		a=0
		#eliminar espacios en blanco antes del mnemonico

		while a<len(validado):
			contaba=contaba+1
			
			if(validado[a]!=' ' or validado[a]!='\t') and (type('a')==type(validado[a])):
				a=len(validado)
			a=a+1


		a=0
		cont=contaba
		inicio=contaba
		while contaba < len(validado):

			cont=cont+1
			if(validado[contaba]==' ' or validado[contaba] =='\t'):
				#sale del for 
				contaba=len(validado)
			contaba=contaba+1

		mnemo=validado[inicio:cont-1]
		print ('Mnemonico:'+ mnemo)
		con=cont
		conta=cont

		while con < len(validado):

			conta=conta+1
			if(type('a')==type(validado[con])):
				con=len(validado)
			con=con+1

		direc=validado[conta-1:len(validado)]
		print ('Direccionamiento:'+ direc)

	#si la linea empieza con algun caracter es una variable constante o etiqueta :)

	else:
		if (type(validado[0]) == type('a') and validado[0]!='\n' and validado.count('*',0,len(validado)-1)<1):
			print('Vairable,constante o etiqueta	: '+ validado)
		else:
			#no se haha 
			print(validado)
