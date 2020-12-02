#Program membuka, membaca, dan menampilkan isi

try:
    cariFile = input("Masukkan nama file : ")
    print("Isi file", cariFile, "adalah :")
    baca = open(cariFile)
    print(baca.read())

#jika data tidak ditemukan
except FileNotFoundError:
    print("!!File tidak ditemukan!!")

#jika salah dalam penulisan
except SyntaxError:
    print("!!Salah dalam penulisan!!")

