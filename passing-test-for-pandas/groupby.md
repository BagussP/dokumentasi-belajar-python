1. buat function group_by parameter data
2. buat wadah untuk menampung hasil yang diberi nama summary
3. lalu kita looping data supaya bisa diakses 1 per 1
    1. kita buat wadah untuk tiap-tiap rumus
    2. kita buat pengecekan apakah kategori saat ini ada di summary
        ## jika tidak ada 
        1. kita tambahkan datanya ke summary. contoh seperti ini  
        item["kategori"]: {
        "total_qty": item["qty"],
        "total_omzet": omzet,
        "total_laba": laba  
        }
        ## jika sudah ada
        1. kita hanya perlu update data yang sebelumnya
4. return summary