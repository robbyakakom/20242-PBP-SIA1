## mendefiniskan fungsi garis
def garis() :
    print("--------------------------------------------")
    print("")

## mendefinisikan fungsi masukan
def masukan() :
    a = int(input("Masukkan nilai a "))
    b = int(input("Masukkan nilai b "))
    return(a,b)

## mendefinisikan operasi jumlah
# def jumlah(a,b) :
#     return(a + b)
## penggunaan lambda pengganti fungsi di atas
jumlah = lambda a,b : a + b

## mendefinisikan fungsi kurang
kurang = lambda a,b : a - b

## mendefinisikan hasil
def hasil(c) :
    print("Hasil ", c)
    print("")