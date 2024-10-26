kata = input("Masukkan kata : ")
word = ""
box = []

for i in range (len(kata)):
    if kata[i] != '.':
        word += kata[i]
    else:
        box.append(word)
        word = ''
box.append(word)

for y in range (len(box)):
    if y == len(box)-1:
        print(box[len(box)-1-y])
    else: print(box[len(box)-1-y], end=".")

#ACC(Budi_R)