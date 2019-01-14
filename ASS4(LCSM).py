with open("/Users/francescodotta/Desktop/rosalind_lcsm.txt") as input:
    string=[]
    input.readline()
    X = ''
    line = input.readline().strip()
    while line != '':
        if line[0] == ">":
            string.append(X)
            X = ''
        else:
            X = X + line
        line = input.readline().strip()
Min_String=min(string,key=len)
LenMin=len(Min_String)
LCSM=''
for i in range(LenMin):
    if LCSM!='':
        break
    for s in range(i+1):
        j=Min_String[s:s+LenMin-i+1]
        if all(k.find(j) >=0 for k in string):
            LCSM=j
            break
print(LCSM)
