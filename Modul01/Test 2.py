nama = input("Masukkan nama Anda: ") #string
umur = int(input("Masukkan umur Anda: ")) #integer
tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam cm): ")) #float
berat_badan = float(input("Masukkan berat badan Anda (dalam kg): ")) #float

print("Hallo", nama)
print("Umur:", umur)
print("Tinggi Badan:", tinggi_badan)
print("Berat Badan:", berat_badan)
print("Berat Badan Ideal:", (tinggi_badan - 100))