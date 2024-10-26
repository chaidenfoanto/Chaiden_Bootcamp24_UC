prime = []

lower = int(input("Masukkan batas bawah : "))
upper = int(input("Masukkan batas atas : "))

if lower == 1:
	for i in range (lower+1, upper+1):
		prima = True
		for y in range (2,i):
			if (i % y == 0):
					prima = False
		if prima == True:
			prime.append(i)
else:
	for i in range (lower, upper+1):
		prima = True
		for y in range (2,i):
			if (i % y == 0):
					prima = False
		if prima == True:
			prime.append(i)

print(f"bilangan prima antara {lower} - {upper} :", prime)	


#ACC(Budi_R)