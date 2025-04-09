import csv
import re
import os
from PIL import Image

# 🎨 Kode warna ANSI Escape
RED = "\033[91m"     
GREEN = "\033[92m"   
YELLOW = "\033[93m"  
BLUE = "\033[94m"    
CYAN = "\033[96m"    
RESET = "\033[0m"    

# 📌 Class Siswa
class Siswa:
    def __init__(self, nama, usia, nilai):
        self.nama = nama
        self.usia = usia
        self.nilai = nilai

    def to_dict(self):
        return {'Nama': self.nama, 'Usia': self.usia, 'Nilai': self.nilai}

# 📌 Class ManajemenSiswa
class ManajemenSiswa:
    def __init__(self, filename='data_siswa.csv'):
        self.filename = filename
        self.siswa_list = self.load_data()

    # 📌 Simpan Data ke CSV
    def save_data(self):
        with open(self.filename, mode='w', newline="") as file:
            writer = csv.DictWriter(file, fieldnames=['Nama', 'Usia', 'Nilai'])
            writer.writeheader()
            for siswa in self.siswa_list:
                writer.writerow(siswa.to_dict())

    # 📌 Load Data dari CSV
    def load_data(self):
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                return [Siswa(row['Nama'], int(row['Usia']), float(row['Nilai'])) for row in reader]
        except FileNotFoundError:
            return []

    # 📌 Validasi Input
    def validasi_nama(self):
        while True:
            try:
                nama = input('Masukkan Nama Siswa: ').strip()
                if re.match(r"^[A-Za-z]+$", nama):
                    return nama
                print(RED + '🚫 Nama minimal harus 4 huruf dan hanya boleh berisi huruf dan spasi!\n' + RESET)
            except ValueError:
                print(RED + '🚫 Masukkan huruf yang valid!' + RESET)

    def validasi_usia(self):
        while True:
            try:
                usia = int(input("Masukkan Usia Siswa: "))
                if 6 <= usia <= 19:
                    return usia
                print(RED + '🚫 Usia harus antara 6-19 tahun!' + RESET)
            except ValueError:
                print(RED + "🚫 Masukkan angka yang valid!" + RESET)

    def validasi_nilai(self):
        while True:
            try:
                nilai = float(input("Masukkan Nilai Rata-rata: "))
                if 0 <= nilai <= 100:
                    return nilai
                print(RED + "🚫 Nilai harus di antara 0 dan 100!" + RESET)
            except ValueError:
                print(RED + "🚫 Masukkan angka yang valid!" + RESET)

    # 📌 Tambah Siswa
    def tambah_siswa(self):
        nama = self.validasi_nama()
        usia = self.validasi_usia()
        nilai = self.validasi_nilai()

        siswa = Siswa(nama, usia, nilai)
        self.siswa_list.append(siswa)
        self.save_data()
        print(GREEN + "✅ Siswa berhasil ditambahkan!\n" + RESET)

# 📌 Lihat Daftar Siswa dengan Format Tabel
    def lihat_siswa(self):
        if not self.siswa_list:
            print(RED + "🚫 Belum ada data siswa.\n" + RESET)
            return
        print(BLUE + "=" * 40)
        print("📋  DAFTAR SISWA".center(40))
        print("=" * 40 + RESET)
        print(f"{CYAN}{'No.':<5} {'Nama':<15} {'Usia':<5} {'Nilai':<6}{RESET}")
        print("-" * 40)

        for i, siswa in enumerate(self.siswa_list, start=1):
            warna_nilai = GREEN if siswa.nilai >= 80 else YELLOW if siswa.nilai >= 65 else RED
            print(f"{i:<5} {siswa.nama:<15} {siswa.usia:<5} {warna_nilai}{siswa.nilai:<6.2f}{RESET}")

        print(BLUE + "=" * 40 + RESET)

    # 📌 Edit Data Siswa
    def edit_siswa(self):
        self.lihat_siswa()
        if not self.siswa_list:
            print(RED + "🚫 Belum ada data siswa.\n" + RESET)
            return

        try:
            index = int(input("Pilih nomor siswa yang ingin diedit: ")) - 1
            if 0 <= index < len(self.siswa_list):
                self.siswa_list[index].nama = self.validasi_nama()
                self.siswa_list[index].usia = self.validasi_usia()
                self.siswa_list[index].nilai = self.validasi_nilai()
                self.save_data()
                print(GREEN + "✅ Data siswa berhasil diperbarui!\n" + RESET)
            else:
                print(RED + "🚫 Nomor tidak valid!\n" + RESET)
        except ValueError:
            print(RED + "🚫 Masukkan angka yang benar!\n" + RESET)

    # 📌 Hapus Siswa
    def hapus_siswa(self):
        self.lihat_siswa()
        if not self.siswa_list:
            print(RED + "🚫 Belum ada data siswa.\n" + RESET)
            return
        
        try:
            index = int(input("Pilih nomor siswa yang ingin dihapus: ")) - 1
            if 0 <= index < len(self.siswa_list):
                del self.siswa_list[index]
                self.save_data()
                print(GREEN + "✅ Siswa berhasil dihapus!\n" + RESET)
            else:
                print(RED + "🚫 Nomor tidak valid!\n" + RESET)
        except ValueError:
            print(RED + "🚫 Masukkan angka yang benar!\n" + RESET)

    # 📌 Cari Siswa
    def cari_siswa(self):
        nama_cari = input("Masukkan nama siswa yang dicari: ").lower()
        hasil = [siswa for siswa in self.siswa_list if siswa.nama.lower() == nama_cari]

        if hasil:
            print(YELLOW + '\n=== 🔍 Hasil Pencarian ===' + RESET)
            for siswa in hasil:
                print(f"Nama: {siswa.nama}, Usia: {siswa.usia}, Nilai: {siswa.nilai}\n")
        else:
            print(RED + "🚫 Siswa tidak ditemukan.\n" + RESET)

    # 📌 Hitung Rata-rata Nilai
    def hitung_rata_rata(self):
        if not self.siswa_list:
            print(RED + '🚫 Tidak ada data siswa untuk dihitung.\n' + RESET)
            return

        # total nilai untuk menjumlahkan nilai siswa
        # sum = perintah menjumlahkan 
        total_nilai = sum(siswa.nilai for siswa in self.siswa_list)
        rata_rata = total_nilai / len(self.siswa_list)
        print(YELLOW + f"📊 Rata-rata nilai siswa: {rata_rata:.2f}\n" + RESET)
        
    # 📌 Tampilkan Menu CRUD
    def tampilkan_menu(self):
        while True:
            print(BLUE + "=" * 40)
            print("📚✨  MENU MANAJEMEN DATA SISWA ✨📚".center(40))
            print("=" * 40 + RESET)
            print("1️⃣  ✏️ Tambah Siswa")
            print("2️⃣  👀 Lihat Daftar Siswa")
            print("3️⃣  📝 Edit Data Siswa")
            print("4️⃣  🗿 Hapus Siswa")
            print("5️⃣  🔎 Cari Siswa")
            print("6️⃣  📊 Hitung Rata-rata Nilai")
            print('7️⃣  Program Untuk Mereset Tulisan')
            print('0️⃣  🚪 Keluar')
            print("=" * 40)

            pilihan = input('📝 Pilih menu (0-7): ')
            if pilihan == "1":
                self.tambah_siswa()
            elif pilihan == "2":
                self.lihat_siswa()
            elif pilihan == "3":
                self.edit_siswa()
            elif pilihan == "4":
                self.hapus_siswa()
            elif pilihan == "5":
                self.cari_siswa()
            elif pilihan == "6":
                self.hitung_rata_rata()
            elif pilihan == '7':
                os.system('cls')
            elif pilihan == "0":
                print(GREEN + "\n👋 Keluar dari program.\n" + RESET)
                print('Made BY Kelompok 1 and Support BY Kelas Terbuka, ChatGPT, and W3Schools\n')

                try:
                    img = Image.open("images.jpg")
                    img.show()
                except FileNotFoundError:
                    print(RED + "🚫 Gambar 'images.jpg' tidak ditemukan." + RESET)
                break
            else:
                print(RED + "🚫 Pilihan tidak valid, coba lagi!\n" + RESET)

# 📌 🔟 Menjalankan Program
app = ManajemenSiswa()
app.tampilkan_menu()