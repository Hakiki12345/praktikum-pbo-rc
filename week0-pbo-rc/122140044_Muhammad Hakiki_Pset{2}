class GradeParser:
    def __init__(self):
        self.grade = {}

    def tambah_nilai(self, nama, nilai):
        self.grade[nama] = nilai

    def masukkan_data(self, jumlah_data):
        for i in range(jumlah_data):
            nama = input(f'Masukkan nama (keys) ke-{i+1}: ')
            nilai = int(input(f'Masukkan nilai (values) {nama}: '))
            print('')
            self.tambah_nilai(nama, nilai)

    def tampilkan_grade(self):
        print('grade =', self.grade)

# Logika main untuk mengakses kelas dan membuat objek GradeParser
if __name__ == "__main__":
    parser = GradeParser()
    jumlah_data = int(input('Masukkan jumlah pasangan keys-values yang  anda inginkan: '))
    parser.masukkan_data(jumlah_data)
    parser.tampilkan_grade()
