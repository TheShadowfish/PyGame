import pygame as pg
from random import randrange
from ms import Mines


# Константы
WINDOW = 900
FPS = 60
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
TIME_STEP = 100

my_ms = Mines(WINDOW//TILE_SIZE, WINDOW//TILE_SIZE, WINDOW//TILE_SIZE)
# # #
print(my_ms)

# Функция для определения координат (X:Y) случайной позиции на игровом поле
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]


# Инициализация объектов
gameScreen = pg.display.set_mode([WINDOW] * 2)

clock = pg.time.Clock()

pg.font.init()
f1 = pg.font.SysFont('arial', TILE_SIZE)
# f2 = pg.font.Font(None, TILE_SIZE)




# Параметры змейки
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0,0)

# Параметры объектов еды
food = snake.copy()
food.center = get_random_position()


time = 0
time_step = TIME_STEP


# Главный цикл игры
while True:
    # Частота обновления экрана
    clock.tick(FPS)

    # Цикл обработки событий
    for event in pg.event.get():
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

    # Управляем змейкой
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now

        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

        # Поедание
        if snake.center == food.center:
            food.center = get_random_position()
            length += 1
            time_step -=1

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

        snake_dir = (0,0)

        # gameScreen.fill((155, 188, 15))
        gameScreen.fill((89, 166, 224))
        [pg.draw.rect(gameScreen, (10, 143, 239), segment) for segment in segments] #120, 149, 12
        #10, 143, 239      13 101 172

        # Рисуем объект еды
        pg.draw.rect(gameScreen, (13, 101, 172), food)

        text1 = f1.render(str(time_step), True,
                          (13, 101, 172))
        text2 = f1.render(str(length), False,
                          (10, 143, 239))

        gameScreen.blit(text1, (WINDOW - (TILE_SIZE<<1), 0))
        gameScreen.blit(text2, (WINDOW - (TILE_SIZE<<1), TILE_SIZE))
        # gameScreen.display.update()

        pg.display.flip()

