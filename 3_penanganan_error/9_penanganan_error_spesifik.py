try:
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    hasil = a / b
    print("Hasil pembagian:", hasil)
except ValueError:
    print("Mohon masukkan angka yang valid!")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol!")
except:
    print("Terjadi kesalahan yang lain!")