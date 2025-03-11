n = int(input())
n = list(map(int, input().split()))
total = 0
for x in range(len(n)):
    if int(n[x]) == 0:
        if x == 0:
            total += n[x+1]
        elif x == len(n)-1:
            total += n[x-1]
        else:
            total += min(n[x-1],n[x+1])
print(total)