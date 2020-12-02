#Menambahkan data pada file

data = input("Masukkan nama file : ")
file = open(data, "a")

#function untuk menambahkan data
def tambahData():
    dataTambahan = input("Data yang mau ditambahkan : ")
    file.write(dataTambahan)
    tanya = input("Mau lagi (y/n) : ")
    if tanya == "y" or tanya == "Y":
        tambahData()
    elif tanya == "n" or tanya == "N":
        file.close()

tambahData()