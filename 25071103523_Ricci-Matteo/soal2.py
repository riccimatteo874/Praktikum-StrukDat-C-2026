stok_gadget = [ 
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
] 
yangada = []
def filter_harga(min_harga, max_harga):
  for i in range(len(stok_gadget)):
    if stok_gadget[i]['harga'] >= min_harga:
      if stok_gadget[i]['harga'] <= max_harga:
        yangada.append(stok_gadget[i])
        
max_harga = int(input('max harga= '))
min_harga = int(input('min harga= '))
daftar = filter_harga(min_harga, max_harga)
if yangada == None:
  print('tidak ada gadget dalam rentang harga tersebut')
else:
  print(yangada)