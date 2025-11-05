Decorators in python are first class citizen 


```
def newfunc(func):
    def wrapper(*args,**kwargs):
        print("In side wrapper before function call")
        result=func(*args,**kwargs)
        print("Inside wrapper after function call")
        return result
    return wrapper

@newfunc       
def oldfunc(a:int, b: int):
    print("Inside oldfunc")
    return a+b
    
#if no decorator is used
#print(newfunc(oldfunc(2,3)))

print(oldfunc(2,3))
```
