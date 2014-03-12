def is_number_repeated_in_list(list_of_numbers):
	for number in list_of_numbers:
		index = list_of_numbers.index(number)
		for num in list_of_numbers[index+1:]:
			if number == num:
				return True
	
	return False

def are_all_numbers_there(list_of_numbers):
	for number in range(1,10):
		is_number_in_list = False
		for n in list_of_numbers:
			if n == number:
				is_number_in_list = True
		
		if is_number_in_list == False:
			return False

	return True


def divite_into_regions(sudoku):
	regions = [[],[],[],[],[],[],[],[],[]]
	rows_of_regions = []
	for row in sudoku:
		rows_of_regions.append(row[:3])
		rows_of_regions.append(row[3:6])
		rows_of_regions.append(row[6:])
	
	for i in range(0,9,3):
		for j in range(3):
			for k in range(0,9,3):
				regions[i+j] += rows_of_regions[i*3 + j + k]

	return regions

def sudoku_solved(sudoku):
	#checking the elements of the rows
	for row in sudoku:
		if is_number_repeated_in_list(row) == True:
			return False
		
		if are_all_numbers_there(row) == False:
			return False

	#checking the elements of the columns
	for i in range(9):
		numbers_in_column = []
		for j in range(9):
			number = sudoku[j][i]
			numbers_in_column.append(number)
		
		if is_number_repeated_in_list(numbers_in_column) == True:
			return False
		
		if are_all_numbers_there(numbers_in_column) == False:
			return False

	regions = divite_into_regions(sudoku)

	#checking if numbers are used twice in the same region
	for region in regions:

		if is_number_repeated_in_list(region) == True:
			return False

		if are_all_numbers_there(region) == False:
			return False

	return True