print ("Selamat datang di sistem reservasi tiket konser Iwan Fals bertajuk Ramadhan!")
m = 8  
n = 5  
total_kursi = m * n

#Menampilkan Layout Kursi Konser
print("\nTampilan Layout Kursi")
for i in range(1, total_kursi+1):
    print(i, end=" ")
    if i % n == 0:
        print()  
        i += 1

#Menampilkan Harga Tiket Konser
print("\nHarga Tiket:")
print("VVIP    Rp 1.800.000")
print("VIP     Rp 1.200.000")
print("Reguler Rp   800.000")
print("Ekonomi Rp   600.000")

#Menampilkan Detail Pemesanan Tiket Konser
jumlah_pemesanan=int(input("\nMasukkan jumlah tiket yang ingin dipesan : "))

terpesan_vvip = 0
terpesan_vip = 0
terpesan_reguler = 0
terpesan_ekonomi = 0
kosong = ","

for i in range(1, jumlah_pemesanan + 1):
    print(f"\nPemesanan ke-{i}")
    nama = input("Masukkan nama Anda: ")
    no_kursi = int(input("Masukkan nomor kursi yang ingin dipesan : "))
    if 1<=no_kursi<=10:
        kategori = "VVIP"
        harga_tiket = 1800000
        terpesan_vvip += 1
    elif 11<=no_kursi<=20:
        kategori = "VIP"
        harga_tiket = 1200000
        terpesan_vip += 1
    elif 21<=no_kursi<=35:
        kategori = "Reguler"
        harga_tiket = 800000
        terpesan_reguler += 1
    elif 36 <= no_kursi <= 40 :
        kategori = "Ekonomi"
        harga_tiket = 600000
        terpesan_ekonomi += 1
    else : 
        kategori = "Kursi Tidak Tersedia"
        harga_tiket = 0
        print("Kursi Tidak Tersedia")
    password = input("Buat password untuk akses konser : ")
    kosong += str(no_kursi) + ","
    print("\n--- Struk Pemesanan Tiket ---")
    print(" ")
    print("Nama         :",nama)
    print("Nomor Kursi  :",no_kursi)
    print("Kategori     :",kategori)
    print("Harga        : Rp",harga_tiket)
    print("Password     :",password)
    print(" ")
    print("------------^-^----------------")

#Menampilkan Sisa Kursi
print("\nSisa kursi per kategori")
sisa_vvip = 10 - terpesan_vvip
sisa_vip = 10 - terpesan_vip
sisa_reguler = 15 - terpesan_reguler
sisa_ekonomi = 5 - terpesan_ekonomi
print("VVIP    : ",sisa_vvip)
print("VIP     : ",sisa_vip)
print("Reguler : ",sisa_reguler)
print("Ekonomi : ",sisa_ekonomi)

#Menampilkan Layout Kursi Stetelah Pemesanan
print("\nLayout Kursi Setelah Pemesanan:")
for j in range(1, 41):
    if f",{j},"  in kosong :
        print("0", end=" ")
    else:
        print(j, end=" ")
    if j % n == 0 :
        print()