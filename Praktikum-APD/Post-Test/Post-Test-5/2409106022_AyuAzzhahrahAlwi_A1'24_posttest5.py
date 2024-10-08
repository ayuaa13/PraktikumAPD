users = [["ayu", "ayu123", "admin"], ["alwi", "alwi123", "user"]]
print(f"username admin : {users[0][0]} ")
print(f"username user : {users[1][0]} ")
penjualan_daging = [
    ["daging", "jumlah", "harga 1Kg", "total harga"]
]

while True:
    print( 
    """
    ==================================
    | SISTEM PENJUALAN PRODUK DAGING |
    ==================================
    |    1. LOGIN                    |           
    |    2. REGISTER                 |          
    |    3. KELUAR                   |      
    ==================================
    """
    )
    pilih = int(input("pilih opsi : "))

    if pilih == 1 : #login
        print("=== SILAHKAN LOGIN ===")
        username = input("Masukkan username anda : ")
        password = input("Masukkan Password anda : ")
        user_login = None
        for user in users :
            if username == user[0] and password == user[1] :
                user_login = user
                print(f"selamat datang, {username} ({user[2]})!")
                break
        if not user_login:
            print("Login gagal !")    
            continue

        if user_login[2] == "admin":
            while True :
                print( 
                """
                ================================
                |       PENJUALAN ADMIN        |
                ================================
                |    1. TAMBAH PENJUALAN       |           
                |    2. TAMPILKAN PENJUALAN    |          
                |    3. UBAH PENJUALAN         |     
                |    4. HAPUS PENJUALAN        |      
                |    5. KELUAR                 |  
                ================================
                """
                )
                pilihan = int(input("PILIH : "))
                if pilihan == 1 :
                    daging = input("DAGING : ")
                    jumlah = int(input("JUMLAH (Kg) : "))
                    harga = int(input("HARGA per Kg :"))
                    total = harga * jumlah
                    penjualan_daging.append([daging, jumlah, harga, total])
                    print("penjualan berhasil ditambahkan")
                elif pilihan == 2 :
                    print("=== PENJUALAN DAGING ===")
                    for i in range(len(penjualan_daging)):
                        print(f"{penjualan_daging[i][0]:<10} | {penjualan_daging[i][1]:<20}Kg | {penjualan_daging[i][2]:<15} | {penjualan_daging[i][3]:<5}")
                        print()
                elif pilihan == 3 :
                    data_daging = input("Daging yang mau diubah : ")
                    for i in range(len(penjualan_daging)):
                        if penjualan_daging[i][0] == data_daging :
                            daging_baru = input("DAGING : ")
                            jumlah_baru = int(input("JUMLAH (Kg) :"))
                            harga_baru = int(input("HARGA per (Kg) : "))
                            Total = jumlah_baru * harga_baru
                            penjualan_daging[i][0] = daging_baru
                            penjualan_daging[i][1] = jumlah_baru
                            penjualan_daging[i][2] = harga_baru
                            penjualan_daging[i][3] = Total
                elif pilihan == 4:
                    data_daging = input("Daging yang ingin dihapus : ")
                    for i in range(len(penjualan_daging)):
                        if penjualan_daging[i][0] == data_daging :
                            del penjualan_daging[i]
                elif pilihan == 5:
                    print("Anda Telah Keluar")
                    break
                else:
                    print("Tidak Valid")

        elif user_login[2] == "user":
            while True :
                print( 
                """
                ================================
                |       PENJUALAN PENGGUNA     |
                ================================
                |    1. TAMPILKAN PENJUALAN    |
                |    2. KELUAR                 |        
                ================================
                """
                )
                pilihan = int(input("PILIH : "))
                if pilihan == 1:
                    print("=== PENJUALAN DAGING ===")
                    print(f"{penjualan_daging[i][0]:<10} | {penjualan_daging[i][1]:<20}Kg | {penjualan_daging[i][2]:<15} | {penjualan_daging[i][3]:<5}")
                elif pilihan == 2 :
                    print("Anda telah Logout")
                    break
                else :
                    print("Tidak Valid")

    elif pilih == 2 : #register
        print("=== SILAHKAN GISTER ===")
        username = input("Masukkan username baru anda : ")
        password = input("Masukkan password baru anda : ")
        peran = "user"
        pengguna = False
        for user in users:
            if username == user[0]:
                print("Username sudah terdaftar!")
                pengguna = True
                break
        if not pengguna:
            users.append([username, password, peran])
            print(f"{username} berhasil didaftarkan sebagai {peran}")
    elif pilih == 3 :
        print("Terima kasih telah berkunjung. ")
        break
    else :
        print("Tidak Valid")


    





    