import pandas as pd
import matplotlib.pyplot as plt

# Membaca file persediaan
persediaan = pd.read_csv('tabel_persediaan.csv')

# Mengambil data persediaan dengan saldo akhir di bawah 10
persediaan_kritis = persediaan[persediaan['Saldo Akhir'] < 10]

# Menampilkan hasil analisis persediaan
print("Barang dengan saldo akhir di bawah 10:")
print(persediaan_kritis)

plt.figure(figsize=(10, 6))
plt.scatter(persediaan_kritis['Nama Barang'], persediaan_kritis['Saldo Akhir'], color='red')
plt.title('Persediaan Barang dengan Saldo Akhir di Bawah 10')
plt.xlabel('Nama Barang')
plt.ylabel('Saldo Akhir')
plt.xticks(rotation=45)
plt.grid(True)  # Menambahkan grid
plt.show()

