def nth_fib_lists(listA, listB, n):
	if n == 1:
		return listA
	if n == 2:
		return listB

	_next = []
	i = 0
	while i < n-2:
		_next = listA+listB
		listA = listB
		listB = _next
		i+=1

	return _next


def member_of_nth_fib_lists(listA, listB, needle):
	if needle == listA or needle == listB:
		return True

	length = len(needle)
	nth_list = []
	n = 3
	while length >= len(nth_fib_lists(listA, listB, n)):
		nth_list = nth_fib_lists(listA, listB, n)
		if needle == nth_list:
			return True
		n+=1

	return False


