class Kasir:
    daftar_harga = {
        1: {"nama": "Acer Predator 21x", "harga": 125000000},
        2: {"nama": "MSI GT75 Titan 4K-012l", "harga": 85000000},
        3: {"nama": "Razer Blade 15", "harga": 69000000},
        4: {"nama": "ASUS ROG Mothership GZ", "harga": 60000000},
        5: {"nama": "Dell Alienware AREA-51M", "harga": 50000000}
    }

    def __init__(self):
        self.keranjang = {}

    def tampilkan_daftar_harga(self):
        print("Daftar Barang:")
        for nomor, barang in self.daftar_harga.items():
            print(f"{nomor}. {barang['nama']} - Rp{barang['harga']}")

    def tambah_barang(self):
        self.tampilkan_daftar_harga()
        try:
            nomor_barang = int(input("\nMasukkan nomor barang yang ingin dibeli: "))
            if nomor_barang in self.daftar_harga:
                barang = self.daftar_harga[nomor_barang]
                jumlah = int(input(f"Masukkan jumlah untuk {barang['nama']}: "))
                
                if barang["nama"] in self.keranjang:
                    self.keranjang[barang["nama"]]["jumlah"] += jumlah
                else:
                    self.keranjang[barang["nama"]] = {"harga": barang["harga"], "jumlah": jumlah}
                
                print(f"{barang['nama']} sebanyak {jumlah} telah ditambahkan ke keranjang.\n")
            else:
                print("Nomor barang tidak valid.\n")
        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan angka yang benar.\n")

    def tampilkan_daftar_barang(self):
        if not self.keranjang:
            print("Keranjang kosong.")
            return
        print("Daftar Barang di Keranjang:")
        for nama_barang, detail in self.keranjang.items():
            harga = detail["harga"]
            jumlah = detail["jumlah"]
            print(f"- {nama_barang}: {jumlah} x Rp{harga} = Rp{harga * jumlah}")
        print()  

    def hitung_total_harga(self):
        total = sum(detail["harga"] * detail["jumlah"] for detail in self.keranjang.values())
        print(f"Total harga: Rp{total}")
        return total

    def cetak_struk(self):
        print("\n--- Struk Pembelian ---")
        self.tampilkan_daftar_barang()
        total = self.hitung_total_harga()
        print(f"Total: Rp{total}")
        print("--- Terima Kasih ---\n")

kasir = Kasir()

while True:
    print("Menu:")
    print("1. Tambah barang ke keranjang")
    print("2. Tampilkan daftar barang di keranjang")
    print("3. Hitung total harga")
    print("4. Cetak struk dan keluar")
    
    pilihan = input("Pilih menu (1/2/3/4): ")
    
    if pilihan == "1":
        kasir.tambah_barang()
    elif pilihan == "2":
        kasir.tampilkan_daftar_barang()
    elif pilihan == "3":
        kasir.hitung_total_harga()
    elif pilihan == "4":
        kasir.cetak_struk()
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang benar.\n")
