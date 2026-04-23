stack = []

stack.append('A')
stack.append('B')
stack.append('C')
print("Stack: ", stack)

topElement = stack[-1]
print("Peek: ", topElement)

poppedElement = stack.pop()
print("Pop: ", poppedElement)

print("Stack after Pop: ", stack)

isEmpty = not bool(stack)
print("isEmpty: ", isEmpty)

print("Size: ",len(stack))