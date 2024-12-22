rows = int(input())          
for i in range(rows):        
    n = input()           
    b = [int(j) for j in n.split()]  
    if (b[1]-b[0]) == (b[3]-b[2]):
        print(*b, b[3]+b[3]-b[2])
    else:
        print(*b, b[3]*int(b[3]/b[2]))