def what_is_my_sign(day, month):
	last_days_of_signs = {1:20, 2:19, 3:20, 4:20, 5:21, 6:21, 7:22, 8:22, 9:23, 10:23, 11:22, 12:21}
	signs = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']

	if day <= last_days_of_signs[month]:
		return signs[month-1]
	else:
		return signs[month]

