num =[3,4,5,6,7]

iter_num = iter(num)
i = 1
while i>0:
    try:
        print(next(iter_num))

    except StopIteration:
        break

# for i in iter_num:
#     print(i)