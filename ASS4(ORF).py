def ComplementaryReverse(sequence):
    RevSeq = sequence[::-1]
    ResSeq = ''
    for e in RevSeq:
        if e == "A":
            ResSeq += "T"
        if e == "T":
            ResSeq += "A"
        if e == "C":
            ResSeq += "G"
        if e == "G":
            ResSeq += "C"
    return ResSeq
def FindStrCodon(sequence):
    codstrs= []
    for i in range(len(sequence)-3):
        if sequence[i:i+3] == 'ATG':
            new_seq = sequence[i:]
            j = 0
            codstr = ""
            while j < len(new_seq)-3:
                if new_seq[j:j+3] in ("TAA", "TAG", "TGA"):
                    codstr = new_seq[:j]
                    codstrs.append(codstr)
                    break
                else:
                    j += 3
    return codstrs
def trans(codingString):
    i = 0
    AAseq = ""
    codontable = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }
    while i <= len(codingString) - 3:
        AAseq += codontable[codingString[i:i+3]]
        i = i + 3
    if AAseq:
        return AAseq
with open("/Users/francescodotta/Desktop/rosalind_orf.txt", "r") as inputfile:
    lines = inputfile.readlines()
    seq = ''
    for i in lines:
        if i[0]!= ">":
            line = i.strip()
            seq += line
    seqs = [seq, ComplementaryReverse(seq)]
    all_cod_seq = []
    for seq in seqs:
        codstrs = FindStrCodon(seq)
        all_cod_seq += codstrs
    trans_seq = [all_cod_seq[0]]
    for seq in all_cod_seq:
        if seq not in trans_seq:
            trans_seq += [seq]
    for seq in trans_seq:
        print (trans(seq))
