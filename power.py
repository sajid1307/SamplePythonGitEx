#calculate the power of given number 

n = eval(input('Enter the number : '))
p = eval(input('Enter the power : '))


def calpow(n,p):
    pow = 1
    for i in range(0,p):
        pow = pow * n
        i=i+1
    return pow

print(f'The {p}th power of {n} is : ',calpow(n,p))