def my_generator():
    for i in range(5):
        yield i 
gen = my_generator()
print(next(gen))

# def fun(max):
#     cnt = 1
#     while cnt <= max:
#         yield cnt
#         cnt += 1 
# ctr = fun(50)
# for n in ctr:
#     print(n)

# Generator Expression
sq = (x * x for x in range(1,6))
for i in sq:
    print(i)