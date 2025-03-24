import random # library untuk menghasilkan angka acak
import datetime #library untuk menangani tanggal dan waktu 

# Struktur Data: List untuk menyimpan buku
library = []

# Fungsi untuk menambahkan buku
def add_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan nama penulis: ")
    year = input("Masukkan tahun terbit: ")
    
    book_id = f"B{random.randint(1000, 9999)}"  # ID buku acak
    added_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    book = {
        "ID": book_id,
        "Judul": title,
        "Penulis": author,
        "Tahun Terbit": year,
        "Tanggal Ditambahkan": added_date
    }
    
    library.append(book)
    print(f"\n📚 Buku '{title}' berhasil ditambahkan dengan ID {book_id}!\n")

# Fungsi untuk melihat daftar buku
def view_books(): 
    if not library: # struktur kontrol
        print("\n📌 Perpustakaan masih kosong!\n")
        return
    
    print("\nDaftar Buku di Perpustakaan:\n")
    for book in library:
        print(f"ID: {book['ID']}, Judul: {book['Judul']}, Penulis: {book['Penulis']}, Tahun: {book['Tahun Terbit']}, Ditambahkan: {book['Tanggal Ditambahkan']}")
    print("\n")

# Menu Utama
def main():
    while True: # struktur kontrol
        print("\n===== Sistem Manajemen Perpustakaan =====")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Keluar")
        
        choice = input("Pilih menu (1-3): ")
        
        if choice == "1": # struktur kontrol 
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print("\n👋 Terima kasih telah menggunakan sistem!\n")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi!\n")

# Menjalankan program
if __name__ == "__main__":
    main()
