# jika dalam membuat parameter kita wajib memberi isi dari parameter tersebut, dengan fitur default parameter kita jadi tidak wajib lagi mengisi parameter tsb
# default parameter adalah nilai awal untuk parameter tersebut
# posisi default parameter tidak boleh di depan parameter biasa
# cara membuat default parameter -> tambahkan "=" dan berikan isi parameternya

def sapa(nama, sapaan="Halo, selamat datang!"):
    print("----------------")
    print(sapaan, nama)

sapa("Eko")
sapa("Sava", "Halo, selamat pagi!")
sapa("Prabowo", "Hey, antek-antek asing!")