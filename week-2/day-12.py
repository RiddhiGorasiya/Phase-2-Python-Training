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

# Use of Python Generators
# 1. Easy to Implement
    # Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.
# iterator code #
# class even:
#     def __init__(self, max):
#         self.n = 2 
#         self.max = max
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n <= self.max:
#             result = self.n
#             self.n += 2
#             return result
#         else:
#             raise StopIteration
#     numbers = even_generator()
#     print(next(numbers))

# generator code #
def even_generator(max):
    n = 2
    while n <= max:
        yield n
        n += 2
numbers = even_generator(4)
print(next(numbers))

# 2. Memory Efficient
    # A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill, if the number of items in the sequence is very large.
    # Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.

# 3. Represent Infinite Stream
    # Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory, and since generators produce only one item at a time, they can represent an infinite stream of data.

# 4. Pipelining Generators
    # Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fibonacci_numbers(10))))