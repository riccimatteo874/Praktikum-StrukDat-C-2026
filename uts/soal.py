pengunjung_hari_ini = [
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

def tampilkan_pengunjung(data):
  print('=====DATA PENGUNJUNG PERPUSTAKAAN=====')
  print('-'*54)
  print(f'{'No':<3} | {'id':<5} | {'nama':<7} | {'usia':<5} | {'kategori':<8} | {'kembali':<10}|')
  print('-'*54)
  for i, data in enumerate(pengunjung_hari_ini, 1):
    print(f'{i:<3} | {data['id']:<5} | {data['nama']:<7} | {data['usia']:<5} | {data['kategori']:<8} | {data['kembali']:<10}|')
  print('-'*54)
tampilkan_pengunjung(pengunjung_hari_ini)

def filter_belum_kembali(data):
  list = [x['nama'] for x in data if x['kembali'] == False]
  belum_kembali = len(list)
  return list, belum_kembali

list_nama, belum = filter_belum_kembali(pengunjung_hari_ini)
print('=====PENGUNJUNG BELUM KEMBALI=====')
for i, j in enumerate(list_nama, 1):
  print(f'{i}. {j}')
print(f'Total pengunjung belum kembali adalah: {belum} pengunjung')

print()

def info_perpustakaan():
  info = ({'Nama' : 'Perpustakaan Kampus Terpadu'},
  {'Alamat' : 'Jl. Pendidikan No. 5, Pekanbaru'},
  {'Telp' : '0761-54321'})
  return info
print('INFO PERPUSTAKAAN')
info = info_perpustakaan()
for i in info:
  print(i)

def rekap_kategori(data):
  list_kategori = []
  for i in data:
    list_kategori.append(i['kategori'])
  return list_kategori
list_kategori = rekap_kategori(pengunjung_hari_ini)
set_kategori = set(list_kategori)
print
print(f'Kategori buku unik = {set_kategori}')
print(f'jumlah kategori = {len(set_kategori)}')

dict_kategori = {}
for i in list_kategori:
  if i in dict_kategori:
    dict_kategori[i] += 1
  else:
    dict_kategori[i] = 1
print()
print('REKAP PER KATEGORI')
for i, j in dict_kategori.items():
  print(f'{i}: {j} pengunjung')

maks = max(dict_kategori.urls())
kategori_terbanyak = []
for i,j in dict_kategori.items():
  if j == maks:
    kategori_terbanyak.append(i)
print(f'kategori_terbanyak = {kategori_terbanyak} ({maks} pengunjung)')
print()

class Pengunjung:
  banyak_pengunjung = 0
  def __init__(self, id, nama, kategori):
    self.__id = id
    self.__nama = nama
    self.__kategori = kategori
    Pengunjung.banyak_pengunjung +=1
  def get_id(self):
    return self.__id
  def get_nama(self):
    return self.__nama
  def get_kategori(self):
    return self.__kategori
  
  def tampilkan_info(self):
    print(f'id = {self.get_id()}')
    print(f'nama = {self.get_nama()}')
    print(f'kategori = {self.get_kategori()}')
    print()

  @staticmethod
  def hitung_pengunjung():
    return Pengunjung.banyak_pengunjung

class PengunjungPrioritas(Pengunjung):
  def __init__(self, id, nama, kategori, prioritas):
    super().__init__(id, nama, kategori)
    self.prioritas = prioritas
  def tampilkan_info(self):
    print(f'id = {self.get_id()}')
    print(f'nama = {self.get_nama()}')
    print(f'kategori = {self.get_kategori()}')
    if self.prioritas == 'mendesak':
      print('**Layani segera**')
    print()
    
  
p1 = Pengunjung('M001', 'Rina', 'Fiksi')
p1.tampilkan_info()
p2 = PengunjungPrioritas('M002', "Radit", 'Fiksi', 'mendesak')
p2.tampilkan_info()

print(f'total pengunjung terdaftar = {Pengunjung.banyak_pengunjung}')



class Node:
  def __init__(self, id, nama, kategori):
    self.data = {'id': id, 'nama': nama, 'kategori': kategori}
    self.next = None

class AntrianPeminjaman:
  def __init__(self):
    self.head = None
  
  def tambah(self, id, nama, kategori):
    baru = Node(id, nama, kategori)
    if self.head == None:
      self.head = baru
      print('telah ditambah')
    else:
      temp = self.head
      while temp.next:
        temp = temp.next
      temp.next = baru
      print('telah ditambah')
  posisi = 0
  def tampilkan(self):
    if self.head == None:
      print('tidak ada antrian')
    temp = self.head
    while temp:
      posisi+=1
      print(f'{temp.data}')
      print(f'posisi = {posisi}')

  def panggil(self):
    if self.head == None:
      print("Tidak ada pengunjung")
    else:
      self.head = self.head.next
      print(self.head.data)
      print('telah dihapus')

  def cari(self, nama):
    temp = self.head
    while temp:
      if temp.data['nama'] == nama:
        print(f'{nama} ditemukan')
        return
    print(f'{nama} tidak ditemukan')


