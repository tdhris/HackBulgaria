def biggest_difference(arr):
	if len(arr) == 1 or len(arr) == 0:
		return 0
	max_dif = arr[0] - arr[1]
	for digit in arr:
		start = arr.index(digit)
		sub_arr = arr[start:]
		for sub_digit in sub_arr:
			if digit - sub_digit < max_dif:
				max_dif = digit - sub_digit

	return max_dif

