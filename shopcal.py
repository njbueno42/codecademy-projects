shopping_list = ["banana", "orange", "apple", "pear"]

stock = {"banana": 6, "apple": 8, "orange": 67, "pear": 32}

prices = {"banana": 3, "apple": 49, "orange": 2, "pear": 150}

def compute_bill(food):
	total = 0
	for item in food:
		if stock[item] > 0:
			total = total + prices[item]
			stock[item] = stock[item] - 1
	return total

print compute_bill(shopping_list)