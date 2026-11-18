def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    # print(f"Hasil perhitungan lingkarannya adalah {luas}")
    return luas

def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    # print(f"Hasil perhitungan persegi adalah {luas}")
    return luas

def hitung_luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2
    # print(f"Luas segitiga adalah {luas}")
    return luas

# hasil_perhitungan = hitung_luas_lingkaran(5)

# print("Luas lingkaran 1 adalah:", hasil_perhitungan)

# hitung_luas_lingkaran(15)
# hitung_luas_persegi(15)
# hitung_luas_segitiga(12, 14)

hitung_luas_lingkaran(15)
angka2 = hitung_luas_persegi(15)
angka3 = hitung_luas_segitiga(12, 14)

