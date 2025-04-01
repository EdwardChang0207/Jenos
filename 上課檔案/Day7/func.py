a, b = 10, 20
def f1(a, b):
    return a+b

def f2(a, b):
    a = a+b
    return a

class A:
    a=10
    def __init__():
        pass

def main():
    global a, b
    a = f1(a,b) #a=30
    b = a + f2(a,b) # a + f2(30, 20) -> 30 + 50 =80
    print(a,b)

main()