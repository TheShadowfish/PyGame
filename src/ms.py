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

    __slots__ = ('hide', 'sign', 'flag', 'question', 'pt_color')
    # flags = ('None','Mine','Question')

    def __init__(self, hide=True, sign=0, flag=0):
        self.hide = hide
        self.sign = sign
        self.flag = False
        self.question = False
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

    # @property
    # def flag(self):
    #     if not self.hide:
    #         self.flag = self.flags[0]
    #     return self.flag


    def check_flag(self, no_question: bool = False):
        if not self.flag and not self.question:
            self.flag = True
        elif self.flag and not no_question:
            self.flag = False
            self.question = True
        else:
            self.flag = False
            self.question = False


class Mines:

    def __init__(self, height, width, mines):
        """
        my_ms = Mines(WINDOW//TILE_SIZE, WINDOW//TILE_SIZE, WINDOW//TILE_SIZE*4)
        """
        self._height = height
        self._width = width
        self.mines = mines
        self._field = []

        self.game_over = False
        self.boom = False
        self.boom_pts = None

        # self._game_result = None

        for i in range(0, self._height):
            pts = []
            for j in range(0, self._width):
                pts.append(Point())
            self._field.append(copy.deepcopy(pts))

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
        count2 = 0

        field = 0
        for i in range(w0, w2):
            for j in range(h0, h2):
                if self._field[i][j].sign == 9:
                    count2 += 1

        for i in self.get_points_list(w, h):
            if self._field[i[0]][i[1]].sign == 9:
                count += 1

        assert count == count2

        return count

    def get_points_list(self, w, h):
        """
        Возвращает список прилегающих ячеек (pts)
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

        point_list = []
        for i in range(w0, w2):
            for j in range(h0, h2):
                if not(i == w and j == h):
                    point_list.append((i, j))
        return point_list


    def recursive_un_hide(self, w, h, depth = 0):
        if self._field[w][h].hide:
            self._field[w][h].hide = False
            if self._field[w][h].sign == 9:
                self.boom = True
                self.boom_pts = (w, h)
                self.game_over = True
            if self._field[w][h].sign == 0:
                depth += 1
                for pts in self.get_points_list(w, h):
                    print(f"depth= {depth}, w,h= {w},{h}")
                    self.recursive_un_hide(pts[0], pts[1], depth)


    def open_near(self, w, h):
        if self._field[w][h].hide != False:
            print("Hide can not!")
            return

        # не даст открыть все поля, если не отмечено нужное количество мин
        sign_checked = 0

        # если мины отмечены, но неправильно - отмечает, что взрыв состоится
        # boom = False

        for pts in self.get_points_list(w, h):
            the_point = self._field[pts[0]][pts[1]]
            if (the_point.flag or the_point.question) and the_point.hide:
               sign_checked += 1
            if not the_point.flag and not the_point.question and the_point.sign == 9:
                self.boom = True
                self.boom_pts = (pts[0], pts[1])
                self.game_over = True
        else:
            # если закрыто меньше мин, чем предусмотрено - ничего не делаем
            if self._field[w][h].sign > sign_checked:
                print(f"It is SUICIDE? NO WAY! Not on my shift!!! {sign_checked}")
                return
            else:
                for pts in self.get_points_list(w, h):
                    the_point = self._field[pts[0]][pts[1]]
                    if the_point.sign == 0:
                        self.recursive_un_hide(pts[0], pts[1], 0)
                    if not the_point.flag and not the_point.question:
                        self._field[pts[0]][pts[1]].hide = False


    def set_flag(self, w, h):
        # Прямо дофига очевидно, что делает. На самом деле просто флаг переключает.

        self._field[w][h].check_flag(False)

    def __str__(self):
        field = ''
        for i in range(0, self._height):

            for j in range(0, self._width):
                field += f"{self._field[j][i].sign} "
            else:
                field += f"\n"
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

            return w, h, self._field[w][h]
            # return w, h, self._field[w][h].color, self._field[w][h].sign, self._field[w][h].hide, self._field[w][h].flag

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

            # return w, h, self._field[w][h]

            return w, h, self._field[w][h]
            # return w, h, self._field[w][h].color, self._field[w][h].sign, self._field[w][h].hide, self._field[w][h].flag
        else:
            raise StopIteration

    def stop_game(self):
        """
        Проверка на выигрышЖ не должно быть скрытых безопасных полей
        """

        if self.game_over:
            print(f"GAME END! (294) game_over= {self.game_over}, boom= {self.boom}")
            return False

        else:
            for pt in self._field:
            # Если мина открыта - она взорвалась, значит всё. Совсем всё.
                if pt[2].sign == 9 and pt[2].hide == False:
                    self._game_result = False
                    # return self._game_result
                    print(f"Невозможная ситуация: взрыв мины не завершил игру ранее.")
                # Если не открыто поле без мины, то игра продолжается
                if pt[2].sign != 9 and pt[2].hide == True:
                    return False
            # взорвавшихся мин нет, скрытых полей нет
            else:
                self.game_over = True
                return True






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
