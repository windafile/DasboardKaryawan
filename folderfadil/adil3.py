def kalkulator():
    print("kalkulator sederhana")
    print("1. tambah\n2. kurang\n3. kali\n4. bagi")
    pilihan = input("pilih operasi (1/2/3/4): ")

    try:
        a = float(input("masukan angka pertama: "))
        b = float(input("masukan angka kedua: "))

        if pilihan == '1':
            print(f"hasil: {a + b}")
        elif pilihan == '2':
            print(f"hasil: {a - b}") 
        elif pilihan == '3':
            print(f"hasil: {a * b}")
        elif pilihan == '4':   
            if b != 0:
                  print(f"hasil: {a / b}")
            else:
                 print("tidak bisa dibagi 0!") 
        else:
             print("pilihan tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")      

#perulangan kalkulator    
while True:
    kalkulator()
    ulang = input("hitung lagi? (y/n): ")
    if ulang.lower() != 'y':
        print("Hatur nuhun pikeun ngagunakeun kalkulator")