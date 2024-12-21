def edit_data():
    print("\n--- Edit Data Barang ---")
    id_barang = int(input("ID Barang yang akan diubah: "))
    nama_barang = input("Nama Baru: ")
    jumlah = int(input("Jumlah Baru: "))
    lokasi = input("Lokasi Baru: ")
    tanggal_input = input("Tanggal Baru (YYYY-MM-DD): ")
    return {
        "id_barang": id_barang,
        "nama_barang": nama_barang,
        "jumlah": jumlah,
        "lokasi": lokasi,
        "tanggal_input": tanggal_input
    }
