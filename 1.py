from itertools import *

a = 'AB BC CD DA'.split() # Связи
s = '123 2356 234262525'.split # Растояние между точками по порядку первой переменной
for p in permutations('ABCDEF'):
    if all(str(p.index(x)+1) in s[p.index(y)] for x,y in a):
        print(*p)