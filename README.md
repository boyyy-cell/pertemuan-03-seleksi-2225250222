# Pertemuan 03 Seleksi Python

## Identitas

Nama: Farid Syahputra
NIM: 2225250222
Kelas: 3F

## Tujuan

Membuat program Python menggunakan struktur seleksi if, if-else, dan nested if serta menguji program menggunakan beberapa test case.

## Cara Menjalankan

Jalankan program melalui terminal VS Code dengan perintah berikut:

    python latihan/01_genap_ganjil.py

    python latihan/02_bandingkan_dua_bilangan.py

    python latihan/03_kelulusan_bersyarat.py

    python latihan/04_jenis_segitiga.py

Untuk menjalankan tugas analisis persamaan kuadrat:

    python tugas/analisis_persamaan_kuadrat.py

## Algoritma Latihan

### 1. Genap atau Ganjil

1. Memasukkan sebuah bilangan bulat.
2. Memeriksa sisa pembagian bilangan dengan 2.
3. Jika sisa pembagian sama dengan 0, bilangan merupakan bilangan genap.
4. Jika tidak, bilangan merupakan bilangan ganjil.

### 2. Membandingkan Dua Bilangan

1. Memasukkan dua bilangan.
2. Membandingkan bilangan pertama dengan bilangan kedua.
3. Menggunakan nested if untuk menentukan apakah bilangan pertama lebih besar, lebih kecil, atau sama dengan bilangan kedua.

### 3. Kelulusan Bersyarat

1. Memasukkan nilai dan persentase kehadiran.
2. Memeriksa apakah nilai minimal 60 dan kehadiran minimal 80%.
3. Jika kedua kondisi terpenuhi, program menampilkan Lulus.
4. Jika salah satu kondisi tidak terpenuhi, program menampilkan Belum lulus.

### 4. Jenis Segitiga

1. Memasukkan tiga panjang sisi.
2. Memeriksa apakah semua sisi bernilai positif.
3. Memeriksa apakah ketiga sisi dapat membentuk segitiga.
4. Jika ketiga sisi sama, program menampilkan segitiga sama sisi.
5. Jika dua sisi sama, program menampilkan segitiga sama kaki.
6. Jika semua sisi berbeda, program menampilkan segitiga sembarang.
7. Jika tidak memenuhi syarat segitiga, program menampilkan Bukan segitiga.

## Algoritma Tugas Analisis Persamaan Kuadrat

Program menganalisis persamaan ax² + bx + c = 0.

1. Memasukkan nilai koefisien a, b, dan c.
2. Memeriksa apakah a = 0.
3. Jika a = 0, program menampilkan bahwa input bukan persamaan kuadrat.
4. Jika a != 0, program menghitung diskriminan dengan rumus D = b² - 4ac.
5. Jika D > 0, program menghitung dan menampilkan dua akar real yang berbeda.
6. Jika D = 0, program menghitung dan menampilkan satu akar real kembar.
7. Jika D < 0, program menampilkan bahwa tidak ada akar real.
8. Nilai akar ditampilkan dengan dua angka di belakang koma.

## Hasil Pengujian

### Latihan 1 - Genap atau Ganjil

| No. | Input | Expected Output | Actual Output | Status |
|---|---:|---|---|---|
| 1 | 8 | Genap | 8 adalah bilangan genap. | PASS |
| 2 | 13 | Ganjil | 13 adalah bilangan ganjil. | PASS |
| 3 | 0 | Genap | 0 adalah bilangan genap. | PASS |
| 4 | -7 | Ganjil | -7 adalah bilangan ganjil. | PASS |

### Latihan 2 - Membandingkan Dua Bilangan

| No. | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| 1 | 7, 4 | Bilangan pertama lebih besar | Bilangan pertama lebih besar. | PASS |
| 2 | 2, 9 | Bilangan pertama lebih kecil | Bilangan pertama lebih kecil. | PASS |
| 3 | 5, 5 | Kedua bilangan sama | Kedua bilangan sama. | PASS |
| 4 | -3, -8 | Bilangan pertama lebih besar | Bilangan pertama lebih besar. | PASS |

### Latihan 3 - Kelulusan Bersyarat

| No. | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| 1 | Nilai 75, Kehadiran 90 | Lulus | Lulus | PASS |
| 2 | Nilai 59, Kehadiran 90 | Belum lulus | Belum lulus | PASS |
| 3 | Nilai 75, Kehadiran 79 | Belum lulus | Belum lulus | PASS |
| 4 | Nilai 60, Kehadiran 80 | Lulus | Lulus | PASS |

### Latihan 4 - Jenis Segitiga

| No. | Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| 1 | 3, 3, 3 | Segitiga sama sisi | Segitiga sama sisi. | PASS |
| 2 | 5, 5, 8 | Segitiga sama kaki | Segitiga sama kaki. | PASS |
| 3 | 3, 4, 5 | Segitiga sembarang | Segitiga sembarang. | PASS |
| 4 | 1, 2, 3 | Bukan segitiga | Bukan segitiga. | PASS |

### Tugas - Analisis Persamaan Kuadrat

| No. | Input (a, b, c) | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| 1 | (1, -5, 6) | Dua akar real: 3.00 dan 2.00 | Dua akar real: x1 = 3.00, x2 = 2.00 | PASS |
| 2 | (1, 2, 1) | Akar real kembar: -1.00 | Akar real kembar: x = -1.00 | PASS |
| 3 | (1, 0, 1) | Tidak ada akar real | Tidak ada akar real. | PASS |
| 4 | (0, 2, 3) | Bukan persamaan kuadrat | Bukan persamaan kuadrat. | PASS |

Semua test case menghasilkan keluaran sesuai dengan yang diharapkan.

## Refleksi

Kesalahan logika yang perlu diperhatikan adalah menentukan kondisi seleksi dengan tepat, terutama pada nilai batas dan kondisi diskriminan.

Pada analisis persamaan kuadrat, program harus membedakan tiga kondisi diskriminan, yaitu D > 0, D = 0, dan D < 0. Kondisi a = 0 juga harus diperiksa terlebih dahulu agar program tidak melakukan perhitungan akar ketika nilai a adalah nol.

Pengujian beberapa test case membantu memastikan setiap cabang program berjalan dengan benar.

## Kesimpulan

Program berhasil menerapkan struktur seleksi if, if-else, dan nested if pada latihan seleksi Python dan analisis persamaan kuadrat.

Seluruh test case yang diberikan telah diuji dan menghasilkan keluaran sesuai dengan yang diharapkan.