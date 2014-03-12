def sum_of_min_and_max(arr):

	small = arr[0]
	for i in arr:
		if i < small:
			small = i

	large = arr[0]
	for i in arr:
		if i > large:
			large = i

	return small + large