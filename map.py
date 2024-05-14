# Anggota Kelompok 3 kelas E 20023
# 1. Ronald  Budi Abdul Wahid (23091397142)
# 2. M.Inbu Nadhif A.(23091397161)
# 3. Refany Dwi Lestari(23091397170)

class Map():
    def __init__(self):
        self.daftarKota = {}
        self.jumlahKota = 0
    
    def tampilkanPeta(self):
        for kota in self.daftarKota:
            print(f"{kota}")
            for kotaSebelah, jarak in self.daftarKota[kota].items():
                print(f"\t--> {jarak} km -- {kotaSebelah}")
        print(f"Jumlah Kota: {self.jumlahKota}")
    
    def tambahkanKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
            self.jumlahKota += 1
    
    def tambahkanJalan(self, kota1, kotaKota):
        for kota in kotaKota:
            if kota1 in self.daftarKota and kota in self.daftarKota:
                self.daftarKota[kota1][kota] = kotaKota[kota]
                self.daftarKota[kota][kota1] = kotaKota[kota]
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
            self.jumlahKota -= 1
    
    def hapusJalan(self, kota1, kota2):
        if kota1 in self.daftarKota and kota2 in self.daftarKota[kota1]:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]

    def dijkstra(self, kota_awal):
        kota_yang_belum_dikunjungi = [*self.daftarKota.keys()]
        jarak = {kota: float("inf") for kota in kota_yang_belum_dikunjungi}
        jarak[kota_awal] = 0
        rute = {}

        while kota_yang_belum_dikunjungi:
            kota_Terdekat = min(kota_yang_belum_dikunjungi, key=lambda kota: jarak[kota])
            
            for tetangga, jarak_ke_tetangga in self.daftarKota[kota_Terdekat].items():
                total_jarak = round(jarak[kota_Terdekat] + jarak_ke_tetangga, 1)
                if total_jarak < jarak[tetangga]:
                    jarak[tetangga] = total_jarak
                    rute[tetangga] = kota_Terdekat
            
            kota_yang_belum_dikunjungi.remove(kota_Terdekat)
        
        del jarak[kota_awal]
        return jarak, rute

kotaKota = ["Semarang", "Salatiga", "Pekalongan", "Magelang", "Tegal", "Surakarta", "Kudus", "Klaten", "Jepara", "Purwodadi", "Demak"]

petaJawatengah = Map()
for kota in kotaKota:
    petaJawatengah.tambahkanKota(kota)

petaJawatengah.tambahkanJalan("Semarang", {"Salatiga": 61, "Pekalongan": 94, "Magelang": 83})
petaJawatengah.tambahkanJalan("Salatiga", {"Tegal": 219, "Surakarta": 61, "Magelang": 82})
petaJawatengah.tambahkanJalan("Magelang", {"Kudus": 134, "Klaten": 79, "Jepara": 154})
petaJawatengah.tambahkanJalan("Purwodadi", {"Demak": 39, "Pekalongan": 169, "Kudus": 47})
petaJawatengah.tambahkanJalan("Demak", {"Tegal": 209, "Semarang": 36, "Klaten": 149})

print("=== Peta Jawa Tengah ===")
petaJawatengah.tampilkanPeta()

[jarak, rute] = petaJawatengah.dijkstra("Semarang")
print(jarak)
print(rute)
