nama = input('masukin namamu : ')
kelamin = input('masukin kelamin mu L/P : ')
tinggi = float(input('masukin tinggi badanmu : '))
Berat = input('masukin Berat badan mu : ')

if kelamin == 'L':
    BBI = tinggi - 100
elif kelamin == 'P':
    BBI = tinggi - 110
else:
    BBI = None

if BBI is not None:
    print(f'Namamu: {nama}')
    print(f'kelaminmu: {kelamin}')
    print(f'tinggimu: {tinggi}cm')
    print(f'beratmu: {Berat}kg')
    print(f'BBImu: {BBI}kg')
else:
    print('masukkan kelamin yang benar')