# Versi 1: Hampir benar — tapi ada kekurangan
def ubah_celcius_ke_fahrenheit(suhu_c):
    return suhu_c * 9 / 5 + 32

# Versi 2: Sudah diperbaiki & lebih aman
def ubah_celcius_ke_fahrenheit_benar(suhu_c):
    """Mengubah suhu dari Celcius ke Fahrenheit"""
    if suhu_c < -273.15:
        return "Suhu tidak mungkin di bawah -273,15°C"
    return (suhu_c * 9 / 5) + 32

# Mencoba jalankan kode
if __name__ == "__main__":
    data_suhu = [0, 25, 50, 100, -300]
    
    print("=== Versi Awal ===")
    for c in data_suhu:
        print(f"{c}°C → {ubah_celcius_ke_fahrenheit(c)}°F")
    
    print("\n=== Versi Sudah Diperbaiki ===")
    for c in data_suhu:
        hasil = ubah_celcius_ke_fahrenheit_benar(c)
        print(f"{c}°C → {hasil}°F")