class AnalizarLinea:
	ctn=[]
	var=[]
	lab=[]
	def Analizar(self,linea,dic,archivo):
		for x in range (len(linea)):
			if len(linea[x])<1:
				try:
					next(archivo)
				except StopIteration:
					print("nada")
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
				if linea [x][1] == 'codigo':
					print("ya entro")
					x=x+1
					c=3000
					while x<len(linea) and linea [x][0] != 'section' :
						ayuda=linea[x][0]
						print(ayuda)
						if((ayuda[0])=='\t'):
							print("entra")
							x=x+1

							"""try:
								#memoria=memoria.append(dic[(linea[x][0]).strip(' \t')])
							except KeyError:

								print("El mnemonico no existe \n")"""

						else:
	
							self.lab.append([str(c),linea[x][0],linea[x][1]])
							c=c+1
							print(self.lab)
							x=x+1
				else:
					try:
						next(archivo)
					except StopIteration:
						print("nada")
