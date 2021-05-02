# dictionary with keys = food, values = people who ordered
orders = {}
customers = int(input())

while(customers != 0):
	for i in range(customers):
		query = list(input().split())
		customer = query[0]
		for i in range(len(query) - 1):
			# if key already exists, add person to it
			if query[i+1] in orders:
				orders[query[i+1]] += " " + customer
			else:
				orders[query[i+1]] = customer
				# add food to orders list, map it to the customer

	for food in sorted(orders):
		# first order names lexicographically
		sorted_names = sorted(list(orders[food].split()))
		sorted_names = " ".join(sorted_names)
		print(food + " " + sorted_names)

	orders.clear()
	customers = int(input())
