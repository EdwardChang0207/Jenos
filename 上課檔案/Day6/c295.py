N, M = map(int, input().split())
l = []
for i in range(N):
    l.append(max(map(int, input().split())))
S = sum(l)
l = [i for i in l if S % i == 0]
print(S)
if l:
    print(*l)
else:
    print(-1)