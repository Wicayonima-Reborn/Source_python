# berkas: perulanganWhile.py

jawab = 'ya'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break

print(f"Total perulagan: {hitung}")