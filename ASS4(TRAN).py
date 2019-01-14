with open ("/Users/francescodotta/Desktop/rosalind_tran.txt","r") as InputFile:
    Fasta=InputFile.read()
    seq1=Fasta.split(">")[1]
    seq2=Fasta.split(">")[2]
    seq1=''.join(seq1.split("\n")[1:])
    seq2=''.join(seq2.split("\n")[1:])
    trans=0
    transver=0
    def SeqSim(a):
        if a=="A":
            return "G"
        elif a=="G":
            return "A"
        elif a=="C":
            return "T"
        else:
            return "C"
    for i in range(len(seq1)):
        if seq1[i]==SeqSim(seq2[i]):
            trans= trans + 1
        elif not seq1[i]==seq2[i]:
            transver= transver + 1
    print(float(trans)/transver)
