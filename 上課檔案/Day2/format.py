import random as r
import math

for i in range(20):
    x = r.randint(0,100)
    # print('I am %3d years old' % x)
    # print('I am {:3d} years old'.format(x))
    # print(f'I am {x:3d} years old')

    x = math.sin(x)
    print('%6.3f' % x)
    print('{:6.3f}'.format(x))
    print(f'{x:6.3f}')

