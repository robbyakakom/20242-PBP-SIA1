## menyisipkan / import file berisi fungsi-fungsi yang sudah di definisikan
import fungsi
import os

## program utama
if __name__ == "__main__" :
    os.system("cls")
    print("Program Kalkulator")
    fungsi.garis()
    ## memasukkan data
    a,b = fungsi.masukan()

    print("Pilih operasi matematika :")
    print("1. Untuk Penjumlahan")
    print("2. Untuk Pengurangan")
    pilih_operasi = input("pilih: ")
    if pilih_operasi == "1" :
        ## operasi jumlah
        c = fungsi.jumlah(a,b)
    elif pilih_operasi == "2" :
        ## operasi kurang
        c = fungsi.kurang(a,b)

    ## tampilkan hasil
    fungsi.hasil(c)





