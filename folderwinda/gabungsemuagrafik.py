import pandas as pd
import matplotlib.pyplot as plt

#baca data
df = pd.read_csv("D:/belajar python/folderwinda/data_karyawan_latihan.csv")
df.columns = df.columns.str.strip()

# Pie Chart - Status
status_counts = df['Status'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Persentase Status Karyawan')
plt.axis('equal')
plt.tight_layout()
plt.savefig('status_piechart.png', dpi=300) # << simpan pie chart
plt.show()

# Bar Chart - Pendidikan
pendidikan_counts = df['Pendidikan'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(pendidikan_counts.index, pendidikan_counts.values, color='skyblue')
plt.title('Jumlah Karyawan per Pendidikan')
plt.xlabel('Pendidikan')
plt.ylabel('Jumlah')
plt.grid(axis='y', linestyle='--',alpha=0.7)
plt.tight_layout()
plt.savefig('pendidikan_barchart.png', dpi=300) # << simpan bar chart
plt.show

# Stacked Bar Chart - Pendidikan dan Status
grouped = df.groupby(['Pendidikan', 'Status']).size().unstack(fill_value=0)
grouped.plot(kind='bar', stacked=True, figsize=(8, 5), color=['orange', 'skyblue'])
plt.title('Jumlah Karyawan Per Pendidikan dan Status')
plt.xlabel('Pendidikan')
plt.ylabel('Jumlah')
plt.legend(title='Status')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('stacked_chart.png', dpi=300) # << simpen stacked bar chart 
plt.show()
