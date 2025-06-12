# import pygame
# import sys
# import math

# pygame.init()

# LEBAR_LAYAR, TINGGI_LAYAR = 800, 600
# FPS = 60
# LEBAR_TIANG = 20
# TINGGI_TIANG = 300
# LEBAR_BENDERA = 200
# TINGGI_BENDERA = 120
# AMPLITUDO_GELORA = 25
# FREKUENSI_GELORA = 0.12

# MERAH = (227, 27, 35)
# PUTIH = (255, 255, 255)
# COKLAT = (139, 69, 19)
# LANGIT = (255, 255, 255)  


# layar = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR))
# pygame.display.set_caption("Bendera Merah Putih Berkibar Kencang di Tiang")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     layar.fill((255,255,255))
#     pygame.display.update()

# pygame.quit


# def gambar_bendera(x, y, offset_gelora):
#     pygame.draw.rect(layar, MERAH, (x, y, LEBAR_BENDERA, TINGGI_BENDERA // 2))
#     pygame.draw.rect(layar, PUTIH, (x, y + TINGGI_BENDERA // 2, LEBAR_BENDERA, TINGGI_BENDERA // 2))
#     for i in range(0, LEBAR_BENDERA, 4):
#         tinggi_gelora = int(AMPLITUDO_GELORA * math.sin(FREKUENSI_GELORA * (i + offset_gelora)))
#         pygame.draw.line(layar, PUTIH, (x + i, y), (x + i, y + TINGGI_BENDERA // 2 + tinggi_gelora), 4)
# #gambar_bendera()
# def utama():
#     jam = pygame.time.Clock()
#     offset_gelora = 0

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#         layar.fill(LANGIT)
#         pygame.draw.rect(layar, COKLAT, (LEBAR_LAYAR // 2 - LEBAR_TIANG // 2, TINGGI_LAYAR - TINGGI_TIANG, LEBAR_TIANG, TINGGI_TIANG), border_radius=6)

#         offset_gelora += 8
#         if offset_gelora > 10000:
#             offset_gelora = 0
#         gambar_bendera(LEBAR_LAYAR // 2 - LEBAR_BENDERA // 2, TINGGI_LAYAR - TINGGI_TIANG - TINGGI_BENDERA, offset_gelora)
#         pygame.display.flip()
#         jam.tick(FPS)

# if __name__ == "_main_":
#     utama()

# import pygame 
# import sys 
# import math

# pygame.init()

# LEBAR_LAYAR, TINGGI_LAYAR = 800, 600
# FPS = 60
# LEBAR_TIANG = 20
# TINGGI_TIANG = 300
# LEBAR_BENDERA = 200
# TINGGI_BENDERA = 120
# AMPLITUDO_GELORA = 25
# FREKUENSI_GELORA = 0.12

# MERAH = (227, 27, 35)
# PUTIH = (255, 255, 255)
# COKLAT = (139, 69, 19)
# LANGIT = (255, 255, 255)

# layar = pygame.display.set_mode((LEBAR_LAYAR, TINGGI_LAYAR)) 
# pygame.display.set_caption("Bendera Merah Putih Berkibar Kencang di Tiang")

# def gambar_bendera(x, y, offset_gelora):
#     pygame.draw.rect(layar, MERAH, (x, y, LEBAR_BENDERA, TINGGI_BENDERA // 2)) 
#     pygame.draw.rect(layar, PUTIH, (x, y + TINGGI_BENDERA // 2, LEBAR_BENDERA,
# TINGGI_BENDERA // 2))
# for i in range(0, LEBAR_BENDERA, 4):
#     tinggi_gelora = int(AMPLITUDO_GELORA * math.sin(FREKUENSI_GELORA * (i + offset_gelora)))
# pygame.draw.line(layar, PUTIH, (x + i, y), (x + i, y + TINGGI_BENDERA // 2 + tinggi_gelora), 4)

# def utama():
#     jam = pygame.time.Clock() 
#     offset_gelora = 0

#     while True:
#         for event in pygame.event.get(): 
#             if event.type == pygame.QUIT:
#                 pygame.quit() 
#                 sys.exit()
#     layar.fill(LANGIT)
#     pygame.draw.rect(layar, COKLAT, (LEBAR_LAYAR // 2 - LEBAR_TIANG // 2, TINGGI_LAYAR - TINGGI_TIANG, LEBAR_TIANG, TINGGI_TIANG), border_radius=6)

# offset_gelora += 8
# if offset_gelora > 10000: offset_gelora = 0
# gambar_bendera(LEBAR_LAYAR // 2 - LEBAR_BENDERA // 2, TINGGI_LAYAR - TINGGI_TIANG - TINGGI_BENDERA, offset_gelora)
# pygame.display.flip() jam.tick(FPS)

# if  name  == " main ": utama()

# 
import time
import os 
import math
from termcolor import cprint

def animasi_bendera(lebar, tinggi):
    for gerak in range(60): 
        os.system("cls") 

        for i in range(tinggi // 2):
            maju_mundur = " " * (5 + int(math.sin((gerak + i) * 0.5) * 3))  
            cprint(maju_mundur + " " * lebar, "white", "on_red")

        for i in range(tinggi // 2):
            maju_mundur = " " * (5 + int(math.sin((gerak + i + 1) * 0.5) * 3))  
            cprint(maju_mundur + " " * lebar, "white", "on_white")

        for i in range(10):
            cprint("||", "grey", "on_blue")

        time.sleep(0.1) 

animasi_bendera(15,6)