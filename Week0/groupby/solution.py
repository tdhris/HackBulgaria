def getUniqueValues(values):
	unique_values = []

	for value in values:
		count = 1
		i = values.index(value)
		for value2 in values[i+1:]:
			if value == value2:
				count +=1

		isPresent = False

		for value3 in unique_values:
			if value == value3:
				isPresent = True

		if isPresent == False:
			unique_values.append(value)

	return unique_values

def groupby(func, seq):
	group = {}
	values = []

	for number in seq:
		values.append(func(number))

	keys = getUniqueValues(values)

	for key in keys:
		lambda_values = []
		for number in seq:
			if func(number) == key:
				lambda_values.append(number)
		group[key] = lambda_values

	return group


