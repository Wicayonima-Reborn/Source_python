import csv  # Import modul CSV agar bisa menyimpan & membaca data dari file

# 📌 1️⃣ Class Siswa (Blueprint untuk Setiap Siswa)
class Siswa:
    def __init__(self, nama, usia, nilai):
        # Menyimpan data siswa sebagai atribut dalam objek Siswa
        self.nama = nama
        self.usia = usia
        self.nilai = nilai

    def to_dict(self):
        # Mengubah data siswa menjadi format dictionary agar bisa disimpan ke CSV
        return {"Nama": self.nama, "Usia": self.usia, "Nilai": self.nilai}


# 📌 2️⃣ Class ManajemenSiswa (Mengelola Data Siswa)
class ManajemenSiswa:
    def __init__(self, filename="data_siswa.csv"):
        # Menentukan nama file tempat menyimpan data siswa
        self.filename = filename
        # Memuat data siswa dari file CSV (jika ada)
        self.siswa_list = self.load_data()

    # 📌 3️⃣ Simpan Data ke CSV
    def save_data(self):
        # Membuka file CSV dalam mode tulis ("w") dan mengatur newline agar format rapi
        with open(self.filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Nama", "Usia", "Nilai"])
            writer.writeheader()  # Menulis header kolom di file CSV
            for siswa in self.siswa_list:
                writer.writerow(siswa.to_dict())  # Menulis data siswa ke file CSV 
    

    # 📌 4️⃣ Baca Data dari CSV
    def load_data(self):
        try:
            # Membuka file CSV dalam mode baca ("r")
            with open(self.filename, mode="r") as file:
                reader = csv.DictReader(file)
                # Mengembalikan daftar objek Siswa berdasarkan isi file CSV
                return [Siswa(row["Nama"], row["Usia"], row["Nilai"]) for row in reader]
                #Membuat list berisi objek siswa dari setiap baris csv
        except FileNotFoundError:
            # Jika file tidak ditemukan, kembalikan daftar kosong
            return []
            # dikembalikan ke list kosong

    # 📌 5️⃣ Menambah Siswa
    def tambah_siswa(self):
        nama = input("Masukkan Nama Siswa: ")
        usia = int(input("Masukkan Usia Siswa: "))
        nilai = float(input("Masukkan Nilai Rata-rata: "))
        siswa = Siswa(nama, usia, nilai)  # Membuat objek siswa
        self.siswa_list.append(siswa)  # Menambah ke daftar siswa
        self.save_data()  # Simpan ke file CSV
        print("✅ Siswa berhasil ditambahkan!\n")

    # 📌 6️⃣ Menampilkan Daftar Siswa
    def lihat_siswa(self):
        if not self.siswa_list:
            print("🚫 Belum ada data siswa.\n")
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
                # memastikan index sama atau lebih dari 0 dan tidak lebih dari self.siswa_list
                #len menghitung jumlah elemen pada objek
                    # Meminta input baru untuk mengganti data siswa yang dipilih
                    self.siswa_list[index].nama = input("Masukkan Nama Baru: ")
                    self.siswa_list[index].usia = int(input("Masukkan Usia Baru: "))
                    self.siswa_list[index].nilai = float(input("Masukkan Nilai Baru: "))
                    self.save_data()  # Simpan perubahan ke CSV
                    print("✅ Data siswa berhasil diperbarui!\n")
                else:
                    print("🚫 Nomor tidak valid!\n")
            except ValueError:
                print("🚫 Masukkan angka yang benar!\n")

    # 📌 8️⃣ Menghapus Siswa
    def hapus_siswa(self):
        self.lihat_siswa()
        if self.siswa_list:
            try:
                index = int(input("Pilih nomor siswa yang ingin dihapus: ")) - 1
                if 0 <= index < len(self.siswa_list):
                    del self.siswa_list[index]  # Hapus siswa dari daftar
                    self.save_data()  # Simpan perubahan ke CSV
                    print("✅ Siswa berhasil dihapus!\n")
                else:
                    print("🚫 Nomor tidak valid!\n")
            except ValueError:
                print("🚫 Masukkan angka yang benar!\n")

    # 📌 9️⃣ Mencari Siswa
    def cari_siswa(self):
        nama_cari = input("Masukkan nama siswa yang dicari: ").lower()
        hasil = [siswa for siswa in self.siswa_list if siswa.nama.lower() == nama_cari]
        if hasil:
            print("\n=== 🔍 Hasil Pencarian ===")
            for siswa in hasil:
                print(f"Nama: {siswa.nama}, Usia: {siswa.usia}, Nilai: {siswa.nilai}\n")
        else:
            print("🚫 Siswa tidak ditemukan.\n")

    # 📌 🔟 Menampilkan Menu
    def tampilkan_menu(self):
        while True:
            # Menampilkan opsi menu kepada pengguna
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
                print('Made BY Kelompok 1 and support by kelas terbuka chat gpt and w3shcool ')
                break  # Keluar dari loop
            else:
                print("🚫 Pilihan tidak valid, coba lagi!\n")

# 📌 🔟 Menjalankan Program
app = ManajemenSiswa()
app.tampilkan_menu()