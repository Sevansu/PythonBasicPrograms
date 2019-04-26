class car:
    def __init__(self):
        self.__updatesoftware()
    def drive(self):
        print("Driving")
    def __updatesoftware(self):
        print("Updating Software")

blackcar=car()
blackcar.drive()
#Uncomment this to see the error
#blackcar.__updatesftware()
