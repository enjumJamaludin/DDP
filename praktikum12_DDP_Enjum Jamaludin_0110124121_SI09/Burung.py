from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.paruh = paruh
        self.warna_bulu = warna_bulu

    def info_burung(self):
        super().info_animal(),
        print("Paruh \t\t\t : ", self.paruh,
              "\nWarna Bulu \t\t : ", self.warna_bulu)
        
Burung_Kenari = Burung("Kenari", "Jagung dan biji-bijian", "Udara dan di darat", "Bertelur", "melengkung", "Warna warni")
Burung_Kenari.info_burung()
print("===============================")
Burung_Kakatua = Burung("Kakatua", "Jagung dan biji-bijian", "Udara dan di darat", "Bertelur", "Melengkung", "putih")
Burung_Kakatua.info_burung()


