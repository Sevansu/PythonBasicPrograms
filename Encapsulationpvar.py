class car:
    __maxspeed=0
    __name=''
    def __init__(self):
        self.__maxspeed=200
        self.__name='supercar'
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    """def setspeed(self,speed):
        self.__maxspeed=speed
        print(self.__maxspeed)"""

c=car()
c.drive()
c.__maxspeed=100
c.drive()
