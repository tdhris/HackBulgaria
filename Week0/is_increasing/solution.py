def is_increasing(seq):
	if len(seq) == 1:
		return True

	i = 0
	while i+1 < len(seq):
		if seq[i] >= seq[i+1]:
			return False
		i+=1
	return True
