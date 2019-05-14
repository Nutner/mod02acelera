class TermoCon():
    def __init__(self):
        self.__unidadMed = "C"
        self.__temperatura = 0
    def __conversor(self, temperatura,uniM):
        if uniM == "C":
            return "{}º F".format(temperatura * 9/5 + 32)
        elif uniM == "F":
            return "{}ª C".format((temperatura - 32) * (5/9))
        else:
            return "unidad incorrecta"
        
    def __str__(self):
        return "{}ª {}".format(self.__temperatura,self.__unidadMed)
    
    def unidadMedida(self, uniM=None):
        if uniM == None:
            return self.__unidadMed
        else:
            if uniM == "F" or uniM =="C":
                self.__unidadMed = uniM
                
    def temp(self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide(self, uniM = None):
        if uniM == None or uniM == self.__unidadMed:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidadMed)
    
    
    
    


    