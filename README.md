# Perbaikan Kode — Proyek Evaluasi AI

**Pemilik:** itsfelicia9-source

---

## Tentang Proyek
Repositori ini berisi contoh kode yang terlihat benar padahal mengandung kekurangan halus — pola yang sering terlewat saat ditinjau.

## Masalah yang Ditemukan
Pada fungsi konversi suhu di `suhu_converter.py`, versi awal:
- Terlihat berjalan benar untuk nilai biasa
- **Tidak ada pengecekan** untuk nilai yang mustahil secara fisika (di bawah -273,15°C)
- Jika menerima nilai tersebut, program tetap menghitung padahal tidak masuk akal

## Perbaikan yang Dilakukan
- Menambahkan pengecekan batas nilai suhu terendah
- Memberikan pesan penjelasan jika nilai tidak masuk akal
- Kode jadi lebih kokoh, aman, dan mudah dipahami

## Status
- Semua kode ditulis sendiri ✅
- Bukan milik perusahaan atau klien
- Belum digabung ke proyek lain
- Sedang belajar & mengembangkan kemampuan

