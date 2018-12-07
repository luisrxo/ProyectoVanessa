from dicc import Dicc
from arch import Archivo
from lines import LeerLineas
from analLine import AnalizarLinea
from toc import Toc

handler=Dicc()
reg=handler.GettReg()
mnem=handler.GettMnemonicos()

lines=[]

exito = 0
while(exito==0):
	try:
		rutaArchivoAsc = input("Nombre de archivo.asm: ")
		documento=Archivo(rutaArchivoAsc)
		exito = 1
	except FileNotFoundError:
		print("\n\tArchivo "+rutaArchivoAsc+" no existe. Intente de nuevo.\n")

	
Tlineas=LeerLineas(documento.getArchivo())

lain=Tlineas.getlin()
for line in lain:
	line=line.strip('\n ')
	lines.append(line.split(' '))
print(lines)

handler2=AnalizarLinea()
#primer pasada
handler2.Analizar(lines,mnem,documento.getArchivo(),1,reg,rutaArchivoAsc)
#segunda pasada
handler2.Analizar(lines,mnem,documento.getArchivo(),0,reg,rutaArchivoAsc)
print(rutaArchivoAsc)

try:
		rutaArchivoO = rutaArchivoAsc[0:-4]+'.O'
		print(rutaArchivoO)
		documento1=Archivo(rutaArchivoO)
except FileNotFoundError:
		print("\n\tArchivo "+rutaArchivoO+" no existe. Intente de nuevo.\n")


line1= documento1.getArchivo().readlines()

handler3=Toc()


handler3.analizaTodo(line1)





