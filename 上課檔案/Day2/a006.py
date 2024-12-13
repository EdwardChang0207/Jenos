#a, b, c = [int(i) for i in input().split()] #['1', '3', '-10']
a, b, c = map(int, input().split())
#1. 判別
D = b**2 - 4*a*c

# #2. 求平方根
if D < 0:
    print('No real root')
else:
    root1 = int((-b + D**.5) /(2*a))
    root2 = int((-b - D**.5) /(2*a))

    if D > 0 :
        print('Two different roots x1={0:d} , x2={1:d}'.format(root1,root2))
    elif D == 0:
        print('Two same roots x={0:d}'.format(root1))