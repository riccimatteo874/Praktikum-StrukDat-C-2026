class Entitas:
  def __init__(self, nama, hp=100, attack=10):
    self.nama = nama
    self.hp = hp
    self.attack = attack

class Player(Entitas):
  def __init__(self, nama):
    super().__init__(nama)
    self.score = 0
    self.exp = 0

class Item:
  def __init__(self, nama, jenis, power):
    self.nama = nama
    self.jenis = jenis
    self.power = power

class Enemy(Entitas):
  def __init__(self, nama):
    super().__init__(nama)
    self.tipe = "Normal"

def save_game(filename, list_pemain):
    """
    Menyimpan seluruh data objek Player dari list ke dalam file .txt.
    Setiap atribut objek dikonversi menjadi string yang dipisahkan koma.
    """
    try:
        # Membuka file dengan mode 'w' (write/tulis ulang)
        f = open(filename, "w")
        for p in list_pemain:
            # Menggabungkan atribut menjadi satu baris teks
            data_string = f"{p.nama},{p.hp},{p.attack},{p.score},{p.exp}\n"
            f.write(data_string)
        f.close()
        print(">>> Progres berhasil disimpan otomatis!")
    except Exception as e:
        print(f">>> Gagal menyimpan data: {e}")

# FUNGSI UNTUK MEMBACA DATA (READ) [cite: 12, 40]
def load_game(filename):
    """
    Membaca file .txt baris demi baris, memecah teksnya (parsing),
    dan membangun kembali objek Player ke dalam list.
    """
    list_pemain = []
    try:
        # Membuka file dengan mode 'r' (read/baca)
        f = open(filename, "r")
        for line in f:
            # Menghapus karakter newline (\n) dan memecah string berdasarkan koma
            data = line.strip().split(",")
            
            # Pastikan jumlah kolom sesuai (nama, hp, attack, score, exp = 5)
            if len(data) == 5:
                # Membuat objek Player baru
                # (Asumsi class Player sudah dibuat dengan constructor nama)
                p = Player(data[0]) 
                p.hp = int(data[1])
                p.attack = int(data[2])
                p.score = int(data[3])
                p.exp = int(data[4])
                
                list_pemain.append(p)
        f.close()
        print(">>> Data pemain berhasil dimuat!")
    except FileNotFoundError:
        # Jika file belum ada (misal: game baru pertama kali dijalankan)
        print(">>> File data tidak ditemukan. Memulai dengan database kosong.")
        return []
    except Exception as e:
        print(f">>> Gagal memuat data: {e}")
        return []
    
    return list_pemain

class NodePemain:
    """Node untuk menyimpan data pemain dalam Single Linked List."""
    def __init__(self, pemain):
        self.pemain = pemain  # Objek Player dari class OOP sebelumnya
        self.next = None

class DaftarPemainLL:
    """Implementasi Single Linked List untuk admin melihat semua pemain."""
    def __init__(self):
        self.head = None

    def tambah_pemain(self, pemain):
        """Menambahkan pemain baru di awal list (O(1))."""
        baru = NodePemain(pemain)
        baru.next = self.head
        self.head = baru

    def tampilkan_semua_pemain(self):
        """Fitur Admin: Melihat data pemain secara berurutan."""
        print("\n=== DATA SELURUH PEMAIN (ADMIN VIEW) ===")
        current = self.head
        if not current:
            print("Belum ada pemain terdaftar.")
            return
        
        while current:
            p = current.pemain
            print(f"Nama: {p.nama} | Skor: {p.score} | Level: {p.level}")
            current = current.next

class NodePemain:
    """Node untuk menyimpan data pemain dalam Single Linked List."""
    def __init__(self, pemain):
        self.pemain = pemain  # Objek Player dari class OOP sebelumnya
        self.next = None

class DaftarPemainLL:
    """Implementasi Single Linked List untuk admin melihat semua pemain."""
    def __init__(self):
        self.head = None

    def tambah_pemain(self, pemain):
        """Menambahkan pemain baru di awal list (O(1))."""
        baru = NodePemain(pemain)
        baru.next = self.head
        self.head = baru

    def tampilkan_semua_pemain(self):
        """Fitur Admin: Melihat data pemain secara berurutan."""
        print("\n=== DATA SELURUH PEMAIN (ADMIN VIEW) ===")
        current = self.head
        if not current:
            print("Belum ada pemain terdaftar.")
            return
        
        while current:
            p = current.pemain
            print(f"Nama: {p.nama} | Skor: {p.score} | Level: {p.level}")
            current = current.next

class LoginSystemHash:
    """Hash Table manual untuk Login/Register (O(1) search)."""
    def __init__(self, size=20):
        self.size = size
        # Menyimpan [username, password]
        self.table = [None] * self.size 

    def _hash_function(self, key):
        """Menghitung index berdasarkan jumlah nilai ASCII karakter."""
        return sum(ord(char) for char in key) % self.size

    def register(self, username, password):
        """Menyimpan username dan password baru."""
        index = self._hash_function(username)
        
        # Linear Probing jika index sudah terisi
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == username:
                return False # Username sudah ada
            index = (index + 1) % self.size
            if index == start_index:
                return False # Table penuh
        
        self.table[index] = [username, password]
        return True

    def login(self, username, password):
        """Verifikasi login pemain."""
        index = self._hash_function(username)
        
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == username:
                if self.table[index][1] == password:
                    return True # Login Sukses
                else:
                    return False # Password Salah
            index = (index + 1) % self.size
            if index == start_index:
                break
        return False # User tidak ditemukan