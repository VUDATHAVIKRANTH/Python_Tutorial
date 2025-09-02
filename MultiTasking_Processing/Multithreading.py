# from threading import *

# def new():
#     for i in range(3):
#         print("Executing...",current_thread())

# t1=Thread(target=new)
# t1.start()
# t1.join()
# print("Bye",current_thread())

# =====================================================

# By Extending Thread class
    
    
# from threading import *

# class newthread(Thread):
#     def run(self):
#         for i in range(3):
#             print("Thread Class")

# nt1=newthread()
# nt1.start()
# nt1.join()
# print("Main Thread")


# =======================================

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(50):
            print("Hello")
            sleep(1)
            

class Hi(Thread):
    def run(self):
        for i in range(50):
            print("Hi")
            sleep(1)

t1=Hello()
t2=Hi()

t1.start()
t2.start()
t1.join()
t2.join()
print("Bye")