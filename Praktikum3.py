#Menjumlahkan data pada file
try:
    file = open ("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter7/data2.txt", "r")
    sum = 0
    for data in file:
        sum = sum + int(data)
    print(sum)

except ValueError:
    print("Tidak bisa penjumlahan string dan integer")