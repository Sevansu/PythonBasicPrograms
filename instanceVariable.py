class student:
    clg="LDRP" #class variable

    def __init__(self,r,n):
        self.rollno=r
        self.name=n

    def display(self):
        print("Student name:",self.name)
        print("Student rollnumber:",self.rollno)
        print("College:",student.clg)


s1=student("1519BEIT30053","Sevansu")
s1.display()

s2=student("1519BEIT30003","Aniket")
s2.display()
        
