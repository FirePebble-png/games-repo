import random

a = str(random.randint(1000, 9999))
cow = 0
bull = 0
while bull != 4:
    bull = 0
    cow = 0
    t = ''
    while len(t) != 4:
        print()
        t = input('Введите число:')
        if len(t) != 4:
            print('Ошибка ввода\nПовторите ввод')
    for i in range(0, len(a)):
        if t[i] == a[i]:
            bull += 1
        elif (t[i] == a[i - 1]) or (t[i] == a[i - 2]) or (t[i] == a[i - 3]):
            cow += 1

    print(f'Кол-во быков: {bull}')
    print(f'Кол-во коров: {cow}')
print('Игра завершена, Вы победили!')
