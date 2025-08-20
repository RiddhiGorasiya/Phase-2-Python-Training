<<<<<<< HEAD
# 1)Create a class Greeter with a method greet(name) that prints a greeting for the provided name.
class greeter:
    def greet(self, name):
        print(f"Hello, {name}!")
g = greeter()
g.greet("Anurag")

# 2)Develop a class Calculator with methods to add and subtract two numbers.
class calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a ,b):
        return a - b
calc = calculator()
print("Sum:", calc.add(5, 3))
print("sub:", calc.sub(5, 3))

# 3)Build a class Employee with multiple constructors that can initialize an employee object in different ways.
class employee:
    def __init__(self, name, id=None, department=None):
        self.name = name
        self.id = id 
        self.department = department
    def display_details(self):
        print(f"Name: {self.name}")
        if self.id:
            print(f"ID: {self.id}")
        if self.department:
            print(f"department: {self.department}")
emp1 = employee("Riddhi")
emp1.display_details()
emp2 = employee("Disha", 1)
emp2.display_details()
emp3 = employee("Heni", 2, "HR")
emp3.display_details()

# 4)Design a class SeriesCalculator that calculates the sum of an arithmetic series.
class SeriesCalculator:
    def calculate_sum(self, n, a=1, d=2):
        return n * (2 * a + (n - 1) * d)
sc = SeriesCalculator()
print("Sum of series:", sc.calculate_sum(5))

# 5)Create a class MaxFinder that identifies the largest number in a list.
class maxfinder:
    def __init__(self, numbers):
        self.numbers = numbers
    def find_max(self):
        if not self.numbers:
            return "List is empty"
        return max(self.numbers)
finder = maxfinder([1,3,5,4,2])
print("The largest number is:", finder.find_max())

# 6)Design a Rectangle class with default attributes for length and width set to 1. Include methods to set these attributes and calculate the area.
class rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
    def set_dimensions(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rect = rectangle()
print("Default area:", rect.area())
rect.set_dimensions(6,6)
print("Update area:", rect.area())

# 7)Person Class with __str__ Method: Create a Person class with first and last name attributes and override the __str__ method to return the full name.
class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f"{self.fname} {self.lname}"
person = person("Riddhi", "Gorasiya")
print(person)

=======
# 1)Create a class Greeter with a method greet(name) that prints a greeting for the provided name.
class greeter:
    def greet(self, name):
        print(f"Hello, {name}!")
g = greeter()
g.greet("Anurag")

# 2)Develop a class Calculator with methods to add and subtract two numbers.
class calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a ,b):
        return a - b
calc = calculator()
print("Sum:", calc.add(5, 3))
print("sub:", calc.sub(5, 3))

# 3)Build a class Employee with multiple constructors that can initialize an employee object in different ways.
class employee:
    def __init__(self, name, id=None, department=None):
        self.name = name
        self.id = id 
        self.department = department
    def display_details(self):
        print(f"Name: {self.name}")
        if self.id:
            print(f"ID: {self.id}")
        if self.department:
            print(f"department: {self.department}")
emp1 = employee("Riddhi")
emp1.display_details()
emp2 = employee("Disha", 1)
emp2.display_details()
emp3 = employee("Heni", 2, "HR")
emp3.display_details()

# 4)Design a class SeriesCalculator that calculates the sum of an arithmetic series.
class SeriesCalculator:
    def calculate_sum(self, n, a=1, d=2):
        return n * (2 * a + (n - 1) * d)
sc = SeriesCalculator()
print("Sum of series:", sc.calculate_sum(5))

# 5)Create a class MaxFinder that identifies the largest number in a list.
class maxfinder:
    def __init__(self, numbers):
        self.numbers = numbers
    def find_max(self):
        if not self.numbers:
            return "List is empty"
        return max(self.numbers)
finder = maxfinder([1,3,5,4,2])
print("The largest number is:", finder.find_max())

# 6)Design a Rectangle class with default attributes for length and width set to 1. Include methods to set these attributes and calculate the area.
class rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
    def set_dimensions(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
rect = rectangle()
print("Default area:", rect.area())
rect.set_dimensions(6,6)
print("Update area:", rect.area())

# 7)Person Class with __str__ Method: Create a Person class with first and last name attributes and override the __str__ method to return the full name.
class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f"{self.fname} {self.lname}"
person = person("Riddhi", "Gorasiya")
print(person)

>>>>>>> 515a01c19f71a92b1c0fc2373077d3fa43947c28
# 8)