#Membuatv Program Sederhana Menghitung data keuangan untuk anak kost-kosan
print("----Program Menghitung Data Keuangan----")
file_nama = "data_keuangan.txt"
data = {}
f = open(file_nama, "a")
f.close()
f = open(file_nama, "r")
for line in f:
    bagian = line.strip().split("|")
    if len(bagian) >= 5:
        nomor = bagian[0]
        tanggal = bagian[1]
        keterangan = bagian[2]
        jumlah = bagian[3]
        tipe = bagian[4]
        data[nomor] = {
            "tanggal": tanggal,
            "keterangan": keterangan,
            "jumlah": jumlah,
            "tipe": tipe  }
f.close()
while True:
    print("\nMenu:")
    print("1. Tambah data keuangan")
    print("2. Hapus data keuangan")
    print("3. Tampilkan semua data")
    print("4. Keluar")
    print()

    # untuk mengolah data keuangannya, tambha data, hapus data, dan tampilkan
    pilihan = input("Pilih menu (1-4): ")
    if pilihan == "1":
        no_data = str(len(data) + 1)
        tanggal = input("Tanggal (YYYY/MM/DD): ")
        keterangan = input("Keterangan  : ")
        jumlah = input("Jumlah uang : ")
        tipe = input("Tipe (pengeluaran/pemasukan): ")
        data[no_data] = {
            "tanggal": tanggal,
            "keterangan": keterangan,
            "jumlah": jumlah,
            "tipe": tipe }
        f = open(file_nama, "w")
        for no_item in data:
            line = no_item + "|" + data[no_item]["tanggal"] + "|" + data[no_item]["keterangan"] + "|" + data[no_item]["jumlah"] + "|" + data[no_item]["tipe"] + "\n"
            f.write(line)
        f.close()
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        print("=== Data Keuangan ===")
        for no_item in data:
            print(no_item + ": " + data[no_item]["tanggal"] + " - " + data[no_item]["keterangan"] + " - " + data[no_item]["jumlah"] + " - " + data[no_item]["tipe"])
        no_hapus = input("Masukkan nomor data yang ingin dihapus: ")
        if no_hapus in data:
            del data[no_hapus]
            f = open(file_nama, "w")
            for no_item in data:
                line = no_item + "|" + data[no_item]["tanggal"] + "|" + data[no_item]["keterangan"] + "|" + data[no_item]["jumlah"] + "|" + data[no_item]["tipe"] + "\n"
                f.write(line)
            f.close()
            print("Data berhasil dihapus!")
        else:
            print("Nomor data tidak ditemukan!")

    elif pilihan == "3":
        if len(data) == 0:
            print("Data anda kosong, silahkan masukkan data baru!")
        else:
            print("\n----Data Keuangan----")
            for no_item in data:
                print(" Nomor:", no_item)
                print(" Tanggal    :", data[no_item]["tanggal"])
                print(" Keterangan :", data[no_item]["keterangan"])
                print(" Jumlah     :", data[no_item]["jumlah"])
                print(" Tipe       :", data[no_item]["tipe"])
                print("-----------------------")
    elif pilihan == "4":
        print("Program selesai. Terima kasih. Semangat Berhemat^^")
        break
    else:
        print("Pilihan tidak valid.") 
