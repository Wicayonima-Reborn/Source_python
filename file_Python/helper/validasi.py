import re

def validasi_nama(nama):
    if re.match(r"^[A-Za-z]+$", nama.strip()):
        return nama.strip()
    raise ValueError("Nama tidak valid")

def validasi_usia(usia):
    usia = int(usia)
    if 6 <= usia <= 19:
        return usia
    raise ValueError("Usia harus antara 6-19 tahun")

def validasi_nilai(nilai):
    nilai = float(nilai)
    if 0 <= nilai <= 100:
        return nilai
    raise ValueError("Nilai harus antara 0-100")