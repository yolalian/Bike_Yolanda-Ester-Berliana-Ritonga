import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import requests
from io import StringIO

# Mengunduh data dari URL CSV
url = "https://raw.githubusercontent.com/yolalian/Bike_Yolanda-Ester-Berliana-Ritonga/main/dashboard/all_data.csv"
response = requests.get(url)
csv_data = StringIO(response.text)

# Load data
all_df = pd.read_csv(csv_data)

# Menggunakan teknik clustering
def categorize_traffic_density(cnt):
    if cnt < 50:
        return 'Sepi'
    elif 50 <= cnt < 200:
        return 'Sedang'
    else:
        return 'Ramai'

all_df['traffic_density'] = all_df['cnt'].apply(categorize_traffic_density)

# Pertanyaan Bisnis 1: Visualisasi penggunaan sepeda per jam
hourly_usage = all_df.groupby('hr')['cnt'].mean()

# Pertanyaan Bisnis 2: Visualisasi penggunaan sepeda berdasarkan kondisi cuaca
weather_effect = all_df.groupby('weathersit')['cnt'].mean()
weather_labels = {1: 'Cerah', 2: 'Berawan', 3: 'Hujan Ringan/Salju', 4: 'Hujan Lebat/Salju'}

# Tambahkan gambar di sidebar
st.sidebar.image("bike.jpeg", use_column_width=True, clamp=True)

# Streamlit Dashboard
st.title('Dashboard Analisis Penggunaan Sepeda')
st.sidebar.title('Pilih Visualisasi')

visualization_option = st.sidebar.selectbox(
    'Pilih Visualisasi yang Ingin Dilihat',
    ('Penggunaan Sepeda per Jam', 'Penggunaan Sepeda Berdasarkan Kondisi Cuaca', 'Pola Trafik Sepeda Berdasarkan Tingkat Kepadatan Lalu Lintas')
)

if visualization_option == 'Penggunaan Sepeda per Jam':
    st.subheader('Rata-rata Penggunaan Sepeda per Jam')
    st.write(hourly_usage)
    st.bar_chart(hourly_usage)

elif visualization_option == 'Penggunaan Sepeda Berdasarkan Kondisi Cuaca':
    st.subheader('Rata-rata Penggunaan Sepeda Berdasarkan Kondisi Cuaca')
    weather_effect.rename(index=weather_labels, inplace=True)
    st.write(weather_effect)
    st.bar_chart(weather_effect)

elif visualization_option == 'Pola Trafik Sepeda Berdasarkan Tingkat Kepadatan Lalu Lintas':
    st.subheader('Pola Trafik Sepeda Berdasarkan Tingkat Kepadatan Lalu Lintas')
    traffic_density_counts = all_df['traffic_density'].value_counts()
    st.write(traffic_density_counts)
    st.bar_chart(traffic_density_counts)
