class Toc:

	codigoC=[]
	
	def analizaTodo(self, lines):
		con=0	
		nueva=""
		index=0
		index2=4
		contr=1
		contv=1
		conts=1
		contdec=1
		contresta=1
		contmult=1
		contdiv=1
		continc=1
		contcmp=1
		contP=1

		while con < len(lines):			 

			linea=(lines[con]).replace(' ','')
			nuevalong=linea.replace('\n','')
			if(linea[0]==';'):
				con=con+1
			else:
				
				nueva=nueva+nuevalong
				con=con+1
		
		cadena=0
		print(nueva)
		print(len(nueva))
		print(nueva[index:index2])
			
		while cadena < len(nueva):
			#MOV
			if(nueva[index:index2]=='0010'):
				aux="r"+str(contr)+"="+nueva[index+8:index2+8]
				self.codigoC.append(aux)
				contr=contr+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			elif(nueva[index:index2]=='0011'):
				aux="var"+str(contv)+"="+nueva[index+8:index2+8]
				self.codigoC.append(aux)
				contv=contv+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			elif(nueva[index:index2]=='0012'):
				aux="r"+str(contr)+"="+nueva[index+8:index2+8]
				self.codigoC.append(aux)
				contr=contr+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			elif(nueva[index:index2]=='0013'):
				aux="var"+str(contv)+"="+nueva[index+8:index2+8]
				self.codigoC.append(aux)
				contv=contv+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#PUSH
			elif(nueva[index:index2]=='0014'):
				print("")
				index=index+8
				index2=index2+8
				cadena=cadena+8				
			#POP
			elif(nueva[index:index2]=='0015'):
				print("")
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#ADD
			elif(nueva[index:index2]=='0016' or nueva[index:index2]=='0017' or nueva[index:index2]=='0018' or nueva[index:index2]=='0019' ):
				op1="a"+str(conts)+"="+nueva[index+4:index2+4]
				self.codigoC.append(op1)
				op2="b"+str(conts)+"="+nueva[index+8:index2+8]
				self.codigoC.append(op2)
				other="sum"+str(conts)+"= a"+str(conts)+"+ b"+str(conts)
				self.codigoC.append(other)
				auxsuma=int(nueva[index+8:index2+8],16)+int(nueva[index+4:index2+4],16)
				aux="sum"+str(conts)+"="+str(auxsuma)
				self.codigoC.append(aux)
				conts=conts+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#DEC
			elif(nueva[index:index2]=='001A'):
				dec=int(nueva[index+4:index2+4],16)-1
				aux="dec"+str(contdec)+"="+str(dec)
				self.codigoC.append(aux)
				contdec=contdec+1
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#SUB
			elif(nueva[index:index2]=='001B' or nueva[index:index2]=='001C' or nueva[index:index2]=='001D' or nueva[index:index2]=='001E'):
				op1="c"+str(contresta)+"="+nueva[index+4:index2+4]
				self.codigoC.append(op1)
				op2="d"+str(contresta)+"="+nueva[index+8:index2+8]
				self.codigoC.append(op2)
				other="resta"+str(contresta)+"= d"+str(contresta)+"- c"+str(contresta)
				self.codigoC.append(other)
				auxresta=int(nueva[index+8:index2+8],16)-int(nueva[index+4:index2+4],16)
				aux="rest"+str(contresta)+"="+str(auxresta)
				self.codigoC.append(aux)
				contresta=contresta+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#MUL
			elif(nueva[index:index2]=='001F' or nueva[index:index2]=='0020' or nueva[index:index2]=='0021' or nueva[index:index2]=='0022'):
				op1="e"+str(contmult)+"="+nueva[index+4:index2+4]
				self.codigoC.append(op1)
				op2="f"+str(contmult)+"="+nueva[index+8:index2+8]
				self.codigoC.append(op2)
				other="mult"+str(contmult)+"= e"+str(contmult)+"* f"+str(contmult)
				self.codigoC.append(other)
				auxmult=int(nueva[index+8:index2+8],16)*int(nueva[index+4:index2+4],16)
				aux="mult"+str(contmult)+"="+str(auxmult)
				self.codigoC.append(aux)
				contmult=contmult+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#DIV
			elif(nueva[index:index2]=='0023' or nueva[index:index2]=='0024' or nueva[index:index2]=='0025' or nueva[index:index2]=='0026'):
				op1="g"+str(contdiv)+"="+nueva[index+4:index2+4]
				self.codigoC.append(op1)
				op2="h"+str(contdiv)+"="+nueva[index+8:index2+8]
				self.codigoC.append(op2)
				other="div"+str(contdiv)+"= g"+str(contdiv)+"/ h"+str(contdiv)
				self.codigoC.append(other)
				try: 
					auxdiv=int(nueva[index+8:index2+8],16)/int(nueva[index+4:index2+4],16)
					aux="div"+str(contdiv)+"="+str(auxdiv)
					self.codigoC.append(aux)
					contdiv=contdiv+1
				except ZeroDivisionError:
					print("No se puede divivir entre cero\n")
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#INC
			elif(nueva[index:index2]=='0027'):	
				inc=int(nueva[index+4:index2+4],16)+1
				aux="inc"+str(continc)+"="+str(inc)
				self.codigoC.append(aux)
				continc=continc+1
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#CMP
			elif(nueva[index:index2]=='0028'):
				auxcmp=int(nueva[index+8:index2+8],16)-int(nueva[index+4:index2+4],16)
				aux="cmp"+str(contcmp)+"="+str(auxcmp)
				self.codigoC.append(aux)
				contcmp=contcmp+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#AND
			elif(nueva[index:index2]=='0029'):
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#printN
			elif(nueva[index:index2]=='0036' or nueva[index:index2]=='0037'):
				impN='printf("'+nueva[index+4:index2+4]+'")"'
				self.codigoC.append(impN)
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#printCh
			elif(nueva[index:index2]=='0038' or nueva[index:index2]=='0039'):

				impCh='printf("'+nueva[index+4:index2+4]+'")'
				self.codigoC.append(impCh)
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#printS
			elif(nueva[index:index2]=='003A'):
				impS='printf("'+nueva[index+4:index2+4]+'")'
				self.codigoC.append(impS)
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#readN
			elif(nueva[index:index2]=='003B'):
				aux="cst"+str(contP)+"="+nueva[index+4:index2+4]
				self.codigoC.append(aux)
				leeN='scanf("%d",&cst'+str(contP)+')'
				self.codigoC.append(leeN)
				contP=contP+1
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#readCh
			elif(nueva[index:index2]=='003C'):
				aux="cst"+str(contP)+"="+nueva[index+4:index2+4]
				self.codigoC.append(aux)
				leeN='scanf("%c",&cst'+str(contP)+')'
				self.codigoC.append(leeN)
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#readS
			elif(nueva[index:index2]=='003D'):
				aux="cst"+str(contP)+"="+nueva[index+4:index2+4]
				self.codigoC.append(aux)
				leeS='scanf("%s",&cst'+str(contP)+')'
				self.codigoC.append(leeS)
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#tff
			elif(nueva[index:index2]=='003E'):
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#CALL
			elif(nueva[index:index2]=='002F'):
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#ret
			elif(nueva[index:index2]=='0030'):
				index=index+4
				index2=index2+4
				cadena=cadena+4
			#jmpz
			elif(nueva[index:index2]=='0031'):
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#jmpnz
			elif(nueva[index:index2]=='0032'):
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#jmp
			elif(nueva[index:index2]=='0033'):
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#jmpp
			elif(nueva[index:index2]=='0034'):
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#jmpn
			elif(nueva[index:index2]=='0035'):
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#test
			elif(nueva[index:index2]=='002E'):
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#nop
			elif(nueva[index:index2]=='002D'):
				index=index+4
				index2=index2+4
				cadena=cadena+4
			#not
			elif(nueva[index:index2]=='002C'):
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#xor
			elif(nueva[index:index2]=='002B'):
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#or
			elif(nueva[index:index2]=='002A'):
				index=index+12
				index2=index2+12
				cadena=cadena+12
			else:
				print("nada")
				index=index+4
				index2=index2+4
				cadena=cadena+4
	
		print(self.codigoC)
		

  

