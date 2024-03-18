import pygame as pg
from random import randrange
from ms import Mines


# Константы
WINDOW = 900
FPS = 60
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
TIME_STEP = 100

my_ms = Mines(WINDOW//TILE_SIZE, WINDOW//TILE_SIZE, WINDOW//TILE_SIZE*4)
# # #
print(my_ms)

# Функция для определения координат (X:Y) случайной позиции на игровом поле
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]


# Инициализация объектов
gameScreen = pg.display.set_mode([WINDOW] * 2, flags=pg.DOUBLEBUF)

clock = pg.time.Clock()

pg.font.init()
f1 = pg.font.SysFont('arial', TILE_SIZE-5)
# f2 = pg.font.Font(None, TILE_SIZE)


"""
Функция flip() решает проблему иным способом. Она дает выигрыш, если в set_mod() были переданы определенные флаги. Например,

pygame.display.set_mode(flags=pygame.FULLSCREEN |
                              pygame.OPENGL |
                              pygame.DOUBLEBUF)
"""

# Параметры змейки
# snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
# snake.center = get_random_position()
# length = 1
# segments = [snake.copy()]
# snake_dir = (0,0)




# Параметры объектов еды
# food = snake.copy()
# food.center = get_random_position()


time = 0
time_step = TIME_STEP


# Главный цикл игры
while True:
    # Частота обновления экрана
    clock.tick(FPS)

    # Цикл обработки событий
    for event in pg.event.get():
        pg.display.set_caption(str(event))

        if event.type == pg.QUIT:
            exit()

        # Обработка нажатий WASD
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = event.dict['pos']
            mouse_btn = event.dict['button']

            w_mouse = pg.MOUSEBUTTONDOWN.__pos__()
            w_mouse.real

            # w_mouse.__pos__()
            print(f"{mouse_pos[0]},{mouse_pos[1]} button= {mouse_btn}")

            w: int = mouse_pos[0] // TILE_SIZE
            h: int = mouse_pos[1] // TILE_SIZE

            my_ms.unhide(w, h)

            print(f"x, y = {w}, {h}")


            # WINDOW = 900
            # FPS = 60
            # TILE_SIZE = 50
            # RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
            # TIME_STEP = 100
            #
            # my_ms = Mines(WINDOW // TILE_SIZE, WINDOW // TILE_SIZE, WINDOW // TILE_SIZE * 4)

    # Управляем змейкой
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now

        # snake.move_ip(snake_dir)
        # segments.append(snake.copy())
        # segments = segments[-length:]
        #
        # # Поедание
        # if snake.center == food.center:
        #     food.center = get_random_position()
        #     length += 1
        #     time_step -=1

        # # Столкновение с границами
        # if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW:
        #     snake.center, food.center = get_random_position(), get_random_position()
        #     length, snake_dir = 1, (0, 0)
        #     segments = [snake.copy()]

        # Столкновение с границами и телом змейки
        # snake_collision = pg.Rect.collidelist(snake, segments[:-1]) != -1
        # if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or snake_collision:
        #     snake.center, food.center = get_random_position(), get_random_position()
        #     length, snake_dir = 1, (0, 0)
        #     time_step = TIME_STEP
        #     segments = [snake.copy()]



        # отрисовать поле
        gameScreen.fill((89, 166, 224))

        for pt in my_ms:
            w, h, color, sign, hide = pt
            point = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])  # snake.copy()
            point.center = (w * TILE_SIZE + TILE_SIZE // 2, h * TILE_SIZE + TILE_SIZE // 2)

            if hide:
                pg.draw.rect(gameScreen, color, point)


            if sign == 0 or sign == 9 or hide:
                pg.draw.rect(gameScreen, color, point)
            else:
                # print(sign)
                pg.draw.rect(gameScreen, ((10, 143, 239)), point)
                # gameScreen.blit(str(sign), (WINDOW - (TILE_SIZE << 1), 0))
                # gameScreen.blit(text2, (WINDOW - (TILE_SIZE << 1), TILE_SIZE))
                text_sign = f1.render(str(sign), True, color)
                place = text_sign.get_rect(center=point.center)
                gameScreen.blit(text_sign, place)




        # snake_dir = (0, 0)
        #
        # # gameScreen.fill((155, 188, 15))
        # gameScreen.fill((89, 166, 224))
        # [pg.draw.rect(gameScreen, (10, 143, 239), segment) for segment in segments]  # 120, 149, 12
        # #10, 143, 239      13 101 172

        # # Рисуем объект еды
        # pg.draw.rect(gameScreen, (13, 101, 172), food)
        #
        # text1 = f1.render(str(time_step), True,
        #                   (13, 101, 172))
        # text2 = f1.render(str(length), False,
        #                   (10, 143, 239))
        #
        # gameScreen.blit(text1, (WINDOW - (TILE_SIZE<<1), 0))
        # gameScreen.blit(text2, (WINDOW - (TILE_SIZE<<1), TILE_SIZE))
        # gameScreen.display.update()

        pg.display.flip()

