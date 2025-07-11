import shutil
import os

asal = r"D:\belajar python\data_karyawan_latihan.csv"
tujuan = r"D:\belajar python\data\data_karyawan_latihan.csv"

# Bikin folder data/ kalau belum ada
os.makedirs(os.path.dirname(tujuan), exist_ok=True)

try:
    shutil.move(asal, tujuan)
    print("✅ File berhasil dipindahkan ke folder data/")
except FileNotFoundError:
    print("❌ File tidak ditemukan. Cek kembali path-nya.")
except Exception as e:
    print(f"❌ Error: {e}")
