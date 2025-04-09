import csv

class mobil:
    def __init__(self, nama, warna, Muatan):
        self.nama = nama
        self.warna = warna
        self.Muatan = Muatan

    def jalan(self):
        print(f"Nama Mobil Adalah {self.nama} dan warnanya adalah {self.warna}!! dan Muatan mobil tersebut sebanyak {self.Muatan} orang")

    def muatan(self):
        if self.Muatan <= 4:
            print(f'{self.nama} muatannya telah penuh')
        else:
            print(f"{self.nama} muatannya belum penuh")


mobil_1 = mobil("Toyota", "Putih", 2)
mobil_2 = mobil('Mitsubishi', 'army', 5)
mobil_3 = mobil('Xpander', 'abu', 5)

mobil_1.jalan()
mobil_2.jalan()
mobil_3.jalan()
mobil_1.muatan()
mobil_2.muatan()
mobil_3.muatan()
