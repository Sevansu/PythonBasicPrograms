class person:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Hello",self.name)

'''self is used to differentiate
between local and instance variable'''
#self refers to object

#1st way
p1=person("Sevansu")
p1.display()

#2nd way
person("Salu").display()

#3rd way
p2=person("STAN171018")
person.display(p2)
