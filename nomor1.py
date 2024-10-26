jumlah=0

lower = int(input("Masukkan batas bawah : "))
upper = int(input("Masukkan batas atas : "))

for i in range (lower,upper+1):
	if (i % 2 == 1):
		jumlah += i

print("Jumlah bilangan ganjil :", jumlah)


#ACC(Budi_R)