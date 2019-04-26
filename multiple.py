class land_animal:
    def lp(self):
        print("This animal lives on land")

class water_animal:
    def wp(self):
        print("This animal lives in water")

class frog(land_animal,water_animal):
    pass

f1=frog()
f1.lp()
f1.wp()
