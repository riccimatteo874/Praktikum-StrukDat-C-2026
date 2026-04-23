skema_komisi = ( 
(100000000, 10), # Penjualan >= 100jt -> Komisi 10% 
(50000000,  5),  # Penjualan >= 50jt  -> Komisi 5% 
(20000000,  2),  # Penjualan >= 20jt  -> Komisi 2% 
(0,         0)   # Di bawah 20jt      
)

def hitung_komisi(total_penjualan, skema, index=0):
  if total_penjualan >= skema[index][0]:
    return skema[index][1]
  else:
    return hitung_komisi(total_penjualan, skema, index+1)



