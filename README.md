# YOLANDA ESTER BERLIANA RITONGA

## Setup Environment
Untuk menjalankan aplikasi dashboard ini, pastikan Anda mengikuti langkah-langkah berikut:

1. Buat sebuah environment menggunakan Conda dengan Python versi 3.9 dengan perintah berikut:

    ```bash
    conda create --name main-ds python=3.9
    ```

2. Aktifkan environment yang telah dibuat menggunakan perintah:

    ```bash
    conda activate main-ds
    ```

3. Instal paket-paket yang dibutuhkan dengan menggunakan pip:

    ```bash
    pip install  pandas matplotlib streamlit
    ```

## Menjalankan Aplikasi Streamlit
Setelah semua paket terinstal, Anda dapat menjalankan aplikasi Streamlit dengan menggunakan perintah berikut:

```bash
streamlit run dashboard.py
