file = open('Me.txt', 'w')

file.write('Nama : Muhammad Hakiki')
file.write('\nNIM : 122140044')
file.write('\nResolusi saya tahun ini: menyempurnakan skil codingan saya')

file.close()

baca_file = open('Me.txt', 'r')
print(baca_file.read())
