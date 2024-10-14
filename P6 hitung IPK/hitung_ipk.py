import os
os.system("cls")

## definisikan fungsi input
def masukan() :
    nama_matakuliah = input("Nama Matakuliah ? ")
    nilai_huruf = input("Nilai Huruf ? ")
    sks = int(input("SKS ? "))
    return(nama_matakuliah,nilai_huruf,sks)

## definisikan fungsi tentukan bobot
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

## definisikan fungsi jumlah bobot
def hitung_jumlah_bobot(jumlah_bobot,bobot,sks) :
    ## Menjumlahkan bobot 
    return(jumlah_bobot + (bobot * sks))

## definiskan fungsi hitung sks
def hitun_jumlah_sks(jumlah_sks, sks):
    ## Menjumlahkan sks
    return(jumlah_sks + sks)

## definikan hitung dan tampilkan hasil IPK
def hiutung_ipk(jumlah_bobot,jumlah_sks) :
    ## Menghitung IPK
    ipk = jumlah_bobot / jumlah_sks
    ## Menampilkan hasil IPK
    print("IPK : ", ipk)

## Program Utama
if __name__ == "__main__" :
    ## Inisialisasi dan deklarasi
    ulang = "y"
    nama_matakuliah = ""
    nilai_huruf = ""
    sks = 0
    bobot = 0
    jumlah_sks = 0
    jumlah_bobot = 0

    ## Program Hitung IPK
    ## Cetak judul program
    print("")
    print("Program Hitung IPK")
    print("==================")
 
    ## Perulangan 
    while ulang == "y" :

        ## memasukkan data
        masukan() 

        ## menentukan bobot    
        bobot = tentukan_bobot(nilai_huruf)

        ## menghitung jumlah bobot
        jumlah_bobot = hitung_jumlah_bobot(jumlah_bobot,bobot,sks)
        
        ## menghitung jumlah sks
        jumlah_sks = hitun_jumlah_sks(jumlah_sks, sks)

        print("========================")
        ulang = input("Apakah akan memasukkan matakuliah lainnya? ")

    hiutung_ipk(jumlah_bobot,jumlah_sks)

    print("")
    print("")