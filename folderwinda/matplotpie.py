import pandas as pd
import matplotlib.pyplot as plt

#Baca data
df = pd.read_csv("D:/belajar python/folderwinda/data_karyawan_latihan.csv")

# Pastikan kolom tanpa spasi
df.columns=df.columns.str.strip()

# Hitung jumlah status
status_counts = df['Status'].value_counts()

# Buat Pie Chart
plt.figure(figsize=(6, 6)) # ini harus langsung tuple, jangan variabel bernama "figure"
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Persentase Status Karyawan')
plt.axis('equal')
plt.show()

# Hitung Jumlah per pendidikan
pendidikan_counts = df['Pendidikan'].value_counts()

# -- Tambah grafik batang di bawah nya
plt.figure(figsize=(6, 4))
plt.bar(pendidikan_counts.index, pendidikan_counts.values, color='skyblue')
plt.title('Jumlah Karyawan per Pendidikan')
plt.xlabel('Pendidikan')
plt.ylabel('Jumlah')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
