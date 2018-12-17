import random

random_list = []
list_length = 20

# populate random_list with 20 random integers from 0 to 10 
count = 0
while count < list_length: # used list_length instead of the magic number 20 
	random_list.append(random.randint(0,10))
	count += 1

# create a list that contains the count of occurances for each number from 0 to 10 in random_list
# initialize a count_list to 11 zeros
count_list = [0] * 11 #NEW FEATURE

# for each number from 0 to 10: count number of occurences in random_list, then add count to count_list at index = number
for n in range(11):
	count = 0
	for e in random_list:
		if e == n:
			count += 1
	count_list[n] = count

print random_list
print count_list
# sum of all numbers in count_list should be 20 if code is right
print sum(count_list)
