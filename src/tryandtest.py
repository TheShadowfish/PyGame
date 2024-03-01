import pygame as pg
# from pygame.locals import *



pg.display.set_mode((600, 400))


while True:
    # Цикл обработки событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        # # print(pg.QUIT)
        # print(event)
        # print(event.type)
            # pg.quit()

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

        print("https://younglinux.info/pygame/framework")
#
#         #<Event(1025-MouseButtonDown {'pos': (584, 17), 'button': 1, 'touch': False, 'window': None})>
# 1025
# <Event(1026-MouseButtonUp {'pos': (584, 17), 'button': 1, 'touch': False, 'window': None})>
        # < Event(1024 - MouseMotion
        # {'pos': (522, 15), 'rel': (8, -7), 'buttons': (0, 0, 0), 'touch': False, 'window': None}) >
        # 1024
        # < Event(1024 - MouseMotion
        # {'pos': (530, 9), 'rel': (8, -6), 'buttons': (0, 0, 0), 'touch': False, 'window': None}) >
        # 1024
        # < Event(1024 - MouseMotion
        # {'pos': (535, 5), 'rel': (5, -4), 'buttons': (0, 0, 0), 'touch': False, 'window': None}) >