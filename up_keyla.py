print("SISTEM PENILAIAN AKADEMIK")

jumlah = int(input("Masukkan jumlah mahasiswa : "))

lulus = 0
tidak_lulus = 0

for i in range(jumlah):
    print()
    print("Mahasiswa ke-", i+1)
    nama = input("Nama : ")
    nilai = int(input("Nilai : "))

    if nilai >= 85:
        huruf = "A"
        ket = "Sangat Baik"
    elif nilai >= 75:
        huruf = "B"
        ket = "Baik"
    elif nilai >= 60:
        huruf = "C"
        ket = "Cukup"
    else:
        huruf = "D"
        ket = "Tidak Lulus"

    print("Nama :", nama)
    print("Nilai :", nilai)
    print("Kategori :", huruf, "-", ket)

    if nilai >= 60:
        print("Status : LULUS")
        lulus = lulus + 1
    else:
        print("Status : TIDAK LULUS")
        tidak_lulus = tidak_lulus + 1

print()
print("=========================")
print("Jumlah yang lulus :", lulus)
print("Jumlah tidak lulus :", tidak_lulus)
print("Total :", jumlah)