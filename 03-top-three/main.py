penjualan = [
    {"produk": "Air Mineral", "kategori": "minuman", "qty": 24, "harga": 3500},
    {"produk": "Roti Coklat", "kategori": "makanan", "qty": 12, "harga": 6000},
    {"produk": "Kopi Sachet", "kategori": "minuman", "qty": 18, "harga": 2500},
    {"produk": "Mie Goreng", "kategori": "makanan", "qty": 20, "harga": 3500},
    {"produk": "Sabun Mandi", "kategori": "kebutuhan_rumah", "qty": 7, "harga": 12000},
    {"produk": "Shampoo", "kategori": "kebutuhan_rumah", "qty": 5, "harga": 18000},
    {"produk": "Tisu", "kategori": "kebutuhan_rumah", "qty": 9, "harga": 10000},
    {"produk": "Susu Kotak", "kategori": "minuman", "qty": 8, "harga": 9500},
    {"produk": "Biskuit", "kategori": "makanan", "qty": 10, "harga": 8500},
    {"produk": "Pulpen", "kategori": "ATK", "qty": 15, "harga": 4000}
]

def get_ranking(data):
    ranking = []

    while len(ranking) < len(data):
        omzet_terbesar = 0
        produk_terbesar = ""

        for item in data:
            omzet = item["harga"] * item["qty"]
            sudah_masuk = False

            for rank in ranking:
                if rank["produk"] == item["produk"]:
                    sudah_masuk = True
                
            if not sudah_masuk and omzet > omzet_terbesar:
                omzet_terbesar = omzet
                produk_terbesar = item["produk"]

        ranking.append({"produk": produk_terbesar, "omzet": omzet_terbesar})   
    return ranking
print(get_ranking(penjualan))