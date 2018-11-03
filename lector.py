#Clase que lee el archivo cvs
import csv
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
		#print(self.Diccionario)
	def getArchivo(self):
		return self.Diccionario