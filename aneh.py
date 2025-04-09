#barang = [input(f"Masukkan barang ke-{i+1}: ") for i in range(5)]
#print("Daftar barang saat ini:", barang)
#
#barang_baru = input("Masukkan barang baru untuk ditambahkan pada posisi ke-2: ")
#barang.insert(1, barang_baru)
#
#print("Daftar barang setelah penambahan:", barang)
#hapus_index = int(input("Masukkan nomor barang yang ingin dihapus (1-{}): ".format(len(barang)))) - 1
#if 0 <= hapus_index < len(barang):
#    barang.pop(hapus_index)
#else:
#    print("Nomor tidak valid.")
#
#print("Daftar barang setelah perubahan:", barang)