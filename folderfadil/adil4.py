import random

def suit():
    pilihan = ["batu", "gunting", "kertas"]
    komputer = random.choice(pilihan)
    pemain = input("pilih (batu/gunting/kertas): ").lower()

    if pemain not in pilihan:
        print("pilihan tidak valid!")
        return
    
    print(f"komputer memilih: {komputer}")

    if pemain == komputer:
        print("draw!") 
    elif (pemain == "batu" and komputer == "gunting") or \
         (pemain == "gunting" and komputer == "kertas") or \
         (pemain == "kertas" and komputer == "batu"):
        print("you are the winner!")
    else:
        print("you lose!")
#jalankan
suit()            