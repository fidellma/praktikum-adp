nomor_mahasiswa = []
nama_mahasiswa = []
nilai_mahasiswa = []
while True :
    print("Manajemen Data : Nilai Mahasiswa Matematika tahun 2024")
    print("1). Tambah data")
    print("2). Hapus data")
    print("3). Tampilkan data")
    print("4). Keluar")
    print()
    data=int(input("Masukkan pilihan : "))
    if data == 1 :
        print()
        print("Tambahkan Data Mahasiswa")
        nomor = int(input("Nomor mahasiswa : "))
        nama = (input("Nama mahasiswa  : "))
        nilai = float(input("Nilai mahasiswa : "))

        nomor_mahasiswa.append(nomor)
        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)
        print("Data berhasil ditambahkan")
        print()

    elif data == 2 :
        print()
        print("Hapus Data Mahasiswa")
        nomor_hapus = int(input("Masukkan Nomor Mahasiswa yang akan dihapus: "))
        ditemukan = False
        for i in range(len(nomor_mahasiswa)):
            if nomor_mahasiswa[i] == nomor_hapus:
                del nomor_mahasiswa[i]
                del nama_mahasiswa[i]
                del nilai_mahasiswa[i]
                ditemukan = True
                print("Data Berhasil dihapus.\n")
                break
        if ditemukan == False:
            print("Data tidak ditemukan.\n")

    elif data == 3 :
        print()
        print("Data Mahasiswa")
        if len(nomor_mahasiswa) == 0:
            print("Belum ada data.\n")
        else:
            gabungan = []
            for i in range(len(nomor_mahasiswa)):
                gabungan.append((nomor_mahasiswa[i], nama_mahasiswa[i], nilai_mahasiswa[i]))
            n = len(gabungan)
            batas = n
            while batas > 1 :
                for i in range(batas -1) :
                    if gabungan[i][2] < gabungan[i+1][2]:
                        temp = gabungan[i]
                        gabungan[i] = gabungan[i+1]
                        gabungan[i+1] = temp
                batas -=1
            print("Nomor Mahasiswa          1Nama Mahasiswa                      Nilai Mahasiswa")
            for data in gabungan:
                print(f" {data[0]:<20}      {data[1]:<20}          {data[2]:<20}")
            print()
    elif data == 4 :
        print("Terima Kasih ^^")
        break
    else :
        print("Pilihan tidak valid , silahkan coba lagi")