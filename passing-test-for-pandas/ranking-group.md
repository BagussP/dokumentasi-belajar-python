1. buat function specific_ranking dengan parameter data dan kategori
2. buat variable ranking untuk menjadi wadah dan total_kategori
3. kita loop data untuk mencari total_kategori
    1. if item["kategori"] nilainya sama dengan kategori maka total_kategori bertambah 1
4. baru kita bikin while selama panjang ranking tidak melebihi total_kategori
    1. kita bikin variable sebagai wadah produk_tertinggi dan omzet_tertinggi
    2. kita loop data untuk bisa akses 1 per 1 yang bertujuan untuk pencocokan nilai
        1. buat variable sudah_masuk bernilai falsy dan omzet yang berisi rumud dan hasil omzet data yang diakses sekarang
        2. lalu kita loop ranking 
            1. buat pengecekan if lagi apakah item["produk"] sudah ada di ranking
                1. maka nilai sudah_masuk kita ubah menjadi true
        3. buat pengecekan ulang jika sudah masuk bernilai falsy dan omzet lebih besar omzet_tertinggi dan kategorinya sama sesuai yang ditentukan parameter
            1. maka nilai omzet_tertinggi akan digantikan oleh omzet
    3. kita tambahkan nilai omzet_tertinggi ke ranking
5. return ranking