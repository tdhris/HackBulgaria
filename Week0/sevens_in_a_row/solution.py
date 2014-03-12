def sevens_in_a_row(arr, n):
	count = 0
	for i in arr:
		if i == 7:
			count += 1
			if count == n:
				return True
		else:
			count = 0

	return False
