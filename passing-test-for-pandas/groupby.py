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

def group_by(data):
    summary = {}

    for item in data:
        omzet = item["harga_jual"] * item["qty"]
        laba = (item["harga_jual"] - item["modal"]) * item["qty"]
        if item["kategori"] not in summary:
            summary[item["kategori"]]= {
                "total_qty": item["qty"],
                "total_omzet": omzet,
                "total_laba": laba  
            }
        else:
            summary[item["kategori"]]["total_qty"] += item["qty"]
            summary[item["kategori"]]["total_omzet"] += omzet
            summary[item["kategori"]]["total_laba"] += laba
    return summary

print(group_by(penjualan))