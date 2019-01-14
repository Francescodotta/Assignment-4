def Reverse_Complement(s):
    str2 = s[::-1]
    seqDNA = ""
    for nuc in str2:
        if nuc == "A":
            seqDNA += "T"
        if nuc == "T":
            seqDNA += "A"
        if nuc == "G":
            seqDNA += "C"
        if nuc == "C":
            seqDNA += "G"
    return seqDNA
with open("/Users/francescodotta/Desktop/rosalind_revp.txt")as f:
    DNA_str = f.readlines()
    seq = ""
    for line in DNA_str:
        line = line.strip()
        if line[0] != ">":
            seq += line
    for i in range(len(seq)):
        for n in range(4,13):
            if seq[i:i+n] == Reverse_Complement(seq[i:i+n]):
                if i + n <= len(seq):
                    print (i+1, n)
