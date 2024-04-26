import pygame as pg
# from random import randrange
from ms import Mines

# Константы
WINDOW = 900
FPS = 60
TILE_SIZE = 50
TIME_STEP = 100


def main():

    mines = (((WINDOW//TILE_SIZE)**2))//10 * 2 #20%
    my_ms = Mines(WINDOW//TILE_SIZE, WINDOW//TILE_SIZE, mines)

    print(my_ms)

    # Инициализация объектов
    gameScreen = pg.display.set_mode([WINDOW] * 2, flags=pg.DOUBLEBUF)

    clock = pg.time.Clock()

    pg.font.init()
    f1 = pg.font.SysFont('arial', TILE_SIZE-5)

    pg.display.set_caption("Mineswiper")

    global_time = 0;

    time = 0
    time_step = TIME_STEP


    # Главный цикл игры
    while True:

        # Частота обновления экрана
        clock.tick(FPS)
        mines = [pt[2] for pt in my_ms if pt[2].sign == 9]
        # pg.display.set_caption(f"WINNER!!! Mineswiper: timer: {str(global_time)}, mines: {len(mines)}")
        pg.display.set_caption(f"Minesweeper: timer: {str(global_time)}, mines: {len(mines)}")

        # Цикл обработки событий
        for event in pg.event.get():

            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.dict['pos']
                mouse_btn = event.dict['button']

                w_mouse = pg.MOUSEBUTTONDOWN.__pos__()
                w: int = mouse_pos[0] // TILE_SIZE
                h: int = mouse_pos[1] // TILE_SIZE


                if my_ms.game_over:
                    helpless(my_ms.boom)

                else:
                    if mouse_btn == 3:
                        my_ms.set_flag(w, h)
                    elif mouse_btn == 2:
                        my_ms.open_near(w, h)
                        print(f"OPEN_NEAR!!")
                    else:
                        # my_ms.un_hide(w, h)
                        my_ms.recursive_un_hide(w, h)

                    my_ms.stop_game()

        # Управляем
        time_now = pg.time.get_ticks()
        if time_now - time > time_step:
            time = time_now
            # if not my_ms.boom and Mines.check_end_game(my_ms):
            if not my_ms.game_over:
                global_time += 1

            fieldpainter(gameScreen, my_ms, f1)



def fieldpainter(gameScreen, my_ms, f1):
    """
    Отрисовка поля, действительно проще в отдельную функцию
    """
    # отрисовать поле
    gameScreen.fill((89, 166, 224))

    for pt in my_ms:

        w, h, the_point = pt
        point = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])  # snake.copy()
        point.center = (w * TILE_SIZE + TILE_SIZE // 2, h * TILE_SIZE + TILE_SIZE // 2)

        if the_point.hide:
            pg.draw.rect(gameScreen, the_point.color, point)

            if the_point.flag:
                text_sign = f1.render('∆', True, "red")  # ∆ ⊗
                place = text_sign.get_rect(center=point.center)
                gameScreen.blit(text_sign, place)
            elif the_point.question:
                text_sign = f1.render('?', True, "blue")  # ∆
                place = text_sign.get_rect(center=point.center)
                gameScreen.blit(text_sign, place)
            elif my_ms.boom:
                if the_point.sign == 9:
                    pg.draw.rect(gameScreen, "black", point)

        elif the_point.sign == 0:
            pg.draw.rect(gameScreen, ((10, 143, 239)), point)

        elif the_point.sign == 9:
            pg.draw.rect(gameScreen, the_point.color, point)

        else:
            pg.draw.rect(gameScreen, ((10, 143, 239)), point)
            text_sign = f1.render(str(the_point.sign), True, the_point.color)
            place = text_sign.get_rect(center=point.center)
            gameScreen.blit(text_sign, place)

    pg.display.flip()

def helpless(fail: bool):
    """
    Бесполезная функция по сути
    """
    if fail:
        print("CA-BOOM!   CA-BOoOOoOOoM!!!      CA-BOOoOoOOOOOOoOOOoOoOM!!!!!!!!!!")
        print("""
        ██╗░░░██╗░█████╗░██╗░░░██╗░░░░░░███████╗██╗░░██╗██████╗░██╗░░░░░░█████╗░██████╗░███████╗██████╗░
        ╚██╗░██╔╝██╔══██╗██║░░░██║░░░░░░██╔════╝╚██╗██╔╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗
        ░╚████╔╝░██║░░██║██║░░░██║░░░░░░█████╗░░░╚███╔╝░██████╔╝██║░░░░░██║░░██║██║░░██║█████╗░░██║░░██║
        ░░╚██╔╝░░██║░░██║██║░░░██║░░░░░░██╔══╝░░░██╔██╗░██╔═══╝░██║░░░░░██║░░██║██║░░██║██╔══╝░░██║░░██║
        ░░░██║░░░╚█████╔╝╚██████╔╝░░░░░░███████╗██╔╝╚██╗██║░░░░░███████╗╚█████╔╝██████╔╝███████╗██████╔╝
        """)
    else:
        print("""
        ██╗░░░██╗░█████╗░██╗░░░██╗░░░░░░██╗░░░░░░░░░░░░██╗░░██╗░░██╗░░░██╗░░░░██║
        ╚██╗░██╔╝██╔══██╗██║░░░██║░░░░░░╚██╗░░░███░░░░██╔╝░░██║░░████╗░██║░░░░██║
        ░╚████╔╝░██║░░██║██║░░░██║░░░░░░░╚██░░██╔██░░██╔╝░░░██║░░██║██╗██║░░░░██║
        ░░╚██╔╝░░██║░░██║██║░░░██║░░░░░░░░╚████╔╝╚████╔╝░░░░██║░░██║░████║░░░░░╚╝
        ░░░██║░░░╚█████╔╝╚██████╔╝░░░░░░░░░╚██╔╝░░╚██╔╝░░░░░██║░░██║░░░██║░░░░██╗
        """)


if __name__ == '__main__':
    main()
