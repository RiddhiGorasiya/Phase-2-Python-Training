# Inheritance lets one class borrow from another. You write class Puppy(Dog): to say, “Puppy is a kind of Dog.” The new class gains all methods and data of Dog without rewriting them.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Riddhi", "Disha")
x.printname()

# Create a Child Class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Alpa", "Mukesh")
x.printname()

# Use the super() Function

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Heer", "Pruthvi")
x.printname()

# Add Properties

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = lname

x = Student("Riddhi", "Gorasiya", 2025)
print(x.graduationyear)

# Add methods

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Riddhi", "Gorasiya", 2025)
x.welcome()

# types of inheritance
# 1-Single Inheritance in Python
x=0
class fruit:
  def __init__(self):
  global x
  x+=1
  print("I'm a fruit")                         
class citrus(fruit):
  def __init__(self):
  super().__init__()
  global x
  x+=2
  print("I'm citrus")                           
x
