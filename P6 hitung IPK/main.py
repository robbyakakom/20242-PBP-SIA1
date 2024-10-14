## Program Hitung IPK
### Import modul
import os
import csv
import Menu

### Main program
if __name__ == "__main__" :
    pilih = True 
    while pilih == True :

        ### Menyiapkan simpanan data matakuliah
        if not os.path.exists("matakuliah.csv"):
            fileMatakuliah = open("matakuliah.csv","w")
            fieldnames = ['nama_matakuliah' ,'nilai_huruf', 'sks']
            writer = csv.DictWriter(fileMatakuliah,fieldnames=fieldnames)
            writer.writeheader()
            fileMatakuliah.close()

        ### label judul program
        os.system("cls")
        print("Program Hitung IPK")
        print("------------------")

        Menu.menu()



