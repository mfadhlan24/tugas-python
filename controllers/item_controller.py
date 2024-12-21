from models.item_model import create_item, get_all_items, update_item, delete_item

def add_item(nama_barang, jumlah, lokasi, tanggal_input):
    create_item(nama_barang, jumlah, lokasi, tanggal_input)

def view_items():
    return get_all_items()

def edit_item(id_barang, nama_barang, jumlah, lokasi, tanggal_input):
    update_item(id_barang, nama_barang, jumlah, lokasi, tanggal_input)

def remove_item(id_barang):
    delete_item(id_barang)

def getItemById(id_barang):
    data = get_all_items()
    for item in data:
        if item["id_barang"] == id_barang:
            return([item])
    


