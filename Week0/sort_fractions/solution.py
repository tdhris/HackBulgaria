def sort_fractions(fractions):
	fraction_dic = {}
	float_list = []
	for fraction in fractions:
		a = fraction[0]
		b = fraction[1]
		float_fraction = a/b
		fraction_dic[float_fraction] = fraction
		float_list.append(float_fraction)

	float_list.sort()
	
	compared_fractions = []
	for fraction in float_list:
		compared_fractions.append(fraction_dic[fraction])

	return compared_fractions

