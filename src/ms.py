from random import randrange
import copy


class Point:
    def __init__(self, hide, sign):
        self.hide = hide
        self.sign = sign


class Mines:

    def __init__(self, height, width, mines):
        self.__height = height
        self.__width = width
        self.mines = mines
        self.__field = []

        for i in range(0, self.__height):
            pts = []
            for j in range(0, self.__width):
                pts.append(Point(True, 0))
            self.__field.append(copy.deepcopy(pts))

        # self.__field = [[0] * self.__width] * self.__height

        h_rand = randrange(0, self.__height)
        w_rand = randrange(0, self.__width)
        self.__field[w_rand][h_rand].sign = 1
        # self.__field[w_rand][h_rand]['class'] = 9
        while self.mines >= 0:
            h_rand = randrange(0, self.__height)
            w_rand = randrange(0, self.__width)
            if self.__field[w_rand][h_rand].sign != 9:
                self.__field[w_rand][h_rand].sign = 9
                self.mines -= 1
                # self.__field[w_rand][h_rand]['class'] = 9
            print(
                f"mines {self.mines}, h_rand {h_rand}, w_rand {w_rand} self.__field[w_rand][h_rand]['class'] {self.__field[w_rand][h_rand].sign}")

        for h in range(0, self.__height):
            for w in range(0, self.__width):
                if self.__field[w][h].sign != 9:
                    self.__field[w][h].sign = self.get_class(w, h)

    def get_class(self, w, h):
        w0 = w - 1
        w2 = w + 2
        h0 = h - 1
        h2 = h + 2
        if w0 < 0: w0 = 0
        if h0 < 0: h0 = 0
        if w2 > self.__width: w2 = self.__width
        if h2 > self.__height: h2 = self.__height

        count = 0
        field = 0
        for i in range(w0, w2):
            for j in range(h0, h2):
                if self.__field[i][j].sign == 9:
                    count += 1
                field += 1
        print(f"field(9) {field}")
        return count

    def __str__(self):
        field = ''
        for i in range(0, self.__height):

            for j in range(0, self.__width):
                field += f"{self.__field[i][j].sign} "
                # print(f"{self.__field[i][j]}", sep=' ')
            else:
                field += f"\n"
                # print(f"\n")
        return field

#
# WINDOW = 900
# FPS = 60
# TILE_SIZE = 50
# RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
#
# my_ms = Mines(WINDOW // TILE_SIZE, WINDOW // TILE_SIZE, WINDOW // TILE_SIZE * 2)
# #
# print("START")
# print(my_ms)
