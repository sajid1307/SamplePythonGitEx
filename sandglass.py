n = int(input('Enter the number of *s : '))

for i in range(0,n) :   
    for j in range(0,i):
        print(' ',end='')
    for k in range(i,n):
        print('*',end=' ')
    print()

for i in range(2,n+1):
    for j in range(n,i,-1):
        print('',end=' ')
    for k in range(i,0,-1):
        print("*",end=' ')
    print()


    
