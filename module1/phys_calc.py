import math


def find_freq(m1: float, m2: float, L: float, R: float) -> float:
    P = (m1 + m2) * 9.81
    print(f"Суммарный вес = {P} Н")

    a = (m1 * (L / 2) + m2 * (L + R)) / (m1 + m2)
    print(f"Координаты центра тяжести = {a} м")

    J = (m1 * L * L / 3) + (m2 * R * R / 2) + m2 * (R+L) * (R+L)
    print(f"Момент инерции относительно оси подвеса = {J} кг*м^2")

    freq = (1 / (2 * 9.81 * math.sqrt(J / (P * a))))
    print(f"Частота  = {freq} Гц")

    return freq
