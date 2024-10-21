import os
users = {'pegawai' :{'password' : 'pegawai123', 'role': 'admin' }}
penjualan_daging = {}
user_login = None

def input_angka(teks):
    try:
        angka = int(input(teks))
        return angka
    except ValueError:
        print("input harus angka")
        return input(teks)


def login():
    global user_login
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
        return False
    return True 

def register():
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



def tambah_data():
    os.system('cls')
    print("=== TAMBAH DAGING ===")
    try:
        daging = input("DAGING : ")
        if daging in penjualan_daging :
            print("daging sudah ada")
        else :
            jumlah = input_angka("JUMLAH (Kg) : ")
            harga = input_angka("HARGA per Kg :")
            total = harga * jumlah
            penjualan_daging[daging] = {"jumlah" : jumlah, "harga": harga, "total" : total}
            print("penjualan berhasil ditambahkan")
    except ValueError :
        print("tidak valid")
    input("tekan enter unuk kembali...")

def tampilkan_data():
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

def ubah_data():
    os.system('cls')
    print("=== UBAH DATA DAGING ===")
    data_daging = input("Daging yang mau diubah : ")
    if data_daging in penjualan_daging:
        try:
            print(f"data saat ini : {penjualan_daging[data_daging]}")
            jumlah_baru = input_angka("JUMLAH (Kg) :")
            harga_baru = input_angka("HARGA per (Kg) : ")
            Total = jumlah_baru * harga_baru
            penjualan_daging[data_daging] = {"jumlah": jumlah_baru, "harga": harga_baru, "total": Total}
            print(f"data daging {data_daging} telah diubah")
        except ValueError :
            print("tidak valid")
    else:
        print("Daging tidak ditemuka! ")
    input("tekan enter untuk kembali...")
    
def hapus_data():
    os.system('cls')
    print("=== HAPUS DATA DAGING ===")
    data_daging = input("Daging yang ingin dihapus : ")
    if data_daging in penjualan_daging:
        del penjualan_daging[data_daging]
        print(f" data daging {data_daging} telah dihapus! ")
    else:
        print("daging tidak ditemukan! ")
    input("tekan enter unutk kembali...")

    
def menu():
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
        try :
            pilih = input_angka("pilih opsi : ")
        except ValueError:
            print("Masukkan pilihan yang valid.")
            continue

        if pilih == 1 : #login
            if login():
                if user_login['role'] == 'admin':
                    menu_admin()
                else:
                    menu_pelanggan()
 
        elif pilih == 2 :
            register()

        elif pilih == 3:
            print("anda keluar dari program")
            break
        else:
            print("tidak valid")
        input("tekan enter untuk kembali...")

def menu_admin():
    while True :
        os.system('cls')
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
        pilihan = input_angka("PILIH : ")
        if pilihan == 1 :
            tambah_data()
        elif pilihan == 2 :
            tampilkan_data()
        elif pilihan == 3 :
            ubah_data()
        elif pilihan == 4 : 
            hapus_data()
        elif pilihan == 5 :
            print("anda telah keluar ! ")
            break
        else:
            print("tidak valid")
            input("tekan enter untuk kembali ")

def menu_pelanggan():
    while True:
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
        pilihan = input_angka("PILIH : ")
        if pilihan == 1:
            tampilkan_data()
        elif pilihan == 2 :
            print("anda telah keluar !")
            break
        else :
            print("Tidak Valid")
            input("tekan enter untuk kembali")

menu()



        


    





    