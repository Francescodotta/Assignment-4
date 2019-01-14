with open ("/Users/francescodotta/Desktop/rosalind_rna-2.txt", "r") as myfile:
    s=myfile.read().strip()
    print (s.replace('T','U'))
