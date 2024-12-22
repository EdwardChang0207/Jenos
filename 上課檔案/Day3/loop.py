#while
# while 條件:
#     要做的事
# while 1 < 2:
#     print(123)

#while loop 輸出1-10
# i = 1
# while i < 11: #有條件的迴圈 -> 不知道做幾次
#     print(i, end='')
#     i += 1
#for 計次的回圈 -> 知道做幾次 -> 給範圍
#1.range(start, end, interval) start -> end-1, add interval for each time
# range(a) -> 0~(a-1), start=0(init), end=a, interval=1(init)
# range(a,b) -> a~(b-1), start=a, end=b, interval=1(init)
# range(a,b,c) -> a~(b-1), add c each for time, start=a, end=b, interval=c

# for i in range(10, 0, -1):
#     print(i)

# l = ['鮭魚','鮪魚','旗魚']
# for i in l:
#     print(i)

s = 'hello' #-> ['h','e','l','l','o']
for i in s:
    print(i)

#continue, break