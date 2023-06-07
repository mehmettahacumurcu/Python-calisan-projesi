from insan import Insan

class Issiz(Insan):
    def __init__(self,tc_no,ad,soyad,yas,cinsiyet,uyruk):
        super().__init__(tc_no,ad,soyad,yas,cinsiyet,uyruk)
        self._tecrube = {"maviyaka":[],"beyazyaka":[],"yonetici":[]}
        self._enuygunstatu = ""
        self._enuygunstatu_deger = 0
        
    def statu_bul(self):
        maviyaka_tecrube = self._tecrube.get("maviyaka")
        maviyaka_max = 0
        for deger in maviyaka_tecrube:
            if deger > maviyaka_max:
                maviyaka_max = deger
        beyazyaka_tecrube = self._tecrube.get("beyazyaka")
        beyazyaka_max = 0
        for deger in beyazyaka_tecrube:
            if deger > beyazyaka_max:
                beyazyaka_max = deger
        yonetici_tecrube = self._tecrube.get("yonetici")
        yonetici_max = 0
        for deger in yonetici_tecrube:
            if deger > yonetici_max:
                yonetici_max = deger

        try:
            maviyaka_max *= 1/5
            beyazyaka_max *= 35/100
            yonetici_max *= 45/100

        except ValueError:
            print("Bulunan degerler 10'luk tabana uygun degil.")

        if maviyaka_max > beyazyaka_max and maviyaka_max > yonetici_max:
            self._enuygunstatu = "maviyaka"
            self._enuygunstatu_deger = maviyaka_max
        elif beyazyaka_max > maviyaka_max and beyazyaka_max > yonetici_max:
            self._enuygunstatu = "beyazyaka"
            self._enuygunstatu_deger = beyazyaka_max
        else:
            self._enuygunstatu = "yonetici"
            self._enuygunstatu_deger = yonetici_max

        return self._enuygunstatu , self._enuygunstatu_deger

    def __str__(self):
        return f"Ad : {self.get_ad} ,  Soyad : {self.get_soyad()} , Yas : {self.get_yas()} , Cinsiyet : {self.get_cinsiyet()} , Uyruk : {self.get_uyruk()} , "
        
        
        
    

 







