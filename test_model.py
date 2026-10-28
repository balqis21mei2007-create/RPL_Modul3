from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")
model.create_buku("Pemrograman Python MVC", "Guido van Rossum", 2023)
print("Data berhasil disimpan ke Laragon MySQL!")

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

from models.buku_model import BukuModel

model = BukuModel()

print("=== PENGUJIAN BUKU MODEL ===")

# CREATE
print("\n[+] Menambahkan data buku...")
model.create_buku(
    "Pemrograman Python MVC",
    "Guido van Rossum",
    2023
)

# UPDATE
print("\n[*] Mengubah data buku ID 6...")
model.update_buku(
    6,
    "Pemrograman Python MVC Updated",
    "Guido van Rossum",
    2024
)

# DELETE
print("\n[-] Menghapus data buku ID 9...")
model.delete_buku(9)

# READ
print("\n=== Daftar Buku Terkini ===")

data_buku = model.get_all_buku()

for buku in data_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )



    from models.anggota_model import AnggotaModel

anggota = AnggotaModel()

print("\n=== PENGUJIAN ANGGOTA MODEL ===")

# CREATE
print("\n[+] Menambahkan data anggota...")
anggota.create_anggota(
    "Balqis Az-zahra",
    "Palu"
)

# READ
print("\n=== Daftar Anggota Terkini ===")

data_anggota = anggota.get_all_anggota()

for data in data_anggota:
    print(
        f"[{data['id_anggota']}] "
        f"{data['nama']} - "
        f"{data['alamat']}"
    )