katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 2}, 
           {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} ]
def update_stok(katalog, sn_target, jumlah_tambah):
  daftar_merk = set()
  for i in katalog:
    if sn_target == i['stok']:
      i['stok'] += jumlah_tambah
    else:
      i['stok']= jumlah_tambah
    daftar_merk.add(i['merk'])


update_stok(katalog, 'SAM01', 1)
update_stok(katalog, 'OPP01', 1)
update_stok(katalog, 'SAM01', 1)
