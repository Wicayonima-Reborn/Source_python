bilangan = int(input('masukin bilangan: '))

#tampilkan tabel perkalian
print('Tabel Perkalian for bilangan ', bilangan)
for i in range(1, 101): 
    hasil = bilangan * i
    print(f'{bilangan} x {i} {hasil}') 
