# FITUR KEYWORD ARGUMENT
# argument adalah nilai yang kita kirim ke function melalui parameter
# saat memanggil function, posisi argument harus sama dengan posisi parameter di function
# saat memanggil function, posisi argument boleh berbeda dengan posisinya di function -> asalkan kita menyebut nama parameternya
# fitur ini disebut dengan KEYWORD ARGUMENT
# saat menggunakan keyword argument, tetap bisa kita kombinasikan dengan argument biasa

def perkenalan(nama, umur, kota):
    print("-------------------")
    print("Namaku adalah:", nama)
    print("Umurku sekarang adalah:", umur)
    print("Aku sekarang tinggal di:", kota)

perkenalan("Sava", 19, "Banyumas")

perkenalan(nama="Budi", kota="Bantul", umur=21)

perkenalan(kota="Kendal", nama="Asif", umur=23)