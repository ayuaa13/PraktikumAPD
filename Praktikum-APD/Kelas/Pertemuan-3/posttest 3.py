#BMR sesuai jenis kelamin

print("1. pria")
print("2. wanita")
Pilihan_Kelamin = int(input("masukkan pilihan (1/2): "))

if Pilihan_Kelamin == 1:
    Berat_Badan = int(input("masukkan berat badan pria (kg): "))
    Tinggi_Badan = int(input("masukkan tinggi badan pria (cm): "))
    Umur = int(input("Masukkan umur pria: "))
    BMR = (10*Berat_Badan) + (6.25*Tinggi_Badan) - (5*Umur) + 5
elif Pilihan_Kelamin == 2:
    Berat_Badan = int(input("masukkan berat badan wanita (kg): "))
    Tinggi_Badan = int(input("masukkan tinggi badan wanita (cm): "))
    Umur = int(input("Masukkan umur wanita: "))
    BMR = (10*Berat_Badan) + (6.25*Tinggi_Badan) - (5*Umur) - 161
else: 
    print("Tidak Valid")

#Level aktivitas harian

print("1. Aktivitas Minimal (Jarang Begerak)")
print("2. Aktivitas Sedang (Olahraga 1-3 kali seminggu)")
print("3. Aktivitas Tinggi (Olahraga 4-7 kali seminggu)")
Pilihan_Aktivitas = int(input("Masukkan pilihan (1/2/3): "))

if Pilihan_Aktivitas == 1:
    Level_Aktivitas = 1.25
elif Pilihan_Aktivitas == 2:
    Level_Aktivitas = 1.36
elif Pilihan_Aktivitas == 3:
    Level_Aktivitas = 1.72
else:
    print("Tidak Valid")

#TDEE

print(f"Hasil TDEE = {BMR*Level_Aktivitas}")

