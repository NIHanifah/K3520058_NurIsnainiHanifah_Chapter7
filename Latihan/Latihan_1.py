#Program membuka, membaca, dan menampilkan isi

try:
    cariFile = input("Masukkan nama file : ")
    print("Isi file", cariFile, "adalah :")
    baca = open(cariFile)
    print(baca.read())

except FileNotFoundError:
    print("File tidak ditemukan")

