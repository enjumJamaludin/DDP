from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, gender, warna_sisit):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.gender = gender
        self.warna_sisit = warna_sisit

    def info_ular(self):
        super().info_animal(),
        print("gender \t\t\t : ", self.gender,
              "\nWarna sisit \t\t : ", self.warna_sisit)
        
Ular_cobra = Ular("Cobra", "Daging hewan kecil", "Darat", "Bertelur", "Jantan", "Hitam")
Ular_cobra.info_ular()
print("===============================")
Ular_Python = Ular("Python", "Daging", "Darat", "B ertelur", "Betina", "Kuning")
Ular_Python.info_ular()