stok_barang = [15, 40, 30, 10, 25]
stok_barang[3]= 50
print(stok_barang)
stok_barang.append(5)
print(stok_barang)
stok_barang.sort(reverse = True)
print(stok_barang)
rata_rata = sum(stok_barang)/len(stok_barang)
print('stok aman') if rata_rata>20 else print('waspada')

data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for nama in data_aktivitas:
  if nama[1] > 80:
    print(f'{nama[0]} mendapat gold')
  elif nama[1] > 50:
    print(f'{nama[0]} mendapat silver')
  else:
    print(f"{nama[0]} mendapat bronze")

ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

print(ukm_coding.difference(ukm_robotik))
print(ukm_coding|ukm_robotik)

def cek(a):
  if a in ukm_robotik:
    return True

m = cek('Andi')
print(m)
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]
print(gudang_pc[0]["item"])
gudang_pc[1]["kategori"]= "Aksesoris"
print(gudang_pc)
gudang_pc.append({"item":"headset", "harga": 35000, "stok": 8})
print(gudang_pc)
for x in range(len(gudang_pc)):
  print(f'item: {gudang_pc[x]["item"]} total ={gudang_pc[x]["harga"]*gudang_pc[x]["stok"]}')