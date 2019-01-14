RNABases = ['U', 'C', 'A', 'G']
Codons = [a+b+c for a in RNABases for b in RNABases for c in RNABases]
aminoacids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
FromDNAtoProt = dict(zip(Codons, aminoacids))
def ProteinSequence(RNAseq):
	template = ""
	for i in range(0,len(RNAseq),3):
		template= template + FromDNAtoProt.get(RNAseq[i]+RNAseq[i+1]+RNAseq[i+2])
	return template.strip('*')
with open("/Users/francescodotta/Desktop/rosalind_splc.txt") as InputFile:
    sequences= [[block.split("\n",1)[0] , block.split("\n",1)[1].replace("\n","")] for block in InputFile.read().split(">")[1:] ]
    codRegion=sequences[0][1]
    for i in range(1,len( sequences)):
	    codRegion = codRegion.replace(sequences[i][1],"")
    codRegion = codRegion.replace("T","U")
    print (ProteinSequence(codRegion))
