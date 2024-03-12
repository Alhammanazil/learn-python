import main
from services import db

def add():
    kode_barang = input("input kode barang: ")
    nama_barang = input("input nama barang: ")
    harga_barang = int(input("input harga barang: "))
    stok_barang = int(input("input stok barang: "))

    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)

def check():
    rows = db.fetch_item()
    for row in rows:
        kode_barang = row[1]
        nama_barang = row[2]
        harga_barang = row[3]
        stok_barang = row[4]
        print(f'''
Code - {kode_barang}
{nama_barang} | {harga_barang}
Stock: {stok_barang}
''')

def start():
    while True:
        menu = int(input('\nmenu:\n\n1. Add item\n2. Show item\n3. Exit\n\ninput number of menu: '))

        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            print("Invalid input. Please input a number between 1 and 3.")

        play_again = input("back to main menu? [y/n] ")

        if play_again == "y":
            main.menu()


if __name__ == "__main__":
    start()
