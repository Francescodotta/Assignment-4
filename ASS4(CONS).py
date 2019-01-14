def ReadFastaFile(collection_dna):
    name, seq = None, []
    for line in collection_dna:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))
list_dna = []
with open('/Users/francescodotta/Desktop/rosalind_cons.txt') as collection_dna:
    for name, _seq_ in ReadFastaFile(collection_dna):
        list_dna.append(_seq_)
length = len(list_dna)
totalseq = len(_seq_)
profilevalues = [[0 for x in range(totalseq)] for y in range(4)]
consensus = ['A','C','G','T']
for x in range(totalseq):
    for y in range(4):
        for z in range(length):
            profilevalues[y][x] += list_dna[z][x].count(consensus[y])
consensusstring = ""
for x in range(totalseq):
    maxvalue = 0
    for y in range(4):
        if profilevalues[y][x] >= profilevalues[maxvalue][x]:
            maxvalue = y
    if maxvalue == 0:
        consensusstring += 'A'
    elif maxvalue == 1:
        consensusstring += 'C'
    elif maxvalue == 2:
        consensusstring += 'G'
    elif maxvalue == 3:
        consensusstring += 'T'
print('%s\n%s\n%s\n%s\n%s' % (consensusstring, 'A: '+ str(profilevalues[0]).strip('[]').replace(',',''),
                              'C: '+str(profilevalues[1]).strip('[]').replace(',',''),
                              'G: '+str(profilevalues[2]).strip('[]').replace(',',''),
                              'T: '+str(profilevalues[3]).strip('[]').replace(',','')))
