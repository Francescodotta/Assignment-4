with open('/Users/francescodotta/Desktop/rosalind_fibd.txt') as InputFile:
    n,m = map(int, InputFile.read().split())
rab = [1]+[0]*(m-1)
for i in range(1, n):
    bun = 0
    for j in range(1,m):
        bun = bun + rab[(i-j-1)%m]
    rab[(i)%m] = bun
print(sum(rab))
