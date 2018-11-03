class Errores:

    def error1(self,linea):
        print("Error 001 Constante inexistente en la linea :"+ str(linea))
    def error2(self,linea):
        print("Error 002 Variable inexistente en la linea: "+ str(linea))
    def error3(self,linea):
        print("Error 003 Etiqueta inexistente en la linea: "+ str(linea))
    def error4(self,linea):
        print("Error 004 Mnemonico inexistente en la linea: "+ str(linea))
    def error5(self,linea):
        print("Error 005 Instruccion carece de operandos en la linea: "+ str(linea))
    def error6(self,linea):
        print("Error 006 instruccion no lleva operandos en la linea: "+ str(linea))
    def error7(self,linea):
        print("Error 007 Magnitud de operando erronea en la linea: "+ str(linea))
    def error8(self,linea):
        print("Error 008 Salto relativo muy lejano en la linea: "+ str(linea))
    def error9(self,linea):
        print("Error 009 instruccion carece de al menos un espacio relativo al margen  en la linea: "+ str(linea))
    def error10(self,linea):
        print("Error 010 No se encuentra END  "+ str(linea))