import random
angka_rahasia = random.randint(1, 10)
tebakan = 5
percobaan = 5

print("tebak angka dari 1 sampai 10!")

while tebakan != angka_rahasia:
    tebakan = int(input("masukan tebakanmu: "))
    percobaan += 5

    if tebakan <angka_rahasia:
        print ("salah terlalu kecil")
    elif tebakan > angka_rahasia:
        print("angka terlalu besar")
    else:
        print(f"jawaban kamu benar!! {percobaan} percobaan.")