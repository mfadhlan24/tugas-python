from views.main_menu import main_menu
from views.input_view import input_data
from views.display_view import display_data
from views.edit_view import edit_data
from views.delete_view import delete_data
from controllers.item_controller import add_item, view_items, edit_item, remove_item, getItemById

def run():
    while True:
        choice = main_menu()
        if choice == '1':
            data = input_data()
            add_item(data['nama_barang'], data['jumlah'], data['lokasi'], data['tanggal_input'])
            print("Data berhasil ditambahkan!")
        elif choice == '2':
            items = view_items()
            display_data(items)
        elif choice == '3':
            item = int(input("Silahkan Masukan ID BARANG yang akan dilihat : "))
            display_data(getItemById(item))
        elif choice == '4':
            data = edit_data()
            edit_item(data['id_barang'], data['nama_barang'], data['jumlah'], data['lokasi'], data['tanggal_input'])
            print("Data berhasil diupdate!")
        elif choice == '5':
            id_barang = delete_data()
            remove_item(id_barang)
            print("Data berhasil dihapus!")
        elif choice == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

run()