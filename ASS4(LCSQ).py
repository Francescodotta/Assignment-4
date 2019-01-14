with open("/Users/francescodotta/Desktop/rosalind_lcsq.txt") as InputFile:
    str1 = InputFile.read()
    str1 = str1.replace("Rosalind_", "")
    str1 = str1.replace("\n", "")
    str1 = ''.join([i for i in str1 if not i.isdigit()])
    LongCommSeq=[]
    LongCommSeq = str1.split(">")
    LongCommSeq.remove("")
    seq1 , seq2= LongCommSeq
    st1 = [''] * (len(seq2) + 1)
    for i in seq1:
        st2 = st1
        st1 = ['']
        for j, k in enumerate(seq2):
            if(i == k):
                st1.append(st2[j] + i)
            else:
                st1.append(max(st2[j+1], st1[-1], key=len))
    print (st1[-1])
