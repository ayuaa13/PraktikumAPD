import os
users = {'pegawai' :{'password' : 'pegawai123', 'role': 'admin' }}
penjualan_daging = {}
user_login = None

while True:
    os.system('cls')
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
        os.system('cls')
        print("=== SILAHKAN LOGIN ===")
        username = input("Masukkan username anda : ")
        password = input("Masukkan Password anda : ")
        if username in users and users[username]["password"] == password :
            user_login = users[username]

            print(f"selamat datang, {username} ({user_login['role']})!")
        else:
            print("Login gagal !") 
            input("tekan enter unutk kembali...")   
            continue
    elif pilih == 2 :
        os.system('cls')
        print("=== silahkan melakukan REGISTER ===")
        username = input("masukkan username :")
        if username in users :
            print("username sudah terdaftar!")
        else:
            password = input("masukkan password : ")
            users[username] = {'password' : password, 'role' : 'user'}
            print(f"registrasi berhasil! {username} sudah ditambahkan sebagai user, silahkan login kembali! ")
        input("tekan enter unutk kembali...")
        continue
    elif pilih == 3:
        print("anda keluar dari program")
        break
    else:
        print("tidak valid")
        input("tekan enter untuk kembali...")
        continue

    while True :
        os.system('cls')
        if user_login["role"] == "admin":
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
                os.system('cls')
                print("=== TAMBAH DAGING ===")
                try:
                    daging = input("DAGING : ")
                    if daging in penjualan_daging :
                        print("daging sudah ada")
                    else :
                        jumlah = int(input("JUMLAH (Kg) : "))
                        harga = int(input("HARGA per Kg :"))
                        total = harga * jumlah
                        penjualan_daging[daging] = {"jumlah" : jumlah, "harga": harga, "total" : total}
                        print("penjualan berhasil ditambahkan")
                except ValueError :
                    print("tidak valid")
                input("tekan enter unuk kembali...")
            elif pilihan == 2 :
                os.system('cls')
                print("=== PENJUALAN DAGING ===")
                if not penjualan_daging:
                    print("belum ada data daging")
                else :
                    for daging, info in penjualan_daging.items():
                        print(f"daging : {daging} ")
                        print(f"jumlah : {info['jumlah']} Kg") 
                        print(f"harga per Kg : Rp {info['harga']}")
                        print(f"total : {info['total']}")
                        print("-"*20)
                input("tekan enter unutk kembali")
            elif pilihan == 3 : #mengubah data
                os.system('cls')
                print("=== UBAH DATA DAGING ===")
                data_daging = input("Daging yang mau diubah : ")
                if daging in penjualan_daging:
                    try:
                        print(f"data saat ini : {penjualan_daging[daging]}")
                        jumlah_baru = int(input("JUMLAH (Kg) :"))
                        harga_baru = int(input("HARGA per (Kg) : "))
                        Total = jumlah_baru * harga_baru
                        penjualan_daging[data_daging] = {"jumlah": jumlah_baru, "harga": harga_baru, "total": Total}
                        print(f"data daging {daging} telah diubah")
                    except ValueError :
                        print("tidak valid")
                else:
                    print("Daging tidak ditemuka! ")
                input("tekan enter untuk kembali...")
            elif pilihan == 4: #menhapus data 
                os.system('cls')
                print("=== HAPUS DATA DAGING ===")
                data_daging = input("Daging yang ingin dihapus : ")
                if data_daging in penjualan_daging:
                    del penjualan_daging[data_daging]
                    print(f" data daging {data_daging} telah dihapus! ")
                else:
                    print("daging tidak ditemukan! ")
                input("tekan enter unutk kembali...")
            elif pilihan == 5:
                print("Anda Telah Keluar")
                break
            else:
                print("Tidak Valid")
                input("tekan enter unutk kembali...")
        elif users[username]["role"] == "user" :
            os.system('cls')
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
                os.system('cls')
                print("=== PENJUALAN DAGING ===")
                if not penjualan_daging:
                    print("belum ada data daging")
                else :
                    for daging, info in penjualan_daging.items():
                        print(f"daging : {daging} ")
                        print(f"jumlah : {info['jumlah']} Kg") 
                        print(f"harga per Kg : Rp {info['harga']}")
                        print(f"total : {info['total']}")
                        print("-"*20)
                input("tekan enter unutk kembali")
            elif pilihan == 2 :
                os.system('cls')
                print("Anda telah Logout")
                print("terimakasih sudah berkunjung")
                break
            else :
                print("Tidak Valid")
                input("tekan enter untuk kembali")
        


    





    