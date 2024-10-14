## import library / modul
import os
import Entry
import Tampil
import Hitung

## Program Utama Hitung Jumlah

if __name__ == "__main__" :
    os.system("cls")
    ## Membuat Judul Aplikasi
    print("Program Kalukulator")
    print("")

    ## Entry Nilai
    a,b = Entry.masukkan()

    ## Menghitun jumlah  
    c = Hitung.jumlah(a,b)

    ## Menghitun Kuran

    ## Menghitung Kali

    ## Tampilkan data
    Tampil.tampilkan(a,b,c)

