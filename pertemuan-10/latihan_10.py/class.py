class StackList:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return len(self.stack) == 0

  def push(self, url):
    self.stack.append(url)

  def pop(self):
    if self.isEmpty():
      return "Riwayat kosong"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return None
    return self.stack[-1]
  
  def size(self):
    return len(self.stack)
  

riwayat = StackList()
riwayat.push('lala')
atas = riwayat.peek()
print(atas)