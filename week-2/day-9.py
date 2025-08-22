# Linked List 
# 1) Traversal of a Linked List
    # Traversing a linked list means to go through the linked list by following the links from one node to the next.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

node1 = Node(5)
node2 = Node(81)
node3 = Node(2)
node4 = Node(54)
node5 = Node(25)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

# 2) Find The Lowest Value in a Linked List
    # Finding the lowest value in a linked list is very similar to how we found the lowest value in an array, except that we need to follow the next link to get to the next node.
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
def findLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(5)
node2 = Node(81)
node3 = Node(2)
node4 = Node(54)
node5 = Node(25)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))

# 3) Delete a Node in a Linked List
    # If you want to delete a node in a linked list, it is important to connect the nodes on each side of the node before deleting it, so that the linked list is not broken.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
def traverseAndPrint(head):
  currentNode =head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")
def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next
  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next
  if currentNode.next is None:
    return head
  currentNode.next = currentNode.next.next
  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)
node1 = deleteSpecificNode(node1,node3)
print("\nAfter deletion:")
traverseAndPrint(node1)

# 4) Insert a Node in a Linked List
    # Inserting a node into a linked list is very similar to deleting a node, because in both cases we need to take care of the next pointers to make sure we do not break the linked list.
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(5)
node2 = Node(81)
node3 = Node(2)
node4 = Node(54)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)
