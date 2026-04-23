class Node:
  def __init__(self, url):
    self.url = url
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, url):
    new_node = Node(url)
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
    return popped_node.url

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.url

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

  def traverseAndPrint(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.url, end=" -> ")
      currentNode = currentNode.next
    print()