# filter() with lambda() 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list)

#filter negative number
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

#zip

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
results = list(zip(my_strings, my_numbers))
print(results)

#map(function_to_apply, list_of_inputs)


items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
#map using lambda
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

#eg:1

my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

#eg:2

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1,7)))
print(result)

#reduce

list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24


from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24
