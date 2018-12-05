class AnalizarLinea:
	ctn=[]
	var=[]
	lab=[]
	def Analizar(self,linea,dic):
		for x in range (len(linea)):
			if len(linea[x])<1:
				linea.next()
			if linea[x][0]=='section':
				if linea [x][1]== 'constantes':
					x=x+1
					c=1000
					while x<len(linea) and linea [x][0] != 'section':
						self.ctn.append([str(c),linea[x][4],linea[x][5]])
						c=c+1		
						print(self.ctn)
						x=x+1
				if linea [X][1] == 'variables':
					x=x+1
					c=2000
					while x<len(linea) and linea [X][0] != 'section':
						self.var.append([str(c),linea[x][4],linea[X][5]])
						c=c+1
						print(self.var)
						x=x+1
				else: 
					linea.next()
				if linea [X][1] == 'codigo':
					x=x+1
					c=3000
					while x<len(linea) and linea [X][0] != 'section':
						if(linea[X][0]=='\t'):
							try:
								memoria=memoria.append(dic[(linea[x][0]).strip(' \t')])
							except KeyError:
								print("El mnemonico no existe \n")
						else:
	
							self.lab.append([str(c),linea[X][4],linea[X][5]])
							c=c+1
							print(self.lab)
							x=x+1
						
