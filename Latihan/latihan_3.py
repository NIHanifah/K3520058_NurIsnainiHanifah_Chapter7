print("----------------------------")
print("--PROGRAM HITUNG RATA-RATA--")
print("----------------------------")

sum = 0
banyak = 0
#function untuk mengolah data bilangan
def hitung(sum, banyak):
    y = "y"
    n = "n"
    try:
        inputBilangan = int(input("Masukkan bilangan bulat :"))
        if inputBilangan % 2 == 0:
            sum += inputBilangan
            tanya = input("Lagi (y/n) : ")
            if tanya == y:
                banyak += 1
                hitung(sum, banyak)
            elif tanya == n:
                banyak += 1
                print("Rata-ratanya adalah : ", sum/banyak)
        elif inputBilangan % 2 == 1:
            print("Bukan bilangan bulat")
            hitung(sum, banyak)
    except ValueError:
        print("Bukan bilangan bulat")
        hitung(sum, banyak)

hitung(sum, banyak)