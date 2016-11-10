from itertools import permutations


def slice_arr(arr,start, end = None):
	if(not end):
		end = len(arr)
	return int(''.join(arr[start:end]))

def check_for_pandigital_products(arr):
	equals_index = int((len(arr)+1)/2)
	product = slice_arr(arr, equals_index)

	multiplicand = 0
	multiplier = 0

	for i in range(1, int(equals_index/2)+1):
		multiplicand = slice_arr(arr, 0, i)
		multiplier = slice_arr(arr, i, equals_index)
		if(multiplicand * multiplier == product):
			return product
	return 0

products = set()
base = ''.join([str(j) for j in range(1,10)])
perms = permutations(base)
for p in perms:
	product = check_for_pandigital_products(p)
	products.add(product)

print(sum(products))
	