import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load data
df = pd.read_csv("D:/belajar python/folderwinda/data_karyawan_latihan.csv")
df.columns = df.columns.str.strip()

#Inisialisasi app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H2("Dashboard Kombinasi - Bar dan Pie Chart"),

    dcc.Dropdown(
        id='dropdown_pendidikan',
        options=[{'label':p, 'value':p} for p in df ['Pendidikan'].unique()],
        value=df['Pendidikan'].unique()[0],
        clearable=False
    ),

    html.Div([
        dcc.Graph(id='bar_chart', style={'display': 'inline-block', 'width': '49%'}),
        dcc.Graph(id='pie_chart', style={'display': 'inline-block', 'width': '49%'})
    ])
])

# Callback: update grafik berdasarkan dropdown
@app.callback(
    Output('bar_chart', 'figure'),
    Output('pie_chart', 'figure'),
    Input('dropdown_pendidikan', 'value')
)
def update_charts(pendidikan_terpilih):
    # filter data
    filtered_df = df[df['Pendidikan'] == pendidikan_terpilih]

    # Bar Chart Status Count
    bar_data = filtered_df['Status'].value_counts().reset_index()
    bar_data.columns = ['Status', 'Jumlah']
    bar_fig = px.bar(bar_data, x='Status', y='Jumlah', color='Status', text='Jumlah',
                     title=f"Jumlah Status Karyawan (Pendidikan:{pendidikan_terpilih})" )
    bar_fig.update_layout(template='plotly_white')

    # Pie Chart
    pie_fig = px.pie(bar_data, names='Status', values='Jumlah',
                     title=f"Proporsi Status Karyawan (Pendidikan: {pendidikan_terpilih})")
    pie_fig.update_traces(textinfo='percent+label')

    return bar_fig, pie_fig

# Jalankan
if __name__ == '__main__':
    app.run(debug=True)