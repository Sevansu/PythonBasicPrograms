class student:
    def __init__(self,m1,m2): #get
            self.m1=m1
            self.m2=m2
    def __add__(self,other): #set
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        s3=student(m1,m2)
        return s3

#Defining methods for operators is known as operator overloading.

s1=student(50,60)
s2=student(70,80)
s3=s1+s2
print(s1)
print(s2)
print(s3)

print(s1.m1)
print(s1.m2)
print(s3.m1)

print(s2.m1)
print(s2.m2)
print(s3.m2)
