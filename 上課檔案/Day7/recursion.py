# def a(b):
#     if b > 0:
#         return a(b-1) + b
#     return 0

# print(a(8))

#counting numbers
# def f(i):
#     if i > 3: return
#     print(i)
#     return f(i+1)

# f(0)

#等差數列
a1 = 1
d = 2
n = 5
result = 0
for i in range(n):
    result += a1 + d*i
print(result)

def f(a1, d, n):
    if n == 0: return 0
    return f(a1, d, n-1) + a1+d*(n-1)

print(f(a1=1, d=2, n=5))

# 等比級數
a1 = 2
r = 2
n = 5
result = 0

for i in range(n):
    result += a1*r**i
print(result)

def f(a1, r, n):
    if n == 0: return 0
    return a1*r**(n-1) + f(a1, r, n-1)

print(f(a1, r, n))