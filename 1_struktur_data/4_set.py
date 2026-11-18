# Set adalah kumpulan data yang tidak berurutan dan tidak memiliki duplikat
# Set ditulis dengan kurung kurawal {} atau fungsi set()
# method add(value) digunakan untuk menambahkan data ke set
# method remove(value) digunakan untuk menghapus data ke set
# karena set memiliki tipe data yang tidak berurutan, maka tidak bisa diakses menggunakan indeks
# untuk mengakses data di set biasanya menggunakan perulangan for

buah = {"jeruk", "apel", "pisang"}
print(buah)

buah.add("mangga")
print(buah)

buah.add("mangga")
print(buah)

buah.remove("jeruk")
print(buah)

for x in buah:
    print(x)