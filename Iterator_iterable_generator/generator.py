# def mera_range(start,end):
#     for i in range(start,end):
#         yield i
# gen=mera_range(1,3)
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for i in gen:
#     print(i)


# def nums():
#     yield 10
#     yield 11
#     yield 12

# gen=nums()

# print(next(gen))
# print(next(gen))
# print(next(gen))

# generator expression

gen =( i**2 for i in range(1,6))

for i in gen:
    print(i)


