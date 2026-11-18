# return value digunakan untuk agar kita bisa mendapatkan nilai dari kegiatan yang dilakukan di dalam function
# function bisa mengembalikan/memberi kita nilai dengan kata kunci return
# setelah kata return, diikuti dengan nilai yang kita inginkan

def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas

luas_lingkaran_1 = hitung_luas_lingkaran(5)
luas_lingkaran_2 = hitung_luas_lingkaran(10)

print("Luas lingkaran 1 adalah:", luas_lingkaran_1)
print("Luas lingkaran 2 adalah:", luas_lingkaran_2)