#Menambahkan data pada file

a = "y"
b = "n"

data = input("Masukkan nama file : ")
file = open(data, "a")

#function untuk menambahkan data
def tambahData():
    dataTambahan = input("Data yang mau ditambahkan : ")
    file.write(dataTambahan)
    tanya = input("Mau lagi (y/n) : ")
    if tanya == a:
        tambahData()
    elif tanya == b:
        file.close()

tambahData()