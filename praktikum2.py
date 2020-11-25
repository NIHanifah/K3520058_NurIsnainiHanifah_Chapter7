#membuka dan mau membaca file
try:
    file = open("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter7/data.txt", "r")
    #baca baris pertama dari file
    #simpan ke dalam variabel bil1 sebagai integer
    bil1 = int(file.readline())

    #bacaa baris pertama dari file
    # simpan ke dalam variabel bil2 sebagai intger
    bil2 = int(file.readline())

    #hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1, "dibagi", bil2, "sama dengan", hasil)

#jika file tidak ditemukan
except FileNotFoundError:
    print("File tidak ditemukan")

#jika pembagian dengan nol
except ZeroDivisionError:
    print("Tidak boleh pembagian dengan nol!")
