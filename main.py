import pygame  # Mengimpor pustaka pygame untuk membuat game
import sys  # Mengimpor sys untuk menangani keluarnya program
import random  # Mengimpor random untuk menghasilkan posisi apel secara acak
import time  # Mengimpor time untuk menambahkan delay dalam game

# Inisialisasi pygame
check_errors = pygame.init()

# Menentukan ukuran layar game
frame_size_x = 720
frame_size_y = 480

# Mengatur judul jendela game
pygame.display.set_caption('Snake Game')

# Membuat jendela game dengan ukuran yang telah ditentukan
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Mengontrol kecepatan frame per detik
fps_controller = pygame.time.Clock()

# Menentukan arah awal pergerakan ular
direction = 'RIGHT'
change_to = direction  # Variabel untuk menyimpan perubahan arah
score = 0  # Variabel untuk menyimpan skor

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

def game_over():
    """Menampilkan layar game over dan keluar dari permainan"""
    my_font = pygame.font.SysFont('Arial', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (360, 120)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

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

    # Mengubah arah berdasarkan input, dengan memastikan ular tidak bisa berbalik arah 180 derajat
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Memindahkan kepala ular sesuai arah
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Mengisi layar dengan warna putih sebagai latar belakang
    game_window.fill(white)
    
    # Menambahkan posisi baru ke tubuh ular
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
        score += 1
        apple_spawn = False
    else:
        snake_body.pop()
    
    # Menggambar tubuh ular di layar
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Jika apel belum muncul, buat apel di posisi acak
    if not apple_spawn:
        apple_pos = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
    apple_spawn = True  # Tandai apel telah muncul
    
    # Menggambar apel di layar
    pygame.draw.rect(game_window, red, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10)) 
    
    # Mengecek apakah ular menabrak dinding
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    
    # Mengecek apakah ular menabrak tubuhnya sendiri
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    
    # Menampilkan skor di layar
    score_font = pygame.font.SysFont('Arial', 20)
    score_surface = score_font.render('Score : ' + str(score), True, black)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (72, 15)
    game_window.blit(score_surface, score_rect)
    
    # Memperbarui tampilan game
    pygame.display.update()
    
    # Mengatur kecepatan game
    fps_controller.tick(10)
