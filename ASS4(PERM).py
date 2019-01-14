from itertools import permutations
with open ("/Users/francescodotta/Desktop/rosalind_perm.txt") as input:
    input = input.read()
    Com= []
    Res=''
    for k in range(int(input)+1):
        Com.append(k)
    Perm = permutations(Com[1:])
    len = 0
    for i in list(Perm):
        Res = Res + str(i)
        len +=1
    Res = Res.replace("(", "\n").replace(")", "").replace(",", "")
    print (str(len) + "\n" + Res[1:])
