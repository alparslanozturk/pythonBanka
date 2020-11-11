

class Hesap:
    def __init__(self, adim = "adsiz", numaram = "1", bakiyem = "0" ):
        self.ad = adim
        self.num = numaram
        self.bak = bakiyem
    def bilgi(self):
        print("----------------------------")
        print("Ad Soyad:", self.ad )
        print("Numara", self.num )
        print("Bakiye:", self.bak )
        print("----------------------------")
    def paraCek(self, miktar = 0):
        if( self.bak - miktar < 0):
            print("bakiyeniz yetersizdir.")
        else:
            self.bak -= miktar
            print("Yeni Bakiyeniz:", self.bak )
    def paraYatir(self, miktar = 0):
        self.bak += miktar
        print("Yeni Bakiyeniz:", self.bak )


hesabim = Hesap("Alparslan Ozturk", 12345, 1000)
hesabim.bilgi()
hesabim.paraCek(1200)
hesabim.paraCek(800)
hesabim.paraYatir(800)
hesabim.bilgi()


