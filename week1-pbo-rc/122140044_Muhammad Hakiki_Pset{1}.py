class Robot:
    def __init__(self, nama, darah, serangan):
        self.nama = nama
        self.darah = darah
        self.serangan = serangan

    def nyerang(self, musuh):
        print(f'{self.nama} melancarkan serangan "Tinju Super" ke {musuh.nama} dengan kekuatan serangan {self.serangan}.')
        musuh.darah -= self.serangan
        if musuh.darah <= 0:
            print(f'{musuh.nama} terkapar dan mengucapkan selamat pada {self.nama}.')

    def bertahan(self, musuh):
        print(f'{self.nama} berhasil menghindari serangan {musuh.nama} dengan "Dance of Defense".')
        self.darah -= musuh.serangan / 2
        if self.darah <= 0:
            print(f'{self.nama} menyerah karena terlalu lelah menari.')

    def hidup(self):
        return self.darah > 0

class Game:
    def __init__(self, robot, musuh):
        self.robot = robot
        self.musuh = musuh
        self.ronde = 0

    def play(self):
        print('Pertandingan dimulai!\n')
        while self.robot.hidup() and self.musuh.hidup():
            self.ronde += 1
            print(f"Round {self.ronde}")
            print(f'{self.robot.nama} (Darah: {self.robot.darah}, Serangan: {self.robot.serangan}) vs '
                  f'{self.musuh.nama} (Darah: {self.musuh.darah}, Serangan: {self.musuh.serangan})\n')

            print('Pilihan Robot:')
            print('1. Tinju Super      2. Dance of Defense      3. Menangis      4. Minum Air Anget      5. Teriak Keras')
            pilihan_robot = int(input(f'{self.robot.nama}, memilih aksi: '))

            print('\nPilihan Musuh:')
            print('1. Tinju Super      2. Dance of Defense      3. Menangis      4. Minum Air Anget      5. Teriak Keras')
            pilihan_musuh = int(input(f'{self.musuh.nama}, memilih aksi: '))

            print('')

            if pilihan_robot == 3 and pilihan_musuh == 3:
                print(f'Pertandingan seri, {self.robot.nama} dan {self.musuh.nama} saling menangis dan memeluk.')
                break

            if pilihan_robot == 2 and pilihan_musuh == 2:
                print('Keduanya menggunakan "Dance of Defense". Tidak ada yang terluka.')
            else:
                if pilihan_robot == 1:
                    self.robot.nyerang(self.musuh)
                elif pilihan_robot == 2:
                    self.robot.bertahan(self.musuh)
                elif pilihan_robot == 3:
                    print(f'{self.robot.nama} menangis karena kalah dan membuat {self.musuh.nama} bingung.')
                    break
                elif pilihan_robot == 4:
                    self.robot.darah += (15 / 100) * self.robot.darah
                    print(f'{self.robot.nama} meminum air anget dan merasa segar kembali.')
                elif pilihan_robot == 5:
                    self.robot.serangan += (10 / 100) * self.robot.serangan
                    print(f'{self.robot.nama} teriak keras, semangat bertambah!')
                else:
                    print('Pilihan tidak valid.')

            if pilihan_musuh == 1:
                self.musuh.nyerang(self.robot)
            elif pilihan_musuh == 2:
                self.musuh.bertahan(self.robot)
            elif pilihan_musuh == 3:
                print(f'{self.musuh.nama} menangis karena kalah dan membuat {self.robot.nama} bingung.')
                break
            elif pilihan_musuh == 4:
                self.musuh.darah += (15 / 100) * self.musuh.darah
                print(f'{self.musuh.nama} minum air anget dan merasa segar kembali.')
            elif pilihan_musuh == 5:
                self.musuh.serangan += (10 / 100) * self.musuh.serangan
                print(f'{self.musuh.nama} teriak keras, semangat bertambah!')
            else:
                print('Pilihan tidak valid.')

robot = Robot('Agus', 150, 40)
musuh = Robot('Joko', 200, 20)
game = Game(robot, musuh)
game.play()
