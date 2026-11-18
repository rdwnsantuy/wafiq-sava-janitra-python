# Local variabel adalah variabel yang hanya bisa dipakai di areanya sendiri
# Global variabel adalah variabel yang bisa dipakai di manapun
# Di dalam area function, global variabel hanya bisa dipakai. Tidak bisa diubah, kecuali dengan key "global"

# ============== LOCAL VARIABEL

def fungsi_test_1():
    a = 10
    print(f"Nilai dari fungsi ini adalah {a}")
    print("---------------------------------")

fungsi_test_1() # menjalankan function

# mencoba mencetak nilai variabel a yang ada di dalam function fungsi_test_1
# print(a) 

# ============= GLOBAL VARIABEL
b = 15

def fungsi_test_2():
    print(f"{b} adalah nilai dari b (variabel global)")
    print("------------------------------------------")

def fungsi_test_3():
    global b
    b = 25

fungsi_test_2()
fungsi_test_3()

print(f"{b} adalah nilai dari variabel b")