# a big task divide into a small parts this small part is called thread
#Threading in python is used to run multiple threads (tasks, function calls) at the same time. Note that this does not mean that they are executed on different CPUs.
# Python threads will NOT make your program faster if it already uses 100 % CPU time.
# when two process are running at the same time there is also a chance of collision

from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


a1=Hello()

a2=Hi()
a1.start()
sleep(0.5)
a2.start()
# sleep save the process from collision and given the time to the process in a (seconds)

#a1.run()
#a2.run()
a1.join() # join is used to run the function when all the process of main function was done
a2.join()
print("bye")

