penjualan = [
    {"produk": "Sabun", "kategori": "kebutuhan_rumah", "qty": 3, "harga": 12000},
    {"produk": "Shampoo", "kategori": "kebutuhan_rumah", "qty": 2, "harga": 18000},
    {"produk": "Pulpen", "kategori": "ATK", "qty": 4, "harga": 6000},
    {"produk": "Beras", "kategori": "makanan", "qty": 1, "harga": 70000},
    {"produk": "Teh", "kategori": "minuman", "qty": 5, "harga": 5000},
    {"produk": "Kopi", "kategori": "minuman", "qty": 2, "harga": 15000},
    {"produk": "Buku Tulis", "kategori": "ATK", "qty": 3, "harga": 9000},
    {"produk": "Mie Instan", "kategori": "makanan", "qty": 6, "harga": 3500}
]

def get_summary(data, minimum):
    summary = {}
    for item in data:
        omzet_total = item["harga"] * item["qty"]
        if omzet_total >= minimum:
            if item["kategori"] not in summary:
                summary[item["kategori"]] = {
                    "total_omzet": 0,
                    "total_qty":0,
                    "total_transaksi":0
                }
            summary[item["kategori"]]["total_omzet"] += omzet_total
            summary[item["kategori"]]["total_qty"] += item["qty"]
            summary[item["kategori"]]["total_transaksi"] += 1
    return summary

def get_highest(data,find):
    highest = {}
    for key,value in data.items():
        if not highest or value[find] > highest[find]:
            highest= {"kategori": key, find: value[find]}

    return highest


print(get_highest(get_summary(penjualan, 25000),"total_qty"))
print(get_summary(penjualan, 25000))

