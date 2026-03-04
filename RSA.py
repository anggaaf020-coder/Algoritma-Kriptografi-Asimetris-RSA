def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd_val, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_val, x, y

    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    return x % phi

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = mod_inverse(e, phi)

print("Public Key (e, n) =", (e, n))
print("Private Key (d, n) =", (d, n))

while True:
    print("\nPilih Proses:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Exit")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        pesan = input("Masukkan pesan: ")
        cipher = []

        for huruf in pesan:
            ascii_val = ord(huruf)
            enkripsi = pow(ascii_val, e, n)
            cipher.append(enkripsi)

        print("Ciphertext:", cipher)

    elif pilihan == "2":
        try:
            cipher_input = input("Masukkan ciphertext (pisahkan dengan spasi): ")
            cipher_list = list(map(int, cipher_input.split()))

            hasil = ""
            for angka in cipher_list:
                dekripsi = pow(angka, d, n)
                hasil += chr(dekripsi)

            print("Hasil Dekripsi:", hasil)

        except:
            print("Input tidak valid! Pastikan hanya angka dipisahkan spasi.")

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")