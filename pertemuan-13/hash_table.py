class HashTablePerpustakaan:
  def __init__(self):
    self.size = 10
    self.table = [[] for _ in range(self.size)]

  def _hash_function(self, kode):
    total_unicode = sum(ord(char) for char in kode)
    return total_unicode % self.size

  def insert(self, kode, judul):
    index = self._hash_function(kode)
    bucket = self.table[index]
    
    for i, item in enumerate(bucket):
      if item[0] == kode:
        bucket[i] = [kode, judul]
        return
    
    bucket.append([kode, judul])

  def search(self, kode):
    index = self._hash_function(kode)
    bucket = self.table[index]
    
    for item in bucket:
      if item[0] == kode:
        return item[1]
  
    return "Buku tidak ditemukan"

  def delete(self, kode):
    index = self._hash_function(kode)
    bucket = self.table[index]
    
    for i, item in enumerate(bucket):
      if item[0] == kode:
        bucket.pop(i)
        return True
    return False

  def display(self):
    print("\n=== ISI HASH TABLE ===")
    for i, bucket in enumerate(self.table):
      print(f"Bucket {i}: {bucket}")
    print("======================\n")

puspus = HashTablePerpustakaan()

puspus.insert("BK111", "Mahir C++ Dalam Satu Jam")
puspus.insert("BK222", "Python Dasar")
puspus.insert("BK333", "Matematika Diskrit")
puspus.insert("BK444", "Atomic Habits")

puspus.display()

puspus.insert("BK045", "Mein Kampf")
puspus.insert("BK111", "Bumi Manusia")

puspus.display()

print(f"Cari BK222: {puspus.search('BK222')}")
print(f"Cari BK999: {puspus.search('BK999')}")

puspus.delete("BK333")

puspus.display()