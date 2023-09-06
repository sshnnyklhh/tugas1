print("Program Python Menghitung Volume Balok dengan Jari-jari dan Tinggi")
print("========================================================")
print()

pi = 22/7
jari = float(input("Masukkan Jari-jari Balok: "))
tinggi = float(input("Masukkan Tinggi Balok: "))

volume = pi*jari*jari*tinggi
print("Tinggi balok:", tinggi, "Jari-jari:", jari, "Memiliki volume:", "{:.2f}".format(volume) )
