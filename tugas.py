# Mengimport Module Yang Diperlukan
import sys
print(sys.executable)
import mysql.connector
from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style, init

# ================================= #
# Initialization For Windows OS
init(autoreset=True)
# ================================= #
# Connection Handle
def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="inventorydb"
    )

# CRUD Controllers (Create, Read, Update dan Delete)

def addItem(id_barang, nama_barang, jumlah, lokasi, tanggal_input):
    try:
        db = conn()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO inventaris (id_barang, nama_barang, jumlah, lokasi, tanggal_input) VALUES (%s, %s, %s, %s, %s)",
            (id_barang, nama_barang, jumlah, lokasi, tanggal_input),
        )
        db.commit()
    except mysql.connector.Error as err:
        print(f"{Fore.RED}Database Error: {err}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
    finally:
        db.close()

def getAllItems():
    try:
        db = conn()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inventaris")
        items = cursor.fetchall()
        return items
    except mysql.connector.Error as err:
        print(f"{Fore.RED}Database Error: {err}")
        return []
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
        return []
    finally:
        db.close()

def findItem(id_barang):
    try:
        db = conn()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM inventaris WHERE id_barang = %s", (id_barang,))
        result = cursor.fetchone()
        return result if result else f"{Fore.RED}Barang tidak ditemukan"
    except mysql.connector.Error as err:
        print(f"{Fore.RED}Database Error: {err}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
    finally:
        db.close()

def updateItem(id_barang, nama_barang, jumlah, lokasi, tanggal_input):
    try:
        db = conn()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE inventaris SET nama_barang=%s, jumlah=%s, lokasi=%s, tanggal_input=%s WHERE id_barang=%s",
            (nama_barang, jumlah, lokasi, tanggal_input, id_barang),
        )
        db.commit()
    except mysql.connector.Error as err:
        print(f"{Fore.RED}Database Error: {err}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
    finally:
        db.close()

def deleteItem(id_barang):
    try:
        db = conn()
        cursor = db.cursor()
        cursor.execute("DELETE FROM inventaris WHERE id_barang=%s", (id_barang,))
        db.commit()
    except mysql.connector.Error as err:
        print(f"{Fore.RED}Database Error: {err}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")
    finally:
        db.close()

# Handle Display
def display_data(items):
    print(f"{Fore.CYAN}\n--- Daftar Barang ---")
    if not items:
        print(f"{Fore.RED}Tidak ada data barang.")
        return
    headers = ["ID", "Nama", "Jumlah", "Lokasi", "Tanggal"]
    data = [
        [item['id_barang'], item['nama_barang'], item['jumlah'], item['lokasi'], item['tanggal_input']]
        for item in items
    ]
    print(tabulate(data, headers=headers, tablefmt="grid"))

# Tampilan Pada Terminal
def run():
    while True:
        print(f"{Fore.YELLOW}=== RASIS GROUP COMUNISM ===")
        print(f"{Fore.YELLOW}=== MENU INVENTARIS ===")
        print(f"{Fore.BLUE}1. Tambah Barang")
        print(f"{Fore.BLUE}2. Lihat Barang")
        print(f"{Fore.BLUE}3. Lihat Barang By ID")
        print(f"{Fore.BLUE}4. Edit Barang")
        print(f"{Fore.BLUE}5. Hapus Barang")
        print(f"{Fore.BLUE}6. Keluar")
        choice = input(f"{Fore.YELLOW}Pilih menu (1-6): ")

        if choice == "1":
            try:
                print(f"{Fore.GREEN}\n=== Input Barang Baru ===")
                data = {
                    "id_barang": input(f"{Fore.YELLOW}Masukan ID Barang : "),
                    "nama_barang": input(f"{Fore.YELLOW}Masukan Nama Barang: "),
                    "jumlah": int(input(f"{Fore.YELLOW}Masukan Kuantitas Barangnya: ")),
                    "lokasi": input(f"{Fore.YELLOW}Masukan Lokasi Nya: "),
                    "tanggal_input": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                addItem(**data)
                print(f"{Fore.GREEN}Barang berhasil ditambahkan!")
            except ValueError:
                print(f"{Fore.RED}Input jumlah harus berupa angka!")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")

        elif choice == "2":
            try:
                items = getAllItems()
                display_data(items)
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")

        elif choice == "3":
            try:
                id_barang = input(f"{Fore.YELLOW}Masukkan ID Barang: ")
                item = findItem(id_barang)
                if isinstance(item, dict):
                    display_data([item])
                else:
                    print(item)
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")

        elif choice == "4":
            try:
                id_barang = input(f"{Fore.YELLOW}Masukkan ID Barang yang ingin diubah: ")
                data = {
                    "nama_barang": input(f"{Fore.YELLOW}Nama Barang Baru: "),
                    "jumlah": int(input(f"{Fore.YELLOW}Kuantitas Baru: ")),
                    "lokasi": input(f"{Fore.YELLOW}Lokasi Baru: "),
                    "tanggal_input": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                updateItem(id_barang, **data)
                print(f"{Fore.GREEN}Barang berhasil diperbarui!")
            except ValueError:
                print(f"{Fore.RED}Input jumlah harus berupa angka!")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")

        elif choice == "5":
            try:
                id_barang = input(f"{Fore.YELLOW}Masukkan ID Barang yang ingin dihapus: ")
                deleteItem(id_barang)
                print(f"{Fore.GREEN}Barang berhasil dihapus!")
            except Exception as e:
                print(f"{Fore.RED}Error: {e}")

        elif choice == "6":
            print(f"{Fore.CYAN}Keluar dari program.")
            break

        else:
            print(f"{Fore.RED}Pilihan tidak valid, coba lagi!")

# run 
run()
