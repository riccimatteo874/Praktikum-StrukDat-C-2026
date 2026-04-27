class Node:
  def __init__(self, nama, keluhan):
    self.nama = nama
    self.keluhan = keluhan
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def enqueue(self, nama, keluhan):
    new_node = Node(nama, keluhan)
    if self.tail is None:
      self.head = self.tail = new_node
      self.length += 1
      print(f'{nama} terdaftar dengan keluhan {keluhan} (No. Antrian {self.length})')
      return
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1
    print(f'{nama} terdaftar dengan keluhan {keluhan} (No. Antrian {self.length})')

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.head
    self.head = temp.next
    self.length -= 1
    if self.head is None:
      self.tail = None
    return temp.nama, temp.keluhan

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.head.nama, self.head.keluhan

  def isEmpty(self):
    return self.length == 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.head
    count = 1
    while temp:
      print(f'{count}. {temp.nama} -> {temp.keluhan}')
      temp = temp.next
      count+=1
    print()

  def clear(self):
    print('Sesi poliklinik selesai. Antrian dikosongkan')
    while self.head:
      self.dequeue()

print('SISTEM ANTREAN POLI UMUM')
print('RUMAH SAKIT SEHAT BERSAMA')

rs_bersama = Queue()
if rs_bersama.isEmpty():
  print('Antrean kosong')
rs_bersama.enqueue('BUDI', 'demam tinggi')
rs_bersama.enqueue('ANI', 'batuk pilek')
rs_bersama.enqueue('CITRA', 'sakit kepala')
print(f'jumlah pasien menunggu: {rs_bersama.length} orang')
nama, keluhan = rs_bersama.peek()
print(f'Pasien berikutnya: {nama} _ {keluhan}')
nama1, keluhan1 = rs_bersama.dequeue()
print(f'Dokter memanggil {nama1}_{keluhan1}')
rs_bersama.enqueue('DODI', 'nyeri perut')
rs_bersama.printQueue()
nama1, keluhan1 = rs_bersama.dequeue()
print(f'Dokter memanggil {nama1}_{keluhan1}')
print(f'jumlah pasien menunggu: {rs_bersama.length} orang')
rs_bersama.clear()
if rs_bersama.isEmpty():
  print('Antrean kosong')
