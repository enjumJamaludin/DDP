from Animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, gender, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.gender = gender
        self.warna_sisit = warna 

    def info_Ikan(self):
        super().info_animal(),
        print("gender \t\t\t : ", self.gender,
              "\nWarna \t\t\t : ", self.warna_sisit)
        
Ikan_Barakuda = Ikan("Barakuda", "yang ada di laut", "Air", "Bertelur", "Jantan", "hitam & silver")
Ikan_Barakuda.info_Ikan()
print("===============================")
Ikan_Hiu = Ikan("Hiu", "Ikan kecil", "Air", "bertelur", "Betina", "Biru & silver")
Ikan_Hiu.info_Ikan()