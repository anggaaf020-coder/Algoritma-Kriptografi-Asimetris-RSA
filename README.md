# Dokumentasi Algoritma RSA (Rivest-Shamir-Adleman)

Repositori ini berisi implementasi sederhana dari algoritma kriptografi asimetris RSA menggunakan bahasa pemrograman Python. Kode ini dirancang untuk mendemonstrasikan proses pembangkitan kunci, enkripsi pesan, dan dekripsi pesan secara bertahap tanpa menggunakan library kriptografi instan.

Implementasi ini bertujuan untuk pembelajaran akademik dan pemahaman konsep dasar RSA.

#Langkah-Langkah Eksekusi Kode

Program ini menjalankan urutan logika sebagai berikut:  
**1. Inisialisasi Fungsi Matematika**  
  Program mendefinisikan beberapa fungsi dasar yang diperlukan dalam algoritma RSA:
  - Fungsi gcd(a, b) untuk menghitung Faktor Persekutuan Terbesar (FPB).
  - Fungsi mod_inverse(e, phi) menggunakan Extended Euclidean Algorithm untuk mencari invers modular.
  - Fungsi extended_gcd() untuk mendukung perhitungan invers modular.

**2. Pembangkitan Parameter RSA**  
  Program menggunakan dua bilangan prima kecil sebagai contoh:
  - p = 61
  - q = 53

  Kemudian program menghitung:
  - n = p × q
  - φ(n) = (p - 1)(q - 1)

  Selanjutnya dipilih nilai:
  - e = 17 (relatif prima terhadap φ(n))
  - d = invers modular dari e terhadap φ(n)

  Hasil akhirnya adalah:
  - Public Key: (e, n)
  - Private Key: (d, n)

**3. Menu Interaktif Program**  
  Setelah pembangkitan kunci, program menampilkan menu pilihan:
  1. Enkripsi
  2. Dekripsi
  3. Exit  
Program berjalan dalam loop sehingga pengguna dapat melakukan proses berulang kali sampai memilih Exit.


    
