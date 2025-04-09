listKota = [  'Dylan', 'Zaensl' ,'Nopal', 'Semarang', 'rama']
i = -1
while i < len(listKota):
  i += 1
  if i % 2 == 0 and i > 0:
    print('skip')
    continue
  print(listKota[i])