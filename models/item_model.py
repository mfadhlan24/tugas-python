from database.conn import conn

def create_item(nama_barang, jumlah, lokasi, tanggal_input):
    db = conn()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO inventaris (nama_barang, jumlah, lokasi, tanggal_input) VALUES (%s, %s, %s, %s)",
        (nama_barang, jumlah, lokasi, tanggal_input),
    )
    db.commit()
    db.close()

def get_all_items():
    db = conn()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventaris")
    items = cursor.fetchall()
    db.close()
    return items

def update_item(id_barang, nama_barang, jumlah, lokasi, tanggal_input):
    db = conn()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE inventaris SET nama_barang=%s, jumlah=%s, lokasi=%s, tanggal_input=%s WHERE id_barang=%s",
        (nama_barang, jumlah, lokasi, tanggal_input, id_barang),
    )
    db.commit()
    db.close()

def delete_item(id_barang):
    db = conn()
    cursor = db.cursor()
    cursor.execute("DELETE FROM inventaris WHERE id_barang=%s", (id_barang,))
    db.commit()
    db.close()

