nama = input("Masukkan nama Anda: ")
jenis_kelamin = input("Masukkan jenis kelamin (Pria/Wanita): ")
tinggi_badan = float(input("Masukkan tinggi badan Anda (cm): "))

if jenis_kelamin == "pria":
    berat_ideal = tinggi_badan - 100
elif jenis_kelamin == "wanita":
    berat_ideal = tinggi_badan - 110
else:
    berat_ideal = None

if berat_ideal is not None:
    print(f"Nama: {nama}")
    print(f"Jenis Kelamin: {jenis_kelamin}")
    print(f"Tinggi Badan: {tinggi_badan} cm")
    print(f"Berat Badan Ideal: {berat_ideal} kg")
else:
    print("Jenis kelamin tidak valid.")