# Dokumentasi Algoritma RSA (Rivest-Shamir-Adleman)

Repositori ini berisi implementasi sederhana dari algoritma kriptografi asimetris **RSA** menggunakan bahasa pemrograman Python. Kode ini dirancang untuk mendemonstrasikan proses pembangkitan kunci, enkripsi, dan dekripsi secara bertahap tanpa menggunakan *library* kriptografi instan.

> **Tujuan:** Pembelajaran akademik dan pemahaman konsep dasar matematika RSA.

---

## Langkah-Langkah Eksekusi Kode

Program ini menjalankan urutan logika sebagai berikut:

### 1. Inisialisasi Fungsi Matematika
Program mendefinisikan beberapa fungsi dasar yang diperlukan:
* **`gcd(a, b)`**: Menghitung Faktor Persekutuan Terbesar (FPB).
* **`mod_inverse(e, phi)`**: Mencari invers modular menggunakan *Extended Euclidean Algorithm*.
* **`extended_gcd()`**: Mendukung perhitungan invers modular secara efisien.

### 2. Pembangkitan Parameter RSA
Program menggunakan dua bilangan prima kecil sebagai contoh:  
&emsp; $p = 61$  
&emsp; $q = 53$

**Perhitungan Parameter:**
* $n = p \times q$
* $\phi(n) = (p - 1)(q - 1)$
* **Public Key:** $(e, n)$ &emsp;
* **Private Key:** $(d, n)$ &emsp;

---

## Menu & Mekanisme Program

### Proses Enkripsi (Opsi 1)
Setiap karakter dikonversi ke nilai ASCII (`ord()`), lalu dihitung dengan rumus:
$$\large C = M^e \pmod n$$
*Hasil enkripsi ditampilkan dalam bentuk daftar angka (ciphertext).*

### Proses Dekripsi (Opsi 2)
Pengguna memasukkan ciphertext (angka dipisahkan spasi). Program menghitung kembali ke plaintext:
$$\large M = C^d \pmod n$$
*Nilai numerik dikonversi kembali menjadi karakter asli (`chr()`).*

---

## Cara Menjalankan Program

### Prasyarat
Pastikan Python sudah terinstal di perangkat Anda.<br>
Cek dengan perintah:
```bash
$ python --version
```
Apabila sudah muncul versi python lalu jalankan perintah:
```bash
$ py nama_file.py
```
Selanjutnya masukkan angka untuk memilih proses enkripsi atau dekripsi dan ikuti intruksi program
