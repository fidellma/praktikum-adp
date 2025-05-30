#Menghitung nilai akhir praktikan pada 1 shift yang sama
def menghitung_nilai_akhir(pretest, postest, tugas, bonus):
    return 0.25 * pretest + 0.25 * postest + 0.5 * tugas + bonus
print("Data nilai akhir Praktikan Shift V")
print()
jumlah = int(input("Masukkan banyak praktikan : "))
praktikan = []
for i in range(jumlah):
    print(f"\nPraktikan ke-{i+1}")
    print()
    nama = input("Nama : ")
    nim = input("NIM  : ")
    pretest = float(input("Nilai pretest : "))
    postest = float(input("Nilai postest : "))
    tugas = float(input("Nilai tugas/makalah : "))
    bonus = float(input("Nilai bonus   : "))
    nilai_akhir = menghitung_nilai_akhir(pretest, postest, tugas, bonus)
    praktikan.append([nama, nim, nilai_akhir])
for i in range(len(praktikan)):
    for j in range(i + 1, len(praktikan)):
        if praktikan[i][2] < praktikan[j][2]:
            praktikan[i], praktikan[j] = praktikan[j], praktikan[i]
print("\n----------------------------------------------------------")
print(f"| {'Nama':<15} | {'NIM':<10} | {'Nilai Akhir':<12} | {'Peringkat':<9}|")
print("----------------------------------------------------------")
total_nilai = 0
for i in range(len(praktikan)):
    nama = praktikan[i][0]
    nim = praktikan[i][1]
    nilai = praktikan[i][2]
    print(f"| {nama:<15} | {nim:<10} | {nilai:<12} | {i+1:<9}|")
    total_nilai += nilai
rata2 = total_nilai / len(praktikan)
print("----------------------------------------------------------")
print(f"| {'Rata-rata nilai akhir :':<15}      | {rata2:<12}            |")
print("----------------------------------------------------------")