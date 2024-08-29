
def count_bases(seq):
	counts = {'C': 0, 'G':0, 'T':0, 'A':0}
	for b in seq:
		counts[b] += 1
	return counts

def reverse_complement(s):
	d = {'A': 'T', 'T': 'A','C': 'G', 'G': 'C'}
	l = []
	for i in range(1, len(s)+1):
		l.append(d[s[-i]])
	return ''.join(l)

def melting_temp(s):
	d = count_bases(s)
	if len(s) < 14:
		return (d['A'] + d['T']) * 2 + (d['G'] + d['C']) * 4
	else:
		return 64.9 + 41 * (d['G']+d['C']-16.4) / len(s)

def has_hairpin(s, k):
	looplen = 4
	for i in range(len(s)-k+1):
		subs = s[i:i+k]
		right = s[i+k:]
		revcl = reverse_complement(subs)
		if revcl in right[looplen:]:
			return True
	return False

# def has_hairpin(s, k):
# 	looplen = 4
# 	for i in range(len(s)-k+1):
# 		subs = s[i:i+k]
# 		left = s[:i-looplen]
# 		right = s[i+k+looplen:]
# 		revcl = reverse_complement(subs)
# 		if revcl in left or revcl in right:
# 			return True
# 	return False