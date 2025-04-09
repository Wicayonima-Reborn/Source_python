#total_belanja = (input("Masukkan Total Belanja Mu : "))
#setelah_diskon = total_belanja
#
#if total_belanja < 100000:
#    diskon = total_belanja * 10/100
#else:
#    diskon = total_belanja * 1/1
#
#setelah_diskon = total_belanja - diskon
#
#print (f'hasilnya adalah {setelah_diskon}')
#total = int(input("Masukkan harga barang: "))
#setelah_diskon = total
#
## Diskon 10% untuk harga kurang dari 100.000, diskon 20% untuk harga lebih dari atau sama dengan 100.000
#if total < 100000:
#    diskon = total * (10 / 100)  # Diskon 10%
#else:
#    diskon = total * (20 / 100)  # Diskon 20%
#
## Menghitung harga setelah diskon
#setelah_diskon = total - diskon
#
## Menampilkan hasil
#print('Diskonnya yaitu: {}'.format(round(diskon, 2)))  # Menampilkan diskon dengan dua angka desimal
#print('Harga setelah diskon: {}'.format(round(setelah_diskon, 2)))  # Menampilkan harga setelah diskon

total_belanja = float(input("Masukkan total belanja : "))

# Menghitung diskon
if total_belanja <= 50000:
    diskon = 0
elif total_belanja <= 100000:
    diskon = 0.1
elif total_belanja <= 200000:
    diskon = 0.15
elif total_belanja <= 500000: 
    diskon = 0.3
else:
    diskon = 0.4

# Menampilkan hasil
besar_diskon = total_belanja * diskon
total_pembayaran = total_belanja - besar_diskon
print(f"Total belanja awal: {total_belanja}")
print(f"Diskon ({diskon * 100}%): {besar_diskon}")
print(f"Total pembayaran setelah diskon: {total_pembayaran}")

