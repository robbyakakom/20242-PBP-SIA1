class Pintu() :
    def __init__ (self) :
        self.pintu = "Pintu"

class Rumah() :
    def __init__(self) :
        self.rumah = "Rumah"
        self.Komponen = Pintu()

    def menggunakan(self) :
        print ("Rumah ini menggunakan ",self.Komponen.pintu)


objRumah = Rumah() 
objRumah.menggunakan()
