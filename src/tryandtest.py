import pygame as pg
# from pygame.locals import *

# здесь подключаются модули
import pygame
import sys

# здесь определяются константы,
# классы и функции
FPS = 60

# здесь происходит инициация,
# создание объектов
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()


print("https://younglinux.info/pygame/framework")
# главный цикл
while True:

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for event in pygame.event.get():
        pg.display.set_caption(str(event))
        if event.type == pygame.QUIT:
            sys.exit()

        # Обработка нажатий WASD
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_w:
        #         snake_dir = (0, -TILE_SIZE)
        #     if event.key == pg.K_s:
        #         snake_dir = (0, TILE_SIZE)
        #     if event.key == pg.K_a:
        #         snake_dir = (-TILE_SIZE, 0)
        #     if event.key == pg.K_d:
        #         snake_dir = (TILE_SIZE, 0)
        if event.type == pg.MOUSEBUTTONDOWN:
            w_mouse = pg.MOUSEBUTTONDOWN.__pos__()
            w_mouse.real
            print(w_mouse.real)
            # print(event)
            # print(event.type)

    # --------
    # изменение объектов
    # --------

    # обновление экрана
    pygame.display.update()



