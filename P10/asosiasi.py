class ClassA() :
    def __init__(self, bilA):
        self.bilA = bilA

class ClassB() :
    def __init__(self,bilA) :
        self.bilA = bilA

    def tampil(self):
        print(self.bilA)

objekA = ClassA(100) 

objekB = ClassB(objekA.bilA)
objekB.tampil()