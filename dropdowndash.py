import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load dan bersihkan data
df = pd.read_csv("data/data_karyawan_latihan.csv")

df.columns = df.columns.str.strip()

# Inisialisasi app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H2("Dasboard Karyawan - Filter Pendidikan"),

    dcc.Dropdown(
        id='filter_pendidikan',
        options=[{'label': p, 'value': p} for p in df['Pendidikan'].unique()],
        value=df['Pendidikan'].unique().tolist()[0],
        clearable=False
    ),

    dcc.Graph(id='grafik_status')
])

# Callback: update grafik berdasarkan dropdown
@app.callback(
    Output('grafik_status', 'figure'),
    Input('filter_pendidikan', 'value')
)
def update_grafik(pendidikan_terpilih):
    filtered_df = df[df['Pendidikan'] == pendidikan_terpilih]
    status_counts = filtered_df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Jumlah']

    fig = px.bar(
        status_counts,
        x='Status', y='Jumlah',
        color='Status',
        title=f'Jumlah Karyawan berdasarkan Status (Pendidikan: {pendidikan_terpilih})',
        text='Jumlah'

    )
    fig.update_layout(template='plotly_white')
    return fig

# Jalankan
if __name__ == '__main__':
    app.run(debug=True)