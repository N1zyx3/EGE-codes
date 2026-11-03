# Вариант 1 (единичные строки)
print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # тут пишем функцию из задания
                f = ((x * (not(y)) + (x == z)) + w)
                if not f:
                    print(w, x, y, z)

# Вариант 2 (нулевые строки)
print("x y z w")
from itertools import *
for x, y, z, w in product([0, 1], repeat = 4):
    # тут пишем функцию из задания
    f = (y <= x) and (not z) and w
    if f:
        print(x, y, z, w)