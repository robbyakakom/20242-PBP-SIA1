## Fungsi Menu

### import modul
import Masukan
import Tampil

def menu() :
    ### pilihan operasi
    print("Menu:")
    print("1. Isi data matakuliah")
    print("2. Tampilkan IPK")
    pilih = input("Pilih menu ? ")

    ### operasi
    if pilih == "1" :
        Masukan.tampilanMasukan()
    elif pilih == "2" :
        Tampil.tampilkan()
    else :
        pilih = True