class student:
    school='rageunseen'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3


    def avg(self): #instance method 1)accessor2)mutator
        return(self.m1+self.m2+self.m3)/3

    
    @classmethod #decorators
    def getschool(cls): #class method 
        return cls.school

    @staticmethod #decorators
    def info(): #static method
        print("This is student class")
    
    
s1=student(34,47,32)
s2=student(89,32,12)

print(s1.avg())
print(student.getschool())

student.info()
