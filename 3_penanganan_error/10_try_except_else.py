try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input tidak valid!")
else:
    print("Angka yang ada masukkan adalah", angka)
    print("-----")
    if angka > 0:
        print(f"Angka {angka} adalah angka positif")
    elif angka < 0:
        print(f"Angka {angka} adalah angka negatif")
    else:
        print(f"Anda memasukkan angka {angka}")