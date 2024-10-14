import os
import csv
import Menu

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
def hitung_jumlah_sks(jumlah_sks, sks):
    ## Menjumlahkan sks
    return(jumlah_sks + sks)

## definikan hitung dan tampilkan hasil IPK
def hitung_ipk(jumlah_bobot,jumlah_sks) :
    ## Menghitung IPK
    ipk = jumlah_bobot / jumlah_sks
    ## Menampilkan hasil IPK
    print("IPK : ", ipk)    

## definiskan tampilan data matakuliah
def tampilkan() :
    jumlah_bobot = 0
    jumlah_sks = 0

    os.system("cls")
    print("Tampilkan Daftar Matakuliah")
    print("---------------------------")
    ## tabel header
    print("{:<25} {:<8} {:<7} {:<7}".format("Matakuliah", "Huruf", "Angka","Bobot"))
    ## tabel baris
    ## baca file matakuliah.csv
    with open("matakuliah.csv","r") as file:
        matakuliah = csv.DictReader(file)
        for itemMatakuliah in matakuliah :
            bobot = tentukan_bobot(itemMatakuliah["nilai_huruf"]) 
            print("{:<25} {:<8} {:<7} {:<7}".format(itemMatakuliah["nama_matakuliah"], itemMatakuliah["nilai_huruf"], itemMatakuliah["sks"],bobot))

            jumlah_bobot = hitung_jumlah_bobot(jumlah_bobot,bobot,int(itemMatakuliah["sks"]))

            jumlah_sks = hitung_jumlah_sks(jumlah_sks, int(itemMatakuliah["sks"]))
            
    print("")
    hitung_ipk(jumlah_bobot,jumlah_sks)

    Menu.menu()

