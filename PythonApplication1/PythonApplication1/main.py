from issiz import Issiz
from insan import Insan
from Calisan import calisan
from MaviYaka import maviyaka
from BeyazYaka import beyazyaka 
import pandas as pd



insan1 = Insan("58191758294", "Ahmet", "Korkmaz", 25, "Erkek", "Turk")
insan2 = Insan("92847582196","John","MacTavish",28,"Erkek","Ingiliz")
print(insan1.__str__())
print(insan2.__str__())



issiz1 = Issiz("12397752264","Taha","Cumurcu",23,"Erkek","Turk")
issiz1.set_tecrube('yonetici',5)
issiz2 = Issiz("86756629385","Mert","Kabalci",19,"Erkek","Turk")
issiz2.set_tecrube("maviyaka",3)
issiz2.set_tecrube("beyazyaka",7)
issiz3 = Issiz("82968495592","John","Price",38,"Erkek","Ingiliz")
issiz3.set_tecrube("yonetici",8)
issiz3.set_tecrube("maviyaka",15)
print(issiz1.__str__() , "1.Issiz icin en uygun statu :" ,issiz1.statu_bul() )
print(issiz2.__str__() , "2.Issiz icin en uygun statu :" ,issiz2.statu_bul() )
print(issiz3.__str__() , "3.Issiz icin en uygun statu :" ,issiz3.statu_bul() )

 
print("Calisan Uyeleri")
calisan1 = calisan("75482295564","Bruce","Wayne",35,"Erkek","Amerikan",5,15000)
calisan1.set_sektor()
calisan1.zam_hakki()
print(calisan1.__str__())
calisan2 = calisan("55609956795","Harvey","Specter",37,"Erkek","Amerikan",15,500000)
calisan2.set_sektor()
calisan2.zam_hakki()
print(calisan2.__str__())
calisan3 = calisan("57682978812","Margot","Robbie",34,"Kadin","Amerikan",5,19000)
calisan3.set_sektor()
calisan3.zam_hakki()
print(calisan3.__str__())
print("--------------------")

 
print("Maviyaka Uyeleri")
maviyaka1 = maviyaka("72859675296","Jessica","Pearson",41,"Kadin","Amerikan",22,550000)
maviyaka1.zam_hakki()
print(maviyaka1.__str__())
maviyaka2 = maviyaka("6572819201","Matthew","Mcconaughey",43,"Erkek","Amerikan",28,1000)
maviyaka2.zam_hakki()
print(maviyaka2.__str__())
maviyaka3 = maviyaka("92785472286","Andrew","Tate",38,"Erkek","Amerikan",29,1000000)
maviyaka3.zam_hakki()
print(maviyaka3.__str__())
print("--------------------")

print("Beyazyaka Uyeleri")
beyazyaka1 = beyazyaka("86729358691","Ali","Cubuk",19,"Erkek","Turk",5,10000)
beyazyaka1.zam_hakki()
print(beyazyaka1.__str__())
beyazyaka2 = beyazyaka("12356692276","Mehmet","Caglar",22,"Erkek","Turk",5,22500)
beyazyaka2.zam_hakki()
print(beyazyaka2.__str__())
beyazyaka3 = beyazyaka("12764958922","Dwayne","Johnson",35,"Erkek","Amerikan",1,12000)
beyazyaka3.zam_hakki()
print(beyazyaka3.__str__())
print("--------------------")

uyeler = {"Uyeler:":["calisan","calisan","calisan","maviyaka","maviyaka","maviyaka","beyazyaka","beyazyaka","beyazyaka"],
          "TCNO:":[calisan1.get_tcno(),calisan2.get_tcno(),calisan3.get_tcno(),maviyaka1.get_tcno(),maviyaka2.get_tcno(),maviyaka3.get_tcno(),beyazyaka1.get_tcno(),beyazyaka2.get_tcno(),beyazyaka3.get_tcno()],
          "Ad:":[calisan1.get_ad(),calisan2.get_ad(),calisan3.get_ad(),maviyaka1.get_ad(),maviyaka2.get_ad(),maviyaka3.get_ad(),beyazyaka1.get_ad(),beyazyaka2.get_ad(),beyazyaka3.get_ad()],
          "Soyad:":[calisan1.get_soyad(),calisan2.get_soyad(),calisan3.get_soyad(),maviyaka1.get_soyad(),maviyaka2.get_soyad(),maviyaka3.get_soyad(),beyazyaka1.get_soyad(),beyazyaka2.get_soyad(),beyazyaka3.get_soyad()],
          "Yas:":[calisan1.get_yas(),calisan2.get_yas(),calisan3.get_yas(),maviyaka1.get_yas(),maviyaka2.get_yas(),maviyaka3.get_yas(),beyazyaka1.get_yas(),beyazyaka2.get_yas(),beyazyaka3.get_yas()],
          "Cinsiyet:":[calisan1.get_cinsiyet(),calisan2.get_cinsiyet(),calisan3.get_cinsiyet(),maviyaka1.get_cinsiyet(),maviyaka2.get_cinsiyet(),maviyaka3.get_cinsiyet(),beyazyaka1.get_cinsiyet(),beyazyaka2.get_cinsiyet(),beyazyaka3.get_cinsiyet()],
          "Uyruk:":[calisan1.get_uyruk(),calisan2.get_uyruk(),calisan3.get_uyruk(),maviyaka1.get_uyruk(),maviyaka2.get_uyruk(),maviyaka3.get_uyruk(),beyazyaka1.get_uyruk(),beyazyaka2.get_uyruk(),beyazyaka3.get_uyruk()],
          'Sektor':[calisan1.get_sektor(),calisan2.get_sektor(),calisan3.get_sektor(),0,0,0,0,0,0],
          "Tecrube":[calisan1.get_tecrube(),calisan2.get_tecrube(),calisan3.get_tecrube(),maviyaka1.get_tecrube(),maviyaka2.get_tecrube(),maviyaka3.get_tecrube(),beyazyaka1.get_tecrube(),beyazyaka2.get_tecrube(),beyazyaka3.get_tecrube()],
          "Maas:":[calisan1.get_maas(),calisan2.get_maas(),calisan3.get_maas(),maviyaka1.get_maas(),maviyaka2.get_maas(),maviyaka3.get_maas(),beyazyaka1.get_maas(),beyazyaka2.get_maas(),beyazyaka3.get_maas()],
          "Yipranma Payi:":[0,0,0,maviyaka1.get_yipranmapayi(),maviyaka2.get_yipranmapayi(),maviyaka3.get_yipranmapayi(),0,0,0],
          "Tesvik Primi:":[0,0,0,0,0,0,beyazyaka1.get_tesvikprimi(),beyazyaka2.get_tesvikprimi(),beyazyaka3.get_tesvikprimi()]
  }
df = pd.DataFrame(uyeler)
print(df)
#Maas Ortalamalari hesaplama
maasortalamalari = df.groupby("Uyeler:")['Maas:'].mean()
print(maasortalamalari)

#Maasi 15000'den fazla olanlari tespit etme
maasi15kdanfazlaolanlar = df[df['Maas:'] > 15000]
print(maasi15kdanfazlaolanlar)

#Maasa bagli dataframe'i duzenleme (en yuksekten en dusuge)
maasa_bagli_df = df.sort_values( by ='Maas:', ascending=False)
print(maasa_bagli_df)

# Tecrubesi 3 seneden fazla olan beyaz yakalilar
grup = (df["Uyeler:"] == "beyazyaka") & (df["Tecrube"] > 3)
beyazyaka_tecrube_istenilen = df[grup]
print(beyazyaka_tecrube_istenilen)

# Maasi 10000 tl'den fazla olup 2-5 arasinda olanlar
istenilen = (df["Maas:"]>10000) & (df.index >=2) & (df.index <= 5)
yazdirilacak = df.loc[istenilen,["TCNO:","Maas:"]]

#Alt dataframe
alt_df = df[["Ad:","Soyad:",'Sektor',"Maas:"]]
print(alt_df)








