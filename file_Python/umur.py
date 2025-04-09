def latihan_1(): # Cek angka positif, negatif, dan nol
    angka = int(input('\nMasukkan angka : '))
    if angka > 0:
        print(f'[{angka} bernilai positif]')
    elif angka < 0:
        print(f'[{angka} bernilai negatif]')
    else:
        print(f'[{angka} bernilai nol]')

def latihan_2(): # Cek angka genap dan ganjil
    angka = int(input('\nMasukkan angka : '))
    if angka % 2 == 0:
        print(f'[{angka} bernilai genap]')
    else:
        print(f'[{angka} bernilai ganjil]')
        
def latihan_3(): # Cek kategori usia
    usia = int(input('\nMasukkan usia : '))
    if usia < 13:
        print('[Anda adalah seorang anak-anak]')
    elif 13 <= usia < 18:
        print('[Anda adalah seorang remaja]')
    elif 18 <= usia < 60:
        print('[Anda adalah seorang dewasa]')
    else:
        print('[Anda adalah seorang lansia]')

def latihan_4(): # Cek password
    password_benar = 'admin123'
    password = input('\nSilahkan isi password : ')
    if password == password_benar:
        print('[Akses diterima]')
    else:
        print('[Akses ditolak]')

def latihan_5(): # FizzBuzz
    angka = int(input('\nMasukkan angka : '))
    if angka % 3 == 0 and angka % 5 != 0:  
        print('[Fizz]') 
    elif angka % 5 == 0 and angka % 3 != 0: 
        print('[Buzz]') 
    elif angka % 3 == 0 and angka % 5 == 0: 
        print('[FizzBuzz]') 
    else:                                   
        print(angka)

def ulang():
    while True:
        ulang = input('\nUlang program? (y/n) : ').strip().lower()
        if ulang == 'y':
            return True
        elif ulang == 'n':
            return False
        else:
            print('[Input salah]')

def pilihan():
    while True:
        print('''
========================
1. Angka positif/negatif
2. Angka genap/ganjil
3. Kategori usia
4. Password (admin123)
5. FizzBuzz
========================''')

        try:
            pilihan = int(input('Pilihan : '))
            latihan = {
                1: latihan_1,
                2: latihan_2,
                3: latihan_3,
                4: latihan_4,
                5: latihan_5,
            }

            if pilihan in latihan:
                while True:
                    latihan[pilihan]() 
                    if not ulang():    
                        return
            else:
                print('[Pilihan tidak valid]')
        except ValueError:
            print("[Input harus berupa angka]")

pilihan()