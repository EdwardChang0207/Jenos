age = 18
print('I am '+str(age)+' years old')
print('I am', age, 'years old')

cars = 2
#%
print('I am %d years old, I have %d cars' % (age, cars))
'''
%d -> int
%f -> float
%s -> str
'''
#format
print('I am {0:f} year old, I have {0:f} cars'.format(age, cars))# . -> 1.的 2.對...做... format:格式化

#f-string
print(f'I am {age+2} years old, I have {cars-1} cars')

