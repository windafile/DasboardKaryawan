import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("data/data_karyawan_latihan.csv")

df.columns = df.columns.str.strip()

# Siapkan data 
pendidikan_counts = df['Pendidikan'].value_counts().reset_index()
pendidikan_counts.columns = ['Pendidikan', 'Jumlah']

# Buat grafik
fig = px.bar(pendidikan_counts, x='Pendidikan', y='Jumlah', color='Pendidikan', text='Jumlah')

# Inisialisasi app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard Karyawan"),
    dcc.Graph(figure=fig)
])

# Jalankan
if __name__ == '__main__':
    app.run(debug=True)