from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("Hii")
            sleep(1)
            
t1=hello()
t2=hi()

t1.start()
sleep(0.2)
t2.start()
print("Bye")
'''
Hello
Hii
Bye
Hello
Hii
Hello
Hii
Hello
Hii
Hello
Hii
'''
'''will print bye in 3rd line by default if you want to print bye \
in last line use t1.join() \n t2.join() before print("Bye") statement\
Hello
Hii
Hello
Hii
Hello
Hii
Hello
Hii
Hello
Hii
Bye
'''
