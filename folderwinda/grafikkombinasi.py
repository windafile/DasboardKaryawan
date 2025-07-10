from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import matplotlib.pyplot as plt

# Baca data 
df = pd.read_csv("D:/belajar python/folderwinda/data_karyawan_latihan.csv")
df.columns = df.columns.str.strip()

# Hitung jumlah dan rata-rata umur per pendidikan
grouped = df.groupby('Pendidikan').agg(
    jumlah_karyawan=('Nama', 'count'),
    rata_umur=('Umur', 'mean')
)

# Plot kombinasi
fig, ax1 = plt.subplots(figsize=(8, 5))

# Bar chart (jumlah karyawan)
ax1.bar(grouped.index, grouped['jumlah_karyawan'], color= 'skyblue')
ax1.set_xlabel('Jumlah Karyawan', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Tambahkan axis kedua untuk line chart
ax2 = ax1.twinx()
ax2.plot(grouped.index, grouped['rata_umur'], color ='darkorange', marker='o', linewidth=2)
ax2.tick_params(axis='y', labelcolor='darkorange')

# Judul dan grid
plt.title('Jumlah Karyawan & Rata-rata Umur per Pendidikan')
ax1.grid(axis='y', linestyle='--',alpha=0.5)
plt.tight_layout()

# Simpan dan tampilkan 
plt.savefig('kombinasi_bar_line.png', dpi=300)
plt.show()