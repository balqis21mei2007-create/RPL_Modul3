
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menghubungkan tombol ke fungsi controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        # Memuat data anggota saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari model
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def simpan_data(self):
        # Mengambil input dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Validasi form
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        # Menyimpan data melalui model
        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )

            self.view.entry_nama.delete(0, "end")
            self.view.entry_alamat.delete(0, "end")

            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Gagal menyimpan data anggota!"
            )

    def run(self):
        self.view.mainloop()