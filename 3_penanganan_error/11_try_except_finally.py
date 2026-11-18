try:
    angka = int(input("Masukkan angka: "))
    print("-----")
    print("Angka anda:", angka)
except ValueError:
    print("Input tidak valid!")
finally:
    print("Program selesai dijalankan ^_^")