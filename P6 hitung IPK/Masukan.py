import os
import csv
import Menu

## definisikan fungsi input
def masukan() :
    nama_matakuliah = input("Nama Matakuliah ? ")
    nilai_huruf = input("Nilai Huruf ? ")
    sks = int(input("SKS ? "))
    return(nama_matakuliah,nilai_huruf,sks)

## definisikan tampilan masukan
def tampilanMasukan() :
    os.system("cls")
    matakuliah = []
    print("Form Memasukkan Data Matakuliah")
    ulang = "Y"
    while ulang == "Y" :
        print("-------------------------------")
        nama_matakuliah,nilai_huruf,sks = masukan()
        itemMatakuliah = {
            "nama_matakuliah":nama_matakuliah,
            "nilai_huruf":nilai_huruf,
            "sks":sks
        }
        matakuliah.append(itemMatakuliah)
        print("-------------------------------")
        ulang = input("Isi data lagi ? [Y/T]")
    
    ## simpan data matakuliah ke file matakuliah.csv
    with open('matakuliah.csv','a',newline='') as file:
        fieldnames = ['nama_matakuliah' ,'nilai_huruf', 'sks']
        writer = csv.DictWriter(file,fieldnames=fieldnames)

        for itemMatakuliah in matakuliah:
            writer.writerow(itemMatakuliah)

    Menu.menu()

        