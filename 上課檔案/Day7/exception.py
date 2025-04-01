try: #可能會出錯的區塊
	x = input('請輸入整數')
	print( int(x) + 1 )
except IOError as e: #如果出錯的處理的方式
	print('錯誤！輸入的不是整數!', e)
except ValueError as e:
	print(e)
else:
	print('hello')
finally:
	print('hi')



# x = input('請輸入整數')
# print( int(x) + 1 )
# print(a)
# l = [1,2]
# for i in range(len(l)+1):
#     print(l[i])

# print('a'-1)
# print(int('3.1'))
# while True:
#     print(1)

# d = {'1':10}
# print(d['2'])
# 
# print(10/0) 

# class A:
#     def __init__(self):
#         self.b = 10

# a = A()
# print(a.c)

# if 1 == 1:
# print('az')

# a = 1
# a = 2