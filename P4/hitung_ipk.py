## Program Hitung IPK

## Inisialisasi dan deklarasi
ulang = "y"
nama_matakuliah = ""
nilai_huruf = ""
sks = 0
bobot = 0
jumlah_sks = 0
jumlah_bobot = 0

## Cetak judul program
print("")
print("Program Hitung IPK")
print("==================")

## Perulangan 
while ulang == "y" :
    nama_matakuliah = input("Nama Matakuliah ? ")
    nilai_huruf = input("Nilai Huruf ? ")
    sks = int(input("SKS ? "))

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

    ## Menjumlahkan bobot 
    jumlah_bobot = jumlah_bobot + (bobot * sks)

    ## Menjumlahka sks
    jumlah_sks = jumlah_sks + sks

    print("========================")
    ulang = input("Apakah akan memasukkan matakuliah lainnya? ")

## Menghitung IPK
ipk = jumlah_bobot / jumlah_sks

## Menampilkan hasil IPK
print("IPK : ", ipk)

print("")
print("")