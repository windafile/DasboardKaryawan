import pandas as pd
# Buat data sederhana
data = {
    'Nama': ['A', 'B', 'C'],
    'Umur': [24, 25, 30],
    'Status': ['Aktif', 'Tidak Aktif', 'Aktif']
}

# Ubah ke Pendaftaran
df = pd.DataFrame(data)

#Lihat Data
print (df)