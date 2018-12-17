import random

random_list = []
list_length = 20

# populate random_list with 20 random integers from 0 to 10 
count = 0
while count < list_length:
	random_list.append(random.randint(0,10))
	count += 1

# create a list that contains the count of occurances for each number from 0 to 10 in random_list
# initialize a count_list to 11 zeros
count_list = [0] * 11

# for each number in random_list: increment element at index = number
for n in random_list:
	count_list[n] += 1

"""
# same solution using while loop:

index = 0
while index < list_length:
  n = random_list[index]
  count_list[n] += 1
  index += 1
"""

print random_list
print count_list
# sum of all numbers in count_list should be 20 if code is right
print sum(count_list)
