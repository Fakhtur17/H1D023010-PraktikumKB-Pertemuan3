Deskripsi
Program ini adalah sistem manajemen perpustakaan sederhana yang dibuat menggunakan Python. Program ini memungkinkan pengguna untuk menambahkan buku ke dalam perpustakaan, melihat daftar buku yang telah ditambahkan, dan keluar dari sistem.
Fitur
Menambahkan Buku: Pengguna dapat memasukkan informasi buku seperti judul, penulis, dan tahun terbit. Sistem akan secara otomatis menghasilkan ID buku dan mencatat tanggal serta waktu penambahan buku.
Melihat Daftar Buku: Menampilkan semua buku yang telah ditambahkan dalam perpustakaan beserta informasi lengkapnya.
Keluar dari Sistem: Mengakhiri program dengan pesan perpisahan.

Teknologi yang Digunakan
Python: Bahasa pemrograman utama untuk menjalankan sistem ini.
Library bawaan Python:
random: Digunakan untuk menghasilkan ID buku secara acak.
datetime: Digunakan untuk mencatat tanggal dan waktu penambahan buku.

Cara Menggunakan
Jalankan program dengan perintah:

python nama_file.py

Pilih menu yang tersedia:
Tekan 1 untuk menambahkan buku baru.
Tekan 2 untuk melihat daftar buku dalam perpustakaan.
Tekan 3 untuk keluar dari program.

Jika memilih menambahkan buku, masukkan informasi yang diminta seperti judul, penulis, dan tahun terbit.
Jika memilih melihat daftar buku, sistem akan menampilkan semua buku yang telah ditambahkan.
Pilih 3 untuk keluar dari program.

Struktur Data

Data buku disimpan dalam bentuk list dengan elemen berbentuk dictionary yang berisi:

{
    "ID": "B1234",
    "Judul": "Nama Buku",
    "Penulis": "Nama Penulis",
    "Tahun Terbit": "2024",
    "Tanggal Ditambahkan": "2025-03-24 14:30:00"
}
Penjelasan Kode

Berikut adalah penjelasan singkat mengenai kode program:
Import Library

import random
import datetime

random: Digunakan untuk menghasilkan ID buku secara acak.
datetime: Digunakan untuk mencatat tanggal dan waktu penambahan buku.

Struktur Data
library = []
library: List yang digunakan untuk menyimpan data buku.

Fungsi Menambahkan Buku

def add_book():
    title = input("Masukkan judul buku: ")
    author = input("Masukkan nama penulis: ")
    year = input("Masukkan tahun terbit: ")
    book_id = f"B{random.randint(1000, 9999)}"
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

Mengambil input dari pengguna untuk judul, penulis, dan tahun terbit.
Menghasilkan ID buku secara acak.
Menyimpan data buku ke dalam list library.

Fungsi Melihat Daftar Buku
def view_books():
    if not library:
        print("\n📌 Perpustakaan masih kosong!\n")
        return
    print("\nDaftar Buku di Perpustakaan:\n")
    for book in library:
        print(f"ID: {book['ID']}, Judul: {book['Judul']}, Penulis: {book['Penulis']}, Tahun: {book['Tahun Terbit']}, Ditambahkan: {book['Tanggal Ditambahkan']}")
    print("\n")
Mengecek apakah perpustakaan kosong.
Jika tidak kosong, mencetak daftar buku yang telah disimpan.

Menu Utama
def main():
    while True:
        print("\n===== Sistem Manajemen Perpustakaan =====")
        print("1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Keluar")
        choice = input("Pilih menu (1-3): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            print("\n👋 Terima kasih telah menggunakan sistem!\n")
            break
        else:
            print("⚠️ Pilihan tidak valid, coba lagi!\n")

Menampilkan menu utama dan menangani input pengguna.
Memanggil fungsi add_book() dan view_books() sesuai pilihan.
Keluar dari program jika pengguna memilih opsi 3.

Menjalankan Program

if __name__ == "__main__":
    main()

Memastikan bahwa program hanya berjalan jika dieksekusi langsung, bukan diimpor sebagai modul.
Struktur Data

Data buku disimpan dalam bentuk list dengan elemen berbentuk dictionary yang berisi:

Catatan
Data buku tidak akan tersimpan secara permanen karena menggunakan struktur data list yang akan hilang setelah program ditutup.
Untuk penyimpanan data permanen, dapat dikembangkan lebih lanjut menggunakan database seperti SQLite atau MySQL.

Lisensi
Program ini bebas digunakan dan dimodifikasi sesuai kebutuhan.
