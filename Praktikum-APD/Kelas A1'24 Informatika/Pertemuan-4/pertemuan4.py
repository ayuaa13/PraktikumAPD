# ulang = 10
# for i in range(ulang):
#     print(f"perulangan ke-{str(i)}")


# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print (i, end=' ')


# for i in range(1, 10, 2): #(awal, akhir, lompatan)
#     print(i)


# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()


# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'): #kondisi/syarat
#     hitung += 2 #hitung = hitung + 2
#     jawab = input("ulang lagi tidak? : ")
# print(f"total perulangan : {hitung}")


# hitung = 0
# while True: #kondisi/syarat
#     hitung += 1 #hitung = hitung + 1
#     ulang = input("ulang lagi tidak ? : ")
#     if ulang == "tidak" or ulang == "Tidak" : #kondisi 
# print(f"total perulangan : {hitung}")


# print("daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 3 == 0:
#         continue
#     print (i)


bilangan = 0 
while True:
    angka = int(input("masukkan angka"))
    if angka < 0:
        break
    bilangan += angka
print(f"total bilangan: " + str(bilangan))


# for i in range(1, 20, 3):
#     if i % 2 == 0 :
#         continue
#     print(i)
    
