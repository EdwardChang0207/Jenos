# import random
# from random import random, randint
#. -> 1.的 2.對...做...
import random as r
ans = r.randint(1,100)
game = True
lower, upper = 0, 100
while game:
    print(lower, '~', upper)
    guess = int(input())
    if guess < lower or guess > upper:
        continue
    if guess == ans:
        print("Correct")
        break
    
    elif guess > ans:
        upper = guess
        print('Too big')

    else: #guess < ans:
        lower = guess
        print('Too small')