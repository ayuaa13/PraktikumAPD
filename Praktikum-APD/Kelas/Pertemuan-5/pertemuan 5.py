# nama = ["celio", "shandy", "farel", "ghazali", "vito"]
# print(f"nama{nama}")
# print(nama[2]) #menggunakan indeks (dimulai dari 0)

# #menambahkan list
# nama = ["celio", "shandy", "farel", "ghazali", "vito"]
# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# nama.append("afrizal") #bisa pake insert (tempat lebih spesifik)
# print(nama)

# #mengganti nama
# nama = ["celio", "shandy", "farel", "ghazali", "vito"]
# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# nama[4] = "fufufafa"
# print(nama)

# #menghanpus list
# nama = ["celio", "shandy", "farel", "ghazali", "vito"]
# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# del nama[3]
# print(nama)

# #slicing list
# nama = ["celio", "shandy", "farel", "ghazali", "vito", "yuyun", "adi", "rizal", "adri", "ifnu"]
# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# print(nama [0:2]) #menggunakan indeks & elemen (elemen dimulai dari 1)
# print(nama[1:9:2]) #menggunakan indeks & elemen & step (step adalah langkah)

# #operasi list
# nama = ["celio", "shandy", "farel", "ghazali", "vito"]
# matkul = ["APD", "APL", "BASDAT", "STKDAT", "WEB", "JARKOM"]
# print("sebelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# data = nama+matkul
# print(data) #penjumlahan
# print(data*3) #perkalian

# #list didalam list (nasted list)
# data = ["farel","Celio", [1,2]]
# print(data[2][0]) #mengambil list didalam list

# #perulangan list
# matkul = ["APD", "APL", "BASDAT", "STKDAT", "WEB", "JARKOM"]
# for i in matkul:
#     print(i)
#     print(i, end="")

# #perulangan nasted list
# data = [1, 2, 3, 4, 5, [1,2]]
# for i in data:
#     for j in i:
#         print(j)

#TUPLE
# nama = ('farel', 'vito', 'shandy', 'celio')
# print(nama[1:])

# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# absen, prodi, nim, nama = mahasiswa
# print(absen)
# pritn(prodi)
# print(nim)
# print(nama)


print(
"""
===========================
|   DATA MAHASISWA        |
===========================
|   1. TAMBAH DATA        |
|   2. TAMPILKAN DATA     | 
|   3. UBAH DATA          |
|   4. HAPUS DATA         |
|   5. KELUA              |
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")




