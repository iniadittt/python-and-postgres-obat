from ast import Str
from database import Database as db
from prettytable import PrettyTable

class Obat:
    def __init__(self):
        self.__kode_obat = None
        self.__nama = None
        self.__merek = None
        self.__bentuk_obat = None
        self.__berat = None
        self.__info = None
        self.db = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info == None):
            return f'Kode Obat: {self.__kode_obat}\nNama Obat: {self.__nama}\nMerek: {self.__merek}\nBentuk Obat: {self.__bentuk_obat}\nBerat: {self.__berat}'
        else:
            return self.__info
    
    @property
    def kode_obat(self):
        return self.__kode_obat

    @kode_obat.setter
    def kode_obat(self, value):
        self.__kode_obat = value
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value
    
    @property
    def merek(self):
        return self.__merek

    @merek.setter
    def merek(self, value):
        self.__merek = value
    
    @property
    def bentuk_obat(self):
        return self.__bentuk_obat

    @bentuk_obat.setter
    def bentuk_obat(self, value):
        self.__bentuk_obat = value
        
    @property
    def berat(self):
        return self.__berat

    @berat.setter
    def berat(self, value):
        self.__berat = value
        
    def save(self):
        self.db = db()
        sql = F'INSERT INTO obat (kode_obat,nama,merek,bentuk_obat,berat) VALUES (\'{self.__kode_obat}\',\'{self.__nama}\',\'{self.__merek}\',\'{self.__bentuk_obat}\',{self.__berat})'
        self.affected = self.db.insert(sql)
        self.db.disconnect
        return self.affected
        
    def update(self, kode_obat):
        self.db = db()
        val = (kode_obat,self.__nama,self.__merek,self.__bentuk_obat,self.__berat, kode_obat)
        sql = 'UPDATE obat SET kode_obat = %s, nama = %s, merek = %s, bentuk_obat = %s, berat = %s WHERE kode_obat = %s;'
        self.affected = self.db.update(sql, val)
        self.db.disconnect
        return self.affected
        
    def delete(self, kode_obat):
        self.db = db()
        sql="DELETE FROM obat WHERE kode_obat='" + str(kode_obat) + "';"
        self.affected = self.db.delete(sql)
        self.db.disconnect
        return self.affected
        
    def getByKodeBarang(self, kode_obat):
        self.db = db()
        sql="SELECT * FROM obat WHERE kode_obat='" + kode_obat + "';"
        self.result = self.db.findOne(sql)
        if(self.result != None):
            self.__kode_obat = self.result[1]
            self.__nama = self.result[2]
            self.__merek = self.result[3]
            self.__bentuk_obat = self.result[4]
            self.__berat = self.result[5]
            self.affected = self.db.cursor.rowcount
        else:
            self.__kode_obat = ''
            self.__nama = ''
            self.__merek = ''
            self.__bentuk_obat = ''
            self.__berat = ''
            self.affected = 0
            self.affected = 0
            self.db.disconnect
            return self.result

    def getAllData(self):
        self.db = db()
        sql = 'SELECT * FROM obat;'
        self.result = self.db.findAll(sql)
        if(self.result == 0):
            return self.result
        else:
            tableObat = PrettyTable(["ID Obat", "Kode Obat", "Nama", "Merek", "Bentuk Obat", "Berat"])
            for res in self.result:
                tableObat.add_row([str(res[0]),res[1],res[2],res[3],res[4],str(res[5])])
            print(tableObat)