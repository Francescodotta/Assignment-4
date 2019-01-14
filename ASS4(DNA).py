with open ("/Users/francescodotta/Desktop/rosalind_dna-2.txt", "r") as myfile:
    s=myfile.readlines()
G = 0
A = 0
C = 0
T = 0

for x in s:
    for y in x:
        if y == "G":
            G = G+1
        if y == "A":
            A = A+1
        if y == "C":
            C = C+1
        if y == "T":
            T = T+1
print (A, C, G, T)
