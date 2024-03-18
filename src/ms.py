from random import randrange
import copy


class Point:
    colors = [(89, 166, 224),
              (10, 143, 239),
              (10, 239, 143),
              (239, 10, 10),
              (90, 200, 200),
              (200, 40, 40),
              (200, 80, 80),
              (200, 160, 160),
              (200, 200, 200),
              (0, 0, 0)]

    __slots__ = ('hide', 'sign', 'pt_color', 'comment')

    def __init__(self, hide=True, sign=0):
        self.hide = hide
        self.sign = sign
        # self.color = 'standart

    @property
    def color(self):
        # Покраска под число(__sign)
        # 89, 166, 224

        if self.hide:
            self.pt_color = (28 * 0, 255 - 15 * 0, 255 - 24 * 0)
        else:
            k = self.sign
            self.pt_color = (28 * k, 255 - 15 * k, 255 - 24 * k)
        return self.pt_color

    @color.setter
    def color(self, color):
        self.pt_color = color


class Mines:

    def __init__(self, height, width, mines):
        """
        my_ms = Mines(WINDOW//TILE_SIZE, WINDOW//TILE_SIZE, WINDOW//TILE_SIZE*4)
        """
        self._height = height
        self._width = width
        self.mines = mines
        self._field = []

        for i in range(0, self._height):
            pts = []
            for j in range(0, self._width):
                pts.append(Point())
            self._field.append(copy.deepcopy(pts))

        # self.__field = [[0] * self.__width] * self.__height

        h_rand = randrange(0, self._height)
        w_rand = randrange(0, self._width)
        self._field[w_rand][h_rand].sign = 1
        # self.__field[w_rand][h_rand]['class'] = 9
        while self.mines >= 0:
            h_rand = randrange(0, self._height)
            w_rand = randrange(0, self._width)
            if self._field[w_rand][h_rand].sign != 9:
                self._field[w_rand][h_rand].sign = 9
                self.mines -= 1
                # self.__field[w_rand][h_rand]['class'] = 9
            # print(
            #     f"mines {self.mines}, h_rand {h_rand}, w_rand {w_rand} self.__field[w][h]['class'] {self._field[w_rand][h_rand].sign}")

        for h in range(0, self._height):
            for w in range(0, self._width):
                if self._field[w][h].sign != 9:
                    self._field[w][h].sign = self.get_sign(w, h)

    def get_sign(self, w, h):
        """
        Установливает число ячейки, равно числу мин вокруг поля.
        :param w:
        :param h:
        :return:
        """
        w0 = w - 1
        w2 = w + 2
        h0 = h - 1
        h2 = h + 2
        if w0 < 0: w0 = 0
        if h0 < 0: h0 = 0
        if w2 > self._width: w2 = self._width
        if h2 > self._height: h2 = self._height

        count = 0
        field = 0
        for i in range(w0, w2):
            for j in range(h0, h2):
                if self._field[i][j].sign == 9:
                    count += 1
                field += 1
        # print(f"field(9) {field}")
        return count


    def unhide(self,w,h):
        self._field[w][h].hide = False

    def __str__(self):
        field = ''
        for i in range(0, self._height):

            for j in range(0, self._width):
                field += f"{self._field[j][i].sign} "
                # print(f"{self.__field[i][j]}", sep=' ')
            else:
                field += f"\n"
                # print(f"\n")
        return field

    def __iter__(self):
        self.current = 0
        return self

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError(f"index must be integer (int). index: {index}")
        if 0 <= index < len(self._height * self._width):
            w = index % self._width
            h = index // self._width

            return w, h, self._field[w][h].color, self._field[w][h].sign, self._field[w][h].hide
        else:
            raise IndexError(f"Index out of a range (0 <= {index} < {self._height * self._width}")

    def __len__(self):
        return len(self._height * self._width)

    def __next__(self):
        if self.current < (self._height * self._width):
            number = self.current
            self.current += 1
            w = number % self._width
            h = number // self._width

            return w, h, self._field[w][h].color, self._field[w][h].sign, self._field[w][h].hide
        else:
            raise StopIteration

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
