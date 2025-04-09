
print('Kalkulator Sederhana\t')

angka_1 = float(input("Masukin Angka Pertama : "))
operator =(input('Masukin Operator (+,-,x,/) : '))
angka_2 = float(input("Masukin Angka Kedua : "))

if operator == '+':
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah --> {hasil}")

elif operator == '-':
    hasil = angka_1 - angka_2
    print(f'hasilnya adalah --> {hasil}')

elif operator == 'x' or operator == "*":
    hasil = angka_1 * angka_2
    print(f'hasilnya adalah --> {hasil}')

elif operator == '/':
    hasil = angka_1 / angka_2
    print(f'hasilnya adalah --> {hasil}')

else:
    print("Masukin Operator Yang Benar")