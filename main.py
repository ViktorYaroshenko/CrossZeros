pole = [[' ', 1, 2, 3], [1, '-', '-', '-'], [2, '-', '-', '-'], [3, '-', '-', '-']]
import time
import random
def output(pole):
    "Функция делает вывод поля"
    for string in pole:
        print(*string)
def magic(pole):
    global cross
    global zeros
    "Функция проверяет, есть выигрыш какой-либо стороны, либо продолжает игру"
    for i in range(4):
        for j in range(4):
            #Проверяем на победу крестиков
            if pole[1][1] == 'x' and pole[2][1] == 'x' and pole[3][1] == 'x':
                cross = True
            elif pole[1][2] == 'x' and pole[2][2] == 'x' and pole[3][2] == 'x':
                cross = True
            elif pole[1][3] == 'x' and pole[2][3] == 'x' and pole[3][3] == 'x':
                cross = True
            elif pole[1][1] == 'x' and pole[1][2] == 'x' and pole[1][3] == 'x':
                cross = True
            elif pole[2][1] == 'x' and pole[2][2] == 'x' and pole[2][3] == 'x':
                cross = True
            elif pole[3][1] == 'x' and pole[3][2] == 'x' and pole[3][3] == 'x':
                cross = True
            elif pole[1][1] == 'x' and pole[2][2] == 'x' and pole[3][3] == 'x':
                cross = True
            elif pole[1][3] == 'x' and pole[2][2] == 'x' and pole[3][1] == 'x':
                cross = True
            #Проверяем на победу ноликов

            if pole[1][1] == 'o' and pole[2][1] == 'o' and pole[3][1] == 'o':
                zeros = True
            elif pole[1][2] == 'o' and pole[2][2] == 'o' and pole[3][2] == 'o':
                zeros = True
            elif pole[1][3] == 'o' and pole[2][3] == 'o' and pole[3][3] == 'o':
                zeros = True
            elif pole[1][1] == 'o' and pole[1][2] == 'o' and pole[1][3] == 'o':
                zeros = True
            elif pole[2][1] == 'o' and pole[2][2] == 'o' and pole[2][3] == 'o':
                zeros = True
            elif pole[3][1] == 'o' and pole[3][2] == 'o' and pole[3][3] == 'o':
                zeros = True
            elif pole[1][1] == 'o' and pole[2][2] == 'o' and pole[3][3] == 'o':
                zeros = True
            elif pole[1][3] == 'o' and pole[2][2] == 'o' and pole[3][1] == 'o':
                zeros = True

cross = False
zeros = False
spisok = [1,2,3]
print("Игра КРЕСТИКИ-НОЛИКИ")
time.sleep(1)
output(pole)
time.sleep(1)
print('Вы играете за крестики, а компьютер за нолики.')
time.sleep(1)
while True:
    #блок 1, ввод крестиков
    while True:
        x = input('Введите координату X (по горизонтали от 1 до 3): ')
        y = input('Введите координату Y (по вертикали от 1 до 3): ')
        if x.isdigit() and y.isdigit() and x and y:
            x = int(x)
            y = int(y)
            if 0 < x < 4 and 0 < y < 4:
                if pole[x][y] == '-':
                    pole[x][y] = 'x'
                    print()
                    print("Это был Ваш ход:")
                    output(pole)
                    break
                else:
                    print("Данное поле уже занято, введите данные снова!")
            else:
                print('Введен некорректный символ, повторите, нужно ввести цифру от 1 до 3')
        else:
            print("Введите одну арабскую цифру: 1, 2 или 3")
    # проверка выигрыша
    magic(pole)
    #блок 2, ввод ноликов компьютером
    if cross:
        print()
        print('Вы победили!')
        break
    if '-' not in pole[1] and '-' not in pole[2] and '-' not in pole[3]:
        print()
        print('Пока победила дружба, но в будущем победит ChatGPT')
        break
    while True:
        x_n = random.choice(spisok)
        y_n = random.choice(spisok)
        if pole[x_n][y_n] == '-':
            pole[x_n][y_n] = 'o'
            print()
            print("Это был ход компьютера:")
            output(pole)
            break
    #блок 3, проверка, не победил ли кто-нибудь
    magic(pole)

    if cross:
        print('Вы победили!')
        break
    elif zeros:
        print('Пффф лузер, иди качай IQ')
        break

    if '-' not in pole[1] and '-' not in pole[2] and '-' not in pole[3]:
        print('Пока победила дружба, но в будущем победит ChatGPT')
        break