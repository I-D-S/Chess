import tkinter as tk
from tkinter import Label

print('x — номер вертикали (при счете слева направо), y — номер горизонтали (при счете снизу вверх)\
x и y должны быть в отрезке [1; 8]\nВведите координаты первой клетки')

while True:
    try:
        x0 = int(input('Введите x0  '))
        assert 1 <= x0 <= 8
        break
    except AssertionError:
        print('Координата не в [1; 8]')
    except ValueError:
        print('Ошибка в значении')

while True:
    try:
        y0 = int(input('Введите y0  '))
        assert 1 <= y0 <= 8
        break
    except AssertionError:
        print('Координата не в [1; 8]')
    except ValueError:
        print('Ошибка в значении')

print('Введите координаты второй клетки')

while True:
    try:
        x1 = int(input('Введите x1  '))
        assert 1 <= x1 <= 8
        break
    except AssertionError:
        print('Координата не в [1; 8]')
    except ValueError:
        print('Ошибка в значении')

while True:
    try:
        y1 = int(input('Введите y1  '))
        assert 1 <= y1 <= 8
        assert y0 != y1 or x0 != x1
        break
    except AssertionError:
        print('Координата не в [1; 8] или вы ввели одинаковые клетки')
    except ValueError:
        print('Ошибка в значении')

def color_check(x0, y0, x1, y1):
    if (x0 + y0) % 2 == (x1 + y1) % 2:
        return True
    else:
        return False


def knight_check(x0, y0, x1, y1):
    if (x1 - x0) ** 2 + (y1 - y0) ** 2 == 5:
        return True
    else:
        return False


def rook_check(x0, y0, x1, y1):
    if x0 == x1 or y0 == y1:
        return True
    else:
        return False


def bishop_check(x0, y0, x1, y1):
    if (x1 - x0) ** 2 == (y1 - y0) ** 2:
        return True
    else:
        return False


def queen_check(x0, y0, x1, y1):
    if rook_check(x0, y0, x1, y1) or bishop_check(x0, y0, x1, y1):
        return True
    else:
        return False


if color_check(x0, y0, x1, y1):
    print('Клетки одного цвета')
else:
    print('Клетки разного цвета')

# Рисуем доску
figure = ''


def draw_desk(x0, y0, x1, y1):
    print('Откройте окно')
    BRD_ROWS = BRD_COLS = 8
    CELL_SZ = 50

    root = tk.Tk()
    root.title('Закройте окно для продолжения')
    Label(text="начальная клетка - желтый, конечная клетка - зелёный, красный - промежуточное значение", width=100,
          height=5) \
        .pack()
    canvas = tk.Canvas(root, width=CELL_SZ * BRD_ROWS, height=CELL_SZ * BRD_COLS)

    cell_colors = ['white', 'black']
    ci = 0  # цветовой индекс

    # Рисует пустую доску
    def draw_empty_desk():
        if row == 8 - y0 and col == x0 - 1:
            canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='yellow')
        elif row == 8 - y1 and col == x1 - 1:
            canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='green')
        else:
            canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill=cell_colors[ci])

    for row in range(BRD_ROWS):
        for col in range(BRD_COLS):
            x_0, y_0 = col * CELL_SZ, row * CELL_SZ
            x_1, y_1 = col * CELL_SZ + CELL_SZ, row * CELL_SZ + CELL_SZ

            if figure == 'ферзь' or figure == 'ладья':
                if row == 8 - y0 and col == x1 - 1:
                    canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='red')
                else:
                    draw_empty_desk()
            elif figure == 'слон':
                if bishop_check(x0, y0, 8-row, col+1) and bishop_check(x1, y1, 8-row, col+1):
                    canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='red')
                else:
                    draw_empty_desk()
            else:
                draw_empty_desk()

            ci = not ci

        ci = not ci

    canvas.pack()

    root.mainloop()


draw_desk(x0, y0, x1, y1)

while True:
    a = 1
    print('True - ход возможен False - ход невозможен ')
    figure = input('Введите название фигуры: ферзь/ладья/слон/конь  ')
    if figure == 'ферзь':
        if queen_check(x0, y0, x1, y1):
            print('ход возможен')
        else:
            print('ход невозможен')
            print('Реализация за два хода')
            draw_desk(x0, y0, x1, y1)
    elif figure == 'ладья':
        if rook_check(x0, y0, x1, y1):
            print('ход возможен')
        else:
            print('ход невозможен')
            print('Реализация за два хода')
            draw_desk(x0, y0, x1, y1)
    elif figure == 'слон':
        if bishop_check(x0, y0, x1, y1):
            print('ход возможен')
        elif color_check(x0, y0, x1, y1):
            print('ход невозможен')
            print('Реализация за два хода')
            draw_desk(x0, y0, x1, y1)

    elif figure == 'конь':
        if knight_check(x0, y0, x1, y1):
            print('ход возможен')
        else:
            print('ход невозможен')
    else:
        a = 0
        print('Неверная фигура')
    if a:
        break
