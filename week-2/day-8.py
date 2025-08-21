# stack

stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Pop: ", poppedElement)

# Stack after Pop
print("Stack after Pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

# Size
print("Size: ",len(stack))

# Creating a stack using class:
# While Python lists can be used as stacks, creating a dedicated Stack class provides better encapsulation and additional functionality:
class stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
mystack = stack()
mystack.push('Riddhi')
mystack.push('Disha')
mystack.push('Heni')
print("Stack: ", mystack.stack)
print("Pop:" , mystack.pop())
print("Stack after pop: ", mystack.stack)
print("Peek: ", mystack.peek())
print("isEmpty: ", mystack.isEmpty())
print("Size: ", mystack.size())

# Creating a Stack using a Linked List:
class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self,value):
        new_node = node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value
    def isEmpty(self):
        return self.size == 0
    def stacksize(self):
        return self.size
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()
mystack = stack()
mystack.push('Vaibhav')
mystack.push('Herry')
mystack.push('Dharam')
print("LinkedList: ", end="")
mystack.traverseAndPrint()
print("Peek: ", mystack.peek())
print("Pop: ", mystack.pop())
print("LinkedList after pop: ", end="")
mystack.traverseAndPrint()
print("isEmpty: ", mystack.isEmpty())
print("Size: ", mystack.stacksize())

# Queue

queue = ["Riddhi", "Disha", "Heni"]
queue.append("Pruthvi")
queue.append("Heer")
print(queue)
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)

# Code Implementation of queue all the operations:
from collections import deque
q = deque()
def isEmpty():
    return len(q) == 0
def qEnqueue(data):
    q.append(data)
def qdequeue():
    if isEmpty():
        return 
    q.popleft
def getFront():
    if isEmpty():
        return -1
    return q[0]
def getRear():
    if isEmpty():
        return -1
    return q[-1]
if __name__ == '__main__':
    qEnqueue(1)
    qEnqueue(8)
    qEnqueue(3)
    qEnqueue(6)
    qEnqueue(2)
    if not isEmpty():
        print("Queue after enqueue opretion: ", list(q))
    print("Front: ", getFront())
    print("Rear: ", getRear())
    print("Queue size: ", len(q))
    qdequeue()
    print("Is queue empty?", "Yes" if isEmpty() else "No")