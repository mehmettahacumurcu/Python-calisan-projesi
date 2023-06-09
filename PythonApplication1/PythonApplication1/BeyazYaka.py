from Calisan import calisan

class beyazyaka(calisan):
    __tesvikprimi = 2000

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas)
        self.__tecrube = tecrube 
        self.__maas = maas 
     
    def zam_hakki(self):
        yenimaas = 0
        if self.get_tecrube() < 2:
            yenimaas = self.get_maas() + self.__tesvikprimi
            self.set_maas(yenimaas)
        elif 2 <= self.get_tecrube() < 4 and self.get_maas() < 15000:
            yenimaas = self.get_maas() + ((self.get_maas() % self.get_tecrube()) * 5) + self.__tesvikprimi
            self.set_maas(yenimaas)
        elif self.get_tecrube() >= 4 and self.get_maas() < 25000:
            yenimaas = self.get_maas() + ((self.get_maas() % self.get_tecrube()) * 4) + self.__tesvikprimi
            self.set_maas(yenimaas)

        
    def get_tesvikprimi(self):
        return self.__tesvikprimi
   

    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrube: {self.get_tecrube()}, Maas: {self.get_maas()}"

