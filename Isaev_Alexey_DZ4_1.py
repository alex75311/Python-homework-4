'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета
для конкретных значений необходимо запускать скрипт с параметрами.
'''


from sys import argv


def zp(argv):
    if len(argv) != 4:
        return print(f'Введены некорректные аргументы')
    script_name, hour, rate, prize = argv
    try:
        hour = int(hour)
        rate = int(rate)
        prize = int(prize)
    except ValueError:
        return print('Введите целые числа')
    return print(f'Заработная плата составила {hour * rate + prize}')


zp(argv)
