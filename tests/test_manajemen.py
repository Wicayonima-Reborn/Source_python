import unittest
from file_Python.Manajement_data_revisi_akhir import ManajemenSiswa, Siswa

class TestManajemenSiswa(unittest.TestCase):

    def setUp(self):
        self.ms = ManajemenSiswa("test_data.csv")
        self.ms.siswa_list = [
            Siswa("Ani", 15, 85.5),
            Siswa("Budi", 16, 70.0),
            Siswa("Cici", 14, 60.0)
        ]

    def test_init(self):
        self.assertIsInstance(self.ms.siswa_list, list)

    def test_save_and_load_data(self):
        self.ms.save_data()
        ms_baru = ManajemenSiswa("test_data.csv")
        self.assertEqual(len(ms_baru.siswa_list), 3)

    def test_validasi_nama(self):
        with self.assertRaises(ValueError):
            from file_Python.helper.validasi import validasi_nama
            validasi_nama("1234")

    def test_validasi_usia(self):
        from file_Python.helper.validasi import validasi_usia
        self.assertEqual(validasi_usia(10), 10)
        with self.assertRaises(ValueError):
            validasi_usia(20)

    def test_validasi_nilai(self):
        from file_Python.helper.validasi import validasi_nilai
        self.assertEqual(validasi_nilai(90.0), 90.0)
        with self.assertRaises(ValueError):
            validasi_nilai(200)

    def test_tambah_siswa_manual(self):
        jumlah_awal = len(self.ms.siswa_list)
        self.ms.siswa_list.append(Siswa("Dina", 13, 77.0))
        self.assertEqual(len(self.ms.siswa_list), jumlah_awal + 1)

    def test_edit_siswa_manual(self):
        self.ms.siswa_list[0].nama = "Anita"
        self.assertEqual(self.ms.siswa_list[0].nama, "Anita")

    def test_hapus_siswa_manual(self):
        jumlah_awal = len(self.ms.siswa_list)
        del self.ms.siswa_list[1]
        self.assertEqual(len(self.ms.siswa_list), jumlah_awal - 1)

    def test_cari_siswa(self):
        hasil = [siswa for siswa in self.ms.siswa_list if siswa.nama.lower() == "budi"]
        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0].nama, "Budi")

if __name__ == '__main__':
    unittest.main()