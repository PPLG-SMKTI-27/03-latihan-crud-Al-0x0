# data buku
books = [
    {"isbn": "9786237121144", "judul": "Kumpulan Solusi Pemrograman Python", "pengarang": "Budi Raharjo", "jumlah": 6, "terpinjam": 0},
    {"isbn": "9786231800718", "judul": "Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang": "Okta Purnawirawan", "jumlah": 15, "terpinjam": 0},
    {"isbn": "9786026163905", "judul": "Analisis dan Perancangan Sistem Informasi", "pengarang": "Adi Sulistyo Nugroho", "jumlah": 2, "terpinjam": 1},
    {"isbn": "9786022912828", "judul": "Animal Farm", "pengarang": "George Orwell", "jumlah": 4, "terpinjam": 0}
]

# data peminjam 
data_peminjaman = [
    {"isbn": "9786022912828", "status": "Selesai", "tanggal_pinjam": "2025-03-21", "tanggal_kembali": "2025-03-28"},
    {"isbn": "9786026163905", "status": "Belum", "tanggal_pinjam": "2025-07-22", "tanggal_kembali": ""}
]

def tampilkan_data():
    print("Daftar Buku: ") 
    for buku in books:
        print(f"ISBN: {buku['isbn']}, Judul: {buku['judul']}, Pengarang: {buku['pengarang']}, Jumlah: {buku['jumlah']}, Terpinjam: {buku['terpinjam']}")

def tambah_data():
    isbn = input("ISBN: ")
    judul = input("Judul: ")
    pengarang = input("Pengarang: ")
    jumlah = int(input("Jumlah: "))
    buku_baru = {"isbn": isbn, "judul": judul, "pengarang": pengarang, "jumlah": jumlah, "terpinjam": 0}
    books.append(buku_baru)
    print("Data buku ditambahkan.")

def edit_data():
    isbn = input("ISBN buku yang diedit: ")
    for buku in books:
        if buku["isbn"] == isbn:
            buku["judul"] = input("Judul baru: ")
            buku["pengarang"] = input("Pengarang baru: ")
            buku["jumlah"] = int(input("Jumlah baru: "))
            print("Data buku diperbarui.")
            return
    print("Buku tidak ditemukan.")

def hapus_data():
    isbn = input("ISBN buku yang dihapus: ")
    for buku in books:
        if buku["isbn"] == isbn:
            books.remove(buku)
            print("Buku dihapus.")
            return
    print("Buku tidak ditemukan.")

def tampilkan_peminjaman():
    print("Semua Peminjaman:")
    for peminjaman in data_peminjaman:
        print(peminjaman)

def tampilkan_belum():
    print("Peminjaman Belum Kembali:")
    for peminjaman in data_peminjaman:
        if peminjaman["status"] == "Belum":
            print(peminjaman)

def peminjaman():
    isbn = input("ISBN yang dipinjam: ")
    for buku in books:
        if buku["isbn"] == isbn:
            if buku["terpinjam"] < buku["jumlah"]:
                tanggal = input("Tanggal pinjam (YYYY-MM-DD): ")
                peminjaman_baru = {"isbn": isbn, "status": "Belum", "tanggal_pinjam": tanggal, "tanggal_kembali": ""}
                data_peminjaman.append(peminjaman_baru)
                buku["terpinjam"] += 1
                print("Berhasil meminjam.")
            else:
                print("Tidak tersedia (habis).")
            return
    print("Buku tidak ditemukan.")

def pengembalian():
    isbn = input("ISBN yang dikembalikan: ")
    for peminjaman in data_peminjaman:
        if peminjaman["isbn"] == isbn and peminjaman["status"] == "Belum":
            tanggal = input("Tanggal kembali (YYYY-MM-DD): ")
            peminjaman["status"] = "Selesai"
            peminjaman["tanggal_kembali"] = tanggal
            for buku in books:
                if buku["isbn"] == isbn:
                    buku["terpinjam"] -= 1
            print("Pengembalian dicatat.")
            return
    print("Data peminjaman belum ditemukan atau sudah selesai.")

while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")
    pilihan = input("Masukkan pilihan menu (1-8 atau x): ").strip().lower()
    if pilihan == "1":
        tampilkan_data()
    elif pilihan == "2":
        tambah_data()
    elif pilihan == "3":
        edit_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        tampilkan_peminjaman()
    elif pilihan == "6":
        tampilkan_belum()
    elif pilihan == "7":
        peminjaman()
    elif pilihan == "8":
        pengembalian()
    elif pilihan == "x":
        print("Keluar program.")
        break
    else:
        print("Pilihan tidak valid.")
