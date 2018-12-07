class CrearObj:
	archivo=0
	def Crear(self,rutaArchivoAsc,listado):
		try:
			self.archivo = open(rutaArchivoAsc[0:-4]+'.O', 'w') 
			self.archivo.write(listado)
			self.archivo.close()
		except Exception:
			print("Hubo un error al guardar archivos")



