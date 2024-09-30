#pemilahan jenis kelamin
print("1. Pria")
print("2. Wanita")
Pilihan_Kelamin = int(input("masukkan pilihan (1/2): "))

if Pilihan_Kelamin == 1:
    Berat_Badan = int(input("Masukkan berat badan pria gr: "))
    Tinggi_Badan = float(input("Masukkan tinggi badan pria km: "))
    Umur = int(input("Masukkan umur pria: "))
    BMR = (10*(Berat_Badan*0.001)) + (6.25*(Tinggi_Badan*100000)) - (5*Umur) + 5
    print(f"Jumlah BMR pria = (10*{Berat_Badan*0.001}kg) + (6.25*{Tinggi_Badan*100000}cm) - (5*{Umur}) + 5 ")
elif Pilihan_Kelamin == 2:
    Berat_Badan = int(input("Masukkan berat badan Wanita gr: "))
    Tinggi_Badan = float(input("Masukkan tinggi badan Wanita km: "))
    Umur = int(input("Masukkan umur Wanita: "))
    BMR = (10*(Berat_Badan*0.001)) + (6.25*(Tinggi_Badan*100000)) - (5*Umur) - 161
    print(f"Jumlah BMR Wanita = (10*{Berat_Badan*0.001}kg) + (6.25*{Tinggi_Badan*100000}cm) - (5*{Umur}) - 161 = {BMR} ")
else:
    print("Tidak Valid")

#pemilihan level aktivitas
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

#menghitung TDEE
TDEE = BMR * Level 
print(f"Kebutuhan Kalori Harian = {BMR} * {Level} = {TDEE}")

