print('x y z w')
from itertools import *
for x, y, z, w in product([0, 1], repeat = 4):
    if (y <= x) and (not z) and w:
        print(x, y, z, w, 1)
    else:
        print(x, y, z, w, 0)

# Продвинутый вариант
