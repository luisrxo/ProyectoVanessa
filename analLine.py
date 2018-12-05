class AnalizarLinea:
	ctn=[]
	var=[]
	lab=[]
	def Analizar(self,linea,dic,archivo):
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
							self.ctn.append([str(c),linea[x][0],linea[x][1]])
							c=c+1		
							print(self.ctn)
							x=x+1
					if linea [x][1] == 'variables':
						x=x+1
						c=2000
						while x<len(linea) and linea [x][0] != 'section':
							self.var.append([str(c),linea[x][0],linea[x][1]])
							c=c+1
							print(self.var)
							x=x+1
					else: 
						try:
							next(archivo)
						except StopIteration:
							print("nada")
					try:		
						print(str(linea[x]))
						if  linea [x][1] == 'codigo'and len(linea[x])>1:
							x=x+1
							c=3000
							while x<len(linea) and linea [x][0] != 'section' :
								ayuda=linea[x][0]

								x=x+1
								if((ayuda[0])=='\t'):
									ayuda=ayuda.strip(' \t')
									try:
									print("\t "+ayuda+ "  conversion:  "+ str(dic[ayuda]))

									except KeyError:

										print("El mnemonico no existe \n")

								else:

									self.lab.append([str(c),linea[x][0],linea[x][1]])
									c=c+1
									print(self.lab)
						else:
							try:
								next(archivo)
							except StopIteration:
								print("")
					except IndexError:
						if(x<len(linea)):
							x=x+1
						else:
							x=len(linea)
