import csv  # Import modul CSV agar bisa menyimpan & membaca data dari file CSV

# 📌 1️⃣ Class Siswa (Blueprint untuk Setiap Siswa)
class Siswa:
    def __init__(self, nama, usia, nilai): # __init__ untuk
        self.nama = nama
        self.usia = usia
        self.nilai = nilai

    def to_dict(self):
        return {"Nama": self.nama, "Usia": self.usia, "Nilai": self.nilai}

# 📌 2️⃣ Class ManajemenSiswa (Mengelola Data Siswa)
class ManajemenSiswa:
    def __init__(self, filename="data_siswa.csv"):
        self.filename = filename
        self.siswa_list = self.load_data()

    # 📌 3️⃣ Simpan Data ke CSV
    def save_data(self):
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Nama", "Usia", "Nilai"])
            writer.writeheader()
            for siswa in self.siswa_list:
                writer.writerow(siswa.to_dict())

    # 📌 4️⃣ Baca Data dari CSV
    def load_data(self):
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                return [Siswa(row["Nama"], row["Usia"], row["Nilai"]) for row in reader]
        except FileNotFoundError:
            return []

    # 📌 5️⃣ Menambah Siswa
    def tambah_siswa(self):
        nama = input("Masukkan Nama Siswa: ")
        usia = input("Masukkan Usia Siswa: ")
        nilai = input("Masukkan Nilai Rata-rata: ")
        siswa = Siswa(nama, usia, nilai)
        self.siswa_list.append(siswa)
        self.save_data()
        print("✅ Siswa berhasil ditambahkan!")

    # 📌 6️⃣ Menampilkan Daftar Siswa
    def lihat_siswa(self):
        if not self.siswa_list:
            print("🚫 Belum ada data siswa.")
        else:
            print("\n=== 📜 Daftar Siswa ===")
            for i, siswa in enumerate(self.siswa_list):
                print(f"{i+1}. Nama: {siswa.nama}, Usia: {siswa.usia}, Nilai: {siswa.nilai}")

    # 📌 7️⃣ Mengedit Data Siswa
    def edit_siswa(self):
        self.lihat_siswa()
        if self.siswa_list:
            try:
                index = int(input("Pilih nomor siswa yang ingin diedit: ")) - 1
                if 0 <= index < len(self.siswa_list):
                    self.siswa_list[index].nama = input("Masukkan Nama Baru: ")
                    self.siswa_list[index].usia = input("Masukkan Usia Baru: ")
                    self.siswa_list[index].nilai = input("Masukkan Nilai Baru: ")
                    self.save_data()
                    print("✅ Data siswa berhasil diperbarui!")
                else:
                    print("🚫 Nomor tidak valid!")
            except ValueError:
                print("🚫 Masukkan angka yang benar!")

    # 📌 8️⃣ Menghapus Siswa
    def hapus_siswa(self):
        self.lihat_siswa()
        if self.siswa_list:
            try:
                index = int(input("Pilih nomor siswa yang ingin dihapus: ")) - 1
                if 0 <= index < len(self.siswa_list):
                    del self.siswa_list[index]
                    self.save_data()
                    print("✅ Siswa berhasil dihapus!")
                else:
                    print("🚫 Nomor tidak valid!")
            except ValueError:
                print("🚫 Masukkan angka yang benar!")

    # 📌 9️⃣ Mencari Siswa
    def cari_siswa(self):
        nama_cari = input("Masukkan nama siswa yang dicari: ").lower()
        hasil = [siswa for siswa in self.siswa_list if siswa.nama.lower() == nama_cari]
        if hasil:
            print("\n=== 🔍 Hasil Pencarian ===")
            for siswa in hasil:
                print(f"Nama: {siswa.nama}, Usia: {siswa.usia}, Nilai: {siswa.nilai}")
        else:
            print("🚫 Siswa tidak ditemukan.")

    # 📌 🔟 Menampilkan Menu
    def tampilkan_menu(self):
        while True:
            print("\n=== 🎓 Menu Manajemen Data Siswa ===")
            print("1. Tambah Siswa")
            print("2. Lihat Daftar Siswa")
            print("3. Edit Data Siswa")
            print("4. Hapus Siswa")
            print("5. Cari Siswa")
            print("6. Keluar")

            pilihan = input("Pilih menu (1-6): ")
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
                print("👋 Keluar dari program.")
                break
            else:
                print("🚫 Pilihan tidak valid, coba lagi!")

# 📌 🔟 Menjalankan Program
app = ManajemenSiswa()
app.tampilkan_menu()