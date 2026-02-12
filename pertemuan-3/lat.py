class Volume:
  def __init__(self, panjang, lebar, tinggi):
    self.panjang = panjang
    self.lebar = lebar
    self.tinggi = tinggi
  
  def hitung(self):
    print(self.lebar * self.panjang * self.tinggi)

  def selisih(self):
    print(self.lebar - self.panjang)

p1 = Volume(1, 2, 3)
p2 = Volume(4, 5, 6)
p3 = Volume(7, 8, 9)

print(p1.lebar, p2.panjang, p3.tinggi)

p1.hitung()
p1.selisih()

p1.panjang = 9

p1.hitung()