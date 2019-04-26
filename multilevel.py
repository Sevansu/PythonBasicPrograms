#base class
class person:
    def display(self):
        print("This is class person")

#derived class1
class employee(person):
    def printing(self):
        print("Derived class emoloyee")

#derived classa3
class programmer(employee):
    def show(self):
        print("Another derived class")

p1=programmer()
p1.display()
p1.printing()
p1.show()
