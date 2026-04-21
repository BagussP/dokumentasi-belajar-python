# soal 1
1. buat function get_summary yang memiliki parameter data, minimum
2. lalu buat variable summary = {} di dalam function dan buat variable omzet_total =item["qty"] * item["harga"]
3. loop parameter data
4. buat logika apakah omzet lebih besar dari parameter minimum
    ## true
    1. buat pengecekan ulang kategori data ada di summary
        ## true
        1. isi summary total_qty, total_omzet, jumlah_transaksi nilai awalnya masing-masing 0
    2. tambahkan total_qty, total_omzet, jumlah_transaksi dengan rumusnya masing-masing
5. return variable summary

# soal 2
1. buat function get_highest parameternya data, find
2. buat variable highest = {}
3. lalu looping parameter data dengan tambahan function items() supaya dapat melakukan key dan value
4. cek apakah key tidak ada di highest or value[find] > highest[find]
5. kita rubah highest menjadi value[find] seperti ini  highest= {"kategori": key, find: value[find]}
6. return highest