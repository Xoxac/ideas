draw = 0                                        # счетчик для ничьей

pole = [['□']*3 for j in range(3)]              # создаем пустое поле 3х3


pole.insert(0, [1, 2, 3])        # добавляем координаты по оси х


c = 0                                           # счетчик координат
for row in pole:                                # цикл добавляет цифру-координату по оси у
    row.insert(0, c)
    c += 1
pole[0][0] = ' '                                # удаляем ненужный ноль с поля


def print_pole(pole):                           # функция для вывода игрового поля
    for i in pole:
        for j in i:
            print(j, end=' ')
        print()



def insert_x(pole, x, y):                       # функция для ввода крестика
    try:
        if pole[y][x]!='x' and pole[y][x]!='○' and x!=0 and y!=0:
            pole[y][x] = 'x'
        else:
            print('Эта клетка недоступна!')
        print_pole(pole)
    except IndexError:
        print('Вы ввели неверные координаты!')
    except:
        print("Неизвестная ошибка, поправим в следующих патчах...")

def insert_y(pole, x, y):                       # функция для ввода нолика
    try:
        if pole[y][x]!='x' and pole[y][x]!='○' and x!=0 and y!=0:
            pole[y][x] = '○'
        else:
            print('Эта клетка недоступна!')
        print_pole(pole)
    except IndexError:
        print('Вы ввели неверные координаты!')
    except:
        print("Неизвестная ошибка, поправим в следующих патчах...")


print('''ПРАВИЛА:
1. Игроки поочередно ставят крестики и нолики, указав координаты нужной клетки.
2. Выигрывает тот, кто поставит три своих символа первым по горизонтали, вертикали или диагонали.
3. Если игрок жульничает и пытается поставить нолик или крестик в уже занятую клетку, либо не цифру,
либо по координатам, выходящим за пределы поля - ход переходит к другому игроку.
''')


print_pole(pole)                                # выводим начальное игровое поле


while True:                                     # игровой цикл. Условия победы проверяются
                                                # после каждого хода, чтобы не пришлось ходить
                                                # игроку 2, если игрок 1 уже выиграл.

    print('игрок 1, поставьте крестик, указав координату X и Y')
    try:
        insert_x(pole, int(input('Введите координату X: ')), int(input('Введите координату Y: ')))
    except ValueError:
        print('Вы должны вводить цифру!')

    draw = 0
    for i in pole:                              # условие для ничьей
        for j in i:
            if j in ("x", "○"):
                draw += 1

    if pole[1][1]=='x' and pole[1][2] == 'x' and pole[1][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[2][1]=='x' and pole[2][2] == 'x' and pole[2][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[3][1]=='x' and pole[3][2] == 'x' and pole[3][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][1]=='x' and pole[2][1] == 'x' and pole[3][1] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][2]=='x' and pole[2][2] == 'x' and pole[3][2] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][3]=='x' and pole[2][3] == 'x' and pole[3][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][1]=='x' and pole[2][2] == 'x' and pole[3][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[3][1]=='x' and pole[2][2] == 'x' and pole[1][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][1]=='○' and pole[1][2] == '○' and pole[1][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[2][1] == '○' and pole[2][2] == '○' and pole[2][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[3][1] == '○' and pole[3][2] == '○' and pole[3][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][1] == '○' and pole[2][1] == '○' and pole[3][1] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][2] == '○' and pole[2][2] == '○' and pole[3][2] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][3] == '○' and pole[2][3] == '○' and pole[3][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][1] == '○' and pole[2][2] == '○' and pole[3][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[3][1] == '○' and pole[2][2] == '○' and pole[1][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif draw == 9:
        print('Ничья!')
        break



    print('игрок 2, поставьте нолик, указав координату X и Y')
    try:
        insert_y(pole, int(input('Введите координату X: ')), int(input('Введите координату Y: ')))
    except ValueError:
        print('Вы должны вводить цифру!')

    draw = 0
    for i in pole:                                # условие для ничьей
        for j in i:
            if j in ("x", "○"):
                draw += 1

    if pole[1][1]=='x' and pole[1][2] == 'x' and pole[1][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[2][1]=='x' and pole[2][2] == 'x' and pole[2][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[3][1]=='x' and pole[3][2] == 'x' and pole[3][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][1]=='x' and pole[2][1] == 'x' and pole[3][1] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][2]=='x' and pole[2][2] == 'x' and pole[3][2] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][3]=='x' and pole[2][3] == 'x' and pole[3][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][1]=='x' and pole[2][2] == 'x' and pole[3][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[3][1]=='x' and pole[2][2] == 'x' and pole[1][3] == 'x':
        print('🏆 Игрок 1 победил! 🏆')
        break
    elif pole[1][1]=='○' and pole[1][2] == '○' and pole[1][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[2][1] == '○' and pole[2][2] == '○' and pole[2][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[3][1] == '○' and pole[3][2] == '○' and pole[3][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][1] == '○' and pole[2][1] == '○' and pole[3][1] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][2] == '○' and pole[2][2] == '○' and pole[3][2] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][3] == '○' and pole[2][3] == '○' and pole[3][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[1][1] == '○' and pole[2][2] == '○' and pole[3][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif pole[3][1] == '○' and pole[2][2] == '○' and pole[1][3] == '○':
        print('🏆 Игрок 2 победил! 🏆')
        break
    elif draw == 9:
        print('Ничья!')
        break
