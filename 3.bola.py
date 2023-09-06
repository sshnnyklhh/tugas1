print("Program Python Menghitung Volume Bola dengan Jari-jari")
print("========================================================")
print()

pi = 22/7
jari = float(input("Masukkan  Jari-jari Bola: "))

volume = 4/3*pi*(jari*jari*jari)
print("Jari-jari bola:", jari, "Memiliki volume:", "{:.3f}".format(volume))