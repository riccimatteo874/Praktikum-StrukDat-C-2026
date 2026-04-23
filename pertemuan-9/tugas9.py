class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class Double_linked:
  def __init__(self):
    self.head = None
  
  def tambah_kendaraan(self, plat):
    new = Node(plat)
    if self.head == None:
      self.head = new
      print(f'{plat} ditambah')
      return
    temp = self.head
    while temp.next:
      temp = temp.next
    temp.next = new
    new.prev = temp
    print(f'{plat} ditambah')
  
  def hapus_kendaraan(self, plat):
    if self.head.data == plat:
      self.head = self.head.next
      print(f'{plat} berhasil dihapus')
      return
    temp = self.head
    while temp:
      if temp.data == plat:
        if temp.prev:
          temp.prev.next = temp.next
        if temp.next:
          temp.next.prev = temp.prev
    print(f'{plat} tidak ditemukan')
  
  def tampilkan_maju(self):
    if self.head == None:
      print('Tidak ada kendaraan')
    else:
      temp = self.head
      while temp:
        print(temp.data)
        temp = temp.next
  
  def tampilkan_mundur(self):
    if self.head == None:
      print('Tidak ada kendaraan')
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      while temp:
        print(temp.data)
        temp = temp.prev

class Node2:
  def __init__(self, nama):
    self.nama =nama
    self.next = None

class Circular:
  def __init__(self):
    self.head = None
  
  def tambah_petugas(self, nama):
    baru = Node2(nama)
    if self.head == None:
      self.head = baru
      baru.next = self.head
      print('ditambah')
      return
    temp = self.head
    while temp.next != self.head:
      temp = temp.next
    temp.next = baru
    baru.next = self.head
    print('ditambah')
  
  def giliran_berikutnya(self, banyak):
    if self.head is None:
        print("Tidak ada petugas dalam antrean.")
        return
    sudah = 0
    temp = self.head
    while sudah != banyak:
        print(f'Giliran {sudah+1} : {temp.nama}')
        sudah+=1
        temp = temp.next

apajalah = Double_linked()
apajalah.tambah_kendaraan('BM 2171 IA')
apajalah.tambah_kendaraan('BM 328 FAJ')
apajalah.tampilkan_maju()
apajalah.hapus_kendaraan('BM 2171 IA')
apajalah.tampilkan_maju()

apajalah2 = Circular()
apajalah2.tambah_petugas('romeo')
apajalah2.tambah_petugas('benaya')
apajalah2.tambah_petugas('erick')
apajalah2.giliran_berikutnya(6)