import pandas as pd
import plotly.express as px

# Baca data
df = pd.read_csv("D:/belajar python/folderwinda/data_karyawan_latihan.csv")
df.columns = df.columns.str.strip()

# Hitung
pendidikan_counts = df['Pendidikan'].value_counts().reset_index()
pendidikan_counts.columns = ['Pendidikan', 'Jumlah']

# Buat grafik interaktif
fig = px.bar(pendidikan_counts,
             x='Pendidikan',
             y='Jumlah',
             title='Jumlah Karyawan per Pendidikan',
             color='Pendidikan',
             text='Jumlah')

fig.update_layout(template='plotly_white')
fig.show()