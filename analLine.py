from crearobj import CrearObj

class AnalizarLinea:
	ctn={}
	var={}
	lab={}
	objeto=CrearObj()
	direcciones=[]
	writer=CrearObj()
	def Analizar(self,linea,dic,archivo,rec,registros,ruta):
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


										if ((part1 in registros)and (part2 in registros)) and ayuda.find('cmp')==-1 and ayuda.find('and')==-1 and ayuda.find('xor')==-1 and ayuda.find('or')==-1 and ayuda.find('test')==-1:
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
										elif(part1 in registros and part2=="" and ayuda.find('print')==-1):	
											print("un operando")
											manual1=dic[ayuda]
											manual2=registros[part1]
											self.direcciones.append(manual1)
											self.direcciones.append(manual2)
										elif(part1 in self.var and part2=="" and ayuda.find('print')==-1):	
											manual1=dic[ayuda]
											manual2=self.var[part1]
											self.direcciones.append(manual1)
											self.direcciones.append(manual2[1])	
										elif(part1 in self.ctn and part2==""and ayuda.find('print')==-1 ):
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
											manual1=manual1[0]
											manual2=registros[part1]

											self.direcciones.append(manual1)
											self.direcciones.append(manual2) 
										elif(ayuda.find('print')!=-1  and (part1 in self.var) and part2==""):
											manual1=dic[ayuda]
											manual2=self.var[part1]
											print("manual "+ str(manual1))
											self.direcciones.append(manual1[1])
			
											self.direcciones.append(manual2[1])
										elif(ayuda.find('print')!=-1 and part1 in self.ctn and part2==""):
											manual1=dic[ayuda]
											manual2=self.ctn[part1]
											self.direcciones.append(manual1[1])
											self.direcciones.append(manual2[1])
										elif(ayuda.find('print')!=-1  and part1!="" and part2!="" and ayuda.find('read')==-1 and ayuda.find('tff')==-1):
											manual1=dic[ayuda]
											if(part1 in self.var and int(part2)<=1999): 	
												manual2=self.var[part1]
												self.direcciones.append(manual1[0])
												self.direcciones.append(manual2[1])
												self.direcciones.append(part2)
											elif(part1 in self.ctn and int(part2)<=1999):
												manual2=self.ctn[part1]
												self.direcciones.append(manual1[0])
												self.direcciones.append(manual2[1])
												self.direcciones.append(part2)
										elif (part1 in registros)and (part2 in registros) and (ayuda.find('cmp')!=-1 or ayuda.find('and')!=-1 or ayuda.find('xor')!=-1 or ayuda.find('or')!=-1 or ayuda.find('test')!=-1):
												
												manual1=dic[ayuda]
												manual2=registros[part1]
												manual3=registros[part2]
												self.direcciones.append(manual1)
												self.direcciones.append(manual2)
												self.direcciones.append(manual3)
										elif(ayuda.find('print')==-1  and part1!="" and part2!="" and (ayuda.find('read')!=-1 or ayuda.find('tff')!=-1)):
												manual1=dic[ayuda]
												if(part1 in self.var and int(part2)<=1999): 	
													manual2=self.var[part1]
													self.direcciones.append(manual1)
													self.direcciones.append(manual2[1])
													self.direcciones.append(part2)
												elif(part1 in self.ctn and int(part2)<=1999):
													manual2=self.ctn[part1]
													self.direcciones.append(manual1)
													self.direcciones.append(manual2[1])
													self.direcciones.append(part2)
									except KeyError:

										print("El mnemonico no existe \n")
									except IndexError:
										print("out of bounds")

								elif(ayuda[0]!='\t'):

									self.lab.update({linea[x-1][0].strip(':'):str(c)})
									c=c+1
									print("etiquetas: "+str(self.lab))
									if(rec==0):
										self.direcciones.append(str(c))
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

		self.AlArchivo(self.direcciones,ruta)
	def AlArchivo(self,direcciones,ruta):
		conthex=0
		obj=""
		print("\t")
		for key in self.ctn:
			print(self.ctn[key])
			print(key)
			obj=obj+('; '+' Traduccion: '+(self.ctn[key])[0]+' nombre: '+key+' Valor:  '+(self.ctn[key])[1]+'\n')
		print(obj)
		for key in self.var:
			print(self.var[key])
			obj=obj+('; '+' Traduccion: '+(self.var[key])[0]+' nombre: '+key+' Valor:  '+(self.var[key])[1]+'\n')
		for key in self.lab:
			print(self.lab[key])
			obj=obj+('; '+' Traduccion: '+(self.lab[key])+' nombre: '+key+'\n')

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
		self.writer.Crear(ruta,obj)
		

