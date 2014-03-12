def slope_style_score(scores):
	smallest = scores[0]
	for score in scores:
		if score < smallest:
			smallest = score

	scores.remove(smallest)

	largest = scores[0]
	for score in scores:
		if score > largest:
			largest = score

	scores.remove(largest)

	return round((sum(scores) / len(scores)), 2)


