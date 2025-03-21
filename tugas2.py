#Input dari pengguna
lamda_t = float(input("Masukkan nilai λt : "))
m = int(input("Masukkan nilai M : "))

#Nilai konstanta e
e = 2.71828

n_faktorial = 1 
for n in range (m + 1):
    p = (e ** (-lamda_t)) * ((lamda_t) ** n) / n_faktorial
    n_faktorial *= (n + 1)
    
    # Menampilkan hasil perhitungan untuk P(N(t) = n)
    print(f"Nilai P(N(t) = {n}) = {p}")