print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x) == 1:
                print(x, y, z, 1)
            else:
                print(x, y, z, 0)

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x * (not(y) + (x == z))) + w:
                    print(w, x, y, z, 1)

# Продвинутый вариант
print('x y z w')
from itertools import *
for x, y, z, w in product([0, 1], repeat = 4):
    if (y <= x) and (not z) and w:
        print(x, y, z, w)