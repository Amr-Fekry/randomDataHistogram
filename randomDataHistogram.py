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

# for each number in random_list: increment element in count_list at index = number
for n in random_list:
	count_list[n] += 1

# summarize data of count_list in a table
print "number | occurence"
for index, n in enumerate(count_list):
	if index != 10: 
		print "     {} | {}".format(index, n)
	else: # special case to fix number 10 indentation
		print "    {} | {}".format(index, n)

"""
# another solution using a while loop:

print "number | occurance"
index = 0
while index < len(count_list):
    if index == 10: ## special case to fix number 10 indentation
        print " "*4 + str(index) + " | " + str(count_list[index])  ## FEATURE: string * integer
    else:     
        print " "*5 + str(index) + " | " + str(count_list[index])
    index += 1

# lesson solutoin:

print "number | occurrence"
index = 0
num_len = len("number")

while index < len(count_list):
  num_spaces = num_len - len(str(index))
  print " " * num_spaces + str(index) + " | " + str(count_list[index])
  index = index + 1
"""
