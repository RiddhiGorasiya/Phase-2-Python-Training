# getattr()

class student:
    name = "riddhi gorasiya"
    age = 20
obj = student()

print("The name is " + getattr(obj, 'name'))


import time

class GfG:
    name = "riddhi gorasiya"
    age = 20

obj = GfG()

# use of getattr to print name
start_getattr = time.time()
print("The name is " + getattr(obj, 'name'))
print("Time to execute getattr " + str(time.time() - start_getattr))

# use of conventional method to print name
start_obj = time.time()
print("The name is " + obj.name)
print("Time to execute conventional method " + str(time.time() - start_obj))

# hasattr()

class stud:
    name = "riddhi"
    age = 20

obj = stud()

print("Does name exist ? " + str(hasattr(obj, 'name')))
print("Does motto exist ? " + str(hasattr(obj, 'motto')))

# setattr()

class Person:
    def __init__(self):
        pass

p = Person()
setattr(p, 'name', 'disha')
print(f"name: {p.name}")


class Animal:
    name = 'lucky'
    
p = Animal()
print('Before modification:', p.name)
setattr(p, 'name', 'Woozoo')

print('After modification:', p.name)
