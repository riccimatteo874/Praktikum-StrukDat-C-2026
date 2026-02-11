stok = [15, 50, 30, 25, 40]
stok.insert(5, 100)
stok.sort(reverse = True)
rata = 0
for x in stok:
  rata += x
ratarata = rata / len(stok)
print(stok)
print(ratarata)


barang = ('B001', 'laptop gaming', '15000000')
print(barang[2])
barang[2] = '14000000' # cara ini menyebabkan error karna tuple tidak dapat diubah sehingga harus diubah dulu ke list 
mybarang = list(barang)
mybarang[2] = '14000000'
barang = tuple(mybarang)
kode, nama, harga = barang
tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL", "nodejs"}
set = tim_frontend.intersection(tim_backend)

nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
}
SO4 = {
  "nama_siswa": "fafa",
  "nilai_tugas": 85,
  "nilai_uts": 80,
  "nilai_uas": 90
}
nilai_siswa.update(SO4)
