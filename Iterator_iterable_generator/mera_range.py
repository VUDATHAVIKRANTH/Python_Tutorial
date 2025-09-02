class mera_range_iterable():
    def __init__(self,start=0,end=6):
        self.start=start
        self.end=end

    def __iter__(self):
        return mera_range_iterator(self)
    

class mera_range_iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj=iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterable_obj.start>= self.iterable_obj.end:
            raise StopIteration
        else:
            current =self.iterable_obj.start
            self.iterable_obj.start+=1
            return current
        

for i in mera_range_iterable(5):
    print(i)

