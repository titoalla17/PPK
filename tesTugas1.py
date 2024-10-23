mahasiswa = []
enkripsi = []

def enkripsiData(nama):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for char in nama:
        if char in lower:
            hasil += upper[(lower.index(char) + 3) % 26]
        else:
            print("Bukan orang")
    return hasil

def tambahMahasiswa(nama, usia, nilai_rata):
    mahasiswa.append([enkripsiData(nama), usia, nilai_rata])
    print("Data mahasiswa berhasil ditambahkan.")

def tampilkanMahasiswa():
    if mahasiswa: 
        i = 1
        for data in mahasiswa:
            print(f"{i}. Nama: {data[0]}, Usia: {data[1]}, Nilai Rata-Rata: {data[2]}")
            i =+ 1
    else:
        print("Data mahasiswa kosong.")
        
def tampilkanNamaAsli():
    if enkripsi:
        print("Nama Asli Mahasiswa: ")
        i = 1
        for nama in enkripsi:
            print(f"{i}. Nama Asli: {nama}")
            i += 1
    else:
        print("Data mahasiswa kosong.")

while True:
    print("\nMenu:")
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan Data mahasiswa (Terenkripsi)")
    print("3. Tampilkan Nama Asli mahasiswa")
    print("4. Cari Mahasiswa Berdasarkan Nama")
    print("5. Hitung Rata-Rata Nilai Mahasiswa")
    print("6. Tampilkan Mahasiswa yang Lulus")
    print("7. Tampilkan Mahasiswa Tertua dan Termuda")
    print("8. Keluar")

    pilihan = input("Pilihan (1-8): ")
    
    if pilihan == "1":
        nama = input("Masukkan nama: ")
        usia = int(input("Masukkan usia: "))
        nilai_rata = float(input("Masukkan nilai rata-rata: "))
        tambahMahasiswa(enkripsiData(nama), usia, nilai_rata)

    elif pilihan == "2:":
        tampilkanMahasiswa()