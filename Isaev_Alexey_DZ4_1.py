from sys import argv


def zp(argv):
    script_name, hour, rate, prize = argv
    hour = int(hour)
    rate = int(rate)
    prize = int(prize)
    return print(f'Заработная плата составила {hour * rate + prize}')


zp(argv)
