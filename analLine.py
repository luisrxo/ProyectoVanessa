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
			print(str(linea[x]))
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
							print("\t")
					try:		
						if  linea [x][1] == 'codigo'and len(linea[x])>1 :
							x=x+1
							c=3000
							while x<len(linea) and linea [x][0] != 'section' :
								ayuda=linea[x][0]


								x=x+1
								print("ayuda"+ayuda)
								if((ayuda[0])=='\t' and rec==0):
									try:
										st=linea[x-1][1]
										if(st.find(',')!=-1):

											part1=st[:st.find(',')]
											part2=st[st.find(',')+1:]
											print(str(self.ctn))	
										elif(st!=""):
											part1=st
											part2=""
										else:
											part1=""
											part2=""

									except IndexError:
										print ("")
										ayuda=ayuda.strip(' \t')
										part1=""
										part2=""
									try:
										ayuda=ayuda.strip(' \t')
										
										print("\t "+ayuda+ "  conversion:  "+ str(dic[ayuda]))


										if (part1 in registros)and (part2 in registros):
											print("primero")
											manual1=dic[ayuda]
											manual2=registros[part1]
											manual3=registros[part2]
											self.direcciones.append(manual1[0])
											self.direcciones.append(manual2)
											self.direcciones.append(manual3)
										elif (part1 in registros) and (part2 in self.ctn):
											manual1=dic[ayuda]
											manual2=registros[part1]
											manual3=self.ctn[part2]
											print("segundo")
											self.direcciones.append(manual1[2])
											self.direcciones.append(manual2)
											self.direcciones.append(manual3[1])
										elif (part1 in registros) and (part2 in self.var):
											print("tercero")
											manual1=dic[ayuda]
											manual2=registros[part1]
											manual3=self.var[part2]
											self.direcciones.append(manual1[2])
											self.direcciones.append(manual2)
											self.direcciones.append(manual3[1])
										elif (part1 in self.var) and (part2 in registros):
											print("cuarto")
											manual1=dic[ayuda]
											manual2=self.var[part1]
											manual3=registros[part2]
											self.direcciones.append(manual1[1])
											self.direcciones.append(manual2[1])
											self.direcciones.append(manual3)
										elif (part1 in self.ctn) and (part2 in registros):
											print("quinto")
											manual1=dic[ayuda]
											manual2=self.ctn[part1]
											manual3=registros[part2]
											self.direcciones.append(manual1[1])
											self.direcciones.append(manual2[1])
											self.direcciones.append(manual3)
										elif (part1 in self.var) and (part2 in self.var): 
											print("sexto")
											manual1=dic[ayuda]
											manual2=self.var[part1]
											manual3=self.var[part2]
											self.direcciones.append(manual1[3])
											self.direcciones.append(manual2[1])
											self.direcciones.append(manual3[1])
										elif (part1 in self.ctn) and (part2 in self.ctn):
											print("septimo")
											manual1=dic[ayuda]
											manual2=self.ctn[part1]
											manual3=self.ctn[part2]
											self.direcciones.append(manual1[3])
											self.direcciones.append(manual2[1])
											self.direcciones.append(manual3[1])
										elif(ayuda in dic and part1=="" ):
											print("nada")
											self.direcciones.append(dic[ayuda])
										elif(part1 in registros and part2==""):	
											print("un operando")
											manual1=dic[ayuda]
											manual2=registros[part1]
											self.direcciones.append(manual1)
											self.direcciones.append(manual2)
										elif(part1 in self.var and part2==""):	
											manual1=dic[ayuda]
											manual2=self.var[part1]
											self.direcciones.append(manual1)
											self.direcciones.append(manual2[1])	
										elif(part1 in self.ctn and part2==""):
											manual1=dic[ayuda]
											manual2=self.ctn[part1]
											self.direcciones.append(manual1)
											self.direcciones.append(manual2[1]) 
										elif(ayuda.find('jmp')!=-1 or ayuda.find('call')!=-1) and (part1 in self.lab):
											manual1=dic[ayuda]
											manual2=self.lab[part1]
											self.direcciones.append(manual1)
											self.direcciones.append(manual2) 
										elif(ayuda.find('print')!=-1 and part1 in registros ):
											manual1=dic[ayuda]
											manual2=registros[part1]
											self.direcciones.append(manual1[0])
											self.direcciones.append(manual2) 
										elif(ayuda.find('print')!=-1 and (part1 in self.var or part1 in self.lab or part1 in self.ctn) ):
											manual1=dic[ayuda]
											manual2=registros[part1]
											self.direcciones.append(manual1[1])
											self.direcciones.append(manual2)
										elif(ayuda.find('print')!=-1 and part1!="" and part2!=""):
											manual1=dic[ayuda]
											manual2=registros[part1]
											#FALTA PONER TAM Y MEM 
											self.direcciones.append(manual1[1])
											self.direcciones.append(manual2)	


											

										
									except KeyError:

										print("El mnemonico no existe \n")

								elif(ayuda[0]!='\t'):

									self.lab.update({linea[x-1][0].strip(':'):str(c)})
									c=c+1
									print("etiquetas: "+str(self.lab))
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
		print("\t")
		for a in direcciones:
			#print(a)
			if (len(a)<5):
				if(len(a)==1):
					a='000'+str(a)
				if(len(a)==2):
					a='00'+str(a)	
				if(len(a)==3):
					a='0'+str(a)
				obj=obj+' '+str(a)
				conthex=conthex+1
				if conthex==4:
					obj = obj+'\n'
					conthex=0
		print(obj)
			
