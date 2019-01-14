def Matrix(sequence_list):
    ResMatrix = []
    for seq1 in sequence_list:
        line=[]
        for seq2 in sequence_list:
            line.append(float(Hamming(seq1, seq2))/ min([len(seq1), len(seq2)]))
        ResMatrix.append(line)
    for i in ResMatrix:
        for j in  i:
            print("%1.5f" % j),
        print
def Hamming(orig , comp):
    HAMMdistance = abs(len(orig) - len(comp))
    index = 0
    max_index = min([len(orig), len(comp)])
    while(index < max_index):
        if(orig[index] != comp[index]):
            HAMMdistance += 1
        index += 1
    return HAMMdistance
with open("/Users/francescodotta/Desktop/rosalind_pdst.txt") as inputfile:
    seqcounter = -1
    labels = []
    seq = []
    len1 = []
    for line in inputfile:
        if(line[-1] == '\n'):
            line = line[:-1]
        if(line[0].startswith(">")):
            seqcounter += 1
            labels.append(line[1:])
            seq.append("")
            len1.append(0)
        else:
            seq[seqcounter] = ''.join([seq[seqcounter], line])
            len1[seqcounter] += len(line)
Matrix(seq)
