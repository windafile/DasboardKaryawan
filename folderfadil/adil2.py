import random
angka_rahasia = random.randint(1, 10)
nyawa = 3

print("tebak angka dari 1 sampai 10. kamu punya 3 nyawa!")

while nyawa > 0:
    tebakan =int(input("masukan tebakanmu: "))
    if tebakan == angka_rahasia:
        print("maneh menang")
        break
    else:
        nyawa -= 1
        if tebakan < angka_rahasia:
            print("terlalu kecil.")
        else:
            print("badag teing.")
        print(f"sisa nyawa: {nyawa}")        
if nyawa == 0:
    print(f"maneh eleh iyeyeh anubener na {angka_rahasia}")        