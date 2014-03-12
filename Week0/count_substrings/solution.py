def count_substrings(haystack, needle):
	count = 0
	first_occ = haystack.find(needle)
	occ = first_occ
	while first_occ >= 0:
		count +=1
		substack = haystack[occ + len(needle):]
		first_occ = substack.find(needle)
		occ += len(needle) + first_occ
		if occ >= len(haystack):
			break

	return count