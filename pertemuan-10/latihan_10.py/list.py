riwayat = []

riwayat.append('url 1')
riwayat.append('url 2')
riwayat.append('url 3')
print("riwayat: ", riwayat)

topurl = riwayat[-1]
print("Peek: ", topurl)

poppedurl = riwayat.pop()
print("Pop: ", poppedurl)

print("riwayat after Pop: ", riwayat)

isEmpty = not bool(riwayat)
print("isEmpty: ", isEmpty)

print("Size: ",len(riwayat))