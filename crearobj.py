class CrearObj:
	archivo=0
	def Crear(self,rutaArchivoAsc):
		try:
			self.archivo = open(rutaArchivoAsc[0:-4]+'.O', 'w') 
		except Exception:
			print("Hubo un error al guardar archivos")
	def Escribir(self,listado):
		try:
			self.archivo.write(listado)
		except Exception:
			print("Hubo un error al guardar archivos")
	def Cerrar(self):
		try:
	
			self.archivo.close()
		except Exception:
			print("Hubo un error al guardar archivos")






