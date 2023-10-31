def bidang_persegi():
    print ("Menghitung Luas Persegi Panjang")
    p = int(input("Masukkan Panjang : "))
    l = int(input("Masukkan Lebar : "))
    luas = p*l
    print ("Luas Persegi Panjang adalah ", luas)
    print ()
    print("Coba lagi [Y?N]?")
    back = input().upper()
    if back == "Y":
        return True
    else:
        return False
    

 