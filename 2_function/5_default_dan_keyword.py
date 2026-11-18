def buat_profil(nama, umur, kota="Sleman", pekerjaan="Programmer"):
    print(f"==== PROFIL {nama.upper()}")
    print(f"umur = {umur} tahun")
    print(f"kota = {kota}")
    print(f"pekerjaan = {pekerjaan}")
    print("===================")

buat_profil("Ridwan", 22)
buat_profil("Sava", 19, kota="Banyumas")
buat_profil("Gibran", 36, pekerjaan="Wakil Presiden")