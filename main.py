from dicc import Dicc
from arch import Archivo
from lines import LeerLineas
from analLine import AnalizarLinea

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

handler2.Analizar(lines,mnem)






