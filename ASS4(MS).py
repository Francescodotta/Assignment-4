with open("/Users/francescodotta/Desktop/rosalind_ms.txt") as inputFile:
	listlin = inputFile.readlines()
	k1 = int(listlin[0])
	k2 = listlin[1].split(" ")
	for i in range(0, k1):
		if "\n" in k2[i]:
			k2[i] = k2[i].replace("\n", "")
			k2[i] = int(k2[i])
		else:
			k2[i] = int(k2[i])
	out = sorted(k2)
	for j in range(0,k1):
		print (out[j])
