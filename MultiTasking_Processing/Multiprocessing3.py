from multiprocessing import *
from time import sleep
def deposit(balance,lock):

    for i in range(5):
        sleep(0.01)
        lock.acquire()
        balance.value=balance.value+1
        lock.release()
        print("in deposit",balance.value)


def withdrawal(balance,lock):

    for i in range(3):
        sleep(0.01)
        lock.acquire()
        balance.value=balance.value-1
        lock.release()
        print("in withdrawal",balance.value)






if __name__=="__main__":
    balance=Value('i',200)
    lock=Lock()
    p1=Process(target=deposit,args=(balance,lock))
    p2=Process(target=withdrawal,args=(balance,lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("process completed",balance.value)
