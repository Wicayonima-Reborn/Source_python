import csv  # Untuk membaca dan menulis file CSV (Comma-Separated Values), seperti saat menyimpan dan memuat data siswa.
import re   # Untuk bekerja dengan ekspresi reguler (regex), digunakan dalam validasi input (misalnya, nama siswa).
import os   # Untuk berinteraksi dengan sistem operasi, misalnya untuk membersihkan layar terminal menggunakan os.system('cls').


# 🎨 Kode warna ANSI Escape
"""mendefinisikan kode warna"""
RED = "\033[91m"     # Warna merah untuk menampilkan pesan kesalahan atau peringatan.
GREEN = "\033[92m"   # Warna hijau untuk menampilkan pesan yang berhasil (sukses).
YELLOW = "\033[93m"  # Warna kuning untuk memberikan perhatian atau informasi.
BLUE = "\033[94m"    # Warna biru untuk judul atau informasi penting.
CYAN = "\033[96m"    # Warna cyan untuk menonjolkan informasi atau teks.
RESET = "\033[0m"    # Reset warna ke warna default terminal setelah penggunaan warna.  

# 📌 Class Siswa
class Siswa:
    def __init__(self, nama, usia, nilai):
        """
        Menginisialisasi objek Siswa dengan atribut nama, usia, dan nilai.

        Parameters:
        nama (str): Nama siswa.
        usia (int): Usia siswa.
        nilai (float): Nilai siswa.
        """
        self.nama = nama       # Menyimpan nama siswa
        self.usia = usia       # Menyimpan usia siswa
        self.nilai = nilai     # Menyimpan nilai siswa

    def to_dict(self):
        """
        Mengembalikan atribut objek dalam bentuk dictionary.

        Returns:
        dict: Dictionary berisi nama, usia, dan nilai siswa.
        """
        return {
            'Nama': self.nama,
            'Usia': self.usia,
            'Nilai': self.nilai
        }


# 📌 Class ManajemenSiswa
class ManajemenSiswa:
    def __init__(self, filename='data_siswa.csv'):
        """
        Menginisialisasi objek ManajemenSiswa dengan atribut filename dan siswa_list.
        
        Parameters:
        filename (str): Nama file untuk menyimpan dan memuat data siswa (default 'data_siswa.csv').
        """
        self.filename = filename  # Menyimpan nama file
        self.siswa_list = self.load_data()  # Memuat data siswa dari file


    # 📌 Simpan Data ke CSV
    def save_data(self):
        """
        Menyimpan data siswa ke file CSV.

        Data siswa disimpan dalam format CSV dengan field 'Nama', 'Usia', dan 'Nilai'.
        """
        with open(self.filename, mode='w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['Nama', 'Usia', 'Nilai'])
            writer.writeheader()  # Menulis header CSV (Nama, Usia, Nilai)
            for siswa in self.siswa_list:
                writer.writerow(siswa.to_dict())  # Menyimpan data setiap siswa ke file CSV


    # 📌 Load Data dari CSV
    def load_data(self):
        """
        Memuat data siswa dari file CSV.

        Method ini mencoba membuka file CSV dan membaca data siswa.
        Jika file tidak ditemukan, mengembalikan list kosong.
    
        Returns:
        list: Daftar objek Siswa yang dimuat dari file CSV.
        """
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                # Membaca setiap baris dan mengonversinya menjadi objek Siswa
                return [Siswa(row['Nama'], int(row['Usia']), float(row['Nilai'])) for row in reader]
        except FileNotFoundError:
            return []  # Jika file tidak ditemukan, kembalikan list kosong


    # 📌 Validasi Input
    def validasi_nama(self):
        """
        Memvalidasi input nama siswa.

        Fungsi ini meminta pengguna untuk memasukkan nama siswa dan memeriksa apakah 
        nama tersebut memenuhi syarat: minimal 4 huruf dan hanya berisi huruf dan spasi.
    
        Returns:
        str: Nama siswa yang valid.
        """
        while True:
            try:
                nama = input('Masukkan Nama Siswa: ').strip()
                # Menyaring input agar hanya menerima huruf dan spasi dengan panjang minimal 4 karakter
                if re.match(r"^[A-Za-z ]{4,}$", nama):
                    return nama  # Mengembalikan nama yang valid
                print(RED + '🚫 Nama minimal harus 4 huruf dan hanya boleh berisi huruf dan spasi!\n' + RESET)
            except ValueError:
                print(RED + '🚫 Masukkan huruf yang valid!' + RESET)


    def validasi_usia(self):
        """
        Memvalidasi input usia siswa.

        Fungsi ini meminta pengguna untuk memasukkan usia siswa dan memeriksa apakah 
        usia tersebut berada dalam rentang yang valid, yaitu antara 6 hingga 19 tahun.
    
        Returns:
        int: Usia siswa yang valid.
        """
        while True:
            try:
                usia = int(input("Masukkan Usia Siswa: "))  # Mengambil input usia dan mengonversinya ke integer
                if 6 <= usia <= 19:  # Memeriksa apakah usia dalam rentang yang valid
                    return usia  # Mengembalikan usia yang valid
                print(RED + '🚫 Usia harus antara 6-19 tahun!' + RESET)
            except ValueError:
                print(RED + "🚫 Masukkan angka yang valid!" + RESET)  # Menangani jika input bukan angka


    def validasi_nilai(self):
        """
        Memvalidasi input nilai rata-rata siswa.

        Fungsi ini meminta pengguna untuk memasukkan nilai rata-rata siswa dan memeriksa 
        apakah nilai tersebut berada dalam rentang yang valid, yaitu antara 0 hingga 100.
        
        Returns:
        float: Nilai rata-rata siswa yang valid.
        """
        while True:
            try:
                nilai = float(input("Masukkan Nilai Rata-rata: "))  # Mengambil input nilai dan mengonversinya ke float
                if nilai < 0:
                    print(RED + "🚫 Nilai tidak boleh negatif!" + RESET)
                elif nilai > 100:
                    print(RED + "🚫 Nilai tidak boleh lebih dari 100!" + RESET)  # Memeriksa apakah nilai dalam rentang yang valid
                else:    
                    return nilai  # Mengembalikan nilai yang valid
            except ValueError:
                print(RED + "🚫 Masukkan angka yang valid!" + RESET)  # Menangani jika input bukan angka


    # 📌 Tambah Siswa
    def tambah_siswa(self):
        """
        Menambahkan siswa baru ke dalam daftar siswa.

        Fungsi ini meminta input nama, usia, dan nilai siswa dari pengguna, kemudian
        membuat objek Siswa dan menambahkannya ke dalam list `siswa_list`.
        Setelah itu, data siswa disimpan ke dalam file CSV.

        Returns:
        None
        """
        # Memvalidasi dan mengambil input untuk nama, usia, dan nilai siswa
        nama = self.validasi_nama()
        usia = self.validasi_usia()
        nilai = self.validasi_nilai()

        # Membuat objek Siswa dengan data yang sudah di input
        siswa = Siswa(nama, usia, nilai)
        
        # Menambahkan objek Siswa ke dalam list siswa_list
        self.siswa_list.append(siswa)
        
        # Menyimpan data siswa yang baru ditambahkan ke dalam file CSV
        self.save_data()
        
        # Memberikan pesan bahwa siswa berhasil ditambahkan
        print(GREEN + '✅ Siswa berhasil ditambahkan!\n' + RESET)


    # 📌 Lihat Daftar Siswa dengan Format Tabel
    def lihat_siswa(self):
        """
        Menampilkan daftar siswa dalam format tabel.

        Fungsi ini akan menampilkan daftar siswa yang telah terdaftar, lengkap dengan
        nama, usia, dan nilai rata-rata mereka. Setiap siswa akan diberi warna pada nilai
        mereka berdasarkan kriteria tertentu: hijau untuk nilai >= 80, kuning untuk nilai >= 65,
        dan merah untuk nilai < 65. Jika tidak ada data siswa, akan muncul pesan kesalahan.

        Returns:
        None
        """
        if not self.siswa_list:  # Mengecek apakah ada data siswa
            print(RED + "🚫 Belum ada data siswa.\n" + RESET)  # Menampilkan pesan jika data kosong
            return

        # Menampilkan header tabel dengan format yang rapi
        print(BLUE + "=" * 40)
        print("📋  DAFTAR SISWA".center(40))
        print("=" * 40 + RESET)
        print(f"{CYAN}{'No.':<5} {'Nama':<15} {'Usia':<5} {'Nilai':<6}{RESET}")
        print("-" * 40)

        # Menampilkan data siswa dalam format tabel
        for i, siswa in enumerate(self.siswa_list, start=1):
            # Menentukan warna berdasarkan nilai siswa
            warna_nilai = GREEN if siswa.nilai >= 80 else YELLOW if siswa.nilai >= 65 else RED
            # Mencetak data siswa dengan format yang rapi dan warna pada nilai
            print(f"{i:<5} {siswa.nama:<15} {siswa.usia:<5} {warna_nilai}{siswa.nilai:<6.2f}{RESET}")

        # Menampilkan footer tabel
        print(BLUE + "=" * 40 + RESET)


    # 📌 Edit Data Siswa
    def edit_siswa(self):
        """
        Mengedit data siswa yang sudah ada dalam daftar.

        Fungsi ini menampilkan daftar siswa dan meminta pengguna untuk memilih nomor siswa
        yang ingin diedit. Setelah itu, data siswa yang dipilih (nama, usia, nilai) akan
        diperbarui sesuai input pengguna. Jika input tidak valid, akan muncul pesan kesalahan.

        Returns:
        None
        """
        # Menampilkan daftar siswa sebelum mengedit
        self.lihat_siswa()

        # Mengecek apakah ada data siswa
        if not self.siswa_list:
            print(RED + "🚫 Belum ada data siswa.\n" + RESET)
            return

        try:
            # Meminta pengguna untuk memilih nomor siswa yang akan diedit
            index = int(input("Pilih nomor siswa yang ingin diedit: ")) - 1

            # Mengecek apakah index yang dipilih valid
            if 0 <= index < len(self.siswa_list):
                # Memperbarui data siswa dengan input baru
                self.siswa_list[index].nama = self.validasi_nama()
                self.siswa_list[index].usia = self.validasi_usia()
                self.siswa_list[index].nilai = self.validasi_nilai()

                # Menyimpan data yang sudah diperbarui
                self.save_data()

                # Memberikan pesan bahwa data berhasil diperbarui
                print(GREEN + "✅ Data siswa berhasil diperbarui!\n" + RESET)
            else:
                print(RED + "🚫 Nomor tidak valid!\n" + RESET)
        except ValueError:
            # Menangani kasus jika input bukan angka
            print(RED + "🚫 Masukkan angka yang benar!\n" + RESET)


    # 📌 Hapus Siswa
    def hapus_siswa(self):
        """
        Menghapus data siswa dari daftar berdasarkan nomor yang dipilih.

        Fungsi ini menampilkan daftar siswa dan meminta pengguna untuk memilih nomor siswa
        yang ingin dihapus. Jika nomor valid, data siswa yang dipilih akan dihapus dari
        daftar dan perubahan disimpan ke dalam file. Jika input tidak valid, akan muncul pesan kesalahan.

        Returns:
        None
        """
        # Menampilkan daftar siswa yang ada sebelum menghapus
        self.lihat_siswa()

        # Mengecek apakah ada data siswa
        if not self.siswa_list:
            print(RED + "🚫 Belum ada data siswa.\n" + RESET)
            return

        try:
            # Meminta pengguna untuk memilih nomor siswa yang ingin dihapus
            index = int(input("Pilih nomor siswa yang ingin dihapus: ")) - 1

            # Mengecek apakah nomor yang dipilih valid
            if 0 <= index < len(self.siswa_list):
                # Menghapus siswa dari daftar
                del self.siswa_list[index]
                
                # Menyimpan perubahan ke file
                self.save_data()

                # Memberikan pesan bahwa siswa berhasil dihapus
                print(GREEN + "✅ Siswa berhasil dihapus!\n" + RESET)
            else:
                print(RED + "🚫 Nomor tidak valid!\n" + RESET)
        except ValueError:
            # Menangani kesalahan jika input bukan angka
            print(RED + "🚫 Masukkan angka yang benar!\n" + RESET)


    # 📌 Cari Siswa
    def cari_siswa(self):
        """
        Mencari data siswa berdasarkan nama yang dimasukkan.

        Fungsi ini memungkinkan pengguna untuk mencari siswa berdasarkan nama. Nama yang dimasukkan
        akan dicocokkan dengan nama siswa dalam daftar, dan hasil pencarian yang sesuai akan ditampilkan.
        Jika siswa ditemukan, informasi siswa akan ditampilkan; jika tidak ditemukan, pesan kesalahan akan muncul.

        Returns:
        None
        """
        # Meminta pengguna untuk memasukkan nama siswa yang ingin dicari, diubah menjadi lowercase untuk pencocokan case-insensitive
        nama_cari = input("Masukkan nama siswa yang dicari: ").lower()

        # Mencari siswa yang nama-namanya cocok dengan input (case-insensitive)
        hasil = [siswa for siswa in self.siswa_list if siswa.nama.lower() == nama_cari]

        # Jika ada siswa yang ditemukan
        if hasil:
            print(YELLOW + '\n=== 🔍 Hasil Pencarian ===' + RESET)
            # Menampilkan informasi siswa yang ditemukan
            for siswa in hasil:
                print(f"Nama: {siswa.nama}, Usia: {siswa.usia}, Nilai: {siswa.nilai}\n")
        else:
            # Menampilkan pesan jika siswa tidak ditemukan
            print(RED + "🚫 Siswa tidak ditemukan.\n" + RESET)


    # 📌 Tampilkan Menu CRUD
    def tampilkan_menu(self):
        """
        Menampilkan menu utama dan mengarahkan pengguna ke pilihan operasi CRUD.

        Fungsi ini menyediakan antarmuka menu untuk mengelola data siswa. Pengguna dapat memilih
        berbagai operasi, seperti menambah, melihat, mengedit, menghapus, mencari data siswa,
        atau mereset tampilan terminal.

        Fungsi ini terus berulang sampai pengguna memilih opsi untuk keluar.
        """
        while True:
            # Menampilkan header menu dengan batas atas dan bawah
            print(BLUE + "=" * 40)
            print("📚✨  MENU MANAJEMEN DATA SISWA ✨📚".center(40))
            print("=" * 40 + RESET)

            # Menampilkan daftar opsi menu
            print("1️⃣  ✏️ Tambah Siswa")
            print("2️⃣  👀 Lihat Daftar Siswa")
            print("3️⃣  📝 Edit Data Siswa")
            print("4️⃣  🗿 Hapus Siswa")
            print("5️⃣  🔎 Cari Siswa")
            print('6️⃣  Program Untuk Mereset Tulisan')
            print('0️⃣  🚪 Keluar')
            print("=" * 40)

            # Meminta input dari pengguna untuk memilih menu
            pilihan = input('📝 Pilih menu (0-6): ')

            # Menjalankan fungsi terkait berdasarkan pilihan pengguna
            if pilihan == "1":
                self.tambah_siswa()  # Tambah siswa
            elif pilihan == "2":
                self.lihat_siswa()  # Lihat daftar siswa
            elif pilihan == "3":
                self.edit_siswa()  # Edit data siswa
            elif pilihan == "4":
                self.hapus_siswa()  # Hapus siswa
            elif pilihan == "5":
                self.cari_siswa()  # Cari siswa
            elif pilihan == '6':
                os.system('cls')  # Mereset terminal
            elif pilihan == "0":
                print(GREEN + "\n👋 Keluar dari program.\n" + RESET)
                print(BLUE + 'Made BY Kelompok 1 and Support BY Kelas Terbuka, ChatGPT, and W3Schools\n' + RESET)
                break  # Keluar dari loop dan program
            else:
                # Menampilkan pesan jika input tidak valid
                print(RED + "Masukkan Angka Yang Benar!!!" + RESET)
                    
# 📌  Menjalankan Program
app = ManajemenSiswa()  # Membuat objek dari class ManajemenSiswa
app.tampilkan_menu()  # Menjalankan method tampilkan_menu() untuk menampilkan menu kepada pengguna