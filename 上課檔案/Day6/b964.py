n = input()
s = list(map(int, input().split()))
s.sort()
print(*s) # s= [1,2,3] print(*s) == print(1,2,3)
if s[0] >= 60:
    print('best case')
    print(s[0])
elif s[-1] < 60:
    print(s[-1])
    print('worst case')
else:
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])