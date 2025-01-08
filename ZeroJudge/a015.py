a, b = [int(i) for i in input().split()] #[2,3]
A = [[int(j) for j in input().split()] for i in range(a)]
AT = [print(*[A[j][i] for j in range(a)]) for i in range(b)]

# for i in range(b):#抓b個行
#     col = [] #抓到A的一個行
#     for j in range(a):
#         col.append(A[j][i])
#     AT.append(col) #放入AT當一個列

# [print(*k) for k in AT]