penjualan = [
    {"produk": "Roti", "qty": 10, "harga": 8000},
    {"produk": "Susu", "qty": 5, "harga": 15000},
    {"produk": "Mie Instan", "qty": 12, "harga": 3500},
    {"produk": "Kopi Sachet", "qty": 20, "harga": 2500},
    {"produk": "Biskuit", "qty": 7, "harga": 9000},
    {"produk": "Air Mineral", "qty": 15, "harga": 4000}
]

def total_omzet(data):
    total = 0

    for item in data:
        omzet = item["qty"] * item["harga"]
        total += omzet

    return total

print(total_omzet(penjualan))
