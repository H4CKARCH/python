# Constructing output list WITHOUT using List comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_list = []

# Using loop for constructing output list
for var in input_list:
    if var % 2 == 0:
        output_list.append(var)

print("Output List using for loop:", output_list)
