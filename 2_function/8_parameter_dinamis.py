# kita bisa memberi * sebelum nama parameter untuk membuat parameter dinamis berupa LIST
# kita bisa memberi ** sebelum nama parameter untuk membuat parameter dinamis berupa DICTIONARY

# PARAMETER DINAMIS UNTUK LIST
def fungsi_1(*kota):
    print("------------")
    for item in kota:
        print(item)

fungsi_1("sleman", "bantul", "kulon progo", "gunung kidul", "yogyakarta")

def fungsi_2(*nilai):
    print("-------------")
    for item in nilai:
        print(item)

fungsi_2(75, 76, 77, 78, 79, 80, 81, 82)

# PARAMETER DINAMIS UNTUK DICTIONARY
def fungsi_3(**data_diri):
    print("-------------")
    for key, value in data_diri.items():
        print(key, value)

fungsi_3(nama="Sava", umur=19, kota="Banyumas")
fungsi_3(nama="Ridwan", nama_lengkap="Ridwan Maulana", kota="Sleman")