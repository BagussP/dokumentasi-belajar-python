penjualan = [
    {"produk": "Roti", "qty": 10, "harga_jual": 8000, "modal": 5000},
    {"produk": "Susu", "qty": 5, "harga_jual": 15000, "modal": 10000},
    {"produk": "Mie Instan", "qty": 12, "harga_jual": 3500, "modal": 2500},
    {"produk": "Kopi Sachet", "qty": 20, "harga_jual": 2500, "modal": 1500},
    {"produk": "Biskuit", "qty": 7, "harga_jual": 9000, "modal": 6000},
    {"produk": "Air Mineral", "qty": 15, "harga_jual": 4000, "modal": 2500}
]

def summary_laba(data):
    summary = {"total_qty":0,
               "total_omzet":0,
               "total_laba":0}
    
    for item in data:
        omzet = item["harga_jual"] * item["qty"]
        laba = (item["harga_jual"] - item["modal"]) * item["qty"]

        summary["total_qty"] += item["qty"]
        summary["total_omzet"] += omzet
        summary["total_laba"] += laba
    return summary

print(summary_laba(penjualan))