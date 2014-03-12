def magic_square(matrix):
	matrix_sum = 0
	for element in matrix[0]:
		matrix_sum+=element

	#checking the sum of the elements of the rows
	for row in matrix:
		row_sum = 0
		for index in range(len(row)):
			row_sum += row[index]
		if row_sum != matrix_sum:
			return False

	#checking the sum of the elements in the main diagonal
	diagonal_sum = 0
	for index in range(len(matrix)):
		diagonal_sum += matrix[index][index]

	if diagonal_sum != matrix_sum:
		return False

	#checking the sum of the elements in the backward main diagonal
	b_diagonal_sum = 0
	for index in range(len(matrix)):
		b_diagonal_sum += matrix[index][len(matrix)-index-1]

	if b_diagonal_sum != matrix_sum:
		return False


	return True

