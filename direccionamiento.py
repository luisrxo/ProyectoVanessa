class Direccionamiento:
	def __init__(self, DiccionarioDireccionamiento, dirMem):
		self.Direccionamientos = DiccionarioDireccionamiento
		self.dirMem = dirMem
		self.labels = {}
		self.objCode = ""
		#print(self.Direccionamientos)
	# Formato de banderas: 
	# [  1,  2,    3,     4,    5,    6,  7 ]
	# [IMM, DIR, IND,X, IND,Y, EXT, INH, REL]
	def buscarDireccionamiento(self, mnemonico, variable,relativo,manejo,lineas):
		bandera = [0]
		self.objCode = ""

		if (str(variable).find('$') != -1 and (str(variable).find('#')==-1)):
			if (len(variable[1:])%2 != 0):
				variable = '$' + '0' + variable[1:len(variable)]

		variable = str(variable)
		if(variable.find("\'") != -1):
			indice = variable.find("'")
			variable = str(ord(variable[indice+1]))
			#print("Código ASCII: "+variable)
		try:
			direccionamientos = self.Direccionamientos[mnemonico.lower()]
			if(str(variable).find('#')==-1):
				if str(variable) =='':
					# Direccionamiento inherente
					if(direccionamientos[5] != 0):
						bandera = direccionamientos[5]
						#print("Direccionamiento inherente")
					else:
						manejo.error6(lineas)
				else:
					if(variable.find(',') == 3):
						if(variable.find('X') == 4):
							# Direccionamiento indexado respecto a X
							if len(variable) > 5:
								manejo.error7(lineas)
							elif(direccionamientos[2] != 0):
								bandera = direccionamientos[2]
								#print("Direccionamiento indexado respecto a X")
							else:
								print("Error")
						elif(variable.find('Y') == 4):
							# Direccionamiento indexado respecto a Y
							if len(variable) > 5:
								manejo.error7(lineas)
							elif(direccionamientos[3] != 0):
								bandera = direccionamientos[3]
								#print("Direccionamiento indexado respecto a Y")
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
								manejo.error7(lineas)
							else:
								bandera = direccionamientos[4]
								#print("Direccionamiento extendido")
						else:
							manejo.error7(lineas)
					elif(len(variable) >=1):
						# Direccionamiento directo
						if(direccionamientos[1] != 0):
							bandera = direccionamientos[1]
							#print("Direccionamiento directo")
							#hexadecimal
							if(variable[0]!='$'):
								hexa=hex(int(variable))
								variable=str(hexa).upper()
								variable=variable[2:len(variable)]
							if len(variable) > 3:
								manejo.error7(lineas)
							else:
								bandera = direccionamientos[1]
								#print("Direccionamiento directo")
						else:
							print("Error")
			elif(direccionamientos[0]!=0):
				# Direccionamiento inmediato o relativo
					if(variable[1]!='$' and variable[1]!="'"):
						hexa=hex(int(variable[1:]))
						variable=str(hexa).upper()
						variable=variable[2:len(variable)]
					if len(variable) > 6 :
						manejo.error7(lineas)
					bandera = direccionamientos[0]
					#print("Direccionamiento inmediato")
			else:
				if (relativo != 0):
					if(direccionamientos[6]!=0):
						self.dirMem = self.dirMem + int(bandera[len(bandera)-1])

					
			#print(str(self.dirMem)+", "+str(bandera))
			self.dirMem = hex(int("0x"+self.dirMem[2:], 16) + int(bandera[len(bandera)-1]))
			variable = variable.strip('#$')
			if(variable.find("0x") != -1):
				variable = variable[2:]
			self.objCode = str(bandera[0]) + variable
			#print("OpCode, tamanio , direccionamiento  : "+str(bandera)+" : Variable: " +str(variable)+" Mem: "+str(self.dirMem))
		
		except KeyError:
			if(mnemonico=='ORG'):
				self.dirMem="0x"+variable[1:]
			elif(mnemonico=='FCB'):
				print()

			else:
				manejo.error4(lineas)
	def direccionamientoRelativo(self, mnemonico, variable, manejo, lineas, salto=0):
		self.objCode = ""
		try:
			direccionamiento = self.Direccionamientos[mnemonico.lower()]
			if (not(variable in self.labels)):
				self.labels[variable] = self.dirMem
			else:
				variable=self.labels[variable]

			if(direccionamiento[6] != 0):
				bandera = direccionamiento[6]
				#print("Direccionamiento relativo")
				#salto=3 #hex(self.dirMem-self.listEti[variable])
				self.dirMem = hex(int("0x"+self.dirMem[2:], 16) + int(bandera[len(bandera)-1]))
				salto = str(salto)
				print(salto)
				if(int(salto,16)< -127 or int(salto,16) >127):
					manejo.error8(lineas)
				else:
					if(len(salto)==4 and salto[0]=='-'):					
						self.objCode = str(bandera[0]) +"0"+salto[3:]
					elif(len(salto)==5 and salto[0]=='-'):
						self.objCode = str(bandera[0]) +salto[3:]
					elif(len(salto)==3):
						self.objCode = str(bandera[0]) +"0"+salto[2:]
					else:
						self.objCode = str(bandera[0]) + salto[2:]
				#print("OpCode, tamanio , direccionamiento  : "+str(bandera)+" : Variable(rel) " +str(salto)+" Mem: "+str(self.dirMem))
			else:
				self.buscarDireccionamiento(mnemonico, variable,1,manejo,lineas)
		except KeyError:
			manejo.error4(lineas)
	def getObjCode(self):
		return self.objCode
	def GettDireccion(self):
		return self.dirMem
	def resetDirMem(self, dirMemoria):
		self.dirMem = dirMemoria
