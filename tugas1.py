# Class untuk manajemen daftar nilai mahasiswa
class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_nilai = []

    def tambah(self, nama, nilai):
        data_mahasiswa = {'nama': nama, 'nilai': nilai}
        self.daftar_nilai.append(data_mahasiswa)
        print(f"Data mahasiswa {nama} berhasil ditambahkan.")

    def tampilkan(self):
        print("\nDaftar Nilai Mahasiswa:")
        for data in self.daftar_nilai:
            print(f"Nama: {data['nama']}, Nilai: {data['nilai']}")

    def hapus(self, nama):
        for data in self.daftar_nilai:
            if data['nama'] == nama:
                self.daftar_nilai.remove(data)
                print(f"Data mahasiswa {nama} berhasil dihapus.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for data in self.daftar_nilai:
            if data['nama'] == nama:
                data['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} berhasil diubah.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

# Contoh penggunaan class DaftarNilaiMahasiswa
if __name__ == "__main__":
    daftar_nilai_mahasiswa = DaftarNilaiMahasiswa()

    # Menambahkan data mahasiswa
    daftar_nilai_mahasiswa.tambah("Asep", 85)
    daftar_nilai_mahasiswa.tambah("Ujang", 90)
    daftar_nilai_mahasiswa.tambah("Cecep", 78)

    # Menampilkan daftar nilai mahasiswa
    daftar_nilai_mahasiswa.tampilkan()

    # Menghapus data mahasiswa
    daftar_nilai_mahasiswa.hapus("Ujang")
    daftar_nilai_mahasiswa.tampilkan()

    # Mengubah data mahasiswa
    daftar_nilai_mahasiswa.ubah("Cecep", 85)
    daftar_nilai_mahasiswa.tampilkan()
