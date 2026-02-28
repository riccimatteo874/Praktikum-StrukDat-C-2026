from kurs import money

def ke_idr(kode, jumlah):
  if kode == "IDR":
    return jumlah
  return jumlah * money[kode]

def dari_idr(kode, jumlah):
  if kode == "IDR":
    return jumlah
  return jumlah / money[kode]













  