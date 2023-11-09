import streamlit as st
import json

# Fungsi untuk membaca data tugas dari berkas JSON
def baca_data_tugas():
    try:
        with open("tugas.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan data tugas ke berkas JSON
def simpan_data_tugas(tugas):
    with open("tugas.json", "w") as file:
        json.dump(tugas, file)

# Inisialisasi data tugas
tugas = baca_data_tugas()

# Fungsi untuk menambahkan tugas
def tambah_tugas(nama, deadline):
    tugas.append({'nama': nama, 'deadline': deadline})
    simpan_data_tugas(tugas)

# Fungsi untuk menghapus tugas berdasarkan indeks
def hapus_tugas(indeks):
    if 0 <= indeks < len(tugas):
        del tugas[indeks]
        simpan_data_tugas(tugas)
        return True
    return False

# Fungsi untuk menampilkan daftar tugas
def tampilkan_daftar_tugas():
    st.header("Daftar Tugas")
    if not tugas:
        st.write("Belum ada tugas yang ditambahkan.")
    else:
        for i, tugas_item in enumerate(tugas):
            st.write(f"{i + 1}. Nama: {tugas_item['nama']}, Deadline: {tugas_item['deadline']}")
        st.write("")

# Fungsi utama
def main():
    st.title("Manajemen Tugas Mahasiswa")

    menu = st.sidebar.selectbox("Menu", ["Tambah Tugas", "Lihat Daftar Tugas", "Hapus Tugas"])

    if menu == "Tambah Tugas":
        st.header("Tambah Tugas")
        nama_tugas = st.text_input("Nama Tugas")
        deadline = st.date_input("Deadline")
        if st.button("Tambah"):
            tambah_tugas(nama_tugas, str(deadline))
            st.success("Tugas berhasil ditambahkan!")

    if menu == "Lihat Daftar Tugas":
        tampilkan_daftar_tugas()

    if menu == "Hapus Tugas":
        st.header("Hapus Tugas")
        if not tugas:
            st.warning("Belum ada tugas yang bisa dihapus.")
        else:
            indeks_tugas = st.selectbox("Pilih Tugas yang Akan Dihapus", range(1, len(tugas) + 1))
            if st.button("Hapus"):
                if hapus_tugas(indeks_tugas - 1):
                    st.success("Tugas berhasil dihapus.")
                else:
                    st.error("Indeks tugas tidak valid.")

if __name__ == "__main__":
    main()
