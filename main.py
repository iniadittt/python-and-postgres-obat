from database import Database
from obat import Obat


class Main:
    def __init__(self):
        try:
            while True:
                print('\n======= Aplikasi CRUD Barang =======')
                print('0. Keluar Program')
                print('1. Tampil Semua Data Obat')
                print('2. Tambah Data Obat')
                print('3. Cari Data Obat')
                print('4. Update Data Obat')
                print('5. Hapus Data Obat')
                menu = int(input('Masukkan Menu: '))
                
                if(menu == 0):
                    break
                elif(menu == 1):
                    print('\n')
                    self.allData()
                elif(menu == 2):
                    print('\n')
                    self.insert()
                elif(menu == 3):
                    print('\n')
                    self.search()
                elif(menu == 4):
                    print('\n')
                    self.update()
                elif(menu == 5):
                    print('\n')
                    self.delete()
                else:
                    print('Keyowrd salah!')
        except:
            print('Except!')
            Main()

    def search(self):
        try:
            print('===== CARI DATA OBAT =====')
            kode = input('Masukkan Kode Obat: ')
            print(kode)
            obat = Obat()
            result = obat.getByKodeBarang(kode)
            value = obat.affected
            if(value != 0):
                print('- DATA OBAT -')
                print(f'Kode Obat   : {obat.kode_obat}')
                print(f'Nama        : {obat.nama}')
                print(f'Merek       : {obat.merek}')
                print(f'Bentuk Obat : {obat.bentuk_obat}')
                print(f'Berat       : {obat.berat}')
            else:
                print('Data Obat Tidak Ditemukan!')
        except:
            pass

    def insert(self):
        try:
            print('===== TAMBAH DATA OBAT =====')
            obat = Obat()
            kode = input('Masukkan Kode Obat: ')
            nama = input('Masukkan Nama Obat: ')
            merek = input('Masukkan Merek Obat: ')
            bentuk_obat = input('Masukkan Bentuk Obat: ')
            berat = input('Masukkan Berat Obat: ')
            obat.kode_obat = kode
            obat.nama = nama.capitalize()
            obat.merek = merek.capitalize()
            obat.bentuk_obat = bentuk_obat.capitalize()
            obat.berat = berat
            simpan = obat.save()
            if(simpan > 0):
                print('Data Obat Disimpan!')
            else:
                print('Data Obat Gagal Disimpan!')
            obat.getAllData()
        except:
            pass

    def update(self):
        try:
            print('===== UBAH DATA OBAT =====')
            kode = input('Masukkan Kode Obat: ')
            obat = Obat()
            result = obat.getByKodeBarang(kode)
            value = obat.affected
            if(value != 0):
                print('- DATA OBAT -')
                print(f'Kode Obat   : {obat.kode_obat}')
                print(f'Nama        : {obat.nama}')
                print(f'Merek       : {obat.merek}')
                print(f'Bentuk Obat : {obat.bentuk_obat}')
                print(f'Berat       : {obat.berat}')
            else:
                print('Maaf data tidak ditemukan!')
            print('\n')
            ubah = input('Apakah anda ingin merubah data (y/n)? ')
            ubah = ubah.lower()
            if(ubah == 'y'):
                namaBaru = input(f'Masukkan Nama Obat Baru ({obat.nama}): ')
                merekBaru = input(f'Masukkan Merek Obat Baru ({obat.merek}): ')
                bentukBaru = input(f'Masukkan Bentuk Obat Baru ({obat.bentuk_obat}): ')
                beratBaru = input(f'Masukkan Berat Obat Baru ({obat.berat}): ')
                
                if(namaBaru == ''):
                    obat.nama = obat.nama
                else:
                    obat.nama = namaBaru.capitalize()
            
                if(merekBaru == ''):
                    obat.merek = obat.merek
                else:
                    obat.merek = merekBaru.capitalize()
                    
                if(bentukBaru == ''):
                    obat.bentuk_obat = obat.bentuk_obat
                else:
                    obat.bentuk_obat = bentukBaru.capitalize()
                    
                if(beratBaru == ''):
                    obat.berat = obat.berat
                else:
                    obat.berat = beratBaru
                    
                simpan = obat.update(kode)
                if(simpan > 0):
                    print('Data Obat Diperbarui')
                else:
                    print('Data Obat Gagal Diperbarui')
                obat.getAllData()
            else:
                pass
        except:
            pass

    def delete(self):
        try:
            print('===== HAPUS DATA OBAT =====')
            kode = input('Masukkan Kode Obat: ')
            obat = Obat()
            simpan = obat.delete(kode)
            if(simpan > 0):
                print('Data Obat Dihapus')
            else:
                print('Data Obat Gagal Dihapus')
            obat.getAllData()
        except:
            pass
    
    def allData(self):
        obat = Obat()
        obat.getAllData()
     
if __name__ ==  '__main__':
    app = Main()