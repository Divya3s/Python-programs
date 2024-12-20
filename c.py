""" for i in range(1,6):
    print(str(i) *5) """
    
    
""" for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print() """
    
    
""" for i in range(1,6):
    print(str(i)*i, end=" ")
    print() """
    
    
""" sum=0   
for i in range(1,6):
    for j in range(0,i):
        sum=sum+1
        print(sum, end=" ")
    print() """
    
    
for i in range(1, 6):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print() 