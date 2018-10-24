#Clase que lee el archivo cvs
class Lector:
    
    def _init_(self, archivo):
        self.documento = open(archivo)
        self.mnemonicos=csv.reader(self.documento)
    #Metodo usado para devolver el archivo leido.
    def getArchivo(self):
        return self.mnemonicos