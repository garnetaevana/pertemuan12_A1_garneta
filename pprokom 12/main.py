import menu
import persegi
import segitiga
import lingkaran

def main():
    while True:
        pilih = menu.daftar_menu()
        if pilih == "1":
            if not persegi.bidang_persegi():
                break
        elif pilih == "2":
            if not lingkaran.bidang_lingkaran():
                break
        elif pilih == "3":
            if not segitiga.bidang_segitiga():
                break
        elif pilih == "4":
            break
        else:
            print ("Tidak valid")

if __name__ == "__main__":
    main()
