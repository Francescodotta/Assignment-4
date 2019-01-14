with open ("/Users/francescodotta/Desktop/rosalind_hamm.txt") as inputfile:
    string1=inputfile.readline().strip()
    string2=inputfile.readline().strip()
    hamming = 0
    index = 0
    for i in string1:
        if string1[index] != string2[index]:
            hamming += 1
        index += 1
    print (hamming)
