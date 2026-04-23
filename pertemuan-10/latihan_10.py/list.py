riwayat = []

riwayat.append('googlr.com')
riwayat.append('lala.com')
riwayat.append('x.com')
print("riwayat: ", riwayat)

topurl = riwayat[-1]
print("Peek: ", topurl)

poppedurl = riwayat.pop()
print("Pop: ", poppedurl)

print("riwayat after Pop: ", riwayat)

isEmpty = not bool(riwayat)
print("isEmpty: ", isEmpty)

print("Size: ",len(riwayat))