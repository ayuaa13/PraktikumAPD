print("login")
username = input("buat username anda: ")
password = int(input("buat password anda: "))
percobaan = 0
percobaan_max = 3
while percobaan < percobaan_max : 
    usr = input("masukkan username anda: ")
    psw = int(input("masukkan password anda: "))
    if usr == username and psw == password :
        print("selamat! ada berhasil login")
        berhasil_login = True
        break
    else:
        percobaan += 1
        print("login tidak berhasil!")
    if percobaan == percobaan_max:
        print("anda telah melakukan login 3 kali. program akan berhenti!")
        exit()

     

if berhasil_login:  
    while True:
        print("1. Pria")
        print("2. Wanita")
        Pilihan_Kelamin = int(input("masukkan pilihan (1/2): "))
        if Pilihan_Kelamin == 1:
            Berat_Badan = int(input("Masukkan berat badan pria gr: "))
            Tinggi_Badan = float(input("Masukkan tinggi badan pria km: "))
            Umur = int(input("Masukkan umur pria: "))
            BMR = (10*(Berat_Badan*0.001)) + (6.25*(Tinggi_Badan*100000)) - (5*Umur) + 5
            print(f"Jumlah BMR pria = {BMR} ")
        elif Pilihan_Kelamin == 2:
            Berat_Badan = int(input("Masukkan berat badan Wanita gr: "))
            Tinggi_Badan = float(input("Masukkan tinggi badan Wanita km: "))
            Umur = int(input("Masukkan umur Wanita: "))
            BMR = (10*(Berat_Badan*0.001)) + (6.25*(Tinggi_Badan*100000)) - (5*Umur) - 161
            print(f"Jumlah BMR Wanita = {BMR} ")
        else :
            print("Tidak Valid")

        print("1. Aktivitas Minimal (Jarang bergerak)")
        print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu)")
        print("3. aktivitas tinggi (olahraga 4-7 kali seminggu)")
        Pilihan_Aktivitas = int(input("masukkan level aktivitas (1/2/3): "))

        if Pilihan_Aktivitas == 1:
            Level = 1.25
            print(f"level aktivitas = {Level}")
        elif Pilihan_Aktivitas == 2:
            Level = 1.36
            print(f"level aktivitas = {Level}")
        elif Pilihan_Aktivitas == 3:
            Level = 1.72
            print(f"level aktivitas = {Level}")
        else:
            print("Tidak Valid")

        TDEE = BMR * Level 
        print(f"TDEE = {BMR} * {Level} = {TDEE}")
        print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah {TDEE} kkal")

        hitung_lagi = input("ingin mencoba ulang YA/TIDAK ? ")
        if hitung_lagi == "TIDAK" :
            print("terimakasih sudah mencoba!")
            break





