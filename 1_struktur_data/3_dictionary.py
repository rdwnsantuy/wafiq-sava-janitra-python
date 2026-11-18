# Prinsipnya sama. List, Tuple, Dictionary, maupun Set sama-sama menyimpan data.
# Dictionary menyimpan data dengan konsep pasangan. Key dan Value.
# Dictionary ditulis dengan kurung kurawal{}
# Key di Dictionary bisa menggunakan tipe data string, integer, float, boolean. Namun kebanyakan menggunakan string.
# Untuk mengakses dan mengubah value, kita bisa menggunakan kurung kotak [] -> seperti pada List
# Len bisa digunakan untuk menghitung panjang data
# Di Dictionary juga bisa dilakukan perulangan for

siswa = {
    "nama" : "Eko",
    "umur" : 17,
    "kelas" : "12A"
}

print(siswa)

print(siswa["nama"])
print(siswa["umur"])
print(siswa["kelas"])

siswa["kelas"] = "15B"
print(siswa)

del siswa["umur"]
print(siswa)

for key in siswa:
    print(key)

for key in siswa:
    print(key, siswa[key])

for key, value in siswa.items():
    print(key, value)