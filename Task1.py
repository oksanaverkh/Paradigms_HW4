# Ваша задача
# Написать скрипт для расчета корреляции Пирсона между двумя случайными величинами (двумя массивами).
# Можете использовать любую парадигму, но рекомендую использовать функциональную,
# т.к. в этом примере она значительно упростит вам жизнь.

from math import sqrt, pow
import random


def correlationPirson(arr1, arr2):

    # Вычисляем для каждого элемента отклонения от среднего арифметического для arr1 и arr2
    arr_diff_x = list(map(lambda x: sum(arr1)/(len(arr1)+1)-x, arr1))
    arr_diff_y = list(map(lambda y: sum(arr2)/(len(arr2)+1)-y, arr2))

    # Рассчитываем сумму квадратов всех отклонений
    sum_diff_x = sum(map(lambda x: pow(x, 2), arr_diff_x))
    sum_diff_y = sum(map(lambda y: pow(y, 2), arr_diff_y))

    # Рассчитываем для каждого элемента произведение разности среднего арифметического и значения
    sum_diff_x_y = sum(map(lambda x, y: x * y, arr_diff_x, arr_diff_y))

    # Подставляем полученные значения в формулу коэффициента корреляции Пирсона
    return round(sum_diff_x_y/sqrt(sum_diff_x * sum_diff_y), 3)


def main():
    array_x, array_y = [], []
    for i in range(7):
        array_x.append(random.randint(-100, 100))
        array_y.append(random.randint(-100, 100))
    print(array_x, array_y, sep="\n")
    print(f'\nCorrelation coefficient = {correlationPirson(array_x, array_y)}')


if __name__ == "__main__":
    main()
