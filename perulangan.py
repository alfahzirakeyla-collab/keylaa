#Sistem Penilaian Mahasiswa - for / if / input

jumlah_mhs= int(input("jumlah mahasiswa : "))

if jumlah_mhs >5 and jumlah_mhs <10:
    print("Jumlah mahasiswa harus 5 - 10!")
else:
    total_nilai = 0
    for urutan in range(1, jumlah_mhs + 1):
        skor = int(input(f"Masukkan Nilai mahasiswa {urutan}: "))
        total_nilai += skor
        if skor >= 90:
            print("  -> Nilai A")
        elif skor >= 80:
            print("  -> Nilai B")
        elif skor >= 70:
            print("  -> Nilai C")
        else:
            print("  -> Nilai D / Tidak Lulus")

    print(f"Nilai rata - rata : {total_nilai / jumlah_mhs}")
