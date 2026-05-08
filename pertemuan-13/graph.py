import heapq

class NavigasiLogistik:
  def __init__(self):
    self.graph = {}

  def tambah_kota(self, nama):
    if nama not in self.graph:
      self.graph[nama] = []

  def tambah_jalan(self, u, v, jarak):
    self.tambah_kota(u)
    self.tambah_kota(v)
    self.graph[u].append((v, jarak))
    self.graph[v].append((u, jarak))
    print(f"[INPUT] Menambahkan jalan: {u} <-> {v} ({jarak} km)")

  def tampilkan_graph(self):
    print("\n[INFO] Struktur Jaringan Distribusi:")
    for kota, tetangga in self.graph.items():
      koneksi = ", ".join([f"{t[0]} ({t[1]})" for t in tetangga])
      print(f"  {kota} terhubung ke: {koneksi}")

  def dijkstra(self, kota_asal):
    jarak_terpendek = {kota: float('inf') for kota in self.graph}
    jarak_terpendek[kota_asal] = 0
    pq = [(0, kota_asal)]
    
    print(f"\n[PROSES] Menghitung rute terpendek dari: {kota_asal}...")

    while pq:
      jarak_skrg, kota_skrg = heapq.heappop(pq)

      if jarak_skrg > jarak_terpendek[kota_skrg]:
        continue

      for tetangga, bobot in self.graph[kota_skrg]:
        jarak_baru = jarak_skrg + bobot
        if jarak_baru < jarak_terpendek[tetangga]:
            jarak_terpendek[tetangga] = jarak_baru
            heapq.heappush(pq, (jarak_baru, tetangga))
    
    return jarak_terpendek

print("SISTEM NAVIGASI LOGISTIK \"KILAT MAJU\"")
print("=" * 40)

logistik = NavigasiLogistik()
logistik.tambah_jalan("Jakarta", "Bandung", 150)
logistik.tambah_jalan("Jakarta", "Cirebon", 200)
logistik.tambah_jalan("Bandung", "Tasikmalaya", 100)
logistik.tambah_jalan("Bandung", "Cirebon", 130)
logistik.tambah_jalan("Cirebon", "Semarang", 250)
logistik.tambah_jalan("Tasikmalaya", "Semarang", 200)

logistik.tampilkan_graph()
hasil_dijkstra = logistik.dijkstra("Jakarta")

print("\n[HASIL] Jarak Terpendek dari Jakarta:")
for i, (kota, jarak) in enumerate(hasil_dijkstra.items(), 1):
    print(f"{i}. Ke {kota}: {jarak} km")

print("\nSimulasi Navigasi Selesai!")