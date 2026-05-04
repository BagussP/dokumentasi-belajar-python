penjualan = [
    {"produk": "Roti", "kategori": "makanan", "qty": 10, "harga_jual": 8000, "modal": 5000},
    {"produk": "Susu", "kategori": "minuman", "qty": 5, "harga_jual": 15000, "modal": 10000},
    {"produk": "Mie Instan", "kategori": "makanan", "qty": 12, "harga_jual": 3500, "modal": 2500},
    {"produk": "Kopi Sachet", "kategori": "minuman", "qty": 20, "harga_jual": 2500, "modal": 1500},
    {"produk": "Biskuit", "kategori": "makanan", "qty": 7, "harga_jual": 9000, "modal": 6000},
    {"produk": "Air Mineral", "kategori": "minuman", "qty": 15, "harga_jual": 4000, "modal": 2500},
    {"produk": "Sabun Cair", "kategori": "kebutuhan_rumah", "qty": 6, "harga_jual": 18000, "modal": 11000},
    {"produk": "Shampoo", "kategori": "kebutuhan_rumah", "qty": 4, "harga_jual": 22000, "modal": 15000}
]

def top_three(data):
    ranking = []

    while len(ranking) < 3:
        laba_tertinggi = 0 
        produk_tertinggi = ""

        for item in data:
            laba = (item["harga_jual"] - item["modal"]) * item["qty"]
            sudah_masuk = False

            for rank in ranking:
                if rank["produk"] == item["produk"]:
                    sudah_masuk = True

            if not sudah_masuk and laba > laba_tertinggi:
                laba_tertinggi = laba
                produk_tertinggi = item["produk"]
        
        ranking.append({"produk":produk_tertinggi, "laba":laba_tertinggi})
    return ranking

print(top_three(penjualan))