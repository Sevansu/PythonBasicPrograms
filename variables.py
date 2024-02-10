class car:
    wheels=4 #class variable

    def __init__(self):
        self.mil=10     #instance variable we can change
        self.com="BMW"

c1=car()
c2=car()

c1.mil=8 #instance variable we can chnage by object

car.wheels=6 #class variable changed by class name

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)

'''
BMW 8 6
BMW 10 6
'''
