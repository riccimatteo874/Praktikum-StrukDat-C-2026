plat = []
genap = []
ganjil = []

def terima_input():
    for i in range(3):
        nopol = input(f"Masukkan plat nomor ke-{i+1} (contoh: B 1234 ABC): ")
        plat.append(nopol.upper())

def proses_ganjil_genap():
    for p in plat:
        bagian = p.split()
        if len(bagian) > 1:
            nomor_seri = bagian[1] 
            angka_terakhir = int(nomor_seri[-1])
            if angka_terakhir % 2 == 0:
                genap.append(p)
            else:
                ganjil.append(p)

terima_input()
proses_ganjil_genap()

print("\n--- Hasil Pengelompokan ---")
print(f"Plat Genap  : {genap}")
print(f"Plat Ganjil : {ganjil}")
#2
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def tambahKendaraan(head, plat_node):
    if not head:
        return plat_node
    
    currentNode = head
    while currentNode.next:
        currentNode = currentNode.next
    
    currentNode.next = plat_node

def hapusKendaraan(head, plat):
  if head == plat:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != plat:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

#3
def sisipkan_vip(head, plat_baru, plat_target):
    currentNode = head
    while currentNode:
        if currentNode.data == plat_target:
            nodebaru = Node(plat_baru)
            nodebaru.next = currentNode.next
            currentNode.next = nodebaru
            return
        currentNode = currentNode.next

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

kendaraan1 = Node("B 1234 ABC")
kendaraan2 = Node("D 8888 XYZ")

# Menambah kendaraan
tambahKendaraan(kendaraan1, kendaraan2)

# Mencoba sisipkan VIP
sisipkan_vip(kendaraan1, "L 1 JP", "B 1234 ABC")

traverseAndPrint(kendaraan1)
print(f"Data Head: {kendaraan1.data}")

