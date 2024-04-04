import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_board(size):
    return [['?' for _ in range(size)] for _ in range(size)]

def print_board(board):
    print("   " + " ".join([str(i+1) for i in range(len(board))]))  # Menampilkan label kolom
    print("  " + "--" * len(board))  # Garis horizontal
    for i, row in enumerate(board):
        print(f"{i+1} | {' | '.join(row)} |")  # Menampilkan baris dengan pemisah |
        print("  " + "--" * len(board))  # Garis horizontal antar baris
    print()

def place_bombs(board, num_bombs):
    bomb_spots = random.sample([(i, j) for i in range(len(board)) for j in range(len(board))], num_bombs)
    for row, col in bomb_spots:
        board[row][col] = 'X'

def count_adjacent_bombs(board, row, col):
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board), col + 2)):
            if board[i][j] == 'X':
                count += 1
    return count

def reveal_square(board, row, col):
    if board[row][col] == 'X':
        return False
    else:
        num_adjacent_bombs = count_adjacent_bombs(board, row, col)
        board[row][col] = str(num_adjacent_bombs) if num_adjacent_bombs > 0 else 'O'
        return True

def play_game(size, num_bombs):
    board = generate_board(size)
    place_bombs(board, num_bombs)
    print("Selamat datang di game Minesweeper alah bang kiki!")
    print("Untuk membuka kotak, kita memakai koordinat baris dan kolom.")
    print("Kode ? merupakan kotak yang belum diketahui.")
    print("Setuju cess?, cuss mulai game nya ces? (Ketik 'ya' untuk mulai)")
    confirmation = input(">> ")
    if confirmation.lower() != 'ya':
        print("wadohh ces, harus nya ketik ya tadi,yaudahlah,terima kasih sudah mampir. Sampai jumpa!")
        return
    
    clear_screen()
    print("Mari kita mulai game Minesweeper!\n")
    print_board(board)
    start_time = time.time()
    while True:
        try:
            row = int(input(f"Masukkan koordinat baris nya ces (1-{size}): ")) - 1
            col = int(input(f"Masukkan koordinat kolom nya  ces (1-{size}): ")) - 1
            if not (0 <= row < size and 0 <= col < size):
                print(f" Waduhh Koordinat di luar batas ces. Silakan sertakan koordinat yang valid. (1-{size}).")
                continue
            if not reveal_square(board, row, col):
                print("BOOM! yah kena boom ces. Game Over!, coba lagi ya jgn nangis!")
                print("gini ces letak yang benar:")
                print_board(board)
                break
            clear_screen()
            print_board(board)
            if all(board[i][j] != '?' for i in range(size) for j in range(size)):
                elapsed_time = time.time() - start_time
                print(f"Selamat ces anda memenangkan permainan dalam waktu {elapsed_time:.2f} detik! Selamat!")
                break
        except ValueError:
            print(f"Input harus berupa bilangan bulat antara 1 dan {size}.")


size = 3  
num_bombs = 3  
play_game(size, num_bombs)
