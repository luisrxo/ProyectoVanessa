#Clase que busca el mnemonico en el archivo cvs
class BuscarMnemonico:
    
    def _init_(self,archivocvs):
        self.mnemonicos = archivocvs
        self.buscarD = buscarDireccionamiento (archivocvs)
    #Metodo que busca el mnemonico en todo el set de instrucciones
    def buscarMnemonico(self,mnemonico):
        for listaMnemonico in self.mnemonicos:
            if (listaMnemonico[1] == mnemonico):
                self.buscarD.metodoDeDireccionamiento(listaMnemonico)
