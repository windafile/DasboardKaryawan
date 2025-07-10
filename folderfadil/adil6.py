import random

def pilih_karakter():
    print("pilih karaktermu:")
    print("1. warrior (hp: 100, attack: 20)")
    print("2. mage (hp: 70, attack: 30)")
    print("3. archer (hp: 80, attack: 25)")
    pilihan = input("masukan pilihan (1/2/3): ")

    if pilihan == "1":
        return {"nama": "warrior", "hp": 100, "attack": 20}
    elif pilihan == "2":
        return {"nama": "mage", "hp": 70, "attack": 30}
    elif pilihan == "3":
        return {"nama": "archer", "hp": 80, "attack": 25}
    else:
        print("pilihan tidak valid. default: warrior")
        return {"nama": "warrior", "hp": 100, "attack": 20}
    
def main():
    player = pilih_karakter()
    musuh = {"nama": "goblin", "hp": 100, "attack": 20} 

    print(f"\n musuh muncul! {musuh['nama']} (Hp: {musuh['hp']})") 
    print(f"kamu adalah {player['nama']} (Hp: {player['hp']})\n") 

    while player["hp"] > 0 and musuh["hp"] > 0:
        print(f"\n{player['nama']} hp: {player['hp']} | {musuh['nama']} hp: {musuh['hp']}")
        aksi = input("aksi (serang / bertahan / lari): ").lower()

        if aksi == "serang":
            damage = player ["attack"] + random.randint(-5, 5)
            musuh["hp"] -= damage
            print(f"kamu menyerang {musuh['nama']} kena {damage} damage.")
            

        elif aksi == "bertahan":
            print("kamu bertahan! menurangi damage serangan musuh.")
            damage = max(musuh["attack"] - random.randint(5, 15), 0) 
            player["hp"] -= damage
            print(f"{musuh['nama']} menyerangmu, tapi kamu hanya kena {damage} damage.")
            continue # lewati gilaran musuh normal

        elif aksi == "lari":
            if random.random() < 0.5:
                print("yahhh lemahhh !!!")
                return
            
            else:
                print("yahhh lemah !!!")
                continue

# giliran musuh (kalau dia masih hidup)
            if musuh["hp"] > 0:
                damage = musuh["attack"] + random.randint(-3, 3)
                player["hp"] -= damage
                print(f"{musuh['nama']} menyarang balik kamu kena {damage} damage.")

    # cek hasil akhir
    if player["hp"] <= 0:
        print("\n noob...")
    elif musuh["hp"] <= 0:
        print("\n selamat hero kau telah mengalahkan musuh")   
# jalan game 
main()                     

    
