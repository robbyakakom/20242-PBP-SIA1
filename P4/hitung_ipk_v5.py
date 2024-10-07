## cetak judul

def cetak_judul():
    ## Cetak judul program
    print("")
    print("Program Hitung IPK")
    print("==================")

def masukkan() :
    nama_matakuliah = input("Nama Matakuliah ? ")
    nilai_huruf = input("Nilai Huruf ? ")
    sks = int(input("SKS ? "))
    return(nama_matakuliah,nilai_huruf,sks)

def tentukan_bobot(nilai_huruf) :
    # Menentukan bobot
    if nilai_huruf == "A" :
        bobot = 4
    elif nilai_huruf == "B" :
        bobot = 3
    elif nilai_huruf == "C" :
        bobot = 2
    elif nilai_huruf == "D" :
        bobot = 1
    else :
        bobot = 0    
    return bobot 

def hitung_jumlah_bobot(jumlah_bobot,sks) :
    ## Menjumlahkan bobot 
    return(jumlah_bobot + (bobot * sks))

def hitung_jumlah_sks(jumlah_sks,sks) :
    ## Menjumlahka sks
    return(jumlah_sks + sks)

def hitung_ipk(jumlah_bobot, jumlah_sks) :
    ## Menghitung IPK
    return(jumlah_bobot / jumlah_sks)   

def tampil_ipk(ipk) :
    ## Menampilkan hasil IPK
    print("IPK : ", ipk)


import os
os.system('cls')

if __name__ == '__main__' :

    ## Inisialisasi dan deklarasi
    ulang = "y"
    nama_matakuliah = ""
    nilai_huruf = ""
    sks = 0
    bobot = 0
    jumlah_sks = 0
    jumlah_bobot = 0

    ## Program Hitung IPK
    ## cetak judul program
    cetak_judul()

    ## Perulangan 
    while ulang == "y" :  

        ## input data
        nama_matakuliah, nilai_huruf, sks = masukkan() 

        ## hitung bobot
        bobot = tentukan_bobot(nilai_huruf)

        ## hitung jumlah bobot
        jumlah_bobot = hitung_jumlah_bobot(jumlah_bobot, sks)

        ## hitung jumlah sks
        jumlah_sks = hitung_jumlah_sks(jumlah_sks,sks)

        print("==================")
        ulang = input("Apakah akan memasukkan matakuliah lainnya? (y/t)")
        print("")
    
    ## hitung ipk
    ipk = hitung_ipk(jumlah_bobot, jumlah_sks)

    ## tampilkan ipk
    tampil_ipk(ipk) 

    print("")
    print("")