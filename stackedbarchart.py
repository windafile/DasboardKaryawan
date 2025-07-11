import pandas as pd
import matplotlib.pyplot as plt

# Baca data
df = pd.read_csv("data/data_karyawan_latihan.csv")

df.columns = df.columns.str.strip()

# Kelompokkan data
grouped = df.groupby(['Pendidikan', 'Status']).size().unstack(fill_value=0)

# Plor stacked Bar Chart
grouped.plot(kind='bar', stacked=True, figsize=(8, 5), color=['orange', 'skyblue'])

plt.title('Jumlah Karyawan per Pendidikan dan Status')
plt.xlabel('Pendidikan')
plt.ylabel('Jumlah')
plt.legend(title='Status')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('stacked_chart.png', dpi=300) # Simpan file gambar ke folder saat ini
plt.show()

# Simpan fig dan ax supaya bisa tambahin label
ax = grouped.plot(kind='bar', stacked=True, figsize=(8, 5), color=['orange', 'skyblue'])

# Tambah label jumlah di atas bar
for i, col in enumerate(grouped.columns):y_offset = grouped.iloc[:, :i].sum(axis=1)  # posisi label
for j, val in enumerate(grouped[col]):
    ax.text(j, y_offset[j] + val / 2, str(val), ha='center', va='center', color='black', fontsize=10)
