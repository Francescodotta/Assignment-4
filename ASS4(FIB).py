def Fib(n,k):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fib(n-1,k) + k*Fib(n-2, k)
with open('/Users/francescodotta/Desktop/rosalind_fib.txt') as inputfile:
	n,k = map(int, inputfile.read().split())
totrabb = str(Fib(n,k))
print (totrabb)
