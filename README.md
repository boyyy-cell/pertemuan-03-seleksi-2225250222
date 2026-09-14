# Pertemuan 03 Seleksi Python

## Identitas

Nama: Farid Syahputra
NIM: 2225250222
Kelas: 3F

## Tujuan

Membuat program Python menggunakan struktur seleksi `if`, `if-else`, dan `nested if` untuk menganalisis persamaan kuadrat.

## Cara Menjalankan

Jalankan program melalui terminal VS Code dengan perintah:

```bash
python tugas/analisis_persamaan_kuadrat.py
```

Jika menggunakan `python3`:

```bash
python3 tugas/analisis_persamaan_kuadrat.py
```

## Algoritma Tugas

1. Memasukkan nilai koefisien `a`, `b`, dan `c`.
2. Memeriksa apakah `a` sama dengan 0.
3. Jika `a = 0`, program menampilkan bahwa input bukan persamaan kuadrat.
4. Jika `a` tidak sama dengan 0, menghitung diskriminan dengan rumus:

   `D = b² - 4ac`
5. Jika `D > 0`, program menghitung dan menampilkan dua akar real yang berbeda.
6. Jika `D = 0`, program menghitung dan menampilkan satu akar real kembar.
7. Jika `D < 0`, program menampilkan bahwa tidak ada akar real.

## Hasil Pengujian

| No. |  a |  b |  c | Hasil                        |
| --- | -: | -: | -: | ---------------------------- |
| 1   |  1 | -5 |  6 | Dua akar real: 3.00 dan 2.00 |
| 2   |  1 |  2 |  1 | Akar real kembar: -1.00      |
| 3   |  1 |  0 |  1 | Tidak ada akar real          |
| 4   |  0 |  2 |  3 | Bukan persamaan kuadrat      |

Semua test case menghasilkan keluaran sesuai dengan yang diharapkan.

## Refleksi

Kesalahan logika yang perlu diperhatikan adalah menentukan kondisi diskriminan dengan tepat. Program harus membedakan tiga kondisi, yaitu `D > 0`, `D = 0`, dan `D < 0`. Pengujian beberapa test case membantu memastikan setiap cabang program berjalan dengan benar.

## Kesimpulan

Program berhasil menganalisis persamaan kuadrat berdasarkan nilai koefisien dan diskriminan menggunakan struktur `nested if`.
