# DB = [
#     ['mary', 20, 30000],
#     ['alan', 30, 100000],
#     ['kevin', 25, 40000]
# ]
# for i in DB:
#     if i[0] == 'alan'

cur_year = 2025
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.year = cur_year-self.age
        self.permission = 'User'
    def sayHi1(self):
        print(f'hi, my name is {self.name}')
    def sayHi2(self):
        print(f'hi, my name is {self.name}')

a = Person('mary', 20, 3000)
age = 30
a.age = 30
print(a.age)