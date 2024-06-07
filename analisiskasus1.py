import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Gantilah 'path_to_your_csv' dengan jalur absolut ke file CSV Anda
penjualan_path = "F:\S1 AKUNTANSI\SEMESTER 4\PENGKODEAN\LATIHAN UAS RIZHA TRI LESTARI/tabel_penjualan.csv"
persediaan_path = "F:\S1 AKUNTANSI\SEMESTER 4\PENGKODEAN\LATIHAN UAS RIZHA TRI LESTARI/tabel_persediaan.csv"

# Data untuk Tabel Penjualan (dari CSV file)
penjualan_df = pd.read_csv(penjualan_path)

# Data untuk Tabel Persediaan (dari CSV file)
persediaan_df = pd.read_csv(persediaan_path)

# Langkah 1: Grupkan dan hitung total jumlah terjual per barang
penjualan_terjual = penjualan_df.groupby('Nama Barang')['Jumlah Terjual'].sum().reset_index()

# Langkah 2: Gabungkan dengan data persediaan untuk mendapatkan jumlah dibeli dan jumlah terjual dalam satu tabel
analisis_stok = pd.merge(persediaan_df, penjualan_terjual, on='Nama Barang')

# Langkah 3: Hitung selisih antara jumlah dibeli dan jumlah terjual
analisis_stok['Selisih'] = analisis_stok['Jumlah Dibeli'] - analisis_stok['Jumlah Terjual']

# Langkah 4: Filter barang yang memiliki selisih lebih dari 5 unit
barang_selisih_besar = analisis_stok[abs(analisis_stok['Selisih']) > 5]

# Langkah 5: Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x='Nama Barang', y='Selisih', data=barang_selisih_besar, palette='viridis')
plt.title('Barang dengan Selisih > 5 Unit antara Jumlah Dibeli dan Jumlah Terjual')
plt.xlabel('Nama Barang')
plt.ylabel('Selisih (Jumlah Dibeli - Jumlah Terjual)')
plt.xticks(rotation=45)
plt.tight_layout()

# Menyimpan gambar
plt.savefig("F:\S1 AKUNTANSI\SEMESTER 4\PENGKODEAN\LATIHAN UAS RIZHA TRI LESTARI/selisih_stok_barang.png")

# Menampilkan plot
plt.show()
