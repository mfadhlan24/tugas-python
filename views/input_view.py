def input_data():
    print("\n--- Input Data Baru ---")
    nama_barang = input("Nama Barang: ")
    jumlah = int(input("Jumlah: "))
    lokasi = input("Lokasi: ")
    tanggal_input = input("Tanggal Input (YYYY-MM-DD): ")
    return {
        "nama_barang": nama_barang,
        "jumlah": jumlah,
        "lokasi": lokasi,
        "tanggal_input": tanggal_input
    }
