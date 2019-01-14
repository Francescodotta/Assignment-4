def IndSequence(pos, seq):
    i = j = 0
    ind = []
    while i < len(pos) and j < len(seq):
        if pos[i] == seq[j]:
            j = j + 1
            ind.append(i + 1)
        i = i + 1
    return ind
with open ("/Users/francescodotta/Desktop/rosalind_sseq.txt") as InputFile:
    DNA= {}
    a = []
    for content in InputFile:
        if '>' in content:
            keySeq = content.rstrip().replace('>', '')
            currentSeq = keySeq
            a.append(keySeq)
            DNA[currentSeq] = ''
        else:
            DNA[currentSeq] += content.rstrip()
    ind = IndSequence(DNA[a[0]], DNA[a[1]])
    print (' '.join(map(str, ind)))
