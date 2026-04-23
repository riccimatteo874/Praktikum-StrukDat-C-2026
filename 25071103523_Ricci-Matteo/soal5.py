from soal1 import registrasi_gadget
from soal3 import update_stok
from soal4 import hitung_komisi, skema_komisi

inventaris = []

while True:
    print("\n=== PyGadget Hub ===")
    print("1. Tambah Gadget")
    print("2. Daftar Inventaris")
    print("3. Update Stok")
    print("4. Cek Komisi")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        m = input("Merk: ")
        t = input("Tipe: ")
        h = float(input("Harga: "))
        s = input("SN: ")
        hasil = registrasi_gadget(m, t, h, s)
        if hasil:
            inventaris.append(hasil)
            print("Berhasil ditambah!")

    elif pilihan == '2':
        print(f"\n{'Merk':<12} | {'Tipe':<10} | {'Harga':<12} | {'SN':<8} | {'Stok'}")
        print("-" * 55)
        for g in inventaris:
            stok = g.get('stok', 0)
            print(f"{g['merk']:<12} | {g['tipe']:<10} | {g['harga']:<12.0f} | {g['sn']:<8} | {stok}")

    elif pilihan == '3':
        target = input("Masukkan SN: ")
        tambah = int(input("Jumlah tambah: "))
        update_stok(inventaris, target, tambah)

    elif pilihan == '4':
        nama_sales = input("Nama Sales: ")
        total = float(input("Total Penjualan: "))
        persen = hitung_komisi(total, skema_komisi)
        nominal = (total * persen) / 100
        print(f"Komisi {nama_sales}: Rp{nominal:,.0f} ({persen}%)")

    elif pilihan == '5':
        print("Sampai jumpa di PyGadget Hub!")
        break