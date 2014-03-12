def nth_fib_lists(listA, listB, n):
	if n == 1:
		return listA
	if n == 2:
		return listB

	i = 0
	_next = []
	while i < n-2:
		_next = listA + listB
		listA = listB
		listB = _next
		i+=1

	return _next
