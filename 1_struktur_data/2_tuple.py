# Tuple ditulis dengan kurung biasa ()
# Data di dalam Tuple tidak bisa diubah setelah dibuat
# Cara mengakses data di Tuple sama dengan di List
# Function len(tuple) digunakan untuk menghitung panjang Tuple
# Di Tuple kita juga bisa melakukan perulangan (iterasi)

# Membuat data Tuple
point = (5, 10)

# Mengakses data Tuple menggunakan nama Tuple
print(point)

# Mengakses data Tuple menggunakan indeks
print(point[0])
print(point[1])

# Membuat data Tuple
tanggal_lahir = (9, 9, 1999)

# Mengakses data Tuple menggunakan nama Tuple
print(tanggal_lahir)

# Melakukan perulangan for pada Tuple
for x in tanggal_lahir:
    print(x)