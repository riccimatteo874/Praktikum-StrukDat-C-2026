from tabulate import tabulate
from kurs import money
import konverter

def tampilkan_tabel():
    tabel = [[k, f"{v:,}"] for k, v in money.items()]
    print('=====KONVERTER MATA UANG=====')
    print(tabulate(tabel, headers=['KODE', 'KURS'], tablefmt='grid'))

def main():
    tampilkan_tabel()
    print()
    dari = input('Dari (IDR/USD/EUR/SGD/JPY): ').upper()
    ke = input('Ke (IDR/USD/EUR/SGD/JPY): ').upper()
    jumlah = float(input('Jumlah: '))
    jumlah_idr = konverter.ke_idr(dari, jumlah)
    hasil = konverter.dari_idr(ke, jumlah_idr)
    if dari == 'IDR':
        print(f'Rp {jumlah} = {hasil} {ke}')
    else:
        print(f'{jumlah} {dari} = {jumlah_idr} rupiah')

if __name__ == "__main__":
    main()

    
    