from Calisan import calisan

class maviyaka(calisan):
    __yipranmapayi = 0.2

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube,maas)
        self.__maas = maas
        self.__tecrube = tecrube

    def zam_hakki(self):
        zamorani = 0
        yenimaas = 0
        try:
            maas = float(self.get_maas())
            tecrube = float(self.get_tecrube())
            if tecrube < 2:
                zamorani = (self.__yipranmapayi * 10)
                yenimaas = maas + (maas * zamorani)
                self.set_maas(yenimaas)
            elif 2 <= tecrube < 4 and maas < 15000:
                zamorani = ((maas % tecrube) / 2) + (self.__yipranmapayi * 10)
                yenimaas = maas + (maas * zamorani)
                self.set_maas(yenimaas)
            elif tecrube >= 4 and maas < 25000:
                zamorani = ((maas % tecrube) / 3) + (self.__yipranmapayi * 10)
                yenimaas = maas + (maas * zamorani)
                self.set_maas(yenimaas)
        except ValueError:
            print("Girilen maas ve tecrube sayi olmalidir.")

    def get_yipranmapayi(self):
        return self.__yipranmapayi
    

    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrube: {self.get_tecrube()}, Maas: {self.get_maas()}"

