from math import *

size_of_grid = 20
number_of_rights = size_of_grid
number_of_downs = size_of_grid

number_of_steps = number_of_downs + number_of_rights


permutations = factorial(number_of_steps)/(factorial(number_of_rights)*factorial(number_of_downs))

print(permutations)
