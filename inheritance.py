class animal:
    def eating(self):
        print("eating")

class dog(animal):
    def bark(self):
        print("barking")


d=dog()
d.eating()
d.bark()
