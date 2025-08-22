# lambda

s1 = "riddhi gorasiya"
s2 = lambda func: func.upper()
print(s2(s1))

# lambda with Condition Checking
# A lambda function can include conditions using if statements.
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(2))
print(n(-1))
print(n(0))

# Difference Between lambda and def Keyword
# using lambda
sq = lambda x: x ** 2
print(sq(3))
# # using def
# def sqdef(x):
#     return x ** 2
# print(sqdef(3))

# Lambda with List Comprehension
# Combining lambda with list comprehensions enables us to apply transformations to data in a concise way.
li = [lambda arg = x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# la,bda with if-else
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(3))
print(check(4))

# Lambda with Multiple Statements
# Lambda functions do not allow multiple statements, however, we can create two lambda functions and then call the other lambda function as a parameter to the first function.
calc = lambda a, b:(a + b, a - b, a * b, a / b)
res = calc(3, 4)
print(res)

# Map Reduce and Filter Operations in Python
# Map Function in Python
def double(n):
    return n * 2
number = [5, 2, 3, 8]
result = map(double,number)
print(list(result))

# Reduce Function in Python
import functools
numbers = [1, 2, 3, 4]
product = functools.reduce(lambda x, y: x * y, numbers)
print("Product of list elements:", product)

# Filter Function in Python
def is_even(n):
    return n % 2 == 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = filter(is_even, num)
print("Even numbers:", list(even_num))

def is_odd(n):
    return n % 2 != 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_num = filter(is_odd, num)
print("Odd numbers:", list(odd_num))