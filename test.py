class Student:
    school='JBK'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def display(self):
        sub='maths'
        print(self.name,self.roll,self.school,sub)
    
    @classmethod
    def classinfo(cls,x):
        print(f'class name is = {Student.school} + {x}')

   # @staticmethod
    #def classinfo(cls):
     #   print(f'class name is = {Student.school}')


s1 = Student('sajid',13)
s2= Student('tejas',15)

s1.classinfo(10)

#s1.display()
