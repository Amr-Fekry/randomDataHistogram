import random

#test randint:
#print "Random number generated = " + str(random.randint(0,10))

random_list = []
list_length = 20

count = 0
while count < 20:
	random_list.append(random.randint(0,10))
	count += 1

"""
# better loop without a counter:

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))
"""

print random_list
