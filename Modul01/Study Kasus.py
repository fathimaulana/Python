nama_mahasiswa = input("Masukkan nama Anda: ") #string
nilai_mahasiswa = int(input("Masukkan nilai Anda: ")) #integer

if nilai_mahasiswa >=90:
    print("Selamat", nama_mahasiswa, "Anda Lulus Dengan Predikat A")
elif nilai_mahasiswa >=75:
    print("Selamat", nama_mahasiswa, "Anda Lulus Dengan Predikat B")
else:
    print("Maaf", nama_mahasiswa, "Anda Tidak Lulus Dengan Predikat C")
