from multiprocessing import *
from time import sleep
square_result=[]
def square(arr):
        global square_result
        for i in arr:
            print("square=",i*i)
            sleep(0.2)
            square_result.append(i*i)
        print("with in function result=",square_result)
        print("square processing completed")

def cube(arr):
        for i in arr:
            print("cube=",i*i*i)
            sleep(0.2)
        print("cube processing completed")

if __name__=="__main__":    
    arr=[2,3,4,5]
    
    p1=Process(target=square,args=(arr,))
    p2=Process(target=cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("result=",square_result)

