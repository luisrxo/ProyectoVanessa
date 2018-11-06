class Errores:
    erroresJuntos=[]
    def error1(self,linea):
        print("Error 001 Constante inexistente en la linea:"+ str(linea))
        self.erroresJuntos.append("Error 001 Constante inexistente en la linea:"+ str(linea))
    def error2(self,linea):
        print("Error 002 Variable inexistente en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 002 Variable inexistente en la linea: "+ str(linea))
    def error3(self,linea):
        print("Error 003 Etiqueta inexistente en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 003 Etiqueta inexistente en la linea: "+ str(linea))
#Error 4 ya esta
    def error4(self,linea):
        print("Error 004 Mnemonico inexistente en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 004 Mnemonico inexistente en la linea: "+ str(linea))
#Error 5 ya esta
    def error5(self,linea):
        print("Error 005 Instruccion carece de operandos en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 005 Instruccion carece de operandos en la linea: "+ str(linea))
#Error 6 ya esta
    def error6(self,linea):
        print("Error 006 instruccion no lleva operandos en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 006 instruccion no lleva operandos en la linea: "+ str(linea))
#Error 7 ya esta
    def error7(self,linea):
        print("Error 007 Magnitud de operando erronea en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 007 Magnitud de operando erronea en la linea: "+ str(linea))
#Error 8 ya esta
    def error8(self,linea):
        print("Error 008 Salto relativo muy lejano en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 008 Salto relativo muy lejano en la linea: "+ str(linea))
#Error 9 ya esta
    def error9(self,linea):
        print("Error 009 instruccion carece de al menos un espacio relativo al margen  en la linea: "+ str(linea))
        self.erroresJuntos.append("Error 009 instruccion carece de al menos un espacio relativo al margen  en la linea: "+ str(linea))
#Erro 10 ya esta
    def error10(self):
        print("Error 010 No se encuentra END  ")
        self.erroresJuntos.append("Error 010 No se encuentra END  ")
    def getJuntos(self):
        return self.erroresJuntos
