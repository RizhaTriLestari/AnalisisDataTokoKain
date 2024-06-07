import pandas as pd
import matplotlib.pyplot as plt

# Membaca file penjualan
penjualan = pd.read_csv('tabel_penjualan.csv')

# Mengonversi kolom Tanggal menjadi tipe data datetime
penjualan['Tanggal'] = pd.to_datetime(penjualan['Tanggal'])

# Menambahkan kolom Bulan berdasarkan Tanggal
penjualan['Bulan'] = penjualan['Tanggal'].dt.strftime('%Y-%m')

# Mengambil data penjualan selama bulan Mei 2023
penjualan_mei_2023 = penjualan[penjualan['Bulan'] == '2023-05']

# Menghitung total penjualan untuk setiap kategori barang selama bulan Mei 2023
total_penjualan_kategori = penjualan_mei_2023.groupby('Kategori Barang')['Total'].sum()

# Menampilkan hasil analisis penjualan
print("\nTotal penjualan untuk setiap kategori barang selama bulan Mei 2023:")
print(total_penjualan_kategori)

import matplotlib.pyplot as plt

# Data untuk diagram pie
labels = total_penjualan_kategori.index
sizes = total_penjualan_kategori.values

# Membuat diagram pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Diagram Pie Chart Total Penjualan per Kategori Barang')
plt.axis('equal')  # Memastikan proporsi lingkaran
plt.show()
