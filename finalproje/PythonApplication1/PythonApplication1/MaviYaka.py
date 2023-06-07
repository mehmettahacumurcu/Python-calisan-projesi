from Calisan import calisan

class maviyaka(calisan):
    __yipranmapayi = 0.2
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk,tecrube,maas):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk,tecrube,maas)
    
    def zam_hakki(self):
        zamorani = 0
        yenimaas = 0
        try:
            self.__maas = float(self.__maas)
            self.__tecrube = float(self.__tecrube)
            if self.__tecrube < 2:
                yenimaas = self.__maas + (self.__yipranmapayi*10)
                self.__maas = yenimaas 
            elif self.__tecrube > 2 and self.__tecrube < 4 and self.__maas < 15000:
                yenimaas = self.__maas + ((self.__maas % self.__tecrube)/2) + (self.__yipranmapayi*10)
                self.__maas = yenimaas
            elif self.__tecrube > 4 and self.__maas < 25000:
                yenimaas = self.__maas + ((self.__maas % self.__tecrube)/3) + (self.__yipranmapayi * 10)
                self.__maas = yenimaas 
        except ValueError:
            print("Girilen maas ve tecrube sayi olmalidir.")

    def __str__(self):
        return f"Ad : {self.get_ad} ,  Soyad : {self.get_soyad()} , Tecrube : {self.get_tecrube()} , Maas : {self.get_maas()}"





        
