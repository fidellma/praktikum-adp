#Daftar Paket Makanan & Harga
print("----------------------------------'Ni Hau!! Its UmmaMiia Dimsum'-----------------------------------")
print("                                   WELCOME to Dimsum Urang Awak                                    ")
print("---------------------------------------------------------------------------------------------------")
print("-------------------------------Paket Dimsum HURRAA Spesial Tahun Baru------------------------------")
print("---------------------------------------------------------------------------------------------------")
print("Paket Dimsum                   Isi                                                      Price      ")
print("Dimsum Ori                     Dimsum saus, Pangsit Basah, Lemontea                     Rp 30.000  ")
print("Black Dimsum                   Dimsum chili oil, Spicy Pangsit, Leci Tea                Rp 45.000  ")
print("Gong Dimsum                    Dimsum Udang, Drumb Stick, Matcha                        Rp 50.000  ")
print("Hot Dimsum                     Spicy Chiken Dimsum, Hot Hakau Laota, Lemontea           Rp 50.000  ")
print("Golden Dimsum                  Dimsum mentai, Hakau Chili oil, Jus Mangga               Rp 60.000  ")
print("---------------------------------------------------------------------------------------------------")
print("----------------------------- ^^ Xie-Xie, Tarimo Kasii lah Balanjoo ^^ ----------------------------")
print("                                                                                                   ")

#Detail Pemesanan
nama=input("Nama :")
nomor_telepon=int(input("Nomor Telepon :"))
alamat=input("Alamat Pengiriman :")
pesanan=input("Paket yang dipesan :")
jumlah=int(input("Jumlah paket yang dipesan :"))

#Harga tiap paket
dimsum_ori=    30000
black_dimsum=  45000
gong_dimsum=   50000
hot_dimsum=    50000
golden_dimsum= 60000

#Menentukan Pesanan dan Harga
if pesanan == "Dimsum Ori" : 
    p = ("Dimsum saus, Pangsit Basah, Lemontea")
    harga = jumlah*dimsum_ori
elif pesanan == "Black Dimsum" :
    p = ("Dimsum chili oil, Spicy Pangsit, Leci Tea")
    harga = jumlah*black_dimsum
elif pesanan == "Gong Dimsum" :
    p = ("Dimsum Udang, Drumb Stick, Matcha")
    harga = jumlah*gong_dimsum
elif pesanan == "Hot Dimsum" :
    p = ("Spicy Chiken Dimsum, Hot Hakau Laota, Lemontea")
    harga = jumlah*hot_dimsum
elif pesanan == "Golden Dimsum" : 
    p = ("Dimsum mentai, Hakau Chili oil, Jus Mangga")
    harga = jumlah*golden_dimsum

#Menentukan Pajak
pajak = harga*(10/100)

#Menentukan Total Harga setelah dipajak
total_harga_setelah_dipajak = harga + pajak

#Menentukan Biaya Pengiriman
if harga < 150000 :
    biaya_pengiriman = 25000
else :
    biaya_pengiriman = 0

#Total Biaya Keseluruhan
total_biaya_keseluruhan = harga + pajak + biaya_pengiriman

#Menampilkan Hasil
print("                                                                                                   ")
print("----------------------------------------STRUK PEMESANAN--------------------------------------------")
print("                                                                                                   ")
print("Nama                               :",nama )
print("Nomor Telepon                      :",nomor_telepon )
print("Alamat Pengiriman                  :",alamat )
print("Detail Pesanan                     : Paket", pesanan , "{",p,"}")
print("Jumlah                             :",jumlah )
print("Total Harga                        :",harga )
print("Pajak (10%)                        :",pajak )
print("Biaya Pengiriman                   :",biaya_pengiriman )
print("Total Akhir                        :",total_biaya_keseluruhan )
print("                                                                                                   ")
print("---------------------------------------------------------------------------------------------------")
