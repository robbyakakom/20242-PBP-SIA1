class ClassA() :
    def __init__(self, bilA) :
        self.bilA = bilA

class ClassB() :
    def __init__(self, bilangan) :
        self.objekA = ClassA(bilangan) 

    def tampil(self) :
        print(self.objekA.bilA)

objekB = ClassB(200)
objekB.tampil()