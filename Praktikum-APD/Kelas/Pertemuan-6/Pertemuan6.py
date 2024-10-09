## dictionary

# daftar_buku = {
#     "buku 1" : "Harry poter",
#     "buku 2" : "percy jackson",
#     "buku 3" : "Twilight"
# }

# print(daftar_buku["buku 2"])

# daftar_buku = {
#     "buku 1" : "Harry poter",
#     "buku 1" : "percy jackson",
#     "buku 3" : "Twilight"
# }

# print(daftar_buku["buku 1"])  # yang keluar buku 1 yang terbaru 

# biodata = {
#     "Nama" : "Aldy madhan SYahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["program web", "struktue data", "Basis data"],
#     "Mahasiswa Aktif" : True, #bool
#     "social Media" :{ 
#         "instagram" : "@aldyrmdhns_",
#         "discord" : "\'Izanami#6848"
#     }

# }
# print("jumlah data dalam dict biodata = ", len(biodata) )

# #menambah
# Film = {
#     "avenger endgame" : "action",
#     "sharelock Holmes" : "mysetry",
#     "the conjuring" : "Horor"
# }
# Film["Zombieland"] = "comedy" #kurung siku
# Film.update({"hour" : "Thriller"})
# print(Film)

# #menghapus
# Film = {
#     "avenger endgame" : "action",
#     "sharelock Holmes" : "mysetry",
#     "the conjuring" : "Horor"
# }
# del Film["the conjuring"]
# hapus = Film.pop("the conjuring")
# Film.clear() #menghapus bersih 
# print(Film)
# print(f"key yang dihapus = {hapus}")

# biodata = {
#     "Nama" : "Aldy madhan SYahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["program web", "struktue data", "Basis data"],
#     "Mahasiswa Aktif" : True, #bool
#     "social Media" :{ 
#         "instagram" : "@aldyrmdhns_",
#         "discord" : "\'Izanami#6848"
#     }
# }
# pinjamdict = biodata.copy()
# print(pinjamdict)

# key = "apel", "jeruk", "mangga"
# value = 1

# buah = dict.fromkeys(key, value)
# print(buah)

#  Film = {
#     "avenger endgame" : "action",
#     "sharelock Holmes" : "mysetry",
#     "the conjuring" : "Horor"
# }
# print(Film)
# print("film : ", Film.setdefault("olbook", "horor"))

# for i in Film.keys():
#  print(i, end=" ")

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# #Sebelum Dilakukan Perubahan
# print(mahasiswa)
# #Menambahkan Item pada Nested Dictionary
# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)
# #Mengubah Item pada Nested Dictionary
# mahasiswa[101]["Nama"] = "Rizal"
# print(mahasiswa)
# #Menghapus Item pada Nested Dictionary
# del mahasiswa[101]["Umur"]
# print(mahasiswa)

Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")