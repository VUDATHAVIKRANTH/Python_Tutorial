# # Sharing memoru nrwn processes
# from multiprocessing import *
# #import multiprocessing
# def square(arr,result,v):
#     v.value=5.67
#     for idx,n in enumerate(arr):
#         result[idx]=n*n

# if __name__=="__main__":
#     arr=[2,3,4]
#     result=Array('i',3)
#     # result=multiprocessing.Array('datatype',size of array)
#     v=Value('d',0.4)
#     # v=multiprocessing.Value('datatype',value)
#     p1=Process(target=square,args=(arr,result,v))
#     # p1= multiprocessing.Process(target=square,args=(arr,result,v))


#     p1.start()
#     p1.join()

#     print("process finished",result[:])
#     print("value updated",v.value)


# ====================================================================
# Multi processing using queue

from multiprocessing import *

def square(arr,q):
    for n in arr:
        q.put(n*n)


if __name__=="__main__":
    arr=[2,3,4]
    q=Queue()
    p1=Process(target=square, args=(arr,q))
    p1.start()
    p1.join()

    while q.empty() is False:
        #print(q.empty())
        print(q.get())
