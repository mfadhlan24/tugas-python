from tabulate import tabulate

def display_data(items):
    print("\n--- Daftar Barang ---")
    if not items:
        print("Tidak ada data barang.")
        return

    # Membuat header tabel
    headers = ["ID", "Nama", "Jumlah", "Lokasi", "Tanggal"]

    # Mengambil data barang dalam bentuk list of lists
    # expression for data in datasheet
    data = [
        [item['id_barang'], item['nama_barang'], item['jumlah'], item['lokasi'], item['tanggal_input']]
        for item in items
    ]
    
    # Menampilkan tabel
    print(tabulate(data, headers=headers, tablefmt="grid"))
