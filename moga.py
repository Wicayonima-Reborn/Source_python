angka = int(input('masukan nilai: '))

if angka % 3 == 0 and angka %5 == 0:
    print('fizzbuzz')
elif angka % 3 == 0:
    print('Fizz')
elif angka % 5 == 0:
    print('Buzz')
else:
    print('Awikwok')
    
