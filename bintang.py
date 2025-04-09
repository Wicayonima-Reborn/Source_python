baris = int(input('masukin jumlah baris: '))
for j in range(1, baris + 1):
    print('* ' * j)

for i in range(baris + 1, 0, -1): 
    for j in range(0, i -1):
        print('* ', end='')
    print('')
#
#baris = int(input('masukin jumlah baris: '))
#i = int(input('masukin jumlah i: '))
#
#while i <= baris:
#    j = i 
#    while j < baris:
#        print('', end='')
#        j += 1
#    while k <= i        
#    k = 1

baris = int(input('Masukin Jumlah Baris: '))
k = 2 * baris - 2
for i in range(0, baris):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="" )
    print("")

while i >= 1:
    j = baris
    while j > i:
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1

#
#rows = 5
#k = 2 * rows - 2
#for i in range(0, rows):
#    for j in range(0, k):
#        print(end=" ")
#    k = k - 2
#    for j in range(0, i + 1):
#        print("* ", end="")
#    print("")
#


