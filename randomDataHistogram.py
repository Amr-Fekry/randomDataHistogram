import random

random_list = []
list_length = 20

# populate random_list with 20 random integers from 0 to 10 
count = 0
while count < 20:
	random_list.append(random.randint(0,10))
	count += 1

# count occurences of number 9 in the list
index = 0
nines = 0
while index < 20:
	if random_list[index] == 9:
		nines += 1
	index += 1

print random_list
print nines
