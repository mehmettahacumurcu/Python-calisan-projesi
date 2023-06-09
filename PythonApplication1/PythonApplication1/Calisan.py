from insan import Insan

class calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = tecrube
        self.__maas = maas
        self.__sektor = None

    def set_sektor(self):
        sektorler = ["teknoloji", "muhasebe", "insaat", "diger"]
        sektor_secimi = int(input("Teknoloji sektoru icin '0', muhasebe sektoru icin '1', insaat sektoru icin '2', diger secenekler icin '3' girisi yapiniz: "))
        if sektor_secimi in range(4):
            self.__sektor = sektorler[sektor_secimi]
        else:
            print("Hatali giris yaptiniz!")

    def get_sektor(self):
        return self.__sektor

    def get_tecrube(self):
        return self.__tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self,maas):
        self.__maas = maas 

    def zam_hakki(self):
        zamorani = 0
        yenimaas = 0
        try:
            self.__maas = float(self.__maas)
            self.__tecrube = float(self.__tecrube)
            if self.__tecrube < 2:
                zamorani = 0
            elif self.__tecrube >= 2 and self.__tecrube <= 4 and self.__maas < 15000:
                zamorani = (self.__maas % self.__tecrube)
                self.__maas = self.__maas + (self.__maas * zamorani)
                
            elif self.__tecrube > 4 and self.__maas < 25000:
                zamorani = (self.__maas % self.__tecrube) / 2
                self.__maas = self.__maas + (self.__maas * zamorani)
                
        except ValueError:
            print("Girilen maas ve tecrube sayi olmalidir!")

    def __str__(self):
        return f"Ad: {self.get_ad()}, Soyad: {self.get_soyad()}, Tecrube: {self.get_tecrube()}, Maas: {self.get_maas()}"

