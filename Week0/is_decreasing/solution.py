def is_decreasing(seq):
	if len(seq) == 1:
		return True

	i = 0
	while i+1 < len(seq):
		if seq[i+1] >= seq[i]:
			return False
		i+=1
	return True
