# def 開啟手機(phone_password):
# def 輸入電話號碼(phone_number):
# def 按下通話():

# def main(phone_number, phone_password): #打電話
#     開啟手機(phone_password)
#     輸入電話號碼(phone_number)
#     按下通話()
#     return 講電話

# main()
#(define)
# def function_name(parameter):
#     ...
#     return output

# def plus(n1,n2):
#     ans = n1 + n2
#     return ans

# def main():
#     n1 = int(input('pls enter n1'))
#     n2 = int(input('pls enter n2'))
#     result = plus(n1, n2)
#     print(result)

# main()

def transfer(a,b,A):
    AT = [[A[j][i] for j in range(a)] for i in range(b)]
    return AT

def main(A):
    a = len(A)
    b = len(A[0])
    AT = transfer(a,b,A)
    print(AT)

A = [
    [1, 2, 3],
    [4, 5, 6]
]
main(A)