# parameter digunakan untuk mengirimkan data ke function
# cara membuat function -> tambahkan nama parameter di dalam kurung function
# ingin lebih dari 1 function? -> gunakan koma
# cara menggunakan -> isi data parameter saat memanggil function

def sapa_nama(nama):
    print("Hello", nama)
    print("Selamat pagi, semangat!")
    print("==============")

sapa_nama("Ridwan")
sapa_nama("Bahlil")

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang adalah:", luas)
    print("==============")


hitung_luas_persegi_panjang(25, 24)
hitung_luas_persegi_panjang(20, 50)