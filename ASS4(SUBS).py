with open('/Users/francescodotta/Desktop/rosalind_subs.txt') as input_data:
	s,t = input_data.readlines()
	s = s.rstrip()
	t = t.rstrip()
loc = []
for i in range(0, len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        loc.append(str(i+1))
print (' '.join(loc))
