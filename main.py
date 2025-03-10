import pygame  # Mengimpor pustaka pygame untuk membuat game
import sys  # Mengimpor sys untuk menangani keluarnya program
import random  # Mengimpor random untuk menghasilkan posisi apel secara acak

# Inisialisasi pygame
check_errors = pygame.init()

# Menentukan ukuran layar game
frame_size_x = 720
frame_size_y = 480

# Mengatur judul jendela game
pygame.display.set_caption('Snake Game')

# Membuat jendela game dengan ukuran yang telah ditentukan
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Menentukan arah awal pergerakan ular
direction = 'RIGHT'
change_to = direction  # Variabel untuk menyimpan perubahan arah

# Inisialisasi posisi awal ular
snake_pos = [100, 50]  # Posisi awal kepala ular
snake_body = [[100, 50], [90, 50], [80, 50]]  # Tubuh ular berisi beberapa segmen

# Menentukan posisi awal apel secara acak
apple_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
apple_spawn = True  # Status apakah apel sudah muncul

# Warna-warna yang digunakan dalam game
white = pygame.Color(255, 255, 255)  # Warna putih untuk background
black = pygame.Color(0, 0, 0)  # Warna hitam
red = pygame.Color(255, 0, 0)  # Warna merah untuk apel
green = pygame.Color(0, 255, 0)  # Warna hijau untuk ular
blue = pygame.Color(0, 0, 255)  # Warna biru

# Loop utama game
while True:
    # Mengecek event yang terjadi dalam game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Jika tombol close ditekan, keluar dari game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # Jika ada tombol yang ditekan
            if event.key == pygame.K_UP:
                change_to = 'UP'  # Ubah arah ke atas
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'  # Ubah arah ke bawah
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'  # Ubah arah ke kiri
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'  # Ubah arah ke kanan
            if event.key == pygame.K_ESCAPE:  # Jika tombol ESC ditekan, keluar dari game
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Mengisi layar dengan warna putih sebagai latar belakang
    game_window.fill(white)
    print(change_to)  # Menampilkan arah pergerakan di terminal

    # Menambahkan posisi baru ke tubuh ular
    snake_body.insert(0, list(snake_pos))
    
    # Menggambar tubuh ular di layar
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Jika apel belum muncul, buat apel di posisi acak
    if not apple_spawn:
        apple_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    apple_spawn = True  # Tandai apel telah muncul
    
    # Menggambar apel di layar
    pygame.draw.rect(game_window, red, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) 
    
    # Memperbarui tampilan game
    pygame.display.update()
