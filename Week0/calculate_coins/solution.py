def calculate_coins(sum):
	sum *= 100

	coins = {1:0,2:0,100:0,5:0,10:0,50:0,20:0}
	amount = 0
	largest = 1

	while amount < sum:
		for coin in coins:
			if largest < coin and coin <= (sum-amount):
				largest = coin
		amount +=largest
		coins[largest]+=1
		largest = 1

	return coins

