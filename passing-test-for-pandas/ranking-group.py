penjualan = [
    {"produk": "Roti", "kategori": "makanan", "qty": 10, "harga": 8000},
    {"produk": "Susu", "kategori": "minuman", "qty": 5, "harga": 15000},
    {"produk": "Mie Instan", "kategori": "makanan", "qty": 12, "harga": 3500},
    {"produk": "Kopi Sachet", "kategori": "minuman", "qty": 20, "harga": 2500},
    {"produk": "Biskuit", "kategori": "makanan", "qty": 7, "harga": 9000},
    {"produk": "Air Mineral", "kategori": "minuman", "qty": 15, "harga": 4000},
    {"produk": "Sabun Cair", "kategori": "kebutuhan_rumah", "qty": 6, "harga": 18000},
    {"produk": "Shampoo", "kategori": "kebutuhan_rumah", "qty": 4, "harga": 22000}
]

def specific_ranking(data,kategori):
    ranking = []
    total_kategori = 0

    for item in data:
        if item["kategori"] == kategori:
            total_kategori += 1

    while len(ranking) < total_kategori:
        omzet_tertinggi = 0
        produk_tertinggi = ""

        for item in data:
            omzet = item["harga"] * item["qty"]
            sudah_masuk = False

            for rank in ranking:
                if rank["produk"] == item["produk"]:
                    sudah_masuk = True

            if not sudah_masuk and omzet > omzet_tertinggi and item["kategori"] == kategori:
                omzet_tertinggi = omzet
                produk_tertinggi = item["produk"]

        ranking.append({'produk': produk_tertinggi, "omzet": omzet_tertinggi})
    return ranking
print(specific_ranking(penjualan,"minuman"))