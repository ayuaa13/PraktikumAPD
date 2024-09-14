print("Biodata saya")

Nama_Lengkap = input("Nama Lengkap: ")
Nama_Panggilan = input("Nama Panggilan: ")
Fakultas = input("Fakultas: ")
Prodi = input("Prodi: ")  
NIM = int(input("NIM: "))
Umur = float(input("Umur: "))
Tinggi_Badan = float(input("Tinggi Badan dalam satuan M: "))
Jarak_Kampus = float(input("Jarak dari rumah atau kos ke Kampus dalam satuan KM: "))
Cita_cita = ["Software engineer","Software developer", "System analyst", "IT consultant","Cyber security specialist"]
Nim_Terakhir = NIM - 2409106000
Nim_Modulus = Nim_Terakhir % 6

print("Nama Saya",Nama_Lengkap,"saya biasa dipanggil",Nama_Panggilan,"saya dari fakultas",Fakultas,"prodi",Prodi,"dengan NIM",NIM)
print("Umur Saya Tahun ini",Umur,"Tahun","Tinggi badan saya",Tinggi_Badan,"M","dan Jarak dari Rumah atau kos Saya ke Kampus",Jarak_Kampus,"KM")
print("cita-cita saya adalah",Cita_cita[1])
print("3 angka terakhir pada NIM saya setelah dimoduluskan dengan 6 adalah",Nim_Modulus)
