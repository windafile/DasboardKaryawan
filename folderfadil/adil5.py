import random

def tebak_kata():
    kata_list = ["lumbung", "binar" , "renjana" , "sukma" , "kidung"]
    kata_rahasia = random.choice(kata_list)
    huruf_tertebak = []
    nyawa = 7

    print("=== game tebak kata ===")
    print(f"kata terdiri dari {len(kata_rahasia)} huruf.")

    while nyawa > 0:
        tampilan = ""
        for huruf in kata_rahasia:
            if huruf in huruf_tertebak:
                tampilan += huruf + " "
            else:
                tampilan += "_ "  
        print("\n"  + tampilan)          
        
        if "_" not in tampilan:
            print("horeee you are the winner!")
            break
        
        tebakan = input("tebakan satu huruf: ").lower()

        if len(tebakan) != 1 or not tebakan.isalpha():
            print("masukkan hanya satu huruf")
            continue
    
        if tebakan in huruf_tertebak:
            print("kamu sudah menebak huruf itu.")
            continue

        huruf_tertebak.append(tebakan)
        
        if tebakan not in kata_rahasia:
           nyawa -= 1
        print(f"salah! nya tersisa: {nyawa}") 

    else:
        print(f"sorry you are lost: {kata_rahasia}")
#jalankan game
tebak_kata()    

                