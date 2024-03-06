class PiramidaGenerator:
    def __init__(self):
        self.tinggi = 0

    def atur_tinggi(self, tinggi):
        self.tinggi = tinggi

    def buat_piramida(self):
        for i in range(1, self.tinggi+1):
            print((self.tinggi - i) * ' ' + (2 * i - 1) * '*')

# Logika main untuk mengakses kelas dan membuat objek PiramidaGenerator
if __name__ == "__main__":
    generator = PiramidaGenerator()
    tinggi_piramida = int(input('Ketik tinggi piramida yang Anda inginkan: '))
    generator.atur_tinggi(tinggi_piramida)
    generator.buat_piramida()
