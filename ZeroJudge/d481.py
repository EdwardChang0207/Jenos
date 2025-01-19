a, b, c, d = [int(i) for i in input().split()]
if b != c:
    print('Error')
else:
    A = [[int(j) for j in input().split()] for i in range(a)]
    B = [[int(j) for j in input().split()] for i in range(c)]
    C = []
    for i in range(a):
        row = []
        for k in range(d):
            t = []
            for j in range(b):
                t.append(A[i][j] * B[j][k])
            row.append(sum(t))
        C.append(row)

    for row in C:
        print(*row)