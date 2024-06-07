import pandas as pd
import matplotlib.pyplot as plt

# Baca data pembelian dan penjualan
pembelian = pd.read_csv('tabel_pembelian.csv')
penjualan = pd.read_csv('tabel_penjualan.csv')

# Gabungkan data pembelian dan penjualan berdasarkan kategori barang
data = pembelian.merge(penjualan, on='Kategori Barang', suffixes=('_pembelian', '_penjualan'))

# Plot scatter plot untuk setiap kategori barang
plt.figure(figsize=(10, 6))
for kategori, group in data.groupby('Kategori Barang'):
    plt.scatter(group['Jumlah Dibeli'], group['Jumlah Terjual'], label=kategori)

# Tambahkan label sumbu
plt.xlabel('Jumlah Barang Dibeli')
plt.ylabel('Jumlah Barang Terjual')
plt.title('Hubungan Antara Pembelian dan Penjualan untuk Setiap Kategori Barang (Mei 2023)')
plt.legend()
plt.grid(True)

# Tampilkan plot
plt.show()
