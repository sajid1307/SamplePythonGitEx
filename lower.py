#Program to convert lowercase vowel to Uppercase in a string

s = input('enter the string : ')


def upper(s):
    str = ''
    for i in range(0,len(s)):
       
        if s[i] in ('a','e','i','o','u'):
            u = s[i].upper()
            str = str + u
        else :
            str = str + s[i]
    return str

print(upper(s))
