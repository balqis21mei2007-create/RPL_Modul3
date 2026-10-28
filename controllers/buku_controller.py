
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        # Menghubungkan tombol dengan fungsi controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Memilih baris buku pada tabel
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_buku)

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari model
        data_buku = self.model.get_all_buku()

        # Menampilkan data ke tabel
        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

    def pilih_buku(self, event=None):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(pilihan[0], "values")

        # Mengisi form berdasarkan baris yang dipilih
        self.bersihkan_form()
        self.view.entry_judul.insert(0, data[1])
        self.view.entry_penulis.insert(0, data[2])
        self.view.entry_tahun.insert(0, data[3])

    def simpan_data(self):
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data buku")

    def update_data(self):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin diperbarui!"
            )
            return

        data = self.view.tabel.item(pilihan[0], "values")
        id_buku = data[0]

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        berhasil = self.model.update_buku(
            id_buku,
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal memperbarui data buku"
            )

    def hapus_data(self):
        pilihan = self.view.tabel.selection()

        if not pilihan:
            messagebox.showwarning("Peringatan", "Pilih buku yang ingin dihapus!")
            return

        data = self.view.tabel.item(pilihan[0], "values")
        id_buku = data[0]

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Yakin ingin menghapus buku dengan ID {id_buku}?"
        )

        if not konfirmasi:
            return

        berhasil = self.model.delete_buku(id_buku)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil dihapus")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            # Pesan ini akan muncul jika buku masih terkait dengan tabel peminjaman
            messagebox.showerror(
                "Gagal Menghapus",
                "Buku ini tidak dapat dihapus karena masih ada riwayat peminjamannya!"
            )
    def run(self):
        self.view.mainloop()