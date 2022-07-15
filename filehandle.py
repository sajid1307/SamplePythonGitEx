a = 10
b = 'sajid'
c = True
d = 10+20j

try:
    print(a*b)
except:
    print(a+b)
else:
    print('else')
finally:
    print('finally')


class Small(Exception):
    def __init__(self,msg):
        self.msg=msg

class Big(Exception):
    def __init__(self,msg):
        self.msg = msg

age = int(input("Enter your age : "))

if age>50:
    raise Big("You are too old to play game...")

elif age<18:
    raise Small("You are too small to play game..")

else :
    print("welcome to the game world..")

