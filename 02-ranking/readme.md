1. pertama kita buat function ranking_laba yang memiliki parameter data
2. kita buat variable ranking yang nantinya dijadikan sebagai menyimpan nilai ranking untuk di return dan counter untuk menyimpan nilai tertinggi sementara dan produk
3. lalu membuat loop while yang mengecek kondisi apakah panjang ranking sudah lebih kecil dari panjang data yang ada
    ## true
    1. loop data supaya bisa diakses nilainya satu per satu
    2. lalu kita buat rumusnya supaya tidak menulis ulang rumus yang sedikit panjang
    3. lalu kita buat variable sudah_masuk yang nantinya untuk mengecek apakah produk ini sudah ada di ranking
    4. kita loop ranking supaya bisa mengecek apakah item produk ada di ranking
        ### true
        1. jika item produk sudah ada di ranking maka kita buat nilainya menjadi true
    5. kita buat pengecekan apakah sudah masuk bernilai true?
        ### true
        1. kita skip data ini
    6. kita buat pengecekan lagi total_laba apakah lebih besar dari counter?
        ### true
        1. maka counter akan dirubah menjadi total_laba data saat ini
        2. maka produk akan dirubah menjadi data saat ini
    7. ketika loopingan selesai maka data yang didapat akan ditambahkan dengan ranking.append({"produk":produk, "laba": counter})  
4. return ranking