
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

		while con < len(lines):			 

			linea=(lines[con]).replace(' ','')
			linealong=linea.replace('\n','')
			nueva=nueva+linealong
			
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
			elif(linea[index:index2]=='0014'):
				print("")				
			#POP
			elif(linea[index:index2]=='0015'):
			#ADD
				print("")
			elif(linea[index:index2]=='0016' or linea[index:index2]=='0017' or linea[index:index2]=='0018' or linea[index:index2]=='0019' ):
				auxsuma=int(nueva[index+8:index2+8])+int(nueva[index+4:index2+4])
				aux="sum"+str(conts)+"="+str(auxsuma)
				self.codigoC.append(aux)
				conts=conts+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#DEC
			elif(linea[index:index2]=='001A'):
				dec=int(nueva[index+4:index2+4])-1
				aux="dec"+str(contdec)+"="+str(dec)
				self.codigoC.append(aux)
				condec=condec+1
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#SUB
			elif(linea[index:index2]=='001B' or linea[index:index2]=='001C' or linea[index:index2]=='001D' or elif(linea[index:index2]=='001E'):
				auxresta=int(nueva[index+8:index2+8])-int(nueva[index+4:index2+4])
				aux="rest"+str(contresta)+"="+str(auxresta)
				self.codigoC.append(aux)
				contresta=contresta+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#MUL
			elif(linea[index:index2]=='001F' or linea[index:index2]=='0020' or linea[index:index2]=='0021' or linea[index:index2]=='0021'):
				auxmult=int(nueva[index+8:index2+8])*int(nueva[index+4:index2+4])
				aux="mult"+str(contmult)+"="+str(auxmult)
				self.codigoC.append(aux)
				contmult=contmult+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#DIV
			elif(linea[index:index2]=='0023' or linea[index:index2]=='0024' or linea[index:index2]=='0025' or linea[index:index2]=='0026'):
				auxdiv=int(nueva[index+8:index2+8])/int(nueva[index+4:index2+4])
				aux="div"+str(contdiv)+"="+str(auxdiv)
				self.codigoC.append(aux)
				contdiv=contdiv+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#INC
			elif(linea[index:index2]=='0027'):	
				inc=int(nueva[index+4:index2+4])+1
				aux="inc"+str(continc)+"="+str(inc)
				self.codigoC.append(aux)
				coninc=coninc+1
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#CMP
			elif(linea[index:index2]=='0028'):
				auxcmp=int(nueva[index+8:index2+8])-int(nueva[index+4:index2+4])
				aux="cmp"+str(contcmp)+"="+str(auxcmp)
				self.codigoC.append(aux)
				contcmp=contcmp+1
				index=index+12
				index2=index2+12
				cadena=cadena+12
			#AND
			elif(linea[index:index2]=='0029'):
				print("")
			#printN
			elif(linea[index:index2]=='0036' or linea[index:index2]=='0037'):
				impN=int(nueva[index+4:index2+4])
				aux=str(impN)
				self.codigoC.append(aux)
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#printCh
			elif(linea[index:index2]=='0038' or linea[index:index2]=='0039'):
				impCh=nueva[index+4:index2+4]
				self.codigoC.append(impCh)
				index=index+8
				index2=index2+8
				cadena=cadena+8
			#printS
			elif(linea[index:index2]=='003A'):
				print("")
			#readN
			elif(linea[index:index2]=='003B'):
			#readCh
			elif(linea[index:index2]=='003C'):
			#readS
			elif(linea[index:index2]=='003D'):
			#tff
			elif(linea[index:index2]=='003E'):
			#CALL
			elif(linea[index:index2]=='002F'):
			#ret
			elif(linea[index:index2]=='0030'):
			#jmpz
			elif(linea[index:index2]=='0031'):
			#jmpnz
			elif(linea[index:index2]=='0032'):
			#jmp
			elif(linea[index:index2]=='0033'):
			#jmpp
			elif(linea[index:index2]=='0034'):
			#jmpn
			elif(linea[index:index2]=='0035'):
			#test
			elif(linea[index:index2]=='002E'):
			#nop
			elif(linea[index:index2]=='002D'):
			#not
			elif(linea[index:index2]=='002C'):
			#xor
			elif(linea[index:index2]=='002B'):
			#or
			elif(linea[index:index2]=='002A'):	
		print(self.codigoC[0])
			
		
		
		
