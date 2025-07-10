import pandas as pd
df = pd.read_csv("D:/belajar python/folderwinda/data_karyawan_latihan.csv")
print(df.head())

# Ambil baris yang status-nya Aktif
df_aktif = df[df['Status'] == 'Aktif']
print(df_aktif)

df_nonaktif = df[df['Status'] !='Aktif']
print(df_nonaktif)

df_aktif = df.query("Status == 'Aktif'")

# Hitung total masing-masing Status
jumlah_status = df['Status'].value_counts()
print(jumlah_status)

persentase_status = df['Status'].value_counts(normalize=True) * 100
print(persentase_status)

#filtet gabungan: Status Aktif dan Pendidikan S1
hasil = df[(df['Status'] =='Aktif') & (df['Pendidikan'] == 'S1')]
print(hasil)

df.query("Status == 'Aktif' and `Jenis Kelamin` == 'Laki-laki'")


