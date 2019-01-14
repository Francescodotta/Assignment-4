def Bin_Search(Array, val):
	return binsearchHelp(Array, val, 0, len(Array))
def binsearchHelp(Array, val, x, y):
	if x >= y:
		return -1
	elif x == y-1:
		if Array[x] == val:
			return x+1
		else:
			return -1
	midpoint = (x + y) // 2
	if Array[midpoint] > val:
		return binsearchHelp(Array, val, x, midpoint)
	else:
		return binsearchHelp(Array, val, midpoint, y)
with open('/Users/francescodotta/Desktop/rosalind_bins.txt') as InputFile:
    n = int(InputFile.readline())
    m = int(InputFile.readline())
    Array = list(map(int, InputFile.readline().split()))
    ks = list(map(int, InputFile.readline().split()))
print(' '.join(map(str, [Bin_Search(Array, val) for val in ks])))

