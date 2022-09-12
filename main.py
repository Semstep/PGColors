import pygame as pg
# class Colors:
# """Переделать файл со строками вида 'DarkBlue	#00008B' в строки вида 'DARKBLUE = (0, 0, 139)' """
#     def __init__(self):
#         FILENAME = 'colors.txt'
#         OUTFILE = 'copypaste_colors.txt'
#
#         colors = dict()
#         with open(FILENAME) as colfile, open(OUTFILE, 'w', encoding='utf8') as outfile:
#             for l in colfile.readlines():
#                 col_val = l.strip().split('\t')
#                 name, val = col_val[0], col_val[1].strip('#')
#                 globals()[name.upper()] = [int(val[s: s+2], base=16) for s in range(0, 6, 2)]
#                 print(f'{name.upper()} = {tuple([int(val[s: s+2], base=16) for s in range(0, 6, 2)])}', file=outfile)
#         print('Constants for Colors was added')
#
# cc = Colors()
from typing import List

BLACK = (0, 0, 0)
NAVY = (0, 0, 128)
DARKBLUE = (0, 0, 139)
MEDIUMBLUE = (0, 0, 205)
BLUE = (0, 0, 255)
DARKGREEN = (0, 100, 0)
GREEN = (0, 128, 0)
TEAL = (0, 128, 128)
DARKCYAN = (0, 139, 139)
DEEPSKYBLUE = (0, 191, 255)
DARKTURQUOISE = (0, 206, 209)
MEDIUMSPRINGGREEN = (0, 250, 154)
LIME = (0, 255, 0)
SPRINGGREEN = (0, 255, 127)
AQUA = (0, 255, 255)
CYAN = (0, 255, 255)
MIDNIGHTBLUE = (25, 25, 112)
DODGERBLUE = (30, 144, 255)
LIGHTSEAGREEN = (32, 178, 170)
FORESTGREEN = (34, 139, 34)
SEAGREEN = (46, 139, 87)
DARKSLATEGRAY = (47, 79, 79)
LIMEGREEN = (50, 205, 50)
MEDIUMSEAGREEN = (60, 179, 113)
TURQUOISE = (64, 224, 208)
ROYALBLUE = (65, 105, 225)
STEELBLUE = (70, 130, 180)
DARKSLATEBLUE = (72, 61, 139)
MEDIUMTURQUOISE = (72, 209, 204)
INDIGO = (75, 0, 130)
DARKOLIVEGREEN = (85, 107, 47)
CADETBLUE = (95, 158, 160)
CORNFLOWERBLUE = (100, 149, 237)
MEDIUMAQUAMARINE = (102, 205, 170)
DIMGRAY = (105, 105, 105)
SLATEBLUE = (106, 90, 205)
OLIVEDRAB = (107, 142, 35)
SLATEGRAY = (112, 128, 144)
LIGHTSLATEGRAY = (119, 136, 153)
MEDIUMSLATEBLUE = (123, 104, 238)
LAWNGREEN = (124, 252, 0)
CHARTREUSE = (127, 255, 0)
AQUAMARINE = (127, 255, 212)
MAROON = (128, 0, 0)
PURPLE = (128, 0, 128)
OLIVE = (128, 128, 0)
GRAY = (128, 128, 128)
SKYBLUE = (135, 206, 235)
LIGHTSKYBLUE = (135, 206, 250)
BLUEVIOLET = (138, 43, 226)
DARKRED = (139, 0, 0)
DARKMAGENTA = (139, 0, 139)
SADDLEBROWN = (139, 69, 19)
DARKSEAGREEN = (143, 188, 143)
LIGHTGREEN = (144, 238, 144)
MEDIUMPURPLE = (147, 112, 216)
DARKVIOLET = (148, 0, 211)
PALEGREEN = (152, 251, 152)
DARKORCHID = (153, 50, 204)
YELLOWGREEN = (154, 205, 50)
SIENNA = (160, 82, 45)
BROWN = (165, 42, 42)
DARKGRAY = (169, 169, 169)
LIGHTBLUE = (173, 216, 230)
GREENYELLOW = (173, 255, 47)
PALETURQUOISE = (175, 238, 238)
LIGHTSTEELBLUE = (176, 196, 222)
POWDERBLUE = (176, 224, 230)
FIREBRICK = (178, 34, 34)
DARKGOLDENROD = (184, 134, 11)
MEDIUMORCHID = (186, 85, 211)
ROSYBROWN = (188, 143, 143)
DARKKHAKI = (189, 183, 107)
SILVER = (192, 192, 192)
MEDIUMVIOLETRED = (199, 21, 133)
INDIANRED = (205, 92, 92)
PERU = (205, 133, 63)
CHOCOLATE = (210, 105, 30)
TAN = (210, 180, 140)
LIGHTGRAY = (211, 211, 211)
PALEVIOLETRED = (216, 112, 147)
THISTLE = (216, 191, 216)
ORCHID = (218, 112, 214)
GOLDENROD = (218, 165, 32)
CRIMSON = (220, 20, 60)
GAINSBORO = (220, 220, 220)
PLUM = (221, 160, 221)
BURLYWOOD = (222, 184, 135)
LIGHTCYAN = (224, 255, 255)
LAVENDER = (230, 230, 250)
DARKSALMON = (233, 150, 122)
VIOLET = (238, 130, 238)
PALEGOLDENROD = (238, 232, 170)
LIGHTCORAL = (240, 128, 128)
KHAKI = (240, 230, 140)
ALICEBLUE = (240, 248, 255)
HONEYDEW = (240, 255, 240)
AZURE = (240, 255, 255)
SANDYBROWN = (244, 164, 96)
WHEAT = (245, 222, 179)
BEIGE = (245, 245, 220)
WHITESMOKE = (245, 245, 245)
MINTCREAM = (245, 255, 250)
GHOSTWHITE = (248, 248, 255)
SALMON = (250, 128, 114)
ANTIQUEWHITE = (250, 235, 215)
LINEN = (250, 240, 230)
LIGHTGOLDENRODYELLOW = (250, 250, 210)
OLDLACE = (253, 245, 230)
RED = (255, 0, 0)
FUCHSIA = (255, 0, 255)
MAGENTA = (255, 0, 255)
DEEPPINK = (255, 20, 147)
ORANGERED = (255, 69, 0)
TOMATO = (255, 99, 71)
HOTPINK = (255, 105, 180)
CORAL = (255, 127, 80)
DARKORANGE = (255, 140, 0)
LIGHTSALMON = (255, 160, 122)
ORANGE = (255, 165, 0)
LIGHTPINK = (255, 182, 193)
PINK = (255, 192, 203)
GOLD = (255, 215, 0)
PEACHPUFF = (255, 218, 185)
NAVAJOWHITE = (255, 222, 173)
MOCCASIN = (255, 228, 181)
BISQUE = (255, 228, 196)
MISTYROSE = (255, 228, 225)
BLANCHEDALMOND = (255, 235, 205)
PAPAYAWHIP = (255, 239, 213)
LAVENDERBLUSH = (255, 240, 245)
SEASHELL = (255, 245, 238)
CORNSILK = (255, 248, 220)
LEMONCHIFFON = (255, 250, 205)
FLORALWHITE = (255, 250, 240)
SNOW = (255, 250, 250)
YELLOW = (255, 255, 0)
LIGHTYELLOW = (255, 255, 224)
IVORY = (255, 255, 240)
WHITE = (255, 255, 255)


class Colors:
    RES_X = 800
    RES_Y = 600
    FONTSIZE = 16
    BORDSIZE = 2
    colors_names: list  # По сути, имена всех глобальных констант модуля
    fontsurfs: List[pg.Surface]
    colsurfs: List[pg.Rect]
    max_fontsize_x: int
    max_fontsize_y: int

    def __init__(self):
        self.colors_names = [name for name in globals().keys() if name.isupper()]
        pg.init()

        self.font = pg.font.Font(None, self.FONTSIZE)

        self.mscr = pg.display.set_mode((self.RES_X, self.RES_Y))
        pg.display.set_caption('Примеры цветов модуля')
        self.fontsurfs, self.colsurfs = [], []
        self.max_fontsize_x, self.max_fontsize_y = self.__render_colnames()

    def __render_colnames(self) -> tuple:
        """ Рендерит названия цветов в список и возвращает максимальный необходимый размер в пикселях """
        maxx, maxy = 0, 0
        for colname in self.colors_names:
            bgcol = globals()[colname]
            curname = self.font.render(colname.capitalize(), True,
                                       self._get_opposite_color(bgcol), bgcol)
            curx, cury = curname.get_size()
            if maxx < curx: maxx = curx
            if maxy < cury: maxy = cury
            self.fontsurfs.append(curname)
        return maxx, maxy

    @staticmethod
    def _get_opposite_color(inp_tuple) -> tuple:
        res = tuple([255 - v for v in inp_tuple])
        return res

    def _render_colrects(self):
        for clr in self.colors_names:
            csurf = pg.Surface(self.max_fontsize_x + self.BORDSIZE * 2,
                               self.max_fontsize_y + self.BORDSIZE * 2).fill(globals()[clr])


    def _show_colors(self):
        curx, cury, lastx, lasty = 0, 0, 0, 0
        for sf in self.fontsurfs:
            if curx + lastx > self.RES_X:
                curx = 0
                cury = cury + self.FONTSIZE
            else:
                curx += lastx
            self.mscr.blit(sf, (curx, cury))
            lastx, lasty = sf.get_size()
            pg.display.update()

    def show_by_pygame(self):
        running = True
        self._show_colors()
        while running:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                    running = False
                    break


if __name__ == '__main__':
    clrs = Colors()
    clrs.show_by_pygame()