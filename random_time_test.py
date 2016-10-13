from random_time import *


num_list = []
count = 0

while count != 2000:
    num_list.append(generate_number())
    count += 1

print(num_list)
