import csv


#Clase que abre el archivo TXT
class LectorTxt:

def _init_(self,archivo):
self.abierto = open(archivo)

def getArchivoTxt(self):
return self.abierto


#Clase que lee el archivo cvs
class Lector:

def _init_(self, archivo):
self.documento = open(archivo)
self.mnemonicos=csv.reader(self.documento)
#Metodo usado para devolver el archivo leido.
def getArchivo(self):
return self.mnemonicos


#Clase que busca el mnemonico en el archivo cvs
class BuscarMnemonico:

def _init_(self,archivocvs):
self.mnemonicos = archivocvs
self.buscarD = buscarDireccionamiento (archivocvs)
#Metodo que busca el mnemonico en todo el set de instrucciones
def buscarMnemonico(self,mnemonico):
for listaMnemonico in self.mnemonicos:
if (listaMnemonico[1] == mnemonico):
self.buscarD.metodoDeDireccionamiento(listaMnemonico)


#Clase que busca el metodo de direccionamiento
class buscarDireccionamiento:

def _init_(self,archivocvs):
self.mnemonicos = archivocvs

#Metodo que busca el metodo de direccionamiento
def metodoDeDireccionamiento(self,lista):
print(lista)




#Abrir el archivo TXT
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
#si la linea empieza con un espacio o tabulador es un mnemonico se quito validado[0] == ' ' or
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

#si la linea empieza con algun caracter es una variable constante o etiqueta ￼

else:
if (type(validado[0]) == type('a') and validado[0]!='\n' and validado.count('*',0,len(validado)-1)<1):
print('Vairable,constante o etiqueta : '+ validado)
else:
#no se haha 
print(validado)
