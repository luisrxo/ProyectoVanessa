from crearobj import CrearObj

class AnalizarLinea:
	ctn={}
	var={}
	lab={}
	objeto=CrearObj()
	direcciones=[]
	def Analizar(self,linea,dic,archivo,rec,registros):
		x=0
		while x < (len(linea)):
			print(x)
			print(str(linea[x]))
			print(str(len(linea[x])))
			if len(linea[x])<1:
				try:
					next(archivo)
				except StopIteration:
					print("")
			else:
				if linea[x][0]=='section':
					if linea [x][1]== 'constantes':
						x=x+1
						c=1000
						while x<len(linea) and linea [x][0] != 'section':
							self.ctn.update({linea[x][0].strip('\t'):[str(c),linea[x][1]]})
							c=c+1		
							print(self.ctn)
							x=x+1
					if linea [x][1] == 'variables':
						x=x+1
						c=2000
						while x<len(linea) and linea [x][0] != 'section':
							self.var.update({linea[x][0].strip('\t'):[str(c),linea[x][1]]})
							c=c+1
							print(self.var)
							x=x+1
					else: 
						try:
							next(archivo)
						except StopIteration:
							print("nada")
					try:		
						if  linea [x][1] == 'codigo'and len(linea[x])>1 and rec==0:
							x=x+1
							c=3000
							while x<len(linea) and linea [x][0] != 'section' :
								ayuda=linea[x][0]


								x=x+1
								if((ayuda[0])=='\t'):
									try:
										st=linea[x-1][1]
										print("print string: "+st)
										if(st.find(',')!=-1):
											print("va a separar")
											part1=st[:st.find(',')]
											part2=st[st.find(',')+1:]
											print("parte1  "+ part1 + "  parte2  "+ part2)
											print(str(self.ctn))	
											if(part1 in registros):		
												print("si está ")

									except IndexError:
										print ("")
										ayuda=ayuda.strip(' \t')
									try:
										ayuda=ayuda.strip(' \t')
										print("ayuda   "+ayuda)
										print("\t "+ayuda+ "  conversion:  "+ str(dic[ayuda]))
										print("parte1  "+ part1 + "  parte2  "+ part2)

										if (part1 in registros)and (part2 in registros):
											print("primero")
										elif ((part1 in registros) and (part2 in self.var))or((part1 in registros) and (part2 in self.ctn)):
											print("segundo")
											
										elif ((part1 in self.var) and (part2 in registros)) or ((part1 in self.ctn) and (part2 in registros)):
											print("tercero")
										elif ((part1 in self.var) and (part2 in self.var)) or ((part1 in self.ctn) and (part2 in self.ctn)):
											print("cuarto")

											

										
									except KeyError:

										print("El mnemonico no existe \n")

								else:

									self.lab.update({linea[x][0]:str(c)})
									c=c+1
									print(self.lab)
						else:
							print("se va al else")
							x=x+1

							try:
								next(archivo)
							except StopIteration:
								print("")
					except IndexError:
						if(x<len(linea)):
							x=x+1
						else:
							x=len(linea)
				else:
					x=x+1

		self.AlArchivo(self.direcciones)
	def AlArchivo(self,direcciones):
		conthex=0
		obj=""
		for a in direcciones:
			print(a)
			if (len(a)<5):
				obj=obj+' '+str(a)
				conthex=conthex+1
			elif conthex==4:
				obj = obj+'\n'
				conthex=0
		print(obj)
