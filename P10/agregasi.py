class ClassA() :
    def __init__(self, bilA) :
        self.bilA = bilA

class ClassB() :
    def __init__(self, objek) :
        self.objek = objek

    def tampil(self) :
        print (self.objek.bilA)

objekA = ClassA(100)

objekB = ClassB(objekA)
objekB.tampil()