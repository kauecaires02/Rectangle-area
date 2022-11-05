# Rectangle-area
    class Retangulo():
        def __init__(self, l, c):
            self.larg = l
            self.comp  = c
     
        def calcArea(self):
            return self.larg*self.comp
     
    objRet = Retangulo(12, 10)
    print(objRet.calcArea())
