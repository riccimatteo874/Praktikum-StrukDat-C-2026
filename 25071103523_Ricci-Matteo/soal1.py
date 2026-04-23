inventaris = []
def registrasi_gadget(merk, tipe, harga, sn):
  if harga > 1000000 and len(sn) >=5:
    return ({"merk": merk, "tipe" : tipe, "harga":harga, "sn":sn, 'status': 'Tersedia'})
  else:
    return None

def input_soal1():
    for i in range(3):
      merk = input("merk = ")
      tipe = input("tipe = ")
      harga = int(input('harga = '))
      sn = input('sn = ')
      gadget = registrasi_gadget(merk, tipe, harga, sn)
      inventaris.append(gadget)

