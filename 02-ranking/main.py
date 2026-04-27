penjualan = [
    {"produk": "Roti", "qty": 10, "harga_jual": 8000, "modal": 5000},
    {"produk": "Susu", "qty": 6, "harga_jual": 15000, "modal": 10000},
    {"produk": "Telur", "qty": 12, "harga_jual": 3000, "modal": 2000},
    {"produk": "Keju", "qty": 3, "harga_jual": 25000, "modal": 15000},
    {"produk": "Coklat", "qty": 5, "harga_jual": 12000, "modal": 7000},
    {"produk": "Air Mineral", "qty": 20, "harga_jual": 4000, "modal": 2500},
    {"produk": "Mie Cup", "qty": 8, "harga_jual": 9000, "modal": 6000},
    {"produk": "Biskuit", "qty": 4, "harga_jual": 18000, "modal": 10000}
]

def ranking_laba(data):
    ranking=[]
    counter = 0
    produk = ''
    while len(ranking) < len(data):
        for item in data:
            total_laba = (item["harga_jual"] - item["modal"]) * item["qty"]
            sudah_masuk = False

            for rank in ranking:
                if item["produk"] == rank["produk"]:
                    sudah_masuk=True

            if sudah_masuk:
                continue
            elif total_laba > counter:
                counter = total_laba
                produk = item["produk"]

        ranking.append({"produk":produk, "laba": counter})        
        counter=0
        produk=''        

    return ranking

print(ranking_laba(penjualan))