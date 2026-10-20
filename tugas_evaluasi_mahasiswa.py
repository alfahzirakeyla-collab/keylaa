# 1. Input
tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai uts: "))
uas = float(input("Masukkan nilai uas: "))
kehadiran_mahasiswa = float(input("Masukkan persentase kehadiran: "))

nilai_akhir = (20 / 100 * tugas) + (30 / 100 * uts) + (50 / 100 * uas)

print("=== SISTEM EVALUASI MAHASISWA ===")
print("Nilai akhir =", nilai_akhir)
print(kehadiran_mahasiswa, "%")

if nilai_akhir >=85 and kehadiran_mahasiswa >=90 and nilai_akhir % 2 == 0:
             print("status : LULUS DENGAN PREDIKAT")
elif nilai_akhir >=75 and kehadiran_mahasiswa >=80:
            print ("status : LULUS")
else :
    print ("status : BELUM LULUS")