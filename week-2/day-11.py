# Decorators

def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper
@decorator
def greet():
    print("Hello, World!")
greet()

# Decorator with Parameters
# Decorators often need to work with functions that have arguments. We use *args and **kwargs so our wrapper can accept any number of arguments.
def Decorator_name(func):
    def wrapper(*args, **kwargs): # *args → collects all positional arguments and **kwargs → collects all keyword arguments
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper
@Decorator_name
def add(a, b):
    return a + b
print(add(9, 6))

# Types of Decorators
# 1. Function Decorators 
    # The most common decorators in Python, used to wrap and enhance functions by adding extra behavior before or after the original function runs.
def simple_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper
@simple_decorator
def greet():
    print("Hello, Riddhi!")
greet()

# 2. Method Decorators
    # Special decorators used for methods inside a class. They work like function decorators but handle the self parameter for instance methods.
def method_decorator(func):
    def wapper(self, *args, **kwargs):
        print("Hiii...")
        res = func(self, *args, **kwargs)
        print("Hello!")
        return res
    return wapper
class MyClass:
    @method_decorator
    def say_hello(self):
        print("Riddhi Gorasiya")
obj = MyClass()
obj.say_hello()

# 3. Class Decorators
    # Class decorators are used to modify or enhance behavior of a class. Like function decorators, class decorators are applied to class definition. They work by taking class as an argument and returning a modified version of class.       
def fun(cla):
    cla.class_name = cla.__name__
    return cla
@fun
class Person:
    pass
print(Person.class_name)

# Built-in Decorators
# 1. @staticmethod
    # It is used to define a method that doesn't operate on an instance of class (i.e., it doesn't use self). Static methods are called on class itself, not on an instance of class.
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
res = MathOperations.add(10,80)
print(res)

# 2. @classmethod 
    # It is used to define a method that operates on class itself (i.e., it uses cls). Class methods can access and modify class state that applies across all instances of class.
class Employee:
    raise_amount = 1.05
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
Employee.set_raise_amount(1.20)
print(Employee.raise_amount)

# 3. @property
    # It is used to define a method as a property, which allows you to access it like an attribute. This is useful for encapsulating implementation of a method while still providing a simple interface.
class Circle:
    def __init__(self,radius):
        self.radius = radius
    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self,value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")
    @property
    def area(self):
        return 3.14259 * (self._radius ** 2)
c = Circle(5)
print(c.radius)
print(c.area)
c.radius = 10
print(c.area)

# Chaining Multiple Decorators
    # Chaining decorators means applying multiple decorators to same function. Each decorator wraps function in sequence, adding layered behavior.
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
@decor1
@decor
def num():
    return 20
@decor1
@decor
def num2():
    return 10
print(num())
print(num2())

