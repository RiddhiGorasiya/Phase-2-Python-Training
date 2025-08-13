# classes & object 

class student: # creating class
    name = "Riddhi"
    age = 20

s1 = student() # creating object(instance)
print(s1.name)
s2 = student
print(s2.name)
print(s2.age)

# __init__ function

class student: 

    # def __init__(self): # default constructors
    #     pass

    name = "anon" # class attr

    def __init__(self, fullname, marks): # parameterized constructors
        self.name = fullname # obj attr > class attr
        self.marks = marks
        print("Adding new student in database..")

s1 = student("Riddhi", 7.98)
print(s1.name, s1.marks)

s2 = student("Disha", 7.83)
print(s2.name, s2.marks)

# method 
# __init__

class student: 

    def __init__(self, fullname, marks):
        self.name = fullname 
        self.marks = marks
        print("Adding new student in database..")

    def welcome(self):
        print("Welcome Student", self.name)

    def get_marks(self):
        return self.marks
    
s1 = student("Riddhi", 7.98)
s1.welcome()
print(s1.get_marks())

# __str__

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    

p1 = Person("Vaibhav", 36)

print(p1)

# practice questions
# Create student class that takes name & marks of 3 subject as arguments in constructor.Then create a method to print the average.
class student: 

    def __init__(self, fullname, marks):
        self.name = fullname 
        self.marks = marks
    
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val 
        print("Hii", self.name, "your avg score is:", sum/3)

std1 = student("Riddhi Gorasiya", [99, 87, 54])
std1.get_avg()

# static method

class stdu:

    @staticmethod
    def hello():
        print("hello")
         
s1 = stdu()
s1.hello()

# abstraction
# (Hiding the implementation details of a class and only showing the essential features to the user.)
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
           self.clutch = True
           self.acc = True
           print("Car started..")

car1 = car()
car1.start()

# encapsulation
# (Wrapping data and functions into a single unit (object).)

# practice questions
# Create account class with 2 attribute - balance & account no.
# Create method for debit, credit & printing the balance.

class Account:

    def __init__(self, bal, acc):
        self.balance = bal 
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000, 12335)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(30000)
acc1.debit(1000)

