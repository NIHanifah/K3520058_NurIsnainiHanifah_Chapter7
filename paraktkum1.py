#menampilkan data pada file
try:
    file = open ("c:/halo.txt", "r")
    print (file.read())
except FileNotFoundError:
    print("File tidak ada")