print()
class Node:
  def __init__(self, id, judul):
    self.id = id
    self.judul = judul
    self.right = None
    self.left = None

class Bst:
  def __init__(self):
    self.root = None

  def insert(self, id_buku, judul):
    new = Node(id_buku, judul)
    if not self.root:
        self.root = new
        return
    
    temp = self.root
    curr = None
    while temp is not None:
        curr = temp
        if new.id == temp.id:
            print(f'terdapat id ({id_buku}) yang sama')
            return
        elif new.id > temp.id:
            temp = temp.right
        else:
            temp = temp.left
    if new.id > curr.id:
        curr.right = new
        print(f'{judul} berhasil ditambah\n')
    else:
        curr.left = new
        print(f'{judul} berhasil ditambah\n')

  def search(self, id_buku):
    temp = self.root
    while temp and temp.id != id_buku:
        if id_buku > temp.id:
            temp = temp.right
        else:
            temp = temp.left
    
    if temp:
        print(f'ID {id_buku} berhasil ditemukan, judul: {temp.judul}')
    else:
        print(f'ID {id_buku} tidak ditemukan')

  def inorder(self, node):
    if node is None:
        return
    self.inorder(node.left)
    print(f"- {node.id}: {node.judul}")
    self.inorder(node.right)

  def get_min(self):
    if not self.root:
      return None
    temp = self.root
    while temp.left != None:
      temp = temp.left
    return temp

  def get_max(self):
    if not self.root:
      return None
    temp = self.root
    while temp.right != None:
      temp = temp.right
    return temp

  def height(self, node):
    if node is None:
      return -1
    left_height = self.height(node.left)
    right_height = self.height(node.right)
    return max(left_height, right_height) + 1

lala = Bst()
lala.insert(50, 'mtk')
lala.insert(30, 'ips')
lala.insert(70, 'ipa')
lala.insert(20, 'Dasar Pemrograman')
lala.insert(40, 'Struktur Data')
lala.insert(60, 'Kecerdasan buatan')
lala.insert(80, 'Algoritma Pemrograman')

print("Daftar Buku (In-order):")
lala.inorder(lala.root)
print()
print("Pencarian:")
lala.search(60)
lala.search(100)
print()
print('STATISTIK')
maks = lala.get_max()
print(f'Maks = {maks.id} {maks.judul}')
min = lala.get_min()
print(f'Min = {min.id} {min.judul}')
print(f'Tinggi = {lala.height(lala.root)}')