barang = {"buku", "pensil", "pulpen"}
harga = {2000, 3000, 5000}
jumlah = {2, 5, 3}
total_harga =  {harga * jumlah for harga, jumlah in zip(harga, jumlah)}
print(total_harga)