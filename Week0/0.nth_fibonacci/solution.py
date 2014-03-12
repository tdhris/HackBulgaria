def nth_fibonacci(n):
	n1 = 1
	n2 = 1

	if n == 1:
		return n1
	if n == 2:
		return n2

	_next = 0
	i = 0
	while i < n - 2:
		_next = n1 + n2
		n1 = n2
		n2 = _next
		i+=1

	return _next