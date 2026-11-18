# LIST ditulis menggunakan kurung siku []

# membuat LIST berisi angka
angka = [1, 2, 3, 4, 5, 6]
print(angka)

# membuat LIST berisi string
nama = ["Eko", "Budi", "Joko"]
print(nama)

# membuat LIST berisikan campuran angka dan string
campuran = ["Eko", 90, "Budi", 85, "Joko", 87]
print(campuran)

# LIST merupakan data yang berurutan, maka cara mengaksesnya adalah menggunakan indeks
# cara mengganti isi LIST sama seperti mengubah isi variabel biasa
# method append(data) -> digunakan untuk menambah data di urutan terakhir
# method insert(index, data) -> digunakan untuk menambah data setelah index
# method remove(index) -> digunakan untuk menghapus data pada index tsb
# method pop() -> digunakan untuk menghapus data terakhir
# function len -> digunakan untuk menghitung panjang list
# operator + -> bisa digunakan untuk menggabungkan list satu dengan list lain
# LIST bisa diiterasi menggunakan for loop

# mengakses data di dalam LIST menggunakan indeks
buah = ["apel", "mangga", "jeruk", "melon"]
print(buah[0])
print(buah[1])
print(buah[2])
print(buah[3])

# mengubah/mengganti data di dalam LIST
warna = ["merah", "kuning", "hijau"]
print(warna)

warna[1] = "jingga"
print(warna)

# menambahkan data di urutan terakhir
warna.append("ungu")
print(warna)

# menambahkan data di urutan yang kita mau
warna.insert(1, "pink")
print(warna)

# menghapus data dengan remove (ketik isi datanya, bukan indeks)
warna.remove("pink")
print(warna)

# menghapus data dengan del (ketik indeksnya, bukan isi data)
del warna[0]
print(warna)

# menghapus data yang ada di urutan terakhir
warna.pop()
print(warna)

# menghitung panjang isi data dengan function len
warna = ["merah", "kuning", "hijau"]
print(len(warna))

# menggabungkan 2 atau lebih data LIST dengan +
satu = [1, 2, 3, 4, 5]
print(satu)

dua = [6, 7, 8, 9, 10]
print(dua)

gabungan = satu + dua
print(gabungan)

# menggunakan perulangan for tehadap data LIST
banyak_buah = ["apel", "mangga", "jeruk", "melon"]

for b in banyak_buah:
    print(b)

for i in range(0, len(banyak_buah)):
    print(banyak_buah[i])

if "salak" in banyak_buah:
    print("ada salak")
else:
    print("tidak ada salak")