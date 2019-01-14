with open('/Users/francescodotta/Desktop/rosalind_revc.txt') as input_data:
    dna = input_data.read().strip()[::-1]
    dna = str.translate(dna, str.maketrans("ATCG", "TAGC"))
    print (dna)
