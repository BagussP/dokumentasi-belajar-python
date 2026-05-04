1. buat function top_three yang mempunyai parameter data
2. buat variable ranking untuk menjadi wadah
3. kita loop while yang dimana kondisinya jika panjang ranking tidak lebih dari 3 maka akan terus loop
    1. buat variable laba_tertinggi dan produk tertinggi
    2. kita loop data supya bisa diakses 1 per 1
        1. buat variable lagi sudah_masuk bernilai false
        2. buat loop ranking
            1. buat pengecekan apakah produk sudah ada di ranking
                ##
                1. kita buat sudah_masuk menjadi true
        3. buat pengecekan apakh sudah_masuk bernilai falsy dan item["produk"] nilainya lebih tinggi dari produk tertinggi
            1. maka kita akan nilai laba_tertinggi dengan laba sekarang
    3. maka ranking akan ditambahkan dengan nilai laba_tertinggi
4. return ranking
        